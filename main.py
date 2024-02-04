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
        ColumnLength = 24
        for row in range(32):
            for cidx, colour in enumerate((1, 3, 2, 4)):
                for idx, char in enumerate(
                    [bs_char.Braille["Dots123456"], *list(bs_char.Shade.values())]
                ):
                    self.AppWindow.PlotRect(
                        row, ColumnLength//4*idx+ColumnLength*cidx,
                        row, ColumnLength//4*(idx+1)-1+ColumnLength*cidx,
                        char,
                        self.AppWindow.ColourPair(0, colour)
                    )

App = ApplicationObject()