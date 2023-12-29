#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# subject to change

import bt_library as btl

# Condition imports
from battery_less_than_30 import BatteryLessThan30
from spot import Spot
from dusty_spot import DustySpot
from general_cleaning import GeneralCleaning

# Task imports
from find_home import FindHome
from go_home import GoHome
from dock import Dock
from clean_spot import CleanSpot
from clean_floor import CleanFloor
from done_spot import DoneSpot
from done_general import DoneGeneral
from do_nothing import DoNothing

from sequence import Sequence
from priority import Priority

# Decorator imports
from until_failure import UntilFailure

# Instantiate the tree according to the assignment.
#

tree_root = Priority([
    Sequence([
        BatteryLessThan30(),
        FindHome(),
        GoHome(),
        Dock()
    ]),
    btl.Selection([
        Sequence([
            Spot(),
            btl.Timer(20, CleanSpot()),
            DoneSpot()
        ]),
        Sequence([
            GeneralCleaning(),
            Sequence([
                Priority([
                    Sequence([
                        DustySpot(),
                        btl.Timer(35, CleanSpot())
                    ]),
                    UntilFailure(CleanFloor())
                ]),
                DoneGeneral()
            ])
        ])
    ]),
    DoNothing()
])

########################################################################################################################
# The following are just examples.

# tree_root = btl.Selection([
#     BatteryLessThan30(),
#     FindHome()])

# tree_root = btl.Timer(5, Attack())

# tree_root = Sequence(
#     [
#         BatteryLessThan30(),
#         btl.Timer(10, FindHome())
#     ]
# )

# tree_root = btl.Sequence(
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )
