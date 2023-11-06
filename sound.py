import RPi.GPIO as GPIO
import time
import requests
import time
import random

BASE_URL = "https://api-v2.voicemonkey.io/trigger?token=7c2452efc861589f35260ed8e952d732_e6d3077cb95c47f9d0e1b556f14b06dd&device="

channel = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

last = 0

def sendRequest(id):
	global BASE_URL
	url = f"{BASE_URL}{id}"
	print(url)
	response = requests.post(url, json={})
	print(response.text)

def callback(channel):
	global last
	if GPIO.input(channel) and time.time() - last > 20:
		last = time.time()
		sendRequest(hannah_bed_id)

if __name__ == "__main__":

	random_sound_timer = 0
	GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
	GPIO.add_event_callback(channel, callback)

	id_list = ["monkey--arrived-home", "monkey--keyboard", "monkey--small-talk", "monkey-one", "monkey-two", "monkey-three", "monkey-four"]
	hannah_bed_id = "monkey--hannah-bed"

	while True:
		time.sleep(1)
		if time.time() - random_sound_timer > 1500:
			print("Playing random sound")
			random_sound_timer = time.time()
			random_id = random.randint(0,len(id_list) -1 )
			sendRequest(id_list[random_id])

