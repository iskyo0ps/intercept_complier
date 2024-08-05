
my os version is 23H2(OS Build 22631.3880)
```powershell
winver
```

>[!CAUTION]
>If you wanna build this demo, you should adjust all this path which located in your environment.

a useful tool in windows is everything.exe developed by voidtool.

# Path to MSVC bin directory  
MSVC_BIN_PATH = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"  
  
  
# Path to include directories  
INCLUDE_PATH1 = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.29.30133\include"  
INCLUDE_PATH2 = "C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0\km\crt"  
  
# Path to library directory  
LIBRARY_PATH1 = "C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\ucrt_enclave\x64"  
LIBRARY_PATH2 = "C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\um\x64" 
LIBRARY_PATH3 = "C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\ucrt\x64" 
LIBRARY_PATH4 = "C:\DK\win\vc\14.29.30133\BuildTools\VC\Tools\MSVC\14.29.30133\lib\x64"

using the following command to build demo
```powershell
C:"\Program Files (x86)"\"Microsoft Visual Studio"\2022\BuildTools\VC\Tools\MSVC\14.40.30113\bin\Hostx64\x64\nmake all
```
run 
```powershell
./MyCppProject.exe
```
to check the output in terminal
