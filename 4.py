import RPi.GPIO as GPIO 
from flask import Flask, request

#Define GPIO pin
led_pin = 21

#set GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#Create Flask app
app = Flask(__name__)

#Define route to handle HTTP POST request
@app.route('/',methods=['POST'])
def handle_post():
	message = request.get_data(as_text=True)
	if message == "ON":
		GPIO.output(led_pin, GPIO.HIGH)
	elif message == "OFF":
		GPIO.output(led_pin, GPIO.LOW)
        return 'OK'

if __name__ =='__main__':
	app.run(host='0.0.0.0', port=8080)
