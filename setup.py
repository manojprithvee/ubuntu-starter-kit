from time import sleep
from data import menu_data,no_internet_menu
import curses, os,subprocess,sys,atexit,platform #curses is the interface for capturing key presses on the menu, os launches the files
@atexit.register
def on_exit():
	try:
		curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
		os.system("reset")
	except:
		os.system("reset")
		pass

# function used to check internert connections
def check_for_internet():
	os.system("echo 'checking for internet connections...'")
	output=runProcess("ping -c 1 8.8.8.8")
	if output.find("100% packet loss")==-1 and output.find("connect: Network is unreachable")==-1:
		return True
	else:
		return False

# This function displays the appropriate menu and returns the option selected
def runmenu(menu, parent):
	display("entering run...."+menu["title"])
	# work out what text to display as the last menu option
	if parent is None:
		lastoption = "Exit"
	else:
		lastoption = "Return to %s menu" % parent["title"]

	optioncount = len(menu["options"]) # how many options in this menu

	pos=0 #pos is the zero-based index of the hightlighted menu option. Every time runmenu is called, position returns to 0, when runmenu ends the position is returned and tells the program what opt$
	oldpos=None # used to prevent the screen being redrawn every time
	x = None #control for while loop, let"s you scroll through options until return key is pressed then returns pos to program	
	# Loop until return key is pressed
	while x !=ord("\n"):
		# Action in loop if resize is True:
		if resize is True:
			y, x = screen.getmaxyx()
			screen.clear()
			curses.resize_term(y, x)
			screen.refresh()
		if pos != oldpos:
			oldpos = pos
			screen.border(0)
			screen.addstr(2,2, menu["title"], curses.A_STANDOUT) # Title for this menu
			screen.addstr(4,2, menu["subtitle"], curses.A_BOLD) #Subtitle for this menu

			# Display all the menu items, showing the "pos" item highlighted
			for index in range(optioncount):
				textstyle = n
				if pos==index:
					textstyle = h
				screen.addstr(5+index,4, "%s" % (menu["options"][index]["title"]), textstyle)
			# Now display Exit/Return at bottom of menu
			textstyle = n
			if pos==optioncount:
				textstyle = h
			screen.addstr(5+optioncount,4, "%s" % (lastoption), textstyle)
			screen.refresh()
			# finished updating screen

		x = screen.getch() # Gets user input

		# What is user input?
		if x >= ord("1") and x <= ord(str(optioncount+1)[0]):
			pos = x - ord("0") - 1 # convert keypress back to a number, then subtract 1 to get index
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
	os.system("echo -n 'Waiting for internet..'")
	while True:
		output=runProcess("ping -c 1 8.8.8.8")
		if output.find("100% packet loss")==-1 and output.find("connect: Network is unreachable")==-1:
			return
		else:
			os.system("echo -n '..'")
			sleep(2)

# This function calls showmenu and then acts on the selected item
def processmenu(menu, parent=None):
	optioncount = len(menu["options"])
	exitmenu = False
	while not exitmenu: #Loop until the user exits the menu
		getin = runmenu(menu, parent)
		if getin == optioncount:
				exitmenu = True
		elif menu["options"][getin]["type"] == "command":
			curses.def_prog_mode()		# save curent curses environment
			os.system("reset")
			if menu["options"][getin]["title"] == "Try again":
				curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
				os.system("clear")
				os.system("sudo python "+sys.argv[0])
				os._exit(0)
			screen.clear() #clears previous screen
			wait_for_internet()
			os.system(menu["options"][getin]["command"]+" && echo Please press <enter> to continue  && read input_variable") # run the command
			screen.clear() #clears previous screen on key press and updates display based on pos
			curses.reset_prog_mode()	 # reset to "current" curses environment
			curses.curs_set(1)				 # reset doesn"t do this right
			curses.curs_set(0)
		elif menu["options"][getin]["type"] == "menu":
					screen.clear() #clears previous screen on key press and updates display based on pos
					processmenu(menu["options"][getin], menu) # display the submenu
					screen.clear() #clears previous screen on key press and updates display based on pos
		elif menu["options"][getin]["type"] == "exitmenu":
					display("exiting run...."+menu["title"])
					exitmenu = True
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True,executable="/bin/bash")
    return p.stdout.read()

def add_aditional_repos_and_updating():
	curses.def_prog_mode()		# save curent curses environment
	os.system("reset")
	screen.clear()
	os.system("echo add aditional repos for installiation...")
	os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list")
	os.system("sudo apt-get install -y python-software-properties && sudo add-apt-repository -y ppa:rwky/redis")
	os.system("sudo add-apt-repository -y ppa:webupd8team/java")
	screen.clear() #clears previous screen on key press and updates display based on pos
	os.system("echo updating the package databases.... && sleep 2 &&sudo apt-get update && echo Please press <enter> to continue  && read input_variable") # run the command
	screen.clear() #clears previous screen on key press and updates display based on pos
	curses.reset_prog_mode()	 # reset to "current" curses environment
	curses.curs_set(1)				 # reset doesn"t do this right
	curses.curs_set(0)

def display(text):
	w=open("ubuntu-stater-kit.log" ,"a")
	w.write(text+"\n")
	w.close()

# Main program
if __name__ == "__main__":
	os.system("setterm -curser off && clear && figlet 'Ubuntu Starter Kit' && sleep 3 && clear && setterm -curser on")
	screen = curses.initscr() #initializes a new window for capturing key presses
	curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
	curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
	curses.start_color() # Lets you use colors when highlighting selected menu option
	screen.keypad(1) # Capture input from keypad
	y, x = screen.getmaxyx()
	resize = curses.is_term_resized(y, x)
	# Change this to use different colors when highlighting
	curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
	h = curses.color_pair(1) #h is the coloring for a highlighted menu option
	n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
	process=None#process is to add child process
	if platform.dist()[0]=="Ubuntu":
		if os.getuid() == 0:
			if check_for_internet() :
				if sys.argv[1]=="log":	
					files=open("ubuntu-stater-kit.log","w")
					files.write("")
					files.close()
					process=subprocess.Popen("gnome-terminal -e 'python logger.py'",stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True,executable="/bin/sh")		
				#add_aditional_repos_and_updating()
				processmenu(menu_data)
			else:
				processmenu(no_internet_menu)
		else:
			curses.endwin() 
			#os.system("clear")
			os.system("sudo python "+sys.argv[0])
			os._exit(0)