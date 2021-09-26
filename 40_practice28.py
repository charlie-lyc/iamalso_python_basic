# pip install : 패키지 설치 명령 <= www.pypi.org

import inspect
from bs4 import BeautifulSoup

# print(inspect.getfile(BeautifulSoup)) # ModuleNotFoundError: No module named 'bs4'

# 터미널에서 아래와 같이 설치를 실행
# % pip install beautifulsoup4

print(inspect.getfile(BeautifulSoup)) # /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/bs4/__init__.py


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# https://pypi.org/project/beautifulsoup4/ 참조하여 실행

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

## 설치된 패키지 리스트 확인
# % pip list
# Package        Version
# -------------- -------
# attrs          21.2.0
# beautifulsoup4 4.10.0
# iniconfig      1.1.1
# packaging      21.0
# parso          0.8.2
# pip            21.2.4
# pluggy         1.0.0
# py             1.10.0
# pyparsing      2.4.7
# setuptools     57.4.0
# soupsieve      2.2.1
# toml           0.10.2

## 특정 패키지 정보 확인
# % pip show beautifulsoup4
# Name: beautifulsoup4
# Version: 4.10.0
# Summary: Screen-scraping library
# Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
# Author: Leonard Richardson
# Author-email: leonardr@segfault.org
# License: MIT
# Location: /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
# Requires: soupsieve
# Required-by:

## 패키지가 설치되어 있지 않으면 설치하고, 이미 설치되어 있으면 업그레이드 하기
# % pip install --upgrade beautifulsoup4

## 패키지 지우기
# % pip uninstall beautifulsoup4