# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:32:04 2018

@author: Luis Antonio V R
"""
import tkinter as tk
import serial
from serial.serialutil import SerialException
#from tkinter import Canvas, StringVar()

class WindowPrinter:
    
    def __init__(self):
        self.s = None
        self.master = tk.Tk()#master
        self.com_num = tk.StringVar()
        self.com_num.set('1')
        
        
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
        #com_text = tk.StringVar()
        #com_text.set('1')
        entry_com = tk.Entry(self.master, 
                             text=self.com_num, 
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
                  font=('Consolas', 12),
                  command=self.conectarCOM).grid(row=0, 
                                              column=3,
                                              padx=8,
                                              pady=20)
        self.master.mainloop()
    
    def IniciaPuertoSerie(self, COMnumero):
        '''
            Conecta con el puerto serie de comunicaciones, sí lo hay.
        '''

        # Configuración general para la comunicación serial
        self.s = serial.Serial(port = COMnumero, 
                               baudrate = 38400, 
                               bytesize = 8, 
                               parity = serial.PARITY_NONE,
                               stopbits = 1)

        # Limpia cualquier dato que haya quedado en el buffer
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
            Set a color to the led
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
    
    def conectarCOM(self):
        '''
            Conecta y evalua el estado del puerto de comunicaciones COM
        '''
        # Obtiene el nuevo valor
        com = 'COM' + self.com_num.get()
        
        try:
            try:
                if self.s.isOpen() == True:
                    
                    if self.s.name == com:
                        self.led_color(1)
                        #self.bot.set('Esperando RPE')
                       
                    else:
                        self.led_color(2)
                        #self.bot.set('Acceso negado')
                        self.s.close()
                        
                elif self.s.isOpen() == False:
                    
                    self.s = self.IniciaPuertoSerie(com)
      
                    if self.s.name == com:
                        self.led_color(1)
                        #self.bot.set('Esperando RPE')
                        
            except AttributeError:
                
                    self.s = self.IniciaPuertoSerie(com)
      
                    if self.s.name == com:
                        self.led_color(1)
                        #self.bot.set('Esperando RPE')
                    
        except SerialException:
            
                self.led_color(2)
                #self.bot.set('Acceso negado')
        
