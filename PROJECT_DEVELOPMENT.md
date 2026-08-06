# **Assessment Task 2 2026** #
## Requirements Outline
### Defining the Purpose
**The Need**

My sister often goes into my room when im not around, or while im wearing headphones (in which I can't hear or don't notice her coming in without asking/knocking). Sometimes even, she'll touch or take my stuff if im not around, coming in without a second thought.

**The Proposed Solution**

I will design a system that detects door movement, emitting the noise of sharp beeps to scare her off, and have an LED light flash continuosly until I manually turn it off myself by clicking the button within the circuitry once I come home; informing me of the break in and scaring my sister even more. Additionally, this will provide me with an indication of her coming in when I am too focused on my own tasks to notice her sneaking in. 

### Key Actions
1. When the ultrasonic sensor detects door movement, the pico emits sharp beeps for 30 seconds
2. Red LED starts flashing once movement is detected but does not turn off when the door is closed after the initial intrusion
3. The adhesive for the "security system" should keep the circuit in place as to not disrupt the sensor input/outputs
4. Button on the side turns off the LED once the user gives it an input (pushing it)
5. Green LED flashes at a constant slow pace when no movement is detected

### Functional Requirements
1. **Ultrasonic Sensor Input** --> *If ultrasonic sensor starts detecting an obstructive object, piezo begins emitting a beep consecutively for 30 seconds*
2. **LED Output** --> *If an obstruction is detected, the red LED starts flashing consecutively until a manual reset of the system occurs; if no obstruction is detected, green LED stays on, flashing at a slow and constant pace*
3. **Adhesive** -->  *Adhesive consistently remains able to keep the system in place*
4. **Button input** --> *Button pressing must immediately turn of the LED output*


### Test Case/s
| Test Case| Input    | Expected Output|
|----------|----------|----------------|
|Door is closed|Ultrasonic sensor sees that there is no obstruction|LED and Piezo remain dormant|
|Door is opened|Ultrasonic sensor sees the obstruction|Red LED begins flashing continuously, and piezo starts beeping for 30 seconds|

### Non-Functional Requirements
Some non-functional requirements necessary to keep the security system optimised:
- Efficiency: The ultrasonic sensor should release a signal once every 5 seconds to optimise a quicker response time, informing the pico to turn on the other components immediately.
- Response Time: The piezo and LED should start their designated outputs ASAP (practically the second the sensor detects movement) to ensure optimised fear and flight response from the intruder as to protect the room within. The same should apply to the button, turning off the LED the moment it is pressed to ensure minimal interuption for the user.
- Accuracy: The sensor should be able to accurately detect movement of the door at any instance to ensure safety of belongings within the room at all time and should remain accurate for at least the time period where the occupant of the room returns home.

## Algorithms
### Pseudocode
```
BEGIN intrusion_protocol()
    WHILE true
        READ button.value()
        IF button.value() = 0
            OUTPUT red_Led.value(1)
            time.sleep(0.5)
            OUTPUT red_Led.value(0)
            time.sleep(0.5) 
            OUTPUT buzzer.on
        ELSE
            ENDWHILE
        ENDIF
    ENDWHILE
END
```
```
BEGIN safety_protocol()
    OUTPUT green_Led.value(1)
    time.sleep(1)
    OUTPUT green_Led.value(0)
    time.sleep(1)
END
```
```
BEGIN
    READ normal_time
    WHILE true
        READ current_time
        IF current_time < normal_time
            intrusion_protocol()
        ELSE
            safety_protocol()
        ENDIF
    ENDWHILE
END
```   

### Flowchart Development
INTRUSION PROTOCOL:

![Intrusion](images/Int_Flow.png)

SAFETY PROTOCOL:

![Safety](images/Saf_Flow.png)

MAINLINE:

![Mainline](images/Main_Flow.png)

WHOLE:

![Full](images/ALL.png)

## Development and Intergration
### First code attempt
```
from machine import Pin
import time

red_led = Pin(16, Pin.OUT)
green_led = Pin(13, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN   )

normal = 1 ''' insert input for ultrasonic sensor'''
#Temporary input for testing 
def intrusion_protocol():
    while True:
        if button.value()==0: #System that starts alerting of a breakin
            red_led.value(1)
            time.sleep(0.5)
            red_led.value(0)
            time.sleep(0.5)
            '''line of code for buzzer''' #Buzzer has been changed to continuously beep instead of for 30 secs; changed from original plan
        else:
            main()
def safety_protocol(): #System that shows safety (like if I was studying with music in and cant hear buzzer I can visually see safety or intrusion)
            green_led.value(1)
            time.sleep(1)
            green_led.value(0)
            time.sleep(1)
            
def main(): #Main UI/program that fetches the protocol functions
    while True:
        current = 1 '''insert current input for ultrasonic sensor'''
        #Temporary input for testing
        if current < normal:
            intrusion_protocol()
        else: 
            safety_protocol()
```

## Testing and Debugging
### Test Cases
|Test Case|Code|Notes|Solution|
|-|-|-|
|Everything|normal=8|My D&I first code didn't work, it said that Line 8 had a syntax error||

## Evaluation
### Peer Evaluation
### Individual Evaluation
In relation to Peer Evaluation:

Achievment of overall requirements:

Final Performance:

Project Management

Suggestions for future improvement:
