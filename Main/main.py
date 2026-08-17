from machine import Pin, time_pulse_us
from functions import safety_protocol, initial, current, intrusion_protocol
import time

green_led = Pin(16, Pin.OUT) # Code that sets up the green LED
red_led = Pin(15, Pin.OUT) # Code that sets up the red LED
alarm = Pin(11, Pin.OUT) # Code that sets up active piezo buzzer
button = Pin(5, Pin.IN, Pin.PULL_DOWN) # Code that sets up button
sound_speed = 340 # Speed of sound
trig_pulse = 10 # How long the frequency pulse pulses
trigger = Pin(9, Pin.OUT) # Code that sets up the ultrasonic sensor trigger 
echo = Pin(8, Pin.IN) # Code that sets up the ultrasonic sensor echo 
ini = 0 # Variable set up for the initial time reading
curr = 0 # Variable set up for the current time reading

time.sleep(20) # Gives the user time to leave the room before the system activates

ini = initial()

while True:
    curr = current()
    if curr + 5 < int(ini): # Checks to see if the doors been opened by seeing if the echo distance is shortened 
        green_led.value(0)
        intrusion_protocol()
        break
    else:
        safety_protocol()
        
