import bs_screen, bs_colourpair
import curses

AppScreen = bs_screen.Screen(curses.initscr())
bs_screen.InitScreen(AppScreen)
AppScreen.Start()
AppScreen.UseColour(bs_colourpair.ColourPair)
bs_screen.TerminateScreen(AppScreen)