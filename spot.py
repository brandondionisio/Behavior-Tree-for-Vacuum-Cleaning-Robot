
import bt_library as btl
from globals import SPOT_CLEANING

# subclass of condition
class Spot(btl.Condition):
    """
    Implementation of the condition "needs spot cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # displaying message that we are checking for spot cleaning
        self.print_message("Checking if there needs spot cleaning")

        user_input = input("Spot Cleaning (y/n): ")
        while user_input != "y" and user_input != "n":
            user_input = input("Invalid command. Please try again (y/n): ")
        if user_input == "y":
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)