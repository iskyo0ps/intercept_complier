import sys 
import subprocess   
  
def modify_command(command):  
    # Example modification: change "Get-Process" to "Get-Process | Select-Object -First 5"  
    if "Get-Process" in command:  
        command = command.replace("Get-Process", "Get-Process | Select-Object -First 5")  
    return command  
  
if __name__ == "__main__":  
    if len(sys.argv) > 1:  
        original_command = sys.argv[1]  
        # print(f"Original Command: {original_command}")  
        modified_command = modify_command(original_command)  
        # print(f"Modified Command: {modified_command}") 
        # print(modified_command)
        
        # Run the modified command in PowerShell  
        process = subprocess.Popen(["powershell", "-Command", modified_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
        output, error = process.communicate()  
        
        # Print the output  
        if process.returncode == 0:  
            print(modified_command)
            print("\n")
            print(output.decode())
            process.kill()
        else:  
            print(f"Error: {error.decode()}") 
           
    else:  
        print("")

    sys.exit() 
