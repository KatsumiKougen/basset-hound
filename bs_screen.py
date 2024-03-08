import curses
import bs_char

class Screen:

    def __init__(self, window: curses.window):
        self.WindowObject = window
        self.GlobalBackground: int = 0

    def InitScreen(self):
        curses.noecho()
        curses.cbreak()
        self.WindowObject.keypad(True)
        curses.start_color()
        curses.curs_set(0)

    def TerminateScreen(self):
        curses.echo()
        curses.nocbreak()
        self.WindowObject.keypad(False)
        curses.endwin()

    def Colour(self, bg: int, fg: int) -> int:
        return bg*8+fg+1

    def ColourPair(self, bg: int, fg: int) -> int:
        return curses.color_pair(self.Colour(bg, fg))

    def UseColour(self, colour_pairs: dict):
        for group_index, group in enumerate(colour_pairs.values()):
            for colour_index, colour in enumerate(group.values()):
                curses.init_pair(self.Colour(group_index, colour_index), colour[1], colour[0])

    def Refresh(self):
        self.WindowObject.refresh()

    def SetBackground(self, bg: int, fg: int = 7, char: str = "\0"):
        self.WindowObject.bkgd(char, self.ColourPair(bg, fg))

    def PlotChar(self, y: int, x: int, char: str, attr: int = 0):
        self.WindowObject.addch(y, x, char, attr)

    def PlotStr(self, y: int, x: int, string: str, attr: int = 0):
        self.WindowObject.addstr(y, x, string, attr)

    def PlotRect(
        self, y0: int, x0: int, y1: int, x1: int,
        char: str, attr: int = 0
    ):
        if y0 > y1:
            y0, y1 = y1, y0
        if x0 > x1:
            x0, x1 = x1, x0
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                self.PlotChar(y, x, char, attr)

    def PlotBraille(self, y: int, x: int, pattern: int, attr: int = 0):
        IntToKey = lambda n: \
            "Dots" \
            f"{1 if n>>5&1==1 else ''}{2 if n>>4&1==1 else ''}{3 if n>>3&1==1 else ''}" \
            f"{4 if n>>2&1==1 else ''}{5 if n>>1&1==1 else ''}{6 if n&1==1 else ''}"

        if pattern == 0:
            self.PlotChar(y, x, bs_char.Braille["Blank"], attr)
        else:
            self.PlotChar(y, x, bs_char.Braille[IntToKey(pattern)], attr)

    def PlotBrailleRect(
        self, y0: int, x0: int, y1: int, x1: int,
        pattern: int, attr: int = 0
    ):
        IntToKey = lambda n: \
            "Dots" \
            f"{1 if n>>5&1==1 else ''}{2 if n>>4&1==1 else ''}{3 if n>>3&1==1 else ''}" \
            f"{4 if n>>2&1==1 else ''}{5 if n>>1&1==1 else ''}{6 if n&1==1 else ''}"

        if y0 > y1:
            y0, y1 = y1, y0
        if x0 > x1:
            x0, x1 = x1, x0
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                self.PlotBraille(y, x, pattern, attr)

    def GetChar(self) -> int:
        return self.WindowObject.getch()

if __name__ == "__main__":
    print(
        f"ncurses version {curses.ncurses_version[0]}.{curses.ncurses_version[1]}\n"
        "Can't you see these commies have my hands tied here! No maternity leave!"
    )