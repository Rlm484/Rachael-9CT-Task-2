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
### Safety Protocol:
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Green LED|green_led.value(1)|The green_led won't turn on for some reason, even though the positive charges are matched and a resistor is used|With the help of [Mr Scott]: After grabbing a bigger breadboard and remaking the circuit at home, the code started working; I am assuming this is because I changed the resistor to a 22 ohm resistor|
|Green LED|time.sleep(1)|The terminal states that "time" isn't defined|With the help of [Core Electronics]: I had only done "from time import sleep", I didn't actually import time, causing the NameError|

### Evaluations for Safety Protocol Test Case:
In regards to this test case, it was the simplest part of the security system, meaning it was easy for me to succesfully meet the test case requirements completely. The green LED flashes green, symbolising no intrusion, and the steps I took by rechecking my code, using a larger breadboard to make it easier to check errors along with asking for help when I needed it allowed me to correctly identify the problem and fix it in my code and physical circuit. What went particularly well was the fact that I didn't actually run into too many issues that had a high difficulty in fixing, meaning once I wired it at home it worked with little to no issue. In regard to what challenged me, it would mostly be the ciruit wiring. Before I switched to a larger breadboard, the LED just wouldn't work, frustrating me greatly and causing slight distress. Areas of program that could be improved is very little, due to this section of the code just being a flashing LED for the safety protocol.

### Intrusion Protocol:
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Red LED|red_led.value(1) & time.sleep(0.25)|Much like the original issue with the green LED, the red LED was not turning on for seemingly no reason what so ever|With the help of  [N/A]: Turns out, and this is for the last testcase in safety protocol as well, I needed to have a wire connected from the GND pin and 3V3 OUT pin to the positive and negative lanes on the other side|
|Piezo|alarm=Pin(11,Pin.OUT) & alarm.value(1)|The only issue with the piezo buzzer was that the one in the kit did not work at all, which I am assuming is a product error due to classmates also having issue with the buzzer.|With the help of [N/A]: I switched the piezo buzzer that came in the coding kit with the active buzzer I got from my engineering kit, which then worked out perfectly with no issues at all|
|Button|While True: if button.value() == 0: & button = Pin(5, Pin.IN, Pin.PULL_DOWN)|The funtion of the button was to turn the alarm system off once home, however the alarm kept going even after I hit the button|With the help of [N/A]: I had placeholders for the current time and final time, meaning I hadn't actually made it so the current time would change. This caused the intrusion protocol to always run, meaning that even when the button deactivated the intrusion protocol, the mainline would then loop it again due to only the protocols while loop "breaking"|

### Evaluations for Intrusion Protocol Test Case:
In regards to this test case, I was mostly successful in creating the alarm system that scares off the intruder. [Though the system does not turn off the actual alarm noise after 30 seconds], the rest of the requirements were mostly successful in which was an overall positive outcome. The red LED flashes red at a faster pace than the green LED, symbolising intrusion, and the alarm continuously beeps at a steady rate. When discussing the steps I took however, they mostly included me looking at my code, realising I had made a silly mistake or trying something that might work, and having it just work. The main example of this is where I was testing the red LED, in which it wasn't working, and I had the random thought to use the two wires set up on the green LED side on the red LED side, powering the red LED as well. I had no clue this would work, but it did, so in the end it was a succesful test case. Following this, overall what went well was my gut instinct working out and usually leading me to the right answer, reflecting this however was the parts that challenged me. The biggest part that challenged me was the button section, in which I forgot how while loops worked and didn't trust the past code I had written in which accounted for this. Overall the areas of the program that could be improved would probably be [the alarm turning off after 30 seconds, which I unfortunately do not have the time, or skill, to achieve this function for now.]

### Ultrasonic Sensor 
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Initial time|ini = 0 & ini = sound_speed * duration / (10000 * 2) & return ini|The variable didn't change even after it was returned from the function, causing the initial time to just not work at all as the variable wasn't set|With the help of  [Claude (NOTE: AI WAS ONLY USED FOR THIS AREA OF CODE, IN NO OTHER WAY WAS IT USED!!! JUST TO REALISE THE VARIABLE NEEDED TO BE EQUAL!)]: The solution to this problem was the fact that I had not made the actual variable with the same "name" equalate to the returned variable from the function (basically I didn't write: ini = initial()); after adding this line of code everything worked just fine.|
|Current time|curr = 0 & curr = sound_speed * duration / (10000 * 2) & return ini|Due to the last function practically being the same, I didn't actually have any issues due to the process being the exact same. However, I do note that it successfully ran, initiating intrusion protocol when the initial time function's variable was greater than the current time variable.|N/A due to there being no issues or necessary/possible improvements (that I know of).|

### Evaluations for Ultrasonic Sensor
In regards to this test case, I was completely successful in creating a detection system using the ultrasonic sensor to detect obstructions, completely meeting the requirements of this section. The initial time function detects the time without any obstructions, and the current time checks it (adding 5 to reduce the margin of error because of the ultrasonic sensors inaccuracy), while comparing the distance to the initial period in order to determine obstructions. When looking at the steps I took to fix errors in this section, I do admit to using AI. This action was taken due to only having one error in my code and my knowledge not being enough at the time due to a mental block. This was the only time I used AI, which was resorted to after I triple checked my code and couldn't find the problem. In regard to went particularly well, I would say everything went well. My circuitry (for the msot part) and code went practically perfectly, and the ultrasonic sensor code ran smoothly with only the issue with equalation. However, in regard to what challenged me, it would be the connecting of the resistor for the ultrasonic sensor to the breadboard and sensor. The resistor would not stick in the wire connectors, and kept falling out, annoying me quite a bit; other than this however, there were no major challenges that affected me. When discussing improvements for this section based on results, there is actually little to add; the sensor code and wiring does what it needs to, fulfilling it's requirements and purpose in regard to the system.

### Final Product:
Please look inside the folder called videos to download an MP4 of my final project. (NOTE: THE MP4 UPLOADED IS TOO LARGE, AND WILL NEED TO HAVE THE RAW DOWNLOADED. KNOW, HOWEVER, THAT THERE IS ANOTHER VIDEO UPLOAD ON GOOGLE CLASSROOM FOR THE SUBMISSION)

Code is under functions and main. (NOTE: In the actual file used for this, all functions and code was in one file. In this repo, for organisation sake, they have been seperated for an easier viewing experience.)

## Evaluation
### Peer Evaluation

### Individual Evaluation
In relation to Peer Evaluation:

Achievment of overall requirements:

Final Performance:

Project Management:

Suggestions for future improvement: