# **Assessment Task 2 2026** #
## Requirements Outline
### Defining the Purpose
**The Need**

My sister often goes into my room when im not around, or while im wearing headphones (in which I can't hear or don't notice her coming in without asking/knocking). Sometimes even, she'll touch or take my stuff if im not around, coming in without a second thought.

**The Proposed Solution**

I will design a system that detects door movement, emitting the noise of sharp beeps to scare her off, and have an LED light flash continuosly until I manually turn it off myself by clicking the button within the circuitry once I come home; informing me of the break in and scaring my sister even more. Additionally, this will provide me with an indication of her coming in when I am too focused on my own tasks to notice her sneaking in. 

### Key Actions
1. When the ultrasonic sensor detects door movement, the piezo buzzer emits sharp beeps
2. Red LED starts flashing once movement is detected but does not turn off when the door is closed after the initial intrusion
3. The adhesive for the "security system" should keep the circuit in place as to not disrupt the sensor input/outputs
4. Button on the side turns off the LED once the user gives it an input (pushing it)
5. Green LED flashes at a constant slow pace when no movement is detected

### Functional Requirements
1. **Ultrasonic Sensor Input** --> *If ultrasonic sensor starts detecting an obstructive object, piezo begins emitting a beep consecutively until turned off*
2. **LED Output** --> *If an obstruction is detected, the red LED starts flashing consecutively until a manual reset of the system occurs; if no obstruction is detected, green LED stays on, flashing at a slow and constant pace*
3. **Adhesive** -->  *Adhesive consistently remains able to keep the system in place*
4. **Button input** --> *Button pressing must immediately turn of the LED output and the piezo buzzer*


### Test Case/s
| Test Case| Input    | Expected Output|
|----------|----------|----------------|
|Door is closed; Safety Protocol|Ultrasonic sensor sees that there is no obstruction|Safety protocol activates, beginning to flash the green led with the rest remaining dormant|
|Door is opened; Intrusion Protocol|Ultrasonic sensor sees the obstruction|Red LED begins flashing continuously, and piezo starts beeping until the button is pressed|
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
In regards to this test case, I was mostly successful in creating the alarm system that scares off the intruder. The red LED flashes red at a faster pace than the green LED, symbolising intrusion, and the alarm continuously beeps at a steady rate, fulfilling the requirements stated for this section. When discussing the steps I took however, they mostly included me looking at my code, realising I had made a silly mistake or trying something that might work, and having it just work. The main example of this is where I was testing the red LED, in which it wasn't working, and I had the random thought to use the two wires set up on the green LED side on the red LED side, powering the red LED as well. I had no clue this would work, but it did, so in the end it was a succesful test case. Following this, overall what went well was my gut instinct working out and usually leading me to the right answer, reflecting this however was the parts that challenged me. The biggest part that challenged me was the button section, in which I forgot how while loops worked and didn't trust the past code I had written in which accounted for this. Overall the areas of the program that could be improved would probably be the alarm being slightly louder to create more alert and attention to either the user or the intruder.

