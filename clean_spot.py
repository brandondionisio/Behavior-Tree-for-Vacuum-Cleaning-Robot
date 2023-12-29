
import bt_library as btl
from globals import SPOT_CLEANING

# subclass of task
class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        self.print_message("Spot Cleaning!")
        
        # setting SPOT_CLEANING to true (done with spot cleaning)
        blackboard.set_in_environment(SPOT_CLEANING, True)

        return self.report_succeeded(blackboard)