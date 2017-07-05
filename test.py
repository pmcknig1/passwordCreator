#!/usr/bin/python

from Tkinter import *

class Example(Frame):

   def __init__ (self, parent):
      Frame.__init__(self, parent, background="white")
      self.parent = parent
      self.initUI()

   def initUI(self):
      width = 16*25
      height = 9*25
      screenWidth = self.parent.winfo_screenwidth()
      screenHeight = self.parent.winfo_screenheight()

      x = (screenWidth - width) / 2
      y = (screenHeight - height) / 2

      self.parent.title("Password Creator")
      self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

      self.pack(fill=BOTH, expand=1)


def main():
   window = Tk()
   app = Example(window)
   window.mainloop()

if __name__ == '__main__':
   main()
