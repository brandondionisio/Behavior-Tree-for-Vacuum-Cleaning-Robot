
import bt_library as btl
from globals import DUSTY_SPOT_SENSOR

# subclass of condition
class DustySpot(btl.Condition):
    """
    Implementation of the condition "dusty spot sensor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        # if dust is detected, report true, if not detected, report false
        if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, 0) == True:
            self.print_message("Dust is detected!")
            return self.report_succeeded(blackboard)
        else:
            self.print_message("Dust not detected.")
            return self.report_failed(blackboard)