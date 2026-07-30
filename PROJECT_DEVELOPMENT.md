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
    WHILE true
        OUTPUT green_Led.value(1)
        time.sleep(0.5)
        OUTPUT green_Led.value(0)
        time.sleep(0.5)
    ENDWHILE
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


## Development and Intergration
### Successful Code

## Testing and Debugging
### Test Cases
|Test Case|Code|Notes|
|-|-|-|

## Evaluation
### Peer Evaluation
### Individual Evaluation
In relation to Peer Evaluation:

Achievment of overall requirements:

Final Performance:

Project Management

Suggestions for future improvement:
