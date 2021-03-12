# Agar live RL

## Description

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

Agar live RL is a project which experiments with deep reinforcement learning on Agar, an online game featuring incomplete information. According to wikipedia:

> The objective of Agar is to grow a cell on a Petri dish by swallowing both randomly generated pellets (agar), which slightly increases a cell's mass, and smaller cells, without being swallowed by even larger cells.

With this in mind, Agar Live RL is a project that trains an RL agent on a real online game and, it plays over and over again until it has a certain level of performance. In order to achieve this goal, we are automating actual game actions using tools such as ```pyautogui``` and ```selenium```.

## Installation

All the dependencies are listed in ```requirements.txt```. Agar live RL also uses selenium to automate certain task therefore you must have chromedriver installed in your machine. For this reason, a script called ```install.py``` is included, it downloads chromedriver for windows in the project's path.

On the other hand, Agar live RL make use of adblocker to skip ads the ads that blocks the screen. Make sure to install adblocker in your machine and update ```adblockExtension``` in the file ```constants.py``` with your adblocker installation path.

## Project task list

- [x] Create AgarLiveDriver, a class which can instantiate and interacts with the game, hidding complexities of the automation tasks.
- [ ] Create AgarLiveEnv, a class that will be composed by an AgarLiveDriver which implements an OpenAI gym environment
- [ ] Build AgarLiveAgent, a class that should implement different RL methods and lastly, train it.