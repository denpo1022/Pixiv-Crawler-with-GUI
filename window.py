import tkinter as tk
import time
from tkinter import filedialog
from crawler import crawlerMain, getTotalWorks


class CrawlerWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.font_style = ("Helvetica", 16)
        self.master = master
        self.master.title("Pixiv Crawler")
        self.master.geometry("600x450")
        self.PAD = 5
        self.work_amount = 0
        self.pack()
        self.createWindow()

    def selectDirectory(self):
        # Everytime when user press select directory button, clean the entry bar first
        self.selectDir_entry.delete("0", "end")

        # Pop up the files explorer window
        self.selectedDir = filedialog.askdirectory()

        # Insert the directory path into the entry bar
        self.selectDir_entry.insert("end", self.selectedDir)

    def startToCraw(self):
        # Three places have to be checked: "Directory", "Keyword", "Amount"
        dir_OK = keyword_OK = amount_OK = False

        if self.getTargetDirectory():
            dir_OK = True
            self.dir_warn.configure(bg="SystemButtonFace", text="")
        else:
            self.dir_warn.configure(
                bg="red", text="Target directory path cannot be empty!"
            )

        if self.getKeyword():
            keyword_OK = True
            self.keyword_warn.configure(bg="SystemButtonFace", text="")
        else:
            self.keyword_warn.configure(bg="red", text="Keyword cannot be empty!")

        if self.getUserAmounts():
            if self.getUserAmounts().isdigit():
                user_amount = int(self.getUserAmounts())
                if user_amount <= self.work_amount and user_amount > 0:
                    amount_OK = True
                    self.amount_warn.configure(bg="SystemButtonFace", text="")
                else:
                    self.amount_warn.configure(
                        bg="red",
                        text="The integer must equal or less than total works!",
                    )
            else:
                self.amount_warn.configure(
                    bg="red", text="Please input positive integer!"
                )
        else:
            self.amount_warn.configure(bg="red", text="Amount cannot be empty!")

        if dir_OK and keyword_OK and amount_OK:
            crawlerMain(
                self.getTargetDirectory(), self.getKeyword(), self.getUserAmounts()
            )

    def getWorkAmounts(self):
        if self.getKeyword():
            self.work_amount = getTotalWorks(self.getKeyword())
            self.amount_work_label.configure(
                bg="SystemButtonFace",
                text="Total {} works found".format(self.work_amount),
            )
        else:
            self.amount_work_label.configure(bg="red", text="Keyword cannot be empty!")

    def getTargetDirectory(self):
        return self.selectDir_entry.get()

    def getKeyword(self):
        return self.search_entry.get()

    def getUserAmounts(self):
        return self.amount_entry.get()

    def createWindow(self):
        # Initialize header label
        self.header_label = tk.Label(self, text="Pixiv Crawler")
        self.header_label.pack()

        # Initialize directory path group
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
            self.selectDir_frame, text="choose", command=self.selectDirectory
        )
        self.selectDir_button.pack(side=tk.RIGHT)

        # Initialize search group
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(side=tk.TOP, pady=self.PAD)
        self.search_label = tk.Label(
            self.search_frame,
            text="Type your keyword to get the amount of works:",
            font=self.font_style,
        )
        self.search_label.pack(side=tk.TOP)
        self.search_entry = tk.Entry(self.search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=self.PAD)
        self.search_button = tk.Button(
            self.search_frame, text="search", command=self.getWorkAmounts
        )
        self.search_button.pack(side=tk.RIGHT)

        # Initialize amount_work group
        self.amount_work = tk.Frame(self)
        self.amount_work.pack(side=tk.TOP, pady=self.PAD)
        self.amount_work_label = tk.Label(
            self.amount_work,
            text="Total {} works found".format(self.work_amount),
            font=self.font_style,
        )
        self.amount_work_label.pack(side=tk.TOP)

        # Initialize amount group
        self.amount_frame = tk.Frame(self)
        self.amount_frame.pack(side=tk.TOP, pady=self.PAD)
        self.amount_label = tk.Label(
            self.amount_frame,
            text="How many works you want to download?",
            font=self.font_style,
        )
        self.amount_label.pack(side=tk.TOP, pady=self.PAD)
        self.amount_entry = tk.Entry(self.amount_frame, width=8)
        self.amount_entry.pack(side=tk.TOP, pady=self.PAD)

        # Initialize download group
        self.download_frame = tk.Frame(self)
        self.download_frame.pack(side=tk.TOP, pady=self.PAD)
        self.download_button = tk.Button(
            self.download_frame, text="download", command=self.startToCraw
        )
        self.download_button.pack(side=tk.TOP, pady=self.PAD)
        self.dir_warn = tk.Label(self.download_frame, font=self.font_style)
        self.dir_warn.pack(side=tk.TOP, pady=self.PAD)
        self.keyword_warn = tk.Label(self.download_frame, font=self.font_style)
        self.keyword_warn.pack(side=tk.TOP, pady=self.PAD)
        self.amount_warn = tk.Label(self.download_frame, font=self.font_style)
        self.amount_warn.pack(side=tk.TOP, pady=self.PAD)
