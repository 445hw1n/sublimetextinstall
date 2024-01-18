#!/usr/bin/env python3
# sublime installation for the debian
import subprocess

gpgkeysublime = "wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null"
stable_rel = "echo " + "deb https://download.sublimetext.com/ apt/stable/" + " |" + " sudo tee /etc/apt/sources.list.d/sublime-text.list "

def install():
	print("------------------")
	subprocess.call(["sudo " + "apt-get " + "update"],shell=True)
	print("------------------")
	subprocess.call([gpgkeysublime],shell=True)
	print("------------------")
	subprocess.call([stable_rel],shell=True)
	print("------------------")
	subprocess.call(["sudo " + "apt-get " + "update"],shell=True)
	print("------------------")
	subprocess.call(["sudo " + "apt-get " + "install " + "sublime-text"],shell=True)
	print("------------------")

install()