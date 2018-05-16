import RPi.GPIO as GPIO
import player as pl
import time


LED_RED = 24
LED_GREEN = 23
LED_WHITE = 18
LED_BLUE = 17

BUTTON_1 = 10
BUTTON_2 = 22
#BUTTON_3 = 27
BUTTON_3 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_RED, GPIO.OUT) 
GPIO.setup(LED_GREEN, GPIO.OUT) 
GPIO.setup(LED_WHITE, GPIO.OUT) 
GPIO.setup(LED_BLUE, GPIO.OUT) 

GPIO.setup(BUTTON_1, GPIO.IN) 
GPIO.setup(BUTTON_2, GPIO.IN) 
GPIO.setup(BUTTON_3, GPIO.IN) 

def btn_clicked(channel):
    if(channel == BUTTON_1):
        GPIO.output(LED_RED, GPIO.HIGH)
        pl.play('default', 'wav/a1.wav')
        GPIO.output(LED_RED, GPIO.LOW)
    elif(channel == BUTTON_2):
        GPIO.output(LED_GREEN, GPIO.HIGH)
        pl.play('default', 'wav/b1.wav')       
        GPIO.output(LED_GREEN, GPIO.LOW)
    elif(channel == BUTTON_3):
        GPIO.output(LED_WHITE, GPIO.HIGH)
        pl.play('default', 'wav/c1.wav')               
        GPIO.output(LED_WHITE, GPIO.LOW)

GPIO.add_event_detect(BUTTON_1, GPIO.RISING, callback=btn_clicked, bouncetime=500)
GPIO.add_event_detect(BUTTON_2, GPIO.RISING, callback=btn_clicked, bouncetime=500)
GPIO.add_event_detect(BUTTON_3, GPIO.RISING, callback=btn_clicked, bouncetime=500)

