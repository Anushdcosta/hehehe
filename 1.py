import itertools
import string
import os
import json

def save_state(state_file, state):
    with open(state_file, 'w') as f:
        json.dump(state, f)

def load_state(state_file):
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            return json.load(f)
    return None

def generate_combinations(file_name, state_file, num_combinations):
    # Include special characters along with letters and digits
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
    characters = string.ascii_letters + string.digits + special_characters
    state = load_state(state_file)
    start_length, start_index = 1, 0

    if state:
        start_length, start_index = state['length'], state['index']

    with open(file_name, 'a') as file:
        count = 0
        for length in range(start_length, 17):
            combinations = itertools.product(characters, repeat=length)
            if length == start_length:
                for _ in range(start_index):
                    next(combinations)
            for index, combo in enumerate(combinations, start=start_index):
                if count >= num_combinations:
                    save_state(state_file, {'length': length, 'index': index})
                    print(f'{num_combinations} combinations written to {file_name}')
                    return
                file.write(''.join(combo) + '\n')
                count += 1
            start_index = 0  # Reset index for new length

    # If finished generating all combinations, remove the state file
    if os.path.exists(state_file):
        os.remove(state_file)
    print(f'{num_combinations} combinations written to {file_name}')

# Parameters
file_name = 'combinations.txt'
state_file = 'state.json'
num_combinations = 1000000000  # Number of combinations to generate

generate_combinations(file_name, state_file, num_combinations)
