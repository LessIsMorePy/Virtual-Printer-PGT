# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:48:57 2018

@author: Luis Antonio V R
"""
from window import WindowPrinter
import serial

def serial_config():
    
    # Serial configuration
    s = serial.Serial(port = 'COM3', 
                      baudrate = 38400, 
                      bytesize = 8, 
                      parity = serial.PARITY_NONE,
                      stopbits = 1)
    
    # Clean Buffer
    s.flushInput()
    s.setDTR()
    
    # State port
    print("Port: " + s.name)
    print("State: ", s.isOpen())
    
    return s

if __name__ == '__main__':
    
    #s = serial_config() 
    WindowPrinter()
    

