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
|Door is closed; Safety Protocol|Ultrasonic sensor sees that there is no obstruction|Safety protocol activates, beginning to flash the green led with the rest remaining dormant|
|Door is opened; Intrusion Protocol|Ultrasonic sensor sees the obstruction|Red LED begins flashing continuously, and piezo starts beeping for 30 seconds|
|Door is closed/opened; Sensor|Ultrasonic sensor sess/doesn't see an obstruction|Ultrasonic sensor sends data to the system, "informing it" which protocol to activate|

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
### Safety Protocol:
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Green LED|green_led.value(1)|The green_led won't turn on for some reason, even though the positive charges are matched and a resistor is used|With the help of [Mr Scott]: After grabbing a bigger breadboard and remaking the circuit at home, the code started working; I am assuming this is because I changed the resistor to a 22 ohm resistor|
|Green LED|time.sleep(1)|The terminal states that "time" isn't defined|With the help of [Core Electronics]: I had only done "from time import sleep", I didn't actually import time, causing the NameError|

### Evaluations for Safety Protocol test case:
In regards to this test case, it was the simplest part of the security system, meaning it was easy for me to succesfully meet the test case requirements completely. The green LED flashes green, symbolising no intrusion, and the steps I took by rechecking my code, using a larger breadboard to make it easier to check errors along with asking for help when I needed it allowed me to correctly identify the problem and fix it in my code and physical circuit. What went particularly well was the fact that I didn't actually run into too many issues that had a high difficulty in fixing, meaning once I wired it at home it worked with little to no issue. In regard to what challenged me, it would mostly be the ciruit wiring. Before I switched to a larger breadboard, the LED just wouldn't work, frustrating me greatly and causing slight distress. Areas of program that could be improved is very little, due to this section of the code just being a flashing LED for the safety protocol.

### Intrusion Protocol:
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Red LED|red_led.value(1) & time.sleep(0.25)|Much like the original issue with the green LED, the red LED was not turning on for seemingly no reason what so ever|With the help of  [N/A]: Turns out, and this is for the last testcase in safety protocol as well, I needed to have a wire connected from the GND pin and 3V3 OUT pin to the positive and negative lanes on the other side|
|Piezo|alarm=Pin(11,Pin.OUT) & alarm.value(1)|


## Evaluation
### Peer Evaluation
### Individual Evaluation
In relation to Peer Evaluation:

Achievment of overall requirements:

Final Performance:

Project Management

Suggestions for future improvement: