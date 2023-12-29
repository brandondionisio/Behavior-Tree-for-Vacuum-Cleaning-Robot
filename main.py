#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# subject to change

import bt_library as btl
import random
from behavior_tree import tree_root

from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH, POWER_OFF, UNTIL_FAILURE

# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")
current_blackboard.set_in_environment(POWER_OFF, False)
current_blackboard.set_in_environment(UNTIL_FAILURE, False)

while True:
    try:
        current_battery_level = int(input("Input battery level (1-100): "))
        if 0 < current_battery_level <= 100:
            current_blackboard.set_in_environment(BATTERY_LEVEL, current_battery_level)
            break
        else:
            print("Invalid battery level. Please try again (1-100): ")
    except ValueError:
        print("Invalid battery level. Please try again (1-100): ")

done = False
while not done:
    # Each cycle in this while-loop is equivalent to 1 second time

    # Step 1: Simulate environment changes (battery, dusty spot, user input)
    current_battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, 0)  # 0 is default value if BATTERY_LEVEL is not found
    current_blackboard.set_in_environment(BATTERY_LEVEL, current_battery_level - 1)  # Simulate battery depletion

    # Simulate the response of the dusty spot sensor (You can implement your logic here)
    # dusty spot detected 20% of the time.
    # if the until failure decorator isn't running for general cleaning
    if current_blackboard.get_in_environment(UNTIL_FAILURE, 0) == False:
        dusty_spot_detected = True if random.random() < 0.2 else False
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, dusty_spot_detected)

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)

    # Step 3: Determine if your solution must terminate (You can implement your termination logic here)
    if current_battery_level < 1:
        done = True
    if current_blackboard.get_in_environment(POWER_OFF, 0) == True:
        done = True

    # Print the battery for each cycle
    print("Current Battery: " + str(current_blackboard.get_in_environment(BATTERY_LEVEL, 0)) + "%")

    # Print the result for each cycle
    print("Cycle Result: Complete")
    if done == True:
        print("Powering off.")