function Invoke-CommandWithModification {  
    param (  
        [string]$Command  
    )  
  
    # Path to your Python script  
    $pythonScriptPath = "path/to/intercept.py"  
  
    # Run the Python script and capture the output
    # !!! all the print message as a return, rather a return function in python scirpt !!!
    $modifiedCommand = & python $pythonScriptPath $Command  

   # Execute the modified command  
    if ($modifiedCommand) {  
        # Invoke-Expression $modifiedCommand  
        Write-Host "Original Command: $Command"  
        Write-Host "Modified Command is:`n $modifiedCommand"  
        Write-Host "New command executed."
    } else {  
        Write-Host "No command to execute."  
    }   
}  
  
function Prompt {  
    $command = Read-Host "Intercept in PS $($pwd) >"  
    if ($command) {  
        Invoke-CommandWithModification -Command $command
        ""
        #infinite loop
        Prompt  
    }  
    ""  
}  
  
# # Ensure the custom prompt function is used  
# $function:prompt = $function:Prompt  