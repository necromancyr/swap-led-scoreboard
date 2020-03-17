# swap-led-scoreboard
Python script to swap between led boards (NHL/MLB) and possibly others if developed.

This is pretty basic.  You need the following:
- Python3
- gpiozero
- supervisor properly setup to run ALL the boards you want run
- some led boards (NHL https://github.com/riffnshred/nhl-led-scoreboard and MLB https://github.com/MLB-LED-Scoreboard/mlb-led-scoreboard)

All you should need to do is go into the python script, make sure things are set for the commands to start/stop your board related supervisor processes.  

Also, on a long hold (time can be set in the script) the pi will shutdown.  

You can also change the button that's it's configured for - as of now, it's 3 so that you can turn the pi back on after shutting it down.  

One issue - when you do the 'shutdown' hold, it will start executing the board flip routine first.  Happy to incorporate a better way to do that, but my skills are...minimal.
