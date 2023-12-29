#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

from .blackboard import Blackboard
from .common import ResultEnum
from .composite import Composite, NodeListType


class Selection(Composite):
    """
    Specific implementation of the selection composite.
    """

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        child_position = self.additional_information(blackboard, 0)

        while child_position < len(self.children):
            child = self.children[child_position]

            result_child = child.run(blackboard)
            if result_child == ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

            child_position = child_position + 1

        return self.report_failed(blackboard, 0)
