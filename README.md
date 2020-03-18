# swap-led-scoreboard
Python script to swap between led boards (NHL/MLB) and possibly others if developed.

This is pretty basic.  You need the following:
- Python3
- gpiozero
- supervisor properly setup to run ALL the boards you want run
- some led boards (NHL https://github.com/riffnshred/nhl-led-scoreboard and MLB https://github.com/MLB-LED-Scoreboard/mlb-led-scoreboard)

All you should need to do is go into the python script, make sure things are set for the names of your supervisor processesfor your led-boards.  

Specifically, the available settings are:
**boardnames** - list of the names of your supervisor processes
**timetohold** - number of seconds to hold the button until the Pi shuts down.
**buttonnumber** - pin number your using for your button (using 3 will let you restart the Pi via a button press)

One issue - when you do the 'shutdown' hold, it will start executing the board flip routine first.  Happy to incorporate a better way to do that, but my skills are...minimal.
