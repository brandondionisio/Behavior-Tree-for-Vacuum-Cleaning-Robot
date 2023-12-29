
import random
import bt_library as btl

# subclass of task
class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        self.print_message("Cleaning Floor!")
        
        # cleans the floor 10% of the time (report task accordingly)
        clean = True if random.random() < 0.1 else False

        if clean:
            self.print_message("The floor is now clean.")
            return self.report_failed(blackboard)
        else:
            return self.report_succeeded(blackboard)