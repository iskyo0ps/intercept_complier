import json  
import os  
import sys  
import subprocess  
from datetime import datetime  
  
# Define the base directory for the JSON files  
base_dir = 'C:\\Users\\qaz\\Desktop\\intercept_complier'  
os.makedirs(base_dir, exist_ok=True)  
  
# Define the JSON file paths  
cache_json_file_path = os.path.join(base_dir, 'cache_commands.json')  
transform_json_file_path = os.path.join(base_dir, 'transform_commands.json')  
  
# Step 1: Cache Each Command  
def intercept_and_cache_command(command):  
    # Get the current time  
    current_time = datetime.now().isoformat()  
      
    # Create a command entry  
    command_entry = {  
        'command': command,  
        'time': current_time  
    }  
      
    # Load existing commands from the JSON file  
    if os.path.exists(cache_json_file_path):  
        with open(cache_json_file_path, 'r') as file:  
            commands = json.load(file)  
    else:  
        commands = []  
      
    # Add the new command entry  
    commands.append(command_entry)  
      
    # Sort commands by time  
    # commands.sort(key=lambda x: x['time'])  
      
    # Save the updated commands back to the JSON file  
    with open(cache_json_file_path, 'w') as file:  
        json.dump(commands, file, indent=4)  
  
# Step 2: Transform Each Command  
def transform_commands():  
    # Load cached commands from the JSON file  
    if os.path.exists(cache_json_file_path):  
        with open(cache_json_file_path, 'r') as file:  
            commands = json.load(file)  
    else:  
        print("No cached commands found.")  
        return []  
      
    # Apply transformations to each command  
    transformed_commands = []  
    for entry in commands:  
        command = entry['command']  
        # Example transformation: change "-First 3" to "-First 5"  
        transformed_command = command #.replace("-First 3", "-First 5")  
        transformed_entry = {  
            'command': transformed_command,  
            'time': entry['time']  
        }  
        transformed_commands.append(transformed_entry)  
      
    # Save the transformed commands to the JSON file  
    with open(transform_json_file_path, 'w') as file:  
        json.dump(transformed_commands, file, indent=4)  
      
    return transformed_commands  
  
# Step 3: Execute Transformed Commands  
def run_command(command_entry):  
    command = command_entry['command']  
    print(command)  
      
    # Execute the command in PowerShell  
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    output, error = process.communicate()  
      
    # Print the output  
    if process.returncode == 0:  
        print(output.decode())  
    else:  
        print(f"Error: {error.decode()}")  
  
def execute_transformed_commands():  
    # Load transformed commands from the JSON file  
    if os.path.exists(transform_json_file_path):  
        with open(transform_json_file_path, 'r') as file:  
            commands = json.load(file)  
    else:  
        print("No transformed commands found.")  
        return  
      
    # Execute each command in sequence  
    for entry in commands:  
        run_command(entry)  
  
if __name__ == "__main__":  
    if len(sys.argv) > 1:  
        original_command = sys.argv[1]  
          
        # Step 1: Cache each command  
        intercept_and_cache_command(original_command)  
          
        # Step 2: Transform the cached commands  
        transformed_commands = transform_commands()  
          
        # Return the modified command  
        if transformed_commands:  
            print(transformed_commands[-1]['command'])  
    else:  
        print("")  
    sys.exit()  
