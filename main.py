import bs_screen, bs_colourpair, bs_char
import curses, time

class ApplicationObject:

    def __init__(self):
        self.AppWindow = bs_screen.Screen(curses.initscr())
        self.AppWindow.InitScreen()
        self.AppWindow.UseColour(bs_colourpair.ColourPair)

        self.DrawIntro()
        self.AppWindow.Refresh()
        self.AppWindow.GetChar()

        self.AppWindow.TerminateScreen()

    def DrawIntro(self):
        ColumnLength = 4*20
        for row in range(32):
            for cidx, colour, char in zip(range(4), (1, 3, 2, 4), [0b001100, 0b101010, 0b111101, 0b111111]):
                self.AppWindow.PlotBrailleRect(
                    row, ColumnLength//4*cidx, row, ColumnLength//4*(cidx+1)-1, char,
                    self.AppWindow.ColourPair(0, colour)
                )

App = ApplicationObject()