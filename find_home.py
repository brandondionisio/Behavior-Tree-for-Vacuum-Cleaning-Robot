#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# subject to change

import bt_library as btl
from globals import HOME_PATH

# subclass of task
class FindHome(btl.Task):
    """
    Implementation of the Task "Find Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Looking for a home")

        blackboard.set_in_environment(HOME_PATH, "Up Left Left Up Right")

        return self.report_succeeded(blackboard)

# prints a message indicating that it's looking for a home.
# updates the value of HOME_PATH in the blackboard (shared data storage) to a specific path, 
# represented as a string. In this example, the path is set to "Up Left Left Up Right". 
# This could is a predefined path or a representation of how the robot should navigate to its home.

# it returns self.report_succeeded(blackboard), indicating that the task has succeeded.