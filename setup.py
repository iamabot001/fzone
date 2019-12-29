import setuptools
from setuptools import setup

setup(
    name='f95zone',
    version='0.2',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'requests_html', 'wheel', 'setuptools', ],
    include_package_data=True,
    url='https://github.com/iamabot001/fzone',
    license='',
    author='iamabot001',
    author_email='',
    description='A simple tool to track your games'
)
