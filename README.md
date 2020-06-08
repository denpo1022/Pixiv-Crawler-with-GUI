# Pixiv-Crawler-with-GUI

Try to use Tkinter GUI with easy Pixiv website crawler together.

![Imgur](https://i.imgur.com/oMrLKhD.jpg)

## Current function

1. You can select a directory for saving pictures.
2. Input the keyword and click "search" button will show you how many works on Pixiv now.
3. You can download images based on your keyword. It will download first page of illustration works (which means 60 works with equal or more than 60 original size pictures) automatically at Pixiv website. The pictures are ordered from latest to oldest.

## How to use

I use `python 3.8.2` on Windows 10 with Powershell 7:

`python .\main.py`

On Linux:

`python main.py` or `python3 main.py`

## TODO

1. Let users can specify how many works they want to download.
2. Add "pause", "stop", "continue" function.
3. Add multi-thread procession.
4. Add more comments for explaining the codes.
5. Maybe rewrite `crawler.py` to make it looks tidy and neat.

Welcome any comment or issue for discussion.
