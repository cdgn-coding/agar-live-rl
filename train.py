import time
from environment import AgarIoEnv
import numpy as np
import pyautogui
from stable_baselines.ddpg.policies import CnnPolicy
from stable_baselines.common.noise import OrnsteinUhlenbeckActionNoise
from stable_baselines import DDPG

if __name__ == '__main__':
    env = AgarIoEnv()
    n_actions = env.action_space.shape[-1]
    action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))
    model = DDPG(CnnPolicy, env, verbose=2, param_noise=None, action_noise=action_noise, tensorboard_log="./tensorboard/")
    model.learn(total_timesteps=400000)
    model.save("agarlive_rl")