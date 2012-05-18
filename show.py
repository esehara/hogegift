#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys,io,time
import shpaml
import cgi
import os
import shpaml
import time
import urllib.parse
sys.stdout = io.TextIOWrapper(
		sys.stdout.buffer,encoding="utf-8")

class NotGift:
	def __init__(self):
		self.cgi_value = cgi.parse_qs(os.environ['QUERY_STRING']) if 'QUERY_STRING' in os.environ else {}
	def is_set(self):
		if "f" in self.cgi_value:
			return True
		return False
	def set_file(self):
		filename = self.cgi_value["f"][0]
		target_file = open("data/" + filename + ".dat",encoding="UTF-8").readlines()
		self.configure = {
				"giftname":safelize(target_file[0])
				,"giftnamejp":safelize(target_file[1])
				,"yourname":safelize(target_file[2])
				,"twitter":safelize(target_file[3])
				,"yourinfo":safelize(target_file[4])
				,"descript":safelize("\n".join(target_file[5:]))
				,"filename":filename
				}

	def nowurl(self):
		if 'HTTP_HOST' in os.environ and 'REQUEST_URI' in os.environ:
			return urllib.parse.quote_plus("http://" + os.environ['HTTP_HOST'] + os.environ['REQUEST_URI'])
		return urllib.parse.quote_plus("http://www45045u.sakura.ne.jp/hogehoge/").encode()

	def output(self):
		template_string = shpaml.convert_text(open("template/show.haml",encoding="UTF-8").read())
		template_string = (template_string
							.replace("{whatisgift}",self.configure["giftname"].rstrip())
							.replace("{whatisgiftjp}",self.configure["giftnamejp"].rstrip())
							.replace("{name}",self.configure["yourname"].rstrip())
							.replace("{twitter}",self.configure["twitter"].rstrip())
							.replace("{yourinfo}",self.configure["yourinfo"].rstrip())
							.replace("{descript}",self.configure["descript"].rstrip())
							.replace("{filename}",self.configure["filename"].rstrip())
							.replace("{url}",self.nowurl())
							)
		print(template_string)

def safelize(st):
	return st.replace("<","＜").replace(">","＞")

def goback():
	print("Content-type: text/html")
	print("Location: index.py")
	print()
	

def main():
	system = NotGift()
	if system.is_set():
			system.set_file()
			print("Content-type: text/html;charset=UTF-8")
			print()
			system.output()
	else:
		goback()

if __name__ == "__main__" : main()

