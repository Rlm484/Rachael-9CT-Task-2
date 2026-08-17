def safety_protocol(): # Protocol that causes the green LED to flash slowly to symbolise safety
    green_led.value(1)
    time.sleep(0.5)
    green_led.value(0)
    time.sleep(0.5)

def intrusion_protocol(): # Protocol designed to scare off the intruder with loud noises and flashing lights
    while True:
        if button.value() == 0:
            red_led.value(1)
            alarm.value(1)
            time.sleep(0.25)
            red_led.value(0)
            alarm.value(0)
            time.sleep(0.25)
        else:
            break  # Stops the alarm once the button is pressed 

def initial(): # Function that tracks the original distance with the ultrasonic distance
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(trig_pulse)
    trigger.value(0)

    duration = time_pulse_us(echo, 1, 30000) # Returns the wave propagation time (in µs)
    ini = sound_speed * duration / (10000 * 2) # 10000 for micro to centi, times 2 bc there and back
    return ini

def current(): # Function that tracks the current distance with the ultrasonic distance
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(trig_pulse)
    trigger.value(0)

    duration = time_pulse_us(echo, 1, 30000) # Returns the wave propagation time (in µs)
    curr = sound_speed * duration / (10000 * 2) # 10000 for micro to centi, times 2 bc there and back
    return curr