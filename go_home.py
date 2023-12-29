import bt_library as btl
from globals import HOME_PATH

# subclass of task
class GoHome(btl.Task):
    """
    Implementation of the Task "Find Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # message printed every call
        self.print_message("Going home")

        # sets home path to empty
        blackboard.set_in_environment(HOME_PATH, "")

        # succeeds the task
        return self.report_succeeded(blackboard)