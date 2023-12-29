from globals import UNTIL_FAILURE
import bt_library as btl

class UntilFailure(btl.Decorator):
    """
    Specific implementation of the until failure decorator.
    """

    def __init__(self, child: btl.TreeNode):
        """
        Default constructor.

        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        blackboard.set_in_environment(UNTIL_FAILURE, True)
        # Evaluate the child
        self.print_message("Cleaning until failure...")
        result_child = self.child.run(blackboard)

        # If the child failed, terminate immediately
        if result_child == btl.ResultEnum.FAILED:
            blackboard.set_in_environment(UNTIL_FAILURE, False)
            return self.report_succeeded(blackboard)

        return self.report_running(blackboard)