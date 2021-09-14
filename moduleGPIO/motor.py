#!/usr/bin/env python3
import RPi.GPIO as GPIO
import spidev
# import GPIO.hcsr04

class MCP3204():        # ADC (MCP3204)

   def __init__(self):
       self.d1tbl = [0x00, 0x40, 0x80, 0xC0]       # send data 1
       self.spi = spidev.SpiDev()

   def rdadc(self, chn):     # Read ADC chn=0,1,2,3 (INTEGER)
       self.spi.open(0, 0) # bus0, CE0
       self.spi.max_speed_hz = 1000000  # 1MHz
       rd = self.spi.xfer2([0x06, self.d1tbl[chn], 0x00])
       self.spi.close()
       
       ret = rd[1] * 256 + rd[2]
       return ret
       
class Motor():

    __shunt_val = 0.1
    CCW = True
    CW = False
    LS_isLimit = False

    __Rotate = True
    __Stop = False
    __adc: MCP3204
    __Direction_pin: int
    __Enable_pin: int
    __ls_lower_pin: int
    __ls_upper_pin: int

    def __init__(self, enable_pin, direction_pin, ls_upper_pin, ls_lower_pin):
        self.__Enable_pin = enable_pin
        self.__Direction_pin = direction_pin
        self.__ls_lower_pin = ls_lower_pin
        self.__ls_upper_pin = ls_upper_pin
        GPIO.setup(self.__Enable_pin, GPIO.OUT)
        GPIO.setup(self.__Direction_pin, GPIO.OUT)
        GPIO.setup(self.__ls_upper_pin, GPIO.IN)
        GPIO.setup(self.__ls_lower_pin, GPIO.IN)
        self.__adc = MCP3204()

    def Stop(self):
        GPIO.output(self.__Enable_pin, self.__Stop)
    
    def Rotate(self, direction):
        GPIO.output(self.__Direction_pin, direction)
        GPIO.output(self.__Enable_pin, self.__Rotate)

    def GetCurrent(self):
        # シャント抵抗の電圧値を計算
        voltage = self.__adc.rdadc(0) * (5 / (2 ^ 12))
        print(voltage)
        current = voltage / self.__shunt_val
        print(current)
        return current

    def GetDistance(self):
        a = 1
        
    @property
    def LS_Lower(self):
        return GPIO.input(self.__ls_lower_pin)

    @property
    def LS_Upper(self):
        return GPIO.input(self.__ls_upper_pin)

