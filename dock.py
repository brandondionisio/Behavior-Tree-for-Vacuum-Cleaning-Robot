

import bt_library as btl
from globals import BATTERY_LEVEL

# subclass of task
class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        self.print_message("Battery is at " +
                           str(blackboard.get_in_environment(BATTERY_LEVEL, 0))
                            + "% recharging to 100%...")
        
        # sets BATTERY_LEVEL to 100 (charges at the dock)
        blackboard.set_in_environment(BATTERY_LEVEL, 100)

        return self.report_succeeded(blackboard)