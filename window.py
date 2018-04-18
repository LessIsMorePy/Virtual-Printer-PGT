# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:32:04 2018

@author: Luis Antonio V R
"""
import tkinter as tk
from tkinter import messagebox
import serial
from serial.serialutil import SerialException

class WindowPrinter:
    
    def __init__(self):
        
        self.s = None
        self.master = tk.Tk()#master
        self.com_num = tk.StringVar()
        self.com_num.set('1')
        self.text_bot = tk.StringVar()
        self.text_bot.set("Esperando conexión")
        
        # Configuration root window
        self.master.iconbitmap('metro.ico')
        self.master.config(bg='white')
        self.master.title('Impresora Virtual PGT')
        
        # Draw led
        self.led(0, 0)
        
        # Label "Puerto COM"        
        labl = tk.Label(self.master, 
                        text='Puerto COM',
                        font = ('Consolas', 14),
                        fg = 'dodgerBlue4',
                        bg = 'white',
                        justify='center')
        labl.grid(row=0, 
                  column=1, 
                  columnspan=1,
                  sticky='WE',
                  padx=8)
        
        # Label bot
        entry_bot = tk.Entry(self.master, 
                             text=self.text_bot, 
                             width=1, 
                             #bg='Azure',
                             bg='White', 
                             bd=0.5, 
                             font=('Consolas', 14),
                             justify='center')
        entry_bot.grid(row=1, 
                       column=0, 
                       columnspan=4, 
                       sticky='WESN',
                       padx=5,
                       pady=5)
        
        # Entry
        entry_com = tk.Entry(self.master, 
                             text=self.com_num, 
                             width=3, 
                             #bg='SlateGray1',
                             bg='White', 
                             bd=0.5, 
                             font=('Consolas', 14),
                             justify='center')
        entry_com.grid(row=0, 
                       column=2, 
                       columnspan=1, 
                       sticky='WE',
                       padx=5)
        
        # Buttons
        tk.Button(self.master, 
                  text='Conectar', 
                  borderwidth = 1, 
                  font=('Consolas', 12),
                  command=self.logic_com).grid(row=0, 
                                              column=3,
                                              padx=8,
                                              pady=20)
        
        self.master.protocol("WM_DELETE_WINDOW", self.when_close)
        self.master.mainloop()
    
    def start_com(self, COMnumero):
        '''
            Start the serial port.
        '''

        # General configuration
        self.s = serial.Serial(port = COMnumero, 
                               baudrate = 38400, 
                               bytesize = 8, 
                               parity = serial.PARITY_NONE,
                               stopbits = 1)

        # Clean any data at buffer
        self.s.flushInput()
        self.s.setDTR()

        return self.s
    
    def led(self, row=0, column=0, color='lavender'):    
        '''
            Draw a led inicator.
        '''
        # Root
        c_circle = tk.Canvas(self.master, width=30, height=30, bg='white')
        c_circle.grid(row=row, column=column, padx=5, pady=5, sticky='W')
        
        # Circle 
        c_circle.create_oval(5, 5, 30, 30, width=0, fill=color)
        
    def led_color(self, state=0):
        '''
            Set a color led
        '''
        if state == 0:
            color = 'lavender' 
        elif state == 1:
            color = 'green2'
        elif state == 2:
            color = 'yellow'
        else:
            color = 'red' 

        self.led(row=0, column=0, color=color)
    
    def logic_com(self):
        '''
            Logic to prepare and connect in the correct way the COM port
        '''
        # Get COM value
        com = 'COM' + self.com_num.get()
        
        # Logic
        try:
            try:
                if self.s.isOpen() == True:
                    
                    if self.s.name == com:
                        self.led_color(1)
                        self.text_bot.set('Acceso a {}'.format(com))
                       
                    else:
                        self.led_color(2)
                        self.text_bot.set('Acceso negado a {}'.format(com))
                        self.s.close()
                        
                elif self.s.isOpen() == False:
                    
                    self.s = self.start_com(com)
      
                    if self.s.name == com:
                        self.led_color(1)
                        self.text_bot.set('Acceso a {}'.format(com))
                        
            except AttributeError:
                
                    self.s = self.start_com(com)
      
                    if self.s.name == com:
                        self.led_color(1)
                        self.text_bot.set('Acceso a {}'.format(com))
                    
        except SerialException:
            
                self.led_color(2)
                self.text_bot.set('Acceso negado a {}'.format(com))
    def when_close(self):
        "Before closing"
        
        if messagebox.askokcancel('Cerrar Virtual Printer PGT', '¿Quieres cerrar la aplicación?'):
        #print(stop_stream.do_run)
        #stop_stream.closeConnection()
        #stop_stream.shutdown = True
            self.master.destroy()
            #return break
