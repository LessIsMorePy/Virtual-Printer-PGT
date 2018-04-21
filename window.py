# -*- coding: utf-8 -*-
"""
Description:
This is a simple user interface that allows you connecting to a serial port for 
getting data and at the same time the application it can store the data in 
a excel file.

It should be mentioned that this application was designed for a specific task. 
In this case, the main task is to receive a special format data from an antique
printer that does not work well currently.

The application has a logic to handle some issues of connexion serial port.

Created on Tue Apr 17 13:32:04 2018

@author: Luis Antonio V R
"""
import tkinter as tk
from tkinter import messagebox
import serial
from serial.serialutil import SerialException
from storage import save_data

class WindowPrinter:
    
    def __init__(self, master):
        
        self.s = None
        self.master = master
        self.com_num = tk.StringVar()
        self.com_num.set('1')
        self.text_bot = tk.StringVar()
        self.text_bot.set("Esperando conexión")
        self.text_ext = tk.StringVar()
        self.text_ext.set(".xls")
        self.text_namef = tk.StringVar()
        self.text_namef.set("L3Ene03")
        
        # Configuration root window
        self.master.iconbitmap('metro.ico')
        self.master.config(bg='white')
        self.master.title('Impresora Virtual PGT Beta')
        
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
                  padx=2)
        
        
        # Label bot
        entry_bot = tk.Entry(self.master, 
                             text=self.text_bot, 
                             width=1, 
                             bg='White', 
                             bd=0.5, 
                             font=('Consolas', 14),
                             justify='center')
        entry_bot.grid(row=1, 
                       column=0, 
                       columnspan=21, 
                       sticky='WE',
                       padx=5,
                       pady=5)
        
        # Entry COM number
        entry_com = tk.Entry(self.master, 
                             text=self.com_num, 
                             width=3, 
                             bg='White', 
                             bd=0.5, 
                             font=('Consolas', 14),
                             justify='center')
        entry_com.grid(row=0, 
                       column=2, 
                       columnspan=1, 
                       sticky='WE',
                       padx=2)
         
        # Buttons
        tk.Button(self.master, 
                  text='Conectar', 
                  borderwidth = 1, 
                  font=('Consolas', 12),
                  command=self.logic_com).grid(row=0, 
                                              column=3,
                                              padx=8,
                                              pady=20)
        
        # Scrollbar
        scroll = tk.Scrollbar(self.master)
        scroll.grid(row=3, column=21, sticky='NS')
        
        # Text
        self.text_pgt = tk.Text(self.master)
        self.text_pgt.config(font=('Times New Roman', 12),
                        height=20, width=100,
                        bg='white',
                        fg='royalblue4',
                        borderwidth=0.4,
                        yscrollcommand=scroll.set)
        self.text_pgt.grid(row = 3, 
                      column = 0, 
                      padx = 5, pady = 10,
                      ipadx = 0, ipady = 0,
                      columnspan = 20, sticky='WE') 
        scroll.config(command=self.text_pgt.yview) 
        
       
        self.read_com_port()
        
        self.master.protocol("WM_DELETE_WINDOW", self.when_close)
    
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
        c_circle.grid(row=row, column=column, padx=1, pady=1, columnspan=1)
        
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
                
    def read_com_port(self):
        """
            Reading serial port, getting data, storing data and writing data
            in the text tkinter widget every mili second. 
        """        
        
        try:
            if self.s.inWaiting() != 0:
                data = self.s.readline()
                data_str = save_data(data)
                self.text_pgt.insert('1.0', data_str + '\n')
            
        except AttributeError:
            pass
        
        self.master.after(1, self.read_com_port)
                
    def when_close(self):
        "Before closing"
        
        if messagebox.askokcancel('Cerrar Virtual Printer PGT', '¿Quieres cerrar la aplicación?'):
            try:
                self.s.close()
                
            except AttributeError:
                pass
            
            self.master.destroy()
            

if __name__ == '__main__':
    
    root = tk.Tk()
    WindowPrinter(root)
    root.mainloop()

 