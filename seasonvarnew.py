from tkinter.scrolledtext import ScrolledText

import requests
from bs4 import BeautifulSoup
import re
import string
from tkinter import *
from tkinter import scrolledtext
from itertools import groupby

try:
    def seasonvar_new():
        url = "http://seasonvar.ru/"
        root = requests.get(url)
        soup = BeautifulSoup(root.content, "lxml")
        g = soup.find("div", {"class": "news"})
        for link12 in g.findAll('div'):  # собирает текст сериалов
            href3 = link12.getText().split()
            line1 = [i for i in [href3.strip() for href3 in href3] if i]
            lik = line1 # [0]= только название
            print(lik)
            write = open('C:\\Users\\netcomisaeko\\Desktop\\serials-anime.txt', "a")
            write.writelines(lik + "\n")


    # for link1 in g.findAll('a'):
    # href = link1.get('href')
    # print(href)

    def animedia():
        ser = requests.get("https://amedia.online/")
        soup =BeautifulSoup(ser.text, "lxml")
        content = soup.find("div", {"class": "section-content clearfix"})
        for link1 in content.findAll('div'):
            href21 = link1.get_text('a').split('a')
            x = href21
            new_x = [el for el, _ in groupby(x)]
            x = new_x[0].split()
            print(x)
        write = open('C:\\Users\\netcomisaeko\\Desktop\\serials-anime.txt', "a")
        write.writelines(x + "\n")
            #contentw = content.find_all("div", {"class": "newtitle"}).get_text(separator=u"<div>")



    def manga_rid():
        url = "https://mangalib.me/manga-list?tags%5Binclude%5D%5B%5D=302"
        rs = requests.get(url)



    def tkinter():
        window = Tk()
        window.title("ModBusReader")
        window.geometry('600x200')
        txt = Entry(window, width=10)
        txt.grid(column=1, row=0)

        def clickedw():
            lbl.configure(seasonvar_new)
        btn = Button(window, text="seasonvar", command=clickedw)
        btn.grid(column=2, row=0)
        btn.pack()
        lbl = Label(window, text=clickedw)
        lbl.pack()

        def clicked1():
            lbl.configure(animedia)
        btn = Button(window, text="animedia", command=clicked1)
        btn.grid(column=2, row=0)
        btn.pack()
        lbl = Label(window, text=clicked1)
        lbl.grid(column=10, row=10)
        lbl.pack()
        window.mainloop()
    tkinter()



except Exception as e:
    print(e)