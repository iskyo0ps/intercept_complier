# intercept_complier
This project is built to intercept all compiled commands executed in powershell(linux environment may later).

Focus on a compilable project, we pass the command line to the python script for processing via powershell profile, and make the necessary changes to the building command via rules in python(or a json file). The building commands would be passed into powershell for further execution.

In turn, we can take more operations with the code based on llvm-ir, not limited to code checking and function insertion.

Intercepted building command is faster than repalyzing a complex and large recorded building commands.

This idea seems good and easy to take, but really need effects to solve some problem we meet, such as cmake test demo check.

demo will be given as a simified one,we change the front complier from MSVC(cl.exe) into LLVM(clang.exe or clang-cl.exe) no matter the cl.exe invoked by make, cmake or other building tools.

# How to (in a wrong way)
To achieve the goal of caching all command lines in PowerShell, allowing a Python script to decide whether to change the command and parameters, and then returning the command to PowerShell for execution, you can follow these steps:

1. **Set up a PowerShell profile script to intercept and cache commands.**
2. **Create a Python script to decide whether to modify the commands.**
3. **Ensure the PowerShell profile script sends commands to the Python script and executes the returned commands.**

powershell only print all this output in command line, not for sequence command lines.

using miniFilter try again.