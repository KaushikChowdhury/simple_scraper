from urllib.request import urlopen , Request
from bs4 import BeautifulSoup
import argparse

from functions import write_html, read_html, parser, url_parser
from constants import HEADER

ap = argparse.ArgumentParser()
ap.add_argument("-rw", "--readwrite", required=True, help="read or write flag - 'r/w'")
ap.add_argument("-p", "--pages", required=True, help="pages to read")
args = vars(ap.parse_args())

if (args["readwrite"] == "w"):
    urls = url_parser(int(args['pages']))
    for index,URL in enumerate(urls):
        request = Request(url=URL, headers=HEADER)
        html = urlopen(request)
        soup = BeautifulSoup(html, 'html.parser')
        soup_ = BeautifulSoup(soup.prettify(), 'html.parser')
        write_html(soup, index)

elif (args["readwrite"] == "r"):
    for i in range(0, int(args['pages'])):
        soup = read_html(i)
        soup_ = BeautifulSoup(soup.prettify(), 'html.parser')
        parser(soup)



