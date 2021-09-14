#!/usr/bin/env python3
import RPi.GPIO as GPIO


class LEDs():
    ON = False
    OFF = True

    __Debug_LED_A_pin: int
    __Debug_LED_B_pin: int
    __Debug_LED_C_pin: int
    __Debug_LED_D_pin: int
    __Debug_LED_A_state: bool
    __Debug_LED_B_state: bool
    __Debug_LED_C_state: bool
    __Debug_LED_D_state: bool

    # コンストラクタ
    def __init__(self,pinA, pinB, pinC, pinD):
        self.__Debug_LED_A_pin = pinA
        self.__Debug_LED_B_pin = pinB
        self.__Debug_LED_C_pin = pinC
        self.__Debug_LED_D_pin = pinD
        GPIO.setup(self.__Debug_LED_A_pin, GPIO.OUT)
        GPIO.setup(self.__Debug_LED_B_pin, GPIO.OUT)
        GPIO.setup(self.__Debug_LED_C_pin, GPIO.OUT)
        GPIO.setup(self.__Debug_LED_D_pin, GPIO.OUT)

    # 整数型からON/OFF制御するための関数
    def setByte(self, byte):
        self.Debug_LED_A = (byte & 0x0001) == 1
        self.Debug_LED_B = ((byte >> 2) & 0x0001) == 1
        self.Debug_LED_C = ((byte >> 3) & 0x0001) == 1
        self.Debug_LED_D = ((byte >> 4) & 0x0001) == 1
    
    # 個別制御のためのプロパティ
    @property
    def Debug_LED_A(self):
        return self.__Debug_LED_A_state
    
    @Debug_LED_A.setter
    def Debug_LED_A(self, val):
        if (type(val) is bool):
            self.__Debug_LED_A_state = val
            GPIO.output(self.__Debug_LED_A_pin, self.__Debug_LED_A_state)

    @property
    def Debug_LED_B(self):
        return self.__Debug_LED_B_state
    
    @Debug_LED_B.setter
    def Debug_LED_B(self, val):
        if (type(val) is bool):
            self.__Debug_LED_B_state = val
            GPIO.output(self.__Debug_LED_B_pin, self.__Debug_LED_A_state)

    @property
    def Debug_LED_C(self):
        return self.__Debug_LED_C_state
    
    @Debug_LED_C.setter
    def Debug_LED_C(self, val):
        if (type(val) is bool):
            self.__Debug_LED_C_state = val
            GPIO.output(self.__Debug_LED_C_pin, self.__Debug_LED_A_state)

    @property
    def Debug_LED_D(self):
        return self.__Debug_LED_D_state
    
    @Debug_LED_D.setter
    def Debug_LED_D(self, val):
        if (type(val) is bool):
            self.__Debug_LED_D_state = val
            GPIO.output(self.__Debug_LED_D_pin, self.__Debug_LED_A_state)