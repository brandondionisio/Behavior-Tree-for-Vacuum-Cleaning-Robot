

import bt_library as btl
from globals import GENERAL_CLEANING

# subclass of task
class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Finishing general clean")
        
        # set GENERAL_CLEANING to false (finish general cleaning)
        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_succeeded(blackboard)