import numpy as np
import gym
import random

env = gym.make("Blackjack-v0")

action_size = env.action_space.n
state_size = env.observation_space.spaces[0].n * env.observation_space.spaces[1].n * env.observation_space.spaces[2].n

qtable = np.zeros((state_size, action_size))

total_episodes = 12000
stepMax = 20
alpha = 0.8
decay = 0.005
gamma = 0.95
epsiMax = 1.0
epsiMin = 0.01
epsilon = 1.0

rewards = []

for episode in range(total_episodes):
    state = env.reset()
    over = False
    step = 0
    cumulReward = 0
    for step in range(stepMax):
        exp_exp_tradeoff = random.uniform(0, 1)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state[0], :])
        else:
            action = env.action_space.sample()
        new_state, reward, over, info = env.step(action)
        qtable[state[0], action] = qtable[state[0], action] + alpha * (reward + gamma * np.max(qtable[new_state[0], :]) - qtable[state[0], action])  # update
        cumulReward += reward
        state = new_state
        if over:
            break
    epsilon = epsiMin + (epsiMax - epsiMin) * np.exp(-decay * episode)
    rewards.append(cumulReward)

print(sum(rewards) / len(rewards))

env.reset()

results = []

for episode in range(50):
    state = env.reset()
    step = 0
    over = False
    for step in range(stepMax):
        action = np.argmax(qtable[state[0], :])
        print(action)
        new_state, reward, over, info = env.step(action)
        print("Reward: ", reward)
        print("__________")
        results.append(reward)
        if over:
            break
        state = new_state
avg = sum(results) / len(results)
print(avg)
env.close()
