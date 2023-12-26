from Client.app_gui import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Semester Planer")
    root.resizable(0,0)
    app = Frame(root)
    
    app.mainloop()


if __name__ == "__main__":
    main()