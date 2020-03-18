from gpiozero import Button
from signal import pause
import time
from subprocess import check_call
from subprocess import call
import os


killallcmd = "sudo supervisorctl stop all" # command to kill all supervisor run processes
boardnames = ["MLB","NHL"] #commands to run various boards/processes
timetohold = 5 # time to hold button before executing shutdown
buttonnumber = 3 # number of the button (actual pin) being used for the button
x = 0 # state tracking variable

Button.was_held = False

def held(btn):
	btn.was_held = True
	print("Button hold detected.  Shutting down.")
	time.sleep(1)
	print("-----SHUTDOWN COMMAND HERE-----")
	os.system("sudo shutdown -h now")

def released(btn):
	global x
	if not btn.was_held:
		pressed()
	time.sleep(1)
	if x == len(boardnames): # resets counter
		x = 0
	y = 0
	while y < len(boardnames):  # iterates through all boards except selected and kills them
		if y != x:
			execcommand = "sudo supervisorctl stop %s" % boardnames[y]
			os.system(execcommand)
		y = y + 1
	execcommand = "sudo supervisorctl start %s" % boardnames[x]
	os.system(execcommand)  # runs the board
	x = x + 1
	btn.was_held = False

def pressed():
	print("Button press detected.  Swapping sports.")

btn = Button(buttonnumber, hold_time=timetohold)

btn.when_held = held
btn.when_released = released

pause()

