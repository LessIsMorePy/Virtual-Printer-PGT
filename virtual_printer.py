# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:32:04 2018

@author: Luis Antonio V R
"""
import tkinter as tk
#from tkinter import Canvas, StringVar()

class WindowPrinter:
    
    def __init__(self, master):
        self.master = master
        
        # Configuration root window
        self.master.iconbitmap('metro.ico')
        self.master.config(bg='white')
        self.master.title('Impresora Virtual PGT')
        
        # Draw led
        self.led(0, 0)
        
        # Label "Puerto COM"        
        labl = tk.Label(self.master, 
                        text='Puerto COM ',
                        font = ('Consolas', 14),
                        fg = 'dodgerBlue4',
                        bg = 'white')
        labl.grid(row=0, 
                  column=1, 
                  columnspan=1,
                  sticky='WE',
                  padx=8)
        
        # Entry
        com_text = tk.StringVar()
        com_text.set('00')
        entry_com = tk.Entry(self.master, 
                             text=com_text, 
                             width=3, 
                             #bg='SlateGray1',
                             bg='White', 
                             bd=0.5, 
                             font=('Consolas', 14))
        entry_com.grid(row=0, 
                       column=2, 
                       columnspan=1, 
                       sticky='WE',
                       padx=5)
        
        # Buttons
        tk.Button(self.master, 
                  text='Conectar', 
                  borderwidth = 1, 
                  font=('Consolas', 12)).grid(row=0, 
                                              column=3,
                                              padx=8,
                                              pady=20)
        
    
    def led(self, row=0, column=0, color='lavender'):    
        '''
            Draw a led inicator.
        '''
        # Root
        c_circle = tk.Canvas(self.master, width=30, height=30, bg='white')
        c_circle.grid(row=row, column=column, padx=5, pady=5, sticky='W')
        
        # Circle 
        c_circle.create_oval(5, 5, 30, 30, width=0, fill=color)
        
        
if __name__ == '__main__':
    
    root = tk.Tk()
    gui = WindowPrinter(root)
    root.mainloop()
    # comment
