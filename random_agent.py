
import gym
import numpy as np

# Creating the Environment
cliff_env = gym.make("CliffWalking-v0", render_mode='ansi')

done = False
state = cliff_env.reset()

while not done:
    print(cliff_env.render())
    action = int(np.random.randint(low=0, high=4, size=1))
    print(state, "--->", action)
    state, reward, done, truncated, info = cliff_env.step(action)
cliff_env.close()