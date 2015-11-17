from time import sleep
import curses, os,subprocess,sys,atexit #curses is the interface for capturing key presses on the menu, os launches the files
@atexit.register
def on_exit():
	curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
	os.system('clear')
	os.system('reset')
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad

# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
h = curses.color_pair(1) #h is the coloring for a highlighted menu option
n = curses.A_NORMAL #n is the coloring for a non highlighted menu option

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"


menu_data = {

	'title': "Ubuntu Stater Kit", 'type': MENU, 'subtitle': "Please select an option...",
	'options':
	[
		{ 'title': "Languages", 'type': MENU, 'subtitle': "select the once u want to install",
			'options': 
			[
				{'title': "Python modules(Recommended)", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install gcc build-essential python-dev python3-dev python-numpy python3-numpy python-scipy python3-scipy python-dateutil python-docutils python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid python-psycopg2 python-psutil python-pybabel python-pychart python-pydot python-pyparsing python-reportlab python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi python3-dateutil python3-docutils python3-feedparser python3-jinja2 python3-lxml python3-mako python3-mock python3-psycopg2 python3-psutil python3-pyparsing python3-reportlab python3-simplejson python3-tz python3-werkzeug python3-yaml' }
					] 
				},
				{'title': "Ruby", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev ruby-full' }
					] 
				},
				{'title': "Java", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "Open JDK", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
							[
								{ 'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install default-jdk' },
							] 
						},
						{'title': "Oracal JDK", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
							[
								{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install oracle-java8-installer' }
							] 
						}
						
					] 
				},
				{'title': "GIT(no need if you have installed ruby)", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install git-core ' }
					] 
				},
				{'title': "Php", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install php5-cli ' }
					] 
				},
				{'title': "Perl", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install perl ' }
					] 
				},
				{'title': "NodeJS", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install nodejs npm ' }
					] 
				},
				{'title': "C++ and C", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install gcc g++ ' }
					] 
				},
				{'title': "GO", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install golang-stable ' }
					] 
				},
				{'title': "Haskell", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install  haskell-platform' }
					] 
				},
				{'title': "Lua", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install lua5.2' }
					] 
				},
				{'title': "Scala", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install scala' }
					] 
				},
				{'title': "R Language", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install r-base' }
					] 
				},
				{'title': "Rust Language", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install curl && curl -sSf https://static.rust-lang.org/rustup.sh | sh' }
					] 
				},
				{'title': "Arduino", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install arduino arduino-core' }
					] 
				}
			]
		},
		{ 'title': "Databases", 'type': MENU, 'subtitle': "select the once u want to install",
			'options': 
			[
				{'title': "MySQL", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install mysql-server && sudo mysql_install_db && sudo /usr/bin/mysql_secure_installation' }
					] 
				},
				{'title': "postgresql", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': 'sudo apt-get install postgresql postgresql-contrib' }
					] 
				},
				{'title': "MongoDB", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': "sudo apt-get install -y mongodb-org" }
					] 
				},
				{'title': "Redis", 'type': MENU, 'subtitle': 'Press Yes if u want to install', 'options': 
					[
						{'title': "YES", 'type': COMMAND, 'command': "sudo apt-get install redis-server" }
					] 
				},
			]
		}
	]
}
no_internet_menu={
	'title': "Ubuntu Stater Kit", 'type': MENU, 'subtitle': "No Network connections...",
	'options':[
				{ 'title': "Try again", 'type': COMMAND, 'command': 'tryagain' }
	]
}

# function used to check internert connections
def check_for_internet():
	screen.addstr("checking for internet connections...")
	output=runProcess("ping -c 1 8.8.8.8")
	if output.find("100% packet loss")==-1 and output.find("connect: Network is unreachable")==-1:
		return True
	else:
		return False

# This function displays the appropriate menu and returns the option selected
def runmenu(menu, parent):
	# work out what text to display as the last menu option
	if parent is None:
		lastoption = "Exit"
	else:
		lastoption = "Return to %s menu" % parent['title']

	optioncount = len(menu['options']) # how many options in this menu

	pos=0 #pos is the zero-based index of the hightlighted menu option. Every time runmenu is called, position returns to 0, when runmenu ends the position is returned and tells the program what opt$
	oldpos=None # used to prevent the screen being redrawn every time
	x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program

	# Loop until return key is pressed
	while x !=ord('\n'):
		if pos != oldpos:
			oldpos = pos
			screen.border(0)
			screen.addstr(2,2, menu['title'], curses.A_STANDOUT) # Title for this menu
			screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) #Subtitle for this menu

			# Display all the menu items, showing the 'pos' item highlighted
			for index in range(optioncount):
				textstyle = n
				if pos==index:
					textstyle = h
				screen.addstr(5+index,4, "%s" % (menu['options'][index]['title']), textstyle)
			# Now display Exit/Return at bottom of menu
			textstyle = n
			if pos==optioncount:
				textstyle = h
			screen.addstr(5+optioncount,4, "%s" % (lastoption), textstyle)
			screen.refresh()
			# finished updating screen

		x = screen.getch() # Gets user input

		# What is user input?
		if x >= ord('1') and x <= ord(str(optioncount+1)[0]):
			pos = x - ord('0') - 1 # convert keypress back to a number, then subtract 1 to get index
		elif x == 258: # down arrow
			if pos < optioncount:
				pos += 1
			else: pos = 0
		elif x == 259: # up arrow
			if pos > 0:
				pos += -1
			else: pos = optioncount

	# return index of the selected item
	return pos

def wait_for_internet():
	os.system('echo -n "Waiting for internet.."')
	while True:
		output=runProcess("ping -c 1 8.8.8.8")
		if output.find("100% packet loss")==-1 and output.find("connect: Network is unreachable")==-1:
			return
		else:
			os.system('echo -n ".."')
			sleep(2)

# This function calls showmenu and then acts on the selected item
def processmenu(menu, parent=None):
	optioncount = len(menu['options'])
	exitmenu = False
	while not exitmenu: #Loop until the user exits the menu
		getin = runmenu(menu, parent)
		if getin == optioncount:
				exitmenu = True
		elif menu['options'][getin]['type'] == COMMAND:
			curses.def_prog_mode()		# save curent curses environment
			os.system('reset')
			if menu['options'][getin]['title'] == 'Try again':
				curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
				os.system('clear')
				os.system("sudo python "+sys.argv[0])
				os._exit(0)
			screen.clear() #clears previous screen
			wait_for_internet()
			os.system(menu['options'][getin]['command']+' && echo "Please press <enter> to continue " && read input_variable') # run the command
			screen.clear() #clears previous screen on key press and updates display based on pos
			curses.reset_prog_mode()	 # reset to 'current' curses environment
			curses.curs_set(1)				 # reset doesn't do this right
			curses.curs_set(0)
		elif menu['options'][getin]['type'] == MENU:
					screen.clear() #clears previous screen on key press and updates display based on pos
					processmenu(menu['options'][getin], menu) # display the submenu
					screen.clear() #clears previous screen on key press and updates display based on pos
		elif menu['options'][getin]['type'] == EXITMENU:
					exitmenu = True
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True,executable="/bin/bash")
    return p.stdout.read()

def add_aditional_repos_and_updating():
	curses.def_prog_mode()		# save curent curses environment
	os.system('reset')
	screen.clear()
	os.system("echo 'add aditional repos for installiation...'")
	os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list")
	os.system("sudo apt-get install -y python-software-properties && sudo add-apt-repository -y ppa:rwky/redis")
	os.system("sudo add-apt-repository -y ppa:webupd8team/java")
	screen.clear() #clears previous screen on key press and updates display based on pos
	os.system('echo "updating the package databases...." && sleep 2 &&sudo apt-get update && echo "Please press <enter> to continue " && read input_variable') # run the command
	screen.clear() #clears previous screen on key press and updates display based on pos
	curses.reset_prog_mode()	 # reset to 'current' curses environment
	curses.curs_set(1)				 # reset doesn't do this right
	curses.curs_set(0)

# Main program
if os.getuid() == 0:
	if check_for_internet() :
		add_aditional_repos_and_updating()
		processmenu(menu_data)
	else:
		processmenu(no_internet_menu)
else:
	curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
	os.system('clear')
	os.system("sudo python "+sys.argv[0])
	os._exit(0)