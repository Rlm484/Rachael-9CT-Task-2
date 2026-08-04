from functions import intrusion, safety


# Example:
# def fight():
#    """
#    Function to handle the fight action.
#    This could include various logic for fighting a creature.
#    """
#    print("You chose to fight the creature!")
#    # Add more fight logic here as needed
#    print("You engage in battle with the creature.")
#    # Example of more details
#    print("The creature is strong, but you're stronger!")
#
#def run_away():
#    """
#    Function to handle the run away action.
#    This could include logic for successfully running away or failing to escape.
#    """
#    print("You chose to run away!")
#    # Add more run away logic here as needed
#    print("You turn and flee from the creature.")
#    # Example of a scenario where running away fails
#    print("Unfortunately, the creature is too fast! It catches up with you!")


# Initial time is tracked before due to the possibility of initial time being registered as the 
# time it takes from the sensor to the door
'''code that reads the initial time from the sensor to the end of the room with the door closed'''
while True:
    '''code that reads current time from the sensor to the closest end (door or wall)''' 
    if '''current time code''' < '''the initial time code''':
        intrusion()
    else:
        safety()
    
     