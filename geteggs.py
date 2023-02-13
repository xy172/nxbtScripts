import time
from random import randint

import nxbt
from nxbt import Buttons
from nxbt import Sticks

"""
    Y
    X
    B
    A
    JCL_SR
    JCL_SL
    R
    ZR
    MINUS
    PLUS
    R_STICK_PRESS
    L_STICK_PRESS
    HOME
    CAPTURE
    DPAD_DOWN
    DPAD_UP
    DPAD_RIGHT
    DPAD_LEFT
    JCR_SR
    JCR_SL
    L
    ZL
"""

def button(sentButton = "A",duration = 0.25):
    nx.press_buttons(controller_idx, [Buttons.sentButton], down = duration, up = 0.25)
    return

def move(direction = "LEFT", duration = 0.25):
    match direction:
        case "UP":
            nx.tilt_stick(controller_idx, Sticks.LEFT_STICK, 0, 100,
                  tilted=duration, released=0.25)
        case "DOWN":
            nx.tilt_stick(controller_idx, Sticks.LEFT_STICK, 0, -100,
                  tilted=duration, released=0.25)
        case "LEFT":
            nx.tilt_stick(controller_idx, Sticks.LEFT_STICK, -100, 0,
                  tilted=duration, released=0.25)
        case "RIGHT":
            nx.tilt_stick(controller_idx, Sticks.LEFT_STICK, 100, 0,
                  tilted=duration, released=0.25)
    return






def returnToGame():
    for x in range(6):
        button("B")
        time.sleep(0.1)
    time.sleep(1.5)
    for x in range(4):
        button("DPAD_LEFT")
        time.sleep(0.1)
    button("DPAD_UP")
    time.sleep(0.1)
    button("A")
    time.sleep(1.5)

def collectEggs():
    for x in range(30):
        time.sleep(60)
        for y in range(8): 
            button("A", 0.50)
            time.sleep(2)






def random_colour():

    return [
        0,
        0,
        255,
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
    returnToGame()
    print("Collecting Eggs.")
    collectEggs()
    print("Macro finished, Exiting...")