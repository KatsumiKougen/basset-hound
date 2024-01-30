import bs_screen, bs_colourpair
import curses

AppScreen = bs_screen.Screen(curses.initscr())
AppScreen.InitScreen()
AppScreen.UseColour(bs_colourpair.ColourPair)
AppScreen.TerminateScreen()