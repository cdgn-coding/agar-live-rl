from environment import AgarIoEnv
import time

if __name__ == '__main__':
    env = AgarIoEnv()
    env.reset()
    while True:
        print(env.driver.playerScore())
        if env.driver.isGameDone():
            break
    env.reset()
    while True:
        print(env.driver.playerScore())
        if env.driver.isGameDone():
            break
    env.close()