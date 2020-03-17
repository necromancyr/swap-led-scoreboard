from gpiozero import Button
from signal import pause
import time
from subprocess import check_call
from subprocess import call
import os


killallcmd = "sudo supervisorctl stop all" # command to kill all supervisor run processes
boardswapcmds = ["sudo supervisorctl start MLB","sudo supervisorctl start NHL"] #commands to run various boards/processes
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
	if x == len(boardswapcmds): # resets counter
		x = 0
	os.system(killallcmd)  # kills all supervisor processes
	os.system(boardswapcmds[x])  # kills all supervisor processes
	x = x + 1
	btn.was_held = False

def pressed():
	print("Button press detected.  Swapping sports.")

btn = Button(buttonnumber, hold_time=timetohold)

btn.when_held = held
btn.when_released = released

pause()

