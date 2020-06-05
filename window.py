import tkinter as tk
from tkinter import filedialog
from crawler import crawlerMain, getTotalWorks


class CrawlerWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.font_style = ("Helvetica", 16)
        self.master = master
        self.master.title("Pixiv Crawler")
        self.master.geometry("600x400")
        self.PAD = 5
        self.work_amount = 0
        self.pack()
        self.createWindow()

    def initCrawler(self):
        crawlerMain(self.getKeyword(), self.getTargetDirectory())

    def selectDirectory(self):
        # Everytime when user press select directory button, clean the entry bar first
        self.selectDir_entry.delete("0", "end")

        # Pop up the files explorer window
        self.selectedDir = filedialog.askdirectory()

        # Insert the directory path into the entry bar
        self.selectDir_entry.insert("end", self.selectedDir)

    def getWorkAmounts(self):
        self.work_amount = getTotalWorks(self.getKeyword())
        self.amount_work_label = tk.Label(
            self.amount_work,
            text="Total {} works found".format(self.work_amount),
            font=self.font_style,
        )
        self.amount_work_label.pack(side=tk.TOP)

    def getTargetDirectory(self):
        return self.selectDir_entry.get()

    def getKeyword(self):
        return self.search_entry.get()

    def createWindow(self):
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
            self.selectDir_frame, text="Choose", command=self.selectDirectory
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
            self.search_frame, text="search", command=self.getWorkAmounts,
        )
        self.search_button.pack(side=tk.RIGHT)

        # initialize amount_work group
        self.amount_work = tk.Frame(self)
        self.amount_work.pack(side=tk.TOP, pady=self.PAD)
