import time
from environment import AgarIoEnv
import numpy as np
import pyautogui
from stable_baselines import DDPG

if __name__ == '__main__':
    env = AgarIoEnv()
    model = DDPG.load("agarlive_rl")
    initial_action = env.sampleAction()
    obs, rewards, dones, info = env.step(initial_action)

    while True:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()

        if (done):
            print(f'Elapsed time {reward}')
            break