import time
from environment import AgarIoEnv
import numpy as np
import pyautogui

if __name__ == '__main__':
    env = AgarIoEnv()
    print(env.observation_space.shape)
    action = env.sampleAction()
    obs, reward, done, _ = env.step(action)
    print(obs.shape)
    print(reward)
    env.reset()