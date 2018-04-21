# -*- coding: utf-8 -*-
"""
Description:
This script allows you storing data in a xls file and also replace 
special characters

Created on Tue Apr 17 16:48:57 2018

@author: Luis Antonio V R
"""
import time

def save_data(data):
    '''
        Save as "xls" file the captured data and replace a special characteres.
        
        parameters:
        data: Data from port serial  
    '''    
   
    # Build text file 
    file = open('Log-'+time.strftime("%d-%m-%y")+'.xls', 'a')
    
    # Save read data
    data = data\
           .replace(b'\xb3',b'\x09')\
           .replace(b'\xc4', b'')\
           .replace(b'\xda', b'')\
           .replace(b'\xbf', b'')\
           .replace(b'\xc3', b'')\
           .replace(b'\xb4', b'')\
           .replace(b'\xc5', b'')\
           .replace(b'\xa2', b'o')\
           .replace(b'\xa1', b'i')\
           .replace(b'\xa3', b'u')\
           .replace(b'\xc0', b'')\
           .replace(b'\xc1', b'')\
           .replace(b'\xd9', b'')\
           .replace(b'\xc2', b'')\
           .replace(b'\x82', b'e')\
           .replace(b'\xa4', b'n')\
           .replace(b'\xa0', b'a') 
   
    try:
        file.write(str(data.decode().strip()) + '\n')
        data_1 = data.decode().strip()
        file.close()
        
        return str(data_1)
        
    except UnicodeDecodeError:
        file.write(str(data) + '\n')
        data_2 = data
        file.close()
        
        return str(data_2)