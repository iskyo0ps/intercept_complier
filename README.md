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

Using Windows Process Monitor (ProcMon) to check command lines with their parameters can be a bit tricky, as ProcMon is primarily designed for monitoring file system, registry, and process/thread activity. However, you can still use it to capture command line arguments by following these steps:

### Using Process Monitor (ProcMon)

1. **Download and Run ProcMon**:
   - Download Process Monitor from the [Microsoft Sysinternals website](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon).
   - Extract the downloaded file and run `Procmon.exe`.

2. **Configure Filters**:
   - When ProcMon starts, it will begin capturing all events. This can be overwhelming, so you need to set up filters.
   - Click on the `Filter` menu and select `Filter...` or press `Ctrl+L`.
   - Add a filter to capture only process creation events:
     - In the filter dialog, set the first drop-down to `Operation`.
     - Set the second drop-down to `is`.
     - Set the third drop-down to `Process Create`.
     - Click `Add`, then `OK`.

3. **Start Capturing**:
   - Click the `Capture` button (or press `Ctrl+E`) to start capturing events if it’s not already running.

4. **Run Your Command**:
   - Execute the command or script you want to monitor.

5. **Stop Capturing**:
   - Once the command has run, click the `Capture` button again to stop capturing events.

6. **Find the Event**:
   - Look through the captured events for the `Process Create` event related to your command.
   - Click on the event to view its details. The command line and parameters should be visible in the event properties.

### Using Windows Event Viewer

If ProcMon does not provide the necessary details, you can use Windows Event Viewer to capture command line arguments for process creation events.

1. **Enable Command Line Auditing**:
   - Open the `Local Group Policy Editor` by typing `gpedit.msc` in the Run dialog (`Win + R`).
   - Navigate to `Computer Configuration -> Windows Settings -> Security Settings -> Advanced Audit Policy Configuration -> System Audit Policies - Local Group Policy Object -> Detailed Tracking`.
   - Enable `Audit Process Creation` and `Audit Process Termination`.

2. **Check Event Viewer**:
   - Open `Event Viewer` by typing `eventvwr.msc` in the Run dialog (`Win + R`).
   - Navigate to `Windows Logs -> Security`.
   - Look for events with `Event ID 4688` (A new process has been created).
   - The event details will include the command line and parameters.

### Using PowerShell

You can also use PowerShell to monitor process creation and capture command line arguments.

1. **Run PowerShell Script**:
   - Open PowerShell with administrative privileges.
   - Use the following script to monitor process creation:

```powershell
$Query = @"
    <QueryList>
        <Query Id="0" Path="Security">
            <Select Path="Security">*[System[(EventID=4688)]]</Select>
        </Query>
    </QueryList>
"@

Register-WmiEvent -Query $Query -SourceIdentifier "ProcessCreationMonitor" -Action {
    $event = $Event.SourceEventArgs.NewEvent
    $commandLine = $event.InsertionStrings[8]
    Write-Output "Process Created: $commandLine"
}
```

This script will monitor for process creation events and output the command line arguments to the console.

By using these methods, you can effectively monitor and capture command line arguments and parameters for processes on a Windows system.