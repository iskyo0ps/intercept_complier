# Makefile for MyCppProject  
  
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
# Compiler  
CXX = $(MSVC_BIN_PATH)\cl  
  
# Linker  
LINKER = $(MSVC_BIN_PATH)\link  
  
# Compiler flags  
CXXFLAGS = /EHsc /I$(INCLUDE_PATH1) /I$(INCLUDE_PATH2)  
  
# Linker flags  
LDFLAGS = /LIBPATH:$(LIBRARY_PATH1) /LIBPATH:$(LIBRARY_PATH2) /LIBPATH:$(LIBRARY_PATH3) /LIBPATH:$(LIBRARY_PATH4) 
  
# Target executable  
TARGET = MyCppProject.exe  
  
# Source files  
SRCS = main.cpp  
  
# Object files  
OBJS = $(SRCS:.cpp=.obj)  
  
# Build target  
all: $(TARGET)  
  
# Link object files to create the executable  
$(TARGET): $(OBJS)  
	$(LINKER) $(OBJS) $(LDFLAGS) /OUT:$@  
  
# Compile source files to object files  
.cpp.obj:  
	$(CXX) $(CXXFLAGS) /c $<  
  
# Clean up build files  
clean:  
	del $(OBJS) $(TARGET)  