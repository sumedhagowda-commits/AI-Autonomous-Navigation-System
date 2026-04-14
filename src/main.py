import sys
import os

# FORCE correct path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from environment import GridEnvironment
from astar import astar
from agent import Agent
from visualization import draw


print("🚀 Program started")

env = GridEnvironment(size=20)
env.add_obstacles(10)

start = (0, 0)
goal = (19, 19)

path = astar(env.grid, start, goal)

print("Path:", path)

agent = Agent(start)
agent.set_path(path)

draw(env.grid, agent, goal)