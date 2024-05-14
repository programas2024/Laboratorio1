from tkinter import Tk
from similar import MusicPlayer

class Main:
    def main(self):
        root = Tk()
        app = MusicPlayer(root)
        root.mainloop()

if __name__ == "__main__":
    main_app = Main()
    main_app.main()
