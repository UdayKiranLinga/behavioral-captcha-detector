import json
import math
import random

def simulate_bot_movement():
    data = []
    x, y = 10, 10
    for i in range(50):
        x += 5
        y += 2
        t = 1000 + i * 100  # perfectly spaced timing
        data.append({'x': x, 'y': y, 't': t})
    return data

with open('../data/bot_mouse_data.json', 'w') as f:
    json.dump(simulate_bot_movement(), f)
# This code simulates mouse movement data for a bot and saves it to a JSON file.