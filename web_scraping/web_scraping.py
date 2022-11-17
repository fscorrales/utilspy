#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtube.com/playlist?list=PLeLGx0BaYD6a1GiowNEeTi5mBp7FLGTaH
Purpose: Web scraping (NOT COMPLETE)
Require package: 
    - bs4
    - pandas
"""

import argparse
import datetime

import pandas
import requests
from bs4 import BeautifulSoup

BASEURL = 'https://www.mercadolibre.com.ar/'

product_links = []

for x in range(1,10):
    #get the webpage
    r = requests.get(f'')
    #get the content of the page
    soup = BeautifulSoup()