import bt_library as btl

# Children are evaluated by priority.
# Fails if all the children fails; otherwise succeeds; 
# immediately returns running if a children returns running
class Priority(btl.Composite):
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
        
        # parse through children
        for child_position in range (0, len(self.children)):
            child = self.children[child_position]

            # run each child
            result_child = child.run(blackboard)
            # if succeeded, report succeeded
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard)

            # if running, report running
            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard)

            child_position = child_position + 1

        # if all nodes fail, report failed
        return self.report_failed(blackboard)
