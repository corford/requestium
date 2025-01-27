# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='requestium',
    version='0.1.9',
    description=(
        "Adds a Selenium webdriver and parsel's parser to a request's Session "
        "object, and makes switching between them seamless. Handles cookie, "
        "proxy and header transfer."
    ),
    long_description='',
    author='Joaquin Alori',
    author_email='joaquin@tryolabs.com',
    url='https://github.com/tryolabs/requestium',
    packages=('requestium',),
    install_requires=(
        'requests>=2.18.1',
        'selenium>=3.7.0',
        'parsel>=1.2.0',
        'tldextract>=2.1.0'
    ),
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
