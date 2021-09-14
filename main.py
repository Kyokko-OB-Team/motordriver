#!/usr/bin/env python3
import RPi.GPIO as GPIO
import moduleGPIO.motor as motor
import moduleGPIO.led as LED

import sys
import time
import signal

Current_Lim = 4.0
Motor: motor.Motor
Led: LED.LEDs

# プログラム開始時の処理
def setup():
    global Motor
    print("!!!Set up!!!")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    Motor = motor.Motor(27, 26, 12, 13)
    Led = LED.LEDs(21, 20, 19, 18)

# プログラム終了時の処理
def cleanup():
    global Motor
    print("!!!Clean up!!!")
    # Cleanup処理いろいろ

    # モーター駆動停止
    Motor.Stop()
    print("!!!Clean up Done!!!")

# タスクキルされたときに入るイベント
def sig_handler(signum, frame) -> None:
    sys.exit(1)

def Motor_monitor():
    global Motor
    current = Motor.GetCurrent()
    # モーター電流値監視
    if (current >= Current_Lim):
        Motor.Stop()
    
    # モーター距離センサ監視

    # モーターLS監視
    if (Motor.LS_Lower is Motor.LS_isLimit):
        Motor.Stop()

    elif (Motor.LS_Upper is Motor.LS_isLimit):
        Motor.Stop()

def main():
    setup()
    signal.signal(signal.SIGTERM, sig_handler)
    try:
        while(True):
            # 受信確認

            # モーター状態確認
            Motor_monitor()
            # 10ms sleep
            time.sleep(1)

    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        cleanup()
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)



if __name__ == "__main__":
    sys.exit(main())