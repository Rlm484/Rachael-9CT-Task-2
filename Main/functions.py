from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # Speed of Sound in Air (m/s)
TRIG_PULSE_DURATION_US=10 # 10ms Pulse

trig_pin = Pin(9, Pin.OUT) 
echo_pin = Pin(8, Pin.IN)  

while True:
    # Prepare le signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Returns the wave propagation time (in µs)
    distance_cm = SOUND_SPEED * ultrason_duration / (10000 * 2) # 10000 for micro to centi, times 2 bc there and back

    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(500)
