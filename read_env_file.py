import os
from config import debug_enabled
# Define a function to read the .env file and collect its attributes
def read_env_file(filepath):
    env_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            line.replace(' ', '')
            line.replace('"', '')
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            key, value = line.split('=', 1)
            env_dict[key] = value.replace(' ', '')
    return env_dict

# Define the path to the .env file (assuming it is in the same directory as this script)
env_path = os.path.join(os.path.dirname(__file__), '.env')

# Read the .env file and collect its attributes
env_vars = read_env_file(env_path)

# Access the collected attributes as a dictionary
if debug_enabled:
    print(env_vars)
