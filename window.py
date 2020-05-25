import tkinter as tk
from tkinter import filedialog
from crawler import crawler_main


class CrawlerWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.font_style = ("Helvetica", 16)
        self.master = master
        self.master.title("Pixiv Crawler")
        self.master.geometry("600x400")
        self.PAD = 5
        self.pack()
        self.create_window()

    def command_init_crawler(self):
        crawler_main(self.get_keyword(), self.get_target_directory())

    def command_select_directory(self):
        self.selectDir_entry.delete("0", "end")
        self.selectedDir = filedialog.askdirectory()
        self.selectDir_entry.insert("end", self.selectedDir)

    def get_target_directory(self):
        return self.selectDir_entry.get()

    def get_keyword(self):
        return self.search_entry.get()

    def create_window(self):

        # initialize header label
        self.header_label = tk.Label(self, text="Pixiv Crawler")
        self.header_label.pack()

        # initialize directory path group
        self.selectDir_frame = tk.Frame(self)
        self.selectDir_frame.pack(side=tk.TOP, pady=self.PAD)
        self.selectDir_label = tk.Label(
            self.selectDir_frame,
            text="Select your directory for saving pictures:",
            font=self.font_style,
        )
        self.selectDir_label.pack(side=tk.TOP)
        self.selectDir_entry = tk.Entry(self.selectDir_frame, width=60)
        self.selectDir_entry.pack(side=tk.LEFT, padx=self.PAD)
        self.selectDir_button = tk.Button(
            self.selectDir_frame, text="Choose", command=self.command_select_directory
        )
        self.selectDir_button.pack(side=tk.RIGHT)

        # initialize search group
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(side=tk.TOP, pady=self.PAD)
        self.search_label = tk.Label(
            self.search_frame,
            text="Type your keyword for searching:",
            font=self.font_style,
        )
        self.search_label.pack(side=tk.TOP)
        self.search_entry = tk.Entry(self.search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=self.PAD)
        self.search_button = tk.Button(
            self.search_frame, text="search", command=self.command_init_crawler,
        )
        self.search_button.pack(side=tk.RIGHT)
