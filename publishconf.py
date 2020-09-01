#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = 'https://github.com/bahackers/blog/'
SITEURL = 'https://denise.matehackers.org/bahackers/'
RELATIVE_URLS = False
WITH_FUTURE_DATES = False

FEED_DOMAIN = 'https://denise.matehackers.org/bahackers/'
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
# AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
