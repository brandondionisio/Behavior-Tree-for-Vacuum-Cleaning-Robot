
import bt_library as btl
from globals import GENERAL_CLEANING

# subclass of condition
class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "needs general cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # displaying message that we are checking for general cleaning
        self.print_message("If needing general cleaning")

        # ask the user if robot should general clean if GENERAL_CLEANING is false
        if blackboard.get_in_environment(GENERAL_CLEANING, 0) == False:
            user_input = input("General Cleaning (y/n): ")
            while user_input != "y" and user_input != "n":
                user_input = input("Invalid command. Please try again (y/n): ")
            if user_input == "y":
                blackboard.set_in_environment(GENERAL_CLEANING, True)
                return self.report_succeeded(blackboard)
            else:
                return self.report_failed(blackboard)
        self.print_message("Already general cleaning")
        return self.report_failed(blackboard)