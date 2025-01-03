import bs_screen, bs_colourpair, bs_char
from textual.app import *
from textual.widgets import *

class BS_AppObject(App):
    
    TITLE = "basset-hound"
    SUB_TITLE = "Untitled"
    CSS_PATH = "bs_style.css"
    
    def compose(self):
        print("composing")
        yield Header()
        yield Static("basset-hound")
        yield Button("exit", id="BS_ExitApp")
    
    def on_button_pressed(self, event: Button):
        print("pressed")
        self.exit(event.id)

if __name__ == "__main__":
    app = BS_AppObject()
    app.run()