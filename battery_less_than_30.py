#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# subject to change

import bt_library as btl
from globals import BATTERY_LEVEL

# subclass of condition
class BatteryLessThan30(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking battery < 30")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(BATTERY_LEVEL, 0) < 30 \
            else self.report_failed(blackboard)

# prints a message indicating that it's checking whether the battery is less than 30%.
# retrieves the current battery level from the blackboard using blackboard.get_in_environment(BATTERY_LEVEL, 0). 
# This is done to get the value of the battery level stored in the blackboard, with a default value of 0 if it's not found.
# compares the battery level obtained from the blackboard with the value 30 (representing 30% battery level).
#
# the battery level is less than 30, it returns self.report_succeeded(blackboard), indicating that the condition has succeeded.
# the battery level is not less than 30, it returns self.report_failed(blackboard), indicating that the condition has failed.