# intercept_complier
This project is built to intercept all compiled commands executed in powershell(linux environment may later).

Focus on a compilable project, we pass the command line to the python script for processing via powershell profile, and make the necessary changes to the building command via rules in python(or a json file). The building commands would be passed into powershell for further execution.

In turn, we can take more operations with the code based on llvm-ir, not limited to code checking and function insertion.

Intercepted building command is faster than repalyzing a complex and large recorded building commands.

This idea seems good and easy to take, but really need effects to solve some problem we meet, such as cmake test demo check.

demo will be given as a simified one,we change the front complier from MSVC(cl.exe) into LLVM(clang.exe or clang-cl.exe) no matter the cl.exe invoked by make, cmake or other building tools.

# How to 
To achieve the goal of caching all command lines in PowerShell, allowing a Python script to decide whether to change the command and parameters, and then returning the command to PowerShell for execution, you can follow these steps:

1. **Set up a PowerShell profile script to intercept and cache commands.**
2. **Create a Python script to decide whether to modify the commands.**
3. **Ensure the PowerShell profile script sends commands to the Python script and executes the returned commands.**

### Step 1: Create a PowerShell Profile Script

1. **Locate or create your PowerShell profile script:**
   ```powershell
   $profile
   ```

   This command will show the path to your PowerShell profile script. If the file does not exist, you can create it by running:
   ```powershell
   New-Item -Path $profile -ItemType File -Force
   ```
    or copy the ps1 file into your path. Remeber to back up your original file.

2. **Edit the profile script to intercept and cache commands:**
   Add the following code to your PowerShell profile script:

   ```powershell
       # chage the path to your intercept.py Python script
       $pythonScriptPath = "C:/path/to/your/intercept.py"
   ```

   This script defines a custom `Prompt` function that intercepts commands entered by the user, sends them to a Python script for modification, and then executes the modified command.

### Step 2: Create the Python Script

1. **Create a Python script to decide whether to modify the commands:**
   Save the following code to a file, for example, `intercept.py`:

   This script reads the original command from the command line arguments, decides whether to modify it, and prints the modified command.

### Step 3: Test the Setup

1. **Open a new PowerShell session:**
   The changes to the profile script will take effect in the new session.

2. **Enter a command:**
   ```powershell
   Get-Process
   ```

   The command should be intercepted, sent to the Python script for potential modification, and then executed as either the original or modified command.

### Explanation

- **PowerShell Profile Script:**
  - The `Prompt` function is overridden to intercept user commands.
  - The `Invoke-CommandWithModification` function sends the command to the Python script and executes the returned command.

- **Python Script:**
  - The script reads the original command, decides whether to modify it, and prints the modified command.

### Customization

You can customize the `modify_command` function in the Python script to apply any modifications you need. The PowerShell profile script can also be extended to handle more complex scenarios, such as logging commands or handling errors.

This setup allows you to intercept, cache, modify, and execute PowerShell commands using a Python script, providing a flexible way to automate and manipulate PowerShell workflows.