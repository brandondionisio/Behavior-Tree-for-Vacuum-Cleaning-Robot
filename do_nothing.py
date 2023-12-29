
import bt_library as btl
from globals import POWER_OFF

# subclass of task
class DoNothing(btl.Task):
    """
    Implementation of the Task "Do Nothing".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Doing Nothing...")
        user_input = input("Would you like to power off the robot? (y/n): ")
        while user_input != "y" and user_input != "n":
            user_input = input("Invalid command. Please try again (y/n): ")
        if user_input == "y":
            blackboard.set_in_environment(POWER_OFF, True)

        return self.report_succeeded(blackboard)