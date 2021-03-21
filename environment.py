from gym import Env, spaces
import numpy as np
from driver import AgarLiveWebdriver
import time

class AgarIoEnv(Env):
    def __init__(self, resize_scale = 0.25):
        print('Creating instance of AgarIoEnv')
        super(AgarIoEnv, self).__init__()

        self.game_mass_history = None
        self.driver = AgarLiveWebdriver(start = False)

        # Angle, velocity, W key and space key
        self.action_space = spaces.Box(low = 0., high = 1., shape = (4,))

        # Current game screen
        width = int(resize_scale * self.driver.browserSize[0])
        height = int(resize_scale * self.driver.browserSize[1])
        self.observation_space = spaces.Box(low=0, high=255, shape=(height, width, 3), dtype=np.uint8)


    def step(self, action):
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
        
        current_mass = self.driver.playerScore()
        previous_mass = self.game_mass_history[-1]
        self.game_mass_history.append(current_mass)

        reward = -1
        if done is not False:
            # Reward is the percentage of change in masses
            reward = (current_mass - previous_mass) / previous_mass

        return obs, reward, done, {
            'max_mass': np.max(self.game_mass_history),
            'min_mass': np.min(self.game_mass_history),
            'mean_mass': np.mean(self.game_mass_history),
            'current_mass': self.game_mass_history[-1]
        }
    
    def sampleAction(self):
        return np.random.uniform(low = .0, high = 1., size = 4)

    def __getMovementSpeed(self, speedAction):
        if speedAction < .25: return 'slow'
        if speedAction < .75: return 'balanced'
        return 'fast'

    def __getObservation(self):
        image = self.driver.screenshot()
        image = image.resize((self.observation_space.shape[1], self.observation_space.shape[0]))
        return np.array(image)[:, :, :3]

    def reset(self):
        print('Resetting AgarIoEnv')
        if self.game_mass_history is not None:
            self.driver.continuePlaying()
            self.game_mass_history = [self.driver.playerScore()]
            return self.__getObservation()
        else:
            self.driver.start()
            self.game_mass_history = [self.driver.playerScore()]
            return self.__getObservation()

    def close(self):
        print('Closing AgarIoEnv')
        self.driver.flush()

    def seed(self):
        pass

    def render(self):
        pass
