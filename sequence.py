import bt_library as btl

# Children are evaluated left to right.
# Fails as soon as one child fails; otherwise succeeds;
# immediately returns running if a children returns running
class Sequence(btl.Composite):
    """
    Specific implementation of the sequence composite.
    """

    def __init__(self, children: btl.NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        child_position = self.additional_information(blackboard, 0)

        # parse through children
        while child_position < len(self.children):
            child = self.children[child_position]

            # run child
            result_child = child.run(blackboard)
            # if child fails, report fails
            if result_child == btl.ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)

            # if child returns running, report running
            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

            child_position = child_position + 1

        # if all children succeed, report succeeded
        return self.report_succeeded(blackboard, 0)
