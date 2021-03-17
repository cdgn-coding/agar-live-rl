from gym import Env, spaces
import numpy as np
from driver import AgarLiveWebdriver
import time

class AgarIoEnv(Env):
    def __init__(self):
        super(AgarIoEnv, self).__init__()

        self.start_time = None
        self.started = False
        self.driver = AgarLiveWebdriver(start = False)

        # Angle, velocity, W key and space key
        self.action_space = spaces.Box(low = 0, high = 1, shape = (1, 4))

        # Current game screen
        width = self.driver.browserSize[0]
        height = self.driver.browserSize[1]
        self.observation_space = spaces.Box(low=0, high=255, shape=(height, width, 3), dtype=np.uint8)


    def step(self, action):
        if not self.started:
            self.driver.start()
            self.start_time = time.time()

        movement_angle = 2 * np.pi * action[0]
        movement_speed = self.__getMovementSpeed(action[1])
        should_eject = action[2] > .5
        should_split = action[3] > .5

        self.driver.move(movement_angle, movement_speed)

        if should_eject: self.driver.eject()
        if should_split: self.driver.split()

        obs = self.__getObservation()
        done = self.driver.isGameDone()

        current_time = time.time()
        reward = current_time - self.start_time

        return obs, reward, done, {}
    
    def sampleAction(self):
        return np.random.uniform(low = .0, high = 1., size = 4)

    def __getMovementSpeed(self, speedAction):
        if speedAction < .25: return 'slow'
        if speedAction < .75: return 'balanced'
        return 'fast'

    def __getObservation(self):
        return self.driver.screenshot()

    def reset(self):
        self.driver.flush()
        self.started = False
        self.start_time = None

    def render(self):
        pass
