from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverFactory:
    def create_driver(self, browser, headless_browser=False, disable_image_load=False):
        if browser == "chrome":
            return self._create_chrome_driver(headless_browser, disable_image_load)
        elif browser == "chromium":
            return self._create_chromium_driver(headless_browser, disable_image_load)
        elif browser == "brave":
            return self._create_brave_driver(headless_browser, disable_image_load)
        elif browser == "firefox":
            return self._create_firefox_driver(headless_browser, disable_image_load)
        elif browser == "edge":
            return self._create_edge_driver(headless_browser, disable_image_load)
        else:
            raise ValueError(f"Navegador {browser} não é suportado.")

    
    def _create_chrome_driver(self, headless_browser, disable_image_load):
        options = ChromeOptions()
        if headless_browser:
            options.add_argument("--headless")
        if disable_image_load:
            options.add_argument("blink-settings=imagesEnabled=false")
        return webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

    def _create_chromium_driver(self, headless_browser, disable_image_load):
        options = ChromeOptions()
        if headless_browser:
            options.add_argument("--headless")
        if disable_image_load:
            options.add_argument("blink-settings=imagesEnabled=false")
        return webdriver.Chrome(service=Service(executabl_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM)), options=options)
    
    def _create_brave_driver(self, headless_browser, disable_image_load):
        options = ChromeOptions()
        if headless_browser:
            options.add_argument("--headless")
        if disable_image_load:
            options.add_argument("blink-settings=imagesEnabled=false")
        return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=options)
    
    def _create_firefox_driver(self, headless_browser, disable_image_load):
        options = FirefoxOptions()
        if headless_browser:
            options.add_argument("--headless")
        if disable_image_load:
            options.set_preference("permissions.default.image", 2)
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def _create_edge_driver(self, headless_browser, disable_image_load):
        options = EdgeOptions()
        if headless_browser:
            options.add_argument("--headless")
        if disable_image_load:
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)
        return webdriver.Edge(service=Service(executable_path=EdgeChromiumDriverManager().install()), options=options)

class DriverSelenium:
    def __init__(self, browser: str = "chrome"):
        self.browser = browser

    def start_driver(self, headless_browser: bool = False, disable_image_load: bool = False):
        factory = DriverFactory()
        return factory.create_driver(self.browser, headless_browser, disable_image_load)
    