### Ultrasonic Sensor 
|Test Case|Code|Notes|Solution/Improvement|
|-|-|-|-|
|Initial time|ini = 0 & ini = sound_speed * duration / (10000 * 2) & return ini|The variable didn't change even after it was returned from the function, causing the initial time to just not work at all as the variable wasn't set|With the help of  [Claude (NOTE: AI WAS ONLY USED FOR THIS AREA OF CODE, IN NO OTHER WAY WAS IT USED!!! JUST TO REALISE THE VARIABLE NEEDED TO BE EQUAL!) and Core Electronics]: The solution to this problem was the fact that I had not made the actual variable with the same "name" equalate to the returned variable from the function (basically I didn't write: ini = initial()); after adding this line of code everything worked just fine.|
|Current time|curr = 0 & curr = sound_speed * duration / (10000 * 2) & return ini|Due to the last function practically being the same, I didn't actually have any issues due to the process being the exact same. However, I do note that it successfully ran, initiating intrusion protocol when the initial time function's variable was greater than the current time variable.|N/A due to there being no issues or necessary/possible improvements (that I know of).|

### Evaluations for Ultrasonic Sensor
In regards to this test case, I was completely successful in creating a detection system using the ultrasonic sensor to detect obstructions, completely meeting the requirements of this section. The initial time function detects the time without any obstructions, and the current time checks it (adding 5 to reduce the margin of error because of the ultrasonic sensors inaccuracy), while comparing the distance to the initial period in order to determine obstructions. When looking at the steps I took to fix errors in this section, I do admit to using AI. This action was taken due to only having one error in my code and my knowledge not being enough at the time due to a mental block. This was the only time I used AI, which was resorted to after I triple checked my code, referring it to the core electronics website I had used to program the sensor, and couldn't find the problem. In regard to went particularly well, I would say everything went well. My circuitry (for the msot part) and code went practically perfectly, and the ultrasonic sensor code ran smoothly with only the issue with equalation. However, in regard to what challenged me, it would be the connecting of the resistor for the ultrasonic sensor to the breadboard and sensor. The resistor would not stick in the wire connectors, and kept falling out, annoying me quite a bit; other than this however, there were no major challenges that affected me. When discussing improvements for this section based on results, there is actually little to add; the sensor code and wiring does what it needs to, fulfilling it's requirements and purpose in regard to the system.

### Final Product:
Please look inside the folder called videos to download an MP4 of my final project. (NOTE: THE MP4 UPLOADED IS TOO LARGE, AND WILL NEED TO HAVE THE RAW DOWNLOADED. KNOW, HOWEVER, THAT THERE IS ANOTHER VIDEO UPLOAD ON GOOGLE CLASSROOM FOR THE SUBMISSION)

Code is under functions and main. (NOTE: In the actual file used for this, all functions and code was in one file. In this repo, for organisation sake, they have been seperated for an easier viewing experience.)

## Evaluation
### Peer Evaluation
#### **Avina**
|P|M|I|
|-|-|-|
|This solution is very effective because it adresses the need Rachael has identified at the start and it works when it senses something going across it|It was a bit hard for me to navigate around in the beginning due to all the wires|I really liked how this system detects any movement and I hadn’t seen something like it before|
|It is very interactive and unique and utilises all the components very well|It might be a bit hard to see the LEDs if there are too many wires covering them|It was very unique compared to the other systems that just utilised LEDs|
|It triggers multiple senses and grabs the attention of the users very well||I found her use of all the components very interesting because they all worked together cohesively|

#### **Sarah**
|P|M|I|
|-|-|-|
|Rachael’s program addresses the target’s need providing a highly interactive user experience. The code is short and organised ensuring that the wiring for the LEDs, buzzer and ultrasonic sensor functions perfectly without any delays.|Rachael’s program and the wiring are both working perfectly. The ultrasonic sensor, buzzer and LEDs all work and fullfils the non functional and functional requirements. I don’t think there are any major issues or anything that needs fixing.|Maybe if possible Rachael could reduce the number of wires used and only wire the components that are necessary, making the circuit clearer and easier to understand.|
|I also really liked how the buzzer was loud and clear, making sure that the user can notice someone entering their room.||She could also use  a resistor to help protect the componenets and ensure the circuit works safely.|

### Individual Evaluation
#### In relation to Peer Evaluation:
In relation to peer evaluations, my project met the solution effectively in an interactive way that utilised all components with an organised code to pair with the circuitry. An example stated of the successful project was the clear functions, no delays, and loud buzzer clearly indicating intrusion. If there were an issue, the only things brought up were the confusing wiring and the difficulty noticing the LEDs due to the wires partially covering them when using the system. However, overall in relation to peer evaluation, the solution ran efficiently and effectivley, meeting the need and purpose in a way that created an enjoyable user experience.

#### Achievment of overall requirements:
The overall achievment of this task was quite high in regards to the completion of the functional and non-functional requirements. When discussing the functional requirements of the task, almost all of the requirements were met. The ultrasonic sensor was able to detect obstructions, with a signal being sent to the other components, the LED turned on automatically for both the safety protocol and the intrusion protocol, indicating the state of room security, and the button input turned everything off with no problem. One thing to note for this section however is the adhesive requirement was not met, due to there being no testing for it. However, if adhesive were to be used, it would've probably been blutack to keep the sensor stuck to the desk in a position that can track the door, but due to the innability to test it the requirement still wasn't met. In regard to the non-functional requirement however, all requirements are met to the dot. The sensor releases a signal even faster than once every 5 seconds, meaning it is optimised efficiently, response time is also completed with the LED and Piezos working immediately after an obstruction is detected (with the button also turning it off once pressed as well). The accuracy of it all is also confirmed due to the '+5' addition to ensure no accidental initiations of the security system and misunderstandings in regard to user error. Overall the requirements on both sides were met completely, functional and non-functional other than the unnecessary adhesive.

#### Final Performance:
Luckily, when testing the code, my sister attempted to come into my room without knocking, setting off the security system for this project. The noise freaked her out, and she questioned, "What the hell?!", allowing me to realise her presence and send her out of my room. This example shows that the security system solution is effective in a real life scenario, warning me when someone has intruded into my space and attempts to bother me while studying. Another example of this is when my uncle also came into my room without asking (23 yrs old and grew up with teasing from mum's side of the family, so it became generational/my problem), and was also slightly perterbed by the alarm system, causing him to walk out after noticing the running circuitry and loud alarm. Overall, using this collected data, the project can be determined to meet the identified need completely, informing the user of intrusion and scaring off the intruder.

#### Project Management:
When refering to project management, I was able to consitently complete my work as planned in an appropriate time frame: the requirements outline was all completed in the first week, algorithms was completed in second, design and integration in thrid, and my final testing, debugging and evaluating being finished in the fifth and final week due to more time being needed to work on these sections. This plan was followed with the assistance of a gantt chart, allowing me to finish my control system with great satisfaction, completing it to the best of my abilities. Overall this project was managed effectively, meaning that I was able to complete everything on time, letting me have a more enjoyable experience for this task.
![Gantt](images/gantt.png)

#### Suggestions for future improvement:
In regard to future improvements of this project, I could add some actual words to the alarm system using another component, scaring off the intruder even more; on top of this, with a raspberry pi pico that has a wifi connector, the security system could ping my phone when there is an intruder in my room. Even something simple like making the buzzer louder, or my wire more organised are all ways I could make improvements to the system I have created, should I have more time or resources to do so. Overall this project went incredibly well, and though these improvements would be useful, they are not vital to meet the success criteria, showing that the project currently displayed meets the stated/defined functional check list, and these improvements could be a fun possibility to improve on an already working control system.
