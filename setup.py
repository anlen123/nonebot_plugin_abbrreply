#!/root/miniconda3/bin/python3 
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='nonebot_plugin_abbrreply',
    version="1.0.0",
    description=(
        '缩写查询器'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='anlen123',
    author_email='1761512493@qq.com',
    maintainer='anlen123',
    maintainer_email='1761512493@qq.com',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/anlen123/nonebot_plugin_abbrreply',
    install_requires=[
        'aiohttp',
    ]
)
