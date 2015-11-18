

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import os,sys,getpass,curses
import subprocess,threading,time
# Define a function for running commands and capturing stdout line by line
# (Modified from Vartec's solution because it wasn't printing all lines)
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True,executable="/bin/bash")
    return p.stdout.read()
def wait_for_internet():
	print "waiting for internet"
	while True:
		output=runProcess("ping -c 1 8.8.8.8")
		print ".",
		if output.find("100% packet loss")==-1 and output.find("connect: Network is unreachable")==-1:
			return

def MyThread ():
	while True:
		print ".",
		time.sleep(0.5)
	
def install_apt_get(name):
	print "Starting Installation of "+name,
	output=runProcess("apt-get -y --force-yes install "+name)
	if output.find("is already the newest version.")!=-1:
		print name+" is already installed"
	elif output.find("E: Unable to locate package")!=-1:
		print "Unable the install "+name+" the package maybe out of date or replaced by an other package"
	elif output.find("Could not resolve")!=-1:
		print "Check Your internet connection and try again"
		wait_for_internet()
		install_apt_get(name)
	elif output.find("is another process using it")!=-1:
		print "An other process is interfering with the resources I need please stop the other process or restart the computer"
		print "Do you want to restart the computer(y/N):"
		a=raw_input()
		if a.lower()=="y" :
			runProcess("reboot")
		else:
			os._exit(0)
	elif output.find("are you root")!=-1:
		print "you should  be root to run the program"
		print 'use the command "sudo python '+sys.argv[0]+'"'
		os._exit(0)
	if output.find("Setting up "+name)!=-1:
		print name+" Installation Complete\n"

def install_pip(name):
	print "Starting Installation of pip "+name,
	output=runProcess("pip install -y "+name)
	if output.find("No distributions at all found for")!=-1:
		print "Unable the install "+name+" the module maybe out of date or replaced by an other module"
	elif output.find("Requirement already satisfied")!=-1:
		print name+" is already installed"
	elif output.find("Cannot fetch index base URL")!=-1:
		print "Check Your internet connection and try again"
		wait_for_internet()
		install_pip(name)
	print "installing complete "+name

def install_pip3(name):
	print "Starting Installation of pip3 "+name,
	output=runProcess("pip3 install -y "+name)
	if output.find("No distributions at all found for")!=-1:
		print "Unable the install "+name+" the module maybe out of date or replaced by an other module"
	elif output.find("Requirement already satisfied")!=-1:
		print name+" is already installed"
	elif output.find("Cannot fetch index base URL")!=-1:
		print "Check Your internet connection and try again"
		wait_for_internet()
		install_pip3(name)
	print "installing complete "+name
def update_apt_get():
	print "updating databases"
	output=runProcess("apt-get update")
	if output.find("Failed to fetch http:")!=-1:
		wait_for_internet()
		update_apt_get() 
def main(a,b,c):
	
	if a.lower()=="y" or a=="" :
		runProcess("wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -")
		runProcess('echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list')
		runProcess("sudo add-apt-repository ppa:webupd8team/java")
		if c.lower()=="y" or c=="": 
			runProcess("sudo add-apt-repository ppa:paolorotolo/android-studio")
		update_apt_get()
		if c.lower()=="y" or c=="":
			install_apt_get("android-studio")
		a='php5-cli oracle-java8-installer google-chrome-stable lib32z1 gcc python-dev python3-dev lib32ncurses5 lib32bz2-1.0 filezilla rubygems ruby-full build-essential nautilus-open-terminal python3-pip python-pip lua5.2 npm nodejs sublime-text-installer git vim android-tools-adb zip unzip vlc putty handbrake python-nautilus python-notify'
		a=a.split()
		for i in a: 
			install_apt_get(i)
	if b.lower()=="y" or b=="":
		a="python-numpy python3-numpy python-scipy python3-scipy python-dateutil python-docutils python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid python-psycopg2 python-psutil python-pybabel python-pychart python-pydot python-pyparsing python-reportlab python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi python3-dateutil python3-docutils python3-feedparser python3-jinja2 python3-lxml python3-mako python3-mock python3-psycopg2 python3-psutil python3-pyparsing python3-reportlab python3-simplejson python3-tz python3-werkzeug python3-yaml"
		a=a.split()
		for i in a:
			install_apt_get(i)
		a="django requests scrapy mitmproxy pyramid scikit-learn beautifulsoup4"
		a=a.split()
		for i in a:
			install_pip(i)
			install_pip3(i)
	os._exit(0)
a=raw_input("\ninstall default programs (Y/n)")
b=raw_input("\nAre you going to program in python (Y/n)")
c=raw_input("\nDo you want android-studio (Y/n)")
thread = threading.Thread(target = main, args=(a,b,c,))
thread.start()
while thread.isAlive():
	sys.stdout.write(".")
	sys.stdout.flush()
	time.sleep(.1)