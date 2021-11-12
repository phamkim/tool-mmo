from datetime import date
from tkinter import *
from typing import List
from gmail import Gmail
from tool import Tool
# window = Tk()

# window.wm_title('tool')

# my_label = Label(window, text="nhập mail: ")
# my_label.grid(row=0, column=0)
# mail = Entry(window)
# mail.grid(row=0, column=1)
# btn_check = Button(window, text="check", width=10, height=2)
# btn_check.grid(row=0, column=2)

# window.mainloop()

# data = open("gmail.txt", "r")
# line = data.readlines()
# listGmail = list(map(lambda n: n.rstrip('\n'), line))
# gmailTool = Tool(listGmail)
# a = gmailTool.checkGmail()
# print(a)

data = open('yahoo.txt','r')
line = data.readlines()
listYahoo = list(map(lambda n: n.rstrip('\n'), line))

mailTool = Tool(listYahoo)
a = mailTool.checkYahoo()
print(a)