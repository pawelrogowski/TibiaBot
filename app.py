import tkinter as tk
from window_manager import get_tibia_windows, get_window_id
from utils import send_key
from time import sleep
WINDOW_ID = int(get_window_id(), 16)
APP_TITLE = "EyePatch BOT"

class App:
    def __init__(self, master):
        self.master = master
        self.master.title(f"{APP_TITLE}")

        # Create the menu bar
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Create a dropdown list
        self.var = tk.StringVar(master)
        self.var.set("Pick a Client")
        clientmenu = tk.Menu(menubar, tearoff=0)
        for client in get_tibia_windows():
            clientmenu.add_command(label=client, command=lambda c=client: self.select_client(c))
        menubar.add_cascade(label="Pick Client", menu=clientmenu)

        # Add the menu bar to the master window
        master.config(menu=menubar)


        # Create a button
        self.button = tk.Button(master, text="Start EyePatch", command=self.startBot)
        self.button.pack()

        self.buttonKey = tk.Button(master, text="Send Key", command=self.sendKey)
        self.buttonKey.pack()

    def select_client(self, client):
        self.var.set(client)
        self.master.title(f"{client} - {APP_TITLE}")

    def open_file(self):
        print("Opening file...")

    def save_file(self):
        print("Saving file...")

    def startBot(self):
        tibia_window = self.var.get()
        if tibia_window != "Pick a Client":
            print(f"Proceeding with Tibia window '{tibia_window}'")

    def sendKey(self):
        key = "F7"
        window_id = self.var.get()
        send_key(key, window_id)




if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.minsize(200, 50)
    print(f"{WINDOW_ID}")
    root.mainloop()
