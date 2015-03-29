#!/usr/bin/env python
import re
import praw 
import os
import urllib
from time import sleep
import BeautifulSoup
import string
from gi.repository import Gio

_REDDIT_API_SLEEP_TIME = 1800 # 30 minutes 
_VALID_CHARS = frozenset(''.join(("-_.() ", string.ascii_letters, string.digits)))


def clean(s, default_name = "image"):
	"""Remove illegal characters and return legal string""" 
	cleaned = ''.join(c for c in s if c in _VALID_CHARS)
	return cleaned if cleaned else default_name 

def download_and_save_image(imageURL, local_filename):
	"""Save the picture at a given URL to a given local filename."""
	print('Title: %s' % local_filename)
	urllib.urlretrieve(imageURL, local_filename)
	set_background(local_filename)
	

def set_background(local_filename):
	escaped_filename = re.escape(local_filename) # Escape special characters
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/danielmxli/mintpaper/" + escaped_filename)
	#sleep(_REDDIT_API_SLEEP_TIME) # Don't wanna get beat by reddit #nahmean 

def fetch_image(submission):
	"""Call download_and_save_image with valid arguments"""
	url = submission.url
	extension = url.split('.')[-1]
	title = clean(submission.title) 
	if title.endswith('.'): title = title[:-1] # In case foo..jpg
	local_filename = '%s.%s' % (title, extension)
	download_and_save_image(url, local_filename)
	

def scrape_and_set(targetSubreddit='wallpapers'):
	# Connect to reddit and download the subreddit front page 
	r = praw.Reddit(user_agent='Mintpaper 1.0 by /u/snowisgone')
	subreddit = r.get_subreddit(targetSubreddit)
	submissions = subreddit.get_hot(limit=1)
	extensions = ['jpg', 'png']
	count = 0 
	for sub in submissions:
		url = sub.url
		if any(sub.url.lower().endswith(ext.lower()) for ext in extensions):
			print('Downloading %s ...' % url)
			fetch_image(sub)
			count += 1 
		#print('Downloaded %s pictures' % count)
		



if __name__ == '__main__':
	scrape_and_set()