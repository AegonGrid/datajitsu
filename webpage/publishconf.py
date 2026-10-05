import sys
import os

sys.path.append(os.path.dirname(__file__))

from pelicanconf import *

# Set this to your real domain before deploying
SITEURL = "https://datajitsu.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
