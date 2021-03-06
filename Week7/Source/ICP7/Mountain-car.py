import gym
import random
import numpy as np
from statistics import mean,median
from collections import Counter

LR = 1e-3
env = gym.make('MountainCar-v0')
env.reset()
goal_Steps = 200
score_requirement = 50
initial_games = 10000

def random_games():
    for episode in range(5):
        env.reset()
        for t in range(goal_Steps):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break

def initial_population():
    training_data=[]
    scores=[]
    accepted_scores=[]
    for _ in range (initial_games):
        score=0
        game_memory=[]
        prev_observation=[]
        for _ in range(goal_Steps):
            action = random.randrange(0,2)
            observation, reward, done, info = env.step(action)
            if len(prev_observation)>0:
                game_memory.append([prev_observation,action])
            prev_observation = observation
            score+=reward
            if done:
                break
        if score>=score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] ==1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
                training_data.append([data[0],output])
        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    np.save('saved.np',training_data_save)
    print('Average accepted scores: ',mean(accepted_scores))
    print('Median accepted scores: ',median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data

random_games()

initial_population()
