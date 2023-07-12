import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

RELAY1 = 20
RELAY2 = 16

FAN   = RELAY1
LIGHT = RELAY2

GPIO.setwarnings(False)
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# set up GPIO output channel
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)

#Your Telegram token key variable.
telegramBotToken = '6212499066:AAEjXEFaH_LQV8OQ6SFn_ZYpa0RbhDQyHe8'


#function to on and off devices
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return "on"

def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return "off"

def handle(msg):
    chat_id = msg['chat']['id']
    print str(chat_id)
    command = str(msg['text'])

    print 'Receive message from Telegram: %s' % command

    if 'Fan' in command or 'fan' in command:
            if 'on' in command:
                    bot.sendMessage(chat_id, str( "Fan " + on(FAN) ))
            elif 'off' in command:
                    bot.sendMessage(chat_id, str( "Fan " + off(FAN) ))
            
    elif 'Light' in command or 'light' in command:
            if 'on' in command:
                    bot.sendMessage(chat_id, str( "Light " + on(LIGHT) ))
            elif 'off' in command:
                    bot.sendMessage(chat_id, str("Light " + off(LIGHT) ))
            
bot = telepot.Bot(telegramBotToken)
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
