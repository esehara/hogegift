#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
import sys,io,time
import shpaml
import cgi
import os
import shpaml
import time
import urllib

sys.stdout = io.TextIOWrapper(
		sys.stdout.buffer,encoding="utf-8")

class NotGift:
	def __init__(self):
		self.cgi_value = cgi.FieldStorage()
	def is_set(self):

		dprint("self.cgi_value has " +  str(self.cgi_value))
		dprint("giftname is " + str("giftname" in self.cgi_value))
		if "giftname" in self.cgi_value: dprint(self.cgi_value["giftname"].value)
		
		return (
				("giftname" in self.cgi_value) and
				("giftnamejp" in self.cgi_value) and
				("yourname" in self.cgi_value) and
				("twitteraccount" in self.cgi_value) and
				("descript" in self.cgi_value)
				)
	
	def filelist(self):
		filelist = os.listdir("data")
		result_string = ""
		for fi in filelist:
			fil = open("data/" + fi, encoding="UTF-8").readlines()
			result_string = result_string + ("<li><a href='show.py?f=%s'>%sへの、%sの支援が募集されています</a></li>" %(fi.replace(".dat",""),fil[2],fil[1]))
		return result_string

	def save(self):
		dprint("[Start] Save Function is Start.")
		filename = str(time.time()).replace(".","")
		dprint("[Debug] Filename is " + filename)
		dprint("[Debug] FileOpen(data/" + filename + ".dat)")
		openfile = open("./data/" + filename + ".dat",mode="w",encoding="utf-8")
		dprint("[Start] FileOpen Now")
		openfile.write(self.cgi_value["giftname"].value + "\n")
		openfile.write(self.cgi_value["giftnamejp"].value + "\n")
		openfile.write(self.cgi_value["yourname"].value + "\n")
		openfile.write(self.cgi_value["twitteraccount"].value + "\n")
		openfile.write(self.cgi_value["yourinfo"].value + "\n")
		openfile.write(self.cgi_value["descript"].value + "\n")
		print("Content-type: text/html")
		print("Location: show.py?f=" + filename)
		print()

def safelize(string):
	return string.replace("<","＜").replace(">","＞")


def dprint(string):
	"""
	Print Function for Debug in Browser.
	"""
	debug = False
	if debug:
		print(string,"<br />")

def main():
	system = NotGift()
	if system.is_set():
		system.save()
	else:
		print("Content-type: text/html;charset=UTF-8")
		print()
		print(
			shpaml.convert_text(
				open("template/index.haml",encoding="UTF-8").read()
				).replace("{whatisgift}","hoge").replace("{whatisgiftjp}","ほげほげ").replace("{list}",system.filelist()))

if __name__ == "__main__" : main()

