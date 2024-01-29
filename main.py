import bs_screen
import curses

AppScreen = bs_screen.Screen(curses.initscr())
bs_screen.InitScreen(AppScreen)
AppScreen.Start()
bs_screen.TerminateScreen(AppScreen)