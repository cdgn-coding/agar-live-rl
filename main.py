import time
from driver import AgarLiveWebdriver
import numpy as np
import pyautogui

if __name__ == '__main__':
    env = AgarLiveWebdriver()
    # Right
    print('Moving right')
    env.move(0, 'balanced')
    time.sleep(3)

    # Up
    print('Moving up')
    env.move(np.pi / 2, 'balanced')
    time.sleep(3)

    # Left
    print('Moving left')
    env.move(np.pi, 'balanced')
    time.sleep(3)

    # Down
    print('Moving down')
    env.move(3 * np.pi / 2, 'balanced')
    time.sleep(3)

    env.flush()