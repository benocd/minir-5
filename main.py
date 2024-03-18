# MicroPython Script to read CO2 PPM from GSS UK / MINIR-5 sensor using Raspbery Pi Pico
# http://co2meters.com/Documentation/Manuals/Manual_GC_0024_0025_0026_Revised8.pdf
# Author: Bernardo Campos Diocaretz - https://www.beno.cl

from machine import UART,Pin
import time

# Use UART pins GP 16 and 17
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
uart.write("K 1")

multiplier = 10 # Command .\r\n Returns 10

while True:
    if uart.any():
        data = uart.read().decode('utf-8')
        #print(data)
        
        # Convert bytes to string and strip whitespace
        data_str = data.strip()

        # Find the index of the first 'Z'
        z_index = data_str.find('Z')

        # Extract the substring from the first 'Z' to the next whitespace
        z_value = int(data_str[z_index + 1:z_index+7])
        
        ppm = z_value * multiplier
        print("PPM:",ppm)

        time.sleep(1)
