

import bt_library as btl
from globals import SPOT_CLEANING

# subclass of task
class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Finishing spot clean")
        
        # sets SPOT_CLEANING to false (finishing spot cleaning)
        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard)