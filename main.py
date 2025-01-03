import bs_colourpair, bs_char
from textual.app import *
from textual.widgets import *
from textual.containers import *

BS_projectName = "Untitled"
BS_canvasSize = [80, 25]
BS_canvasCoordinate = [0, 0]

class BS_Canvas(Static):
    
    def on_mount(self):
        self.styles.width = BS_canvasSize[0]
        self.styles.height = BS_canvasSize[1]

class BS_CanvasContainer(Vertical):
    
    def compose(self):
        yield BS_Canvas()
        yield Label(f"{BS_canvasSize[0]}x{BS_canvasSize[1]}, coord: ({BS_canvasCoordinate[0]}, {BS_canvasCoordinate[1]})")

class BS_AppObject(App):
    
    TITLE = "basset-hound"
    SUB_TITLE = "Untitled"
    CSS_PATH = "bs_style.css"
    
    def compose(self):
        yield Header()
        yield BS_CanvasContainer()

if __name__ == "__main__":
    app = BS_AppObject()
    app.run()