import curses

class Screen:

    def __init__(self, window: curses.window):
        self.WindowObject = window

    def Start(self):
        self.WindowObject.clear()
        self.PlotRect(1, 1, 3, 3, "a", curses.color_pair(0))
        self.Refresh()
        self.WindowObject.getch()

    def Refresh(self):
        self.WindowObject.refresh()

    def PlotCh(self, y: int, x: int, char: str, attr: int = 0):
        self.WindowObject.addch(y, x, char, attr)

    def PlotStr(self, y: int, x: int, string: str, attr: int = 0):
        self.WindowObject.addstr(y, x, string, attr)

    def PlotRect(
        self, y0: int, y1: int, x0: int, x1: int,
        char: str, attr: int = 0
    ):
        for y in range(y0, y1+1):
            self.WindowObject.addnstr(y, x0, char, x1-x0, attr)

def InitScreen(screen: Screen):
    curses.noecho()
    curses.cbreak()
    screen.WindowObject.keypad(True)
    curses.start_color()

def TerminateScreen(screen: Screen):
    curses.echo()
    curses.nocbreak()
    screen.WindowObject.keypad(False)
    curses.endwin()

if __name__ == "__main__":
    print(
        f"ncurses version {curses.ncurses_version[0]}.{curses.ncurses_version[1]}\n"
        "Can't you see these commies have my hands tied here! No maternity leave!"
    )