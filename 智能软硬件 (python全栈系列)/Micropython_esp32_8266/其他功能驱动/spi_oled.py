from machine import Pin,SPI
import Screen
import time

#d0-clk,d1-mosi
spi=SPI(1,sck=Pin(19,Pin.OUT),mosi=Pin(21,Pin.OUT))#,baudrate=24000000)

# width:128, height:64, dc-->pin5, res-->pin18 cs->gnd
s = Screen.create(128, 64, spi, Pin(5,Pin.OUT), Pin(18,Pin.OUT))
s.print('Hello, world.')
s.print('')
s.print('Hello, world.')

s.clear()
s.show()

