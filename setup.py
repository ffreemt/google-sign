# pylint: disable=invalid-name
from pathlib import Path
import re

from setuptools import setup, find_packages

name = """google-sign"""
description = 'Calculate sign string for google translate and baidu translate'
dir_name, *_ = find_packages()
# dir_name = 'google_sign'
curr_dir = Path(__file__).parent

_ = Path(f'{dir_name}/__init__.py').read_text(encoding='utf-8')
version, *_ = re.findall(r"__version__\W*=\W*'([^']+)'", _)
targz = 'v_' + version.replace('.', '') + '.tar.gz'

install_requires = []

README_rst = f'{curr_dir}/README.md'
long_description = (
    open(README_rst, encoding='utf-8').read() if Path(README_rst).exists() else ''
)

setup(
    name=name,
    packages=find_packages(),
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['machine translation', 'free', 'sign'],
    author="mikeee",
    url=fr'http://github.com/ffreemt/{name}',
    download_url=fr'https://github.com/ffreemt/{name}/archive/' + targz,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT License',
)