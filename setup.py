from setuptools import setup, find_packages

setup(
    name='instapro',
    version='0.1.0',
    author='gleyson do nascimento carvalho',
    author_email='gleysondonascimentocarvalho@gmail.com',
    description='A library to interact with Instagram in a simplified way.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    url='https://github.com/GLDNC/instapro',
    packages=find_packages(),
    install_requires=[
        'selenium',
        
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)
