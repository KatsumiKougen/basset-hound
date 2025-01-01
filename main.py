import bs_screen, bs_colourpair, bs_char
import curses, time

class ApplicationObject:

    def __init__(self):
        self.appWindow = bs_screen.Screen(curses.initscr())
        self.appWindow.initScreen()
        self.appWindow.useColour(bs_colourpair.colourPair)

        self.drawIntro()
        self.appWindow.refresh()
        self.appWindow.getChar()

        self.appWindow.terminateScreen()

    def drawIntro(self):
        columnLength = 4*20
        for row in range(32):
            for cidx, colour, char in zip(range(4), (1, 3, 2, 4), [0b001100, 0b101010, 0b111101, 0b111111]):
                self.appWindow.plotBrailleRect(
                    row, columnLength//4*cidx, row, columnLength//4*(cidx+1)-1, char,
                    self.appWindow.colourPair(0, colour)
                )

app = ApplicationObject()