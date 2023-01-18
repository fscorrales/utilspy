#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites
Purpose: Web scraping (NOT COMPLETE)
Require package: 
    - bs4
    - pandas
"""

import argparse
import datetime
from urllib.request import urlopen

# import pandas
# import requests
# from bs4 import BeautifulSoup

# The web page that you’ll open is at the following URL:
url = "http://olympus.realpython.org/profiles/aphrodite"
alt_url = 'http://olympus.realpython.org/profiles/poseidon'

# To open the web page, pass url to urlopen():
page = urlopen(alt_url)

# urlopen() returns an HTTPResponse object. To extract 
# the HTML from the page, first use the HTTPResponse object’s 
# .read() method, which returns a sequence of bytes. Then 
# use .decode() to decode the bytes to a string using UTF-8:
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# python web_scraper.py