import curses
import bs_char

class Screen:

    def __init__(self, window: curses.window):
        self.windowObject = window
        self.globalBackground: int = 0

    def initScreen(self):
        curses.noecho()
        curses.cbreak()
        self.windowObject.keypad(True)
        curses.start_color()
        curses.curs_set(0)

    def terminateScreen(self):
        curses.echo()
        curses.nocbreak()
        self.windowObject.keypad(False)
        curses.endwin()

    def colour(self, bg: int, fg: int) -> int:
        return bg*8+fg+1

    def colourPair(self, bg: int, fg: int) -> int:
        return curses.color_pair(self.colour(bg, fg))

    def useColour(self, colourPairs: dict):
        for group_index, group in enumerate(colourPairs.values()):
            for colour_index, colour in enumerate(group.values()):
                curses.init_pair(self.colour(group_index, colour_index), colour[1], colour[0])

    def refresh(self):
        self.windowObject.refresh()

    def setBackground(self, bg: int, fg: int = 7, char: str = "\0"):
        self.windowObject.bkgd(char, self.ColourPair(bg, fg))

    def plotChar(self, y: int, x: int, char: str, attr: int = 0):
        self.windowObject.addch(y, x, char, attr)

    def plotStr(self, y: int, x: int, string: str, attr: int = 0):
        self.windowObject.addstr(y, x, string, attr)

    def plotRect(self, y0: int, x0: int, y1: int, x1: int, char: str, attr: int = 0):
        if y0 > y1:
            y0, y1 = y1, y0
        if x0 > x1:
            x0, x1 = x1, x0
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                self.plotChar(y, x, char, attr)

    def plotBraille(self, y: int, x: int, pattern: int, attr: int = 0):
        intToKey = lambda n: \
            "Dots" \
            f"{1 if n>>5&1==1 else ''}{2 if n>>4&1==1 else ''}{3 if n>>3&1==1 else ''}" \
            f"{4 if n>>2&1==1 else ''}{5 if n>>1&1==1 else ''}{6 if n&1==1 else ''}"

        if pattern == 0:
            self.plotChar(y, x, bs_char.braille["Blank"], attr)
        else:
            self.plotChar(y, x, bs_char.braille[intToKey(pattern)], attr)

    def plotBrailleRect(self, y0: int, x0: int, y1: int, x1: int, pattern: int, attr: int = 0):
        intToKey = lambda n: \
            "Dots" \
            f"{1 if n>>5&1==1 else ''}{2 if n>>4&1==1 else ''}{3 if n>>3&1==1 else ''}" \
            f"{4 if n>>2&1==1 else ''}{5 if n>>1&1==1 else ''}{6 if n&1==1 else ''}"

        if y0 > y1:
            y0, y1 = y1, y0
        if x0 > x1:
            x0, x1 = x1, x0
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                self.plotBraille(y, x, pattern, attr)

    def getChar(self) -> int:
        return self.windowObject.getch()

if __name__ == "__main__":
    print(
        f"ncurses version {curses.ncurses_version[0]}.{curses.ncurses_version[1]}\n"
        "Can't you see these commies have my hands tied here! No maternity leave!"
    )