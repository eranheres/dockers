#defaults write org.macosforge.xquartz.X11 enable_iglx -bool true

import matplotlib.pyplot as plt
import gym
import time

env = gym.make('CartPole-v0')
done = False

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

#fig.show()
#fig.canvas.draw()
for _ in range(200):
    done = False
    env.reset()

    while not done:
        # action = pi.act(True, obs)[0] # pi means a policy which produces an action, if you have
        # obs, reward, done, info = env.step(action) # do action, if you have
        _, _, done, _ = env.step(env.action_space.sample())
        env_rnd = env.render(mode='rgb_array')
        ax.clear()
        ax.imshow(env_rnd)
        #fig.canvas.draw()
        #time.sleep(0.001)
        #print("run step")

env.close()