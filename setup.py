# setup.py
from setuptools import setup, find_packages

setup(
    name='pyairos',
    version='0.0.1',
    author='@kmstumpff',
    author_email='kmstumpff@users.noreply.github.com',
    description="Python library for Ubiquiti's AirOS",
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.11.14,<4.0.0',
        'asyncio>=3.4.3,<4.0.0',
        'typing-extensions>=4.13.1,<5.0.0',
    ],
)