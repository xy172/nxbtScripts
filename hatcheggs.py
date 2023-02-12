import time
from random import randint

import nxbt
from nxbt import Buttons
from nxbt import Sticks

ReturntoGame = """
LOOP 12
    B 0.1s
    0.1s
1.5s
LOOP 4
    DPAD_LEFT 0.075s
    0.075s
DPAD_UP 0.075s
0.075s
A 0.1s
1.5s
"""

CollectEggs = """
LOOP 60
    30.0s
    Loop 8
        A 0.5s
        2s
"""


def random_colour():

    return [
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    ]


if __name__ == "__main__":

    # Init NXBT
    nx = nxbt.Nxbt()

    # Get a list of all available Bluetooth adapters
    adapters = nx.get_available_adapters()
    # Prepare a list to store the indexes of the
    # created controllers.
    controller_idxs = []
    # Loop over all Bluetooth adapters and create
    # Switch Pro Controllers
    for i in range(0, len(adapters)):
        index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            adapter_path=adapters[i],
            colour_body=random_colour(),
            colour_buttons=random_colour())
        controller_idxs.append(index)

    # Select the last controller for input
    controller_idx = controller_idxs[-1]

    # Wait for the switch to connect to the controller
    nx.wait_for_connection(controller_idx)

    # Run a macro on the last controller
    print("Returning to game.")
    macro_id = nx.macro(controller_idx, ReturntoGame)
    print("Running main macro.")
    macro_id = nx.macro(controller_idx, CollectEggs)
    print("Macro finished, Exiting...")