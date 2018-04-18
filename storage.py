# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:48:57 2018

@author: Luis Antonio V R
"""

def save_data(data):
    '''
        Save and print the captured data.
        
        parameters:
        data: Data from port serial  
    '''    
   
    # Build text file 
    archivo = open('Log-'+strftime("%d-%m-%y")+'.xls', 'a')
    
    # Save read data
    data = data.replace(b'\xb3',b'\x09').replace(b'\xc4', b'').replace(b'\xda', b'').replace(b'\xbf', b'').replace(b'\xc3', b'').replace(b'\xb4', b'').replace(b'\xc5', b'').replace(b'\xa2', b'o').replace(b'\xa1', b'i').replace(b'\xa3', b'u').replace(b'\xc0', b'').replace(b'\xc1', b'').replace(b'\xd9', b'').replace(b'\xc2', b'').replace(b'\x82', b'e').replace(b'\xa4', b'n').replace(b'\xa0', b'a') 
   
    try:
        archivo.write(str(data.decode().strip()) + '\n')
        print(data.decode().strip())
        
    except UnicodeDecodeError:
        
        archivo.write(str(data) + '\n')
        print(data)
    
    archivo.close()
    

