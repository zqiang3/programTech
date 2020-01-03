## os.mkdir()

**Syntax:** os.mkdir(path, mode = 0o777, *, dir_fd = None)

**Parameter:**
**path**: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
**mode** (optional) : A Integer value representing mode of the directory to be created. If this parameter is omitted then default value Oo777 is used.
**dir_fd** (optional) : A file descriptor referring to a directory. The default value of this parameter is None.
If the specified path is absolute then dir_fd is ignored.

**Note:** The ‘*’ in parameter list indicates that all following parameters (Here in our case ‘dir_fd’) are keyword-only parameters and they can be provided using their name, not as positional parameter.

**Return Type:** This method does not return any value.



**Code #1**

```python
# Python program to explain os.mkdir() method 
	
# importing os module 
import os 

# Directory 
directory = "GeeksForGeeks"

# Parent Directory path 
parent_dir = "/home/User/Documents"

# Path 
path = os.path.join(parent_dir, directory) 

# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 
print("Directory '%s' created" %directory) 


# Directory 
directory = "ihritik"

# Parent Directory path 
parent_dir = "/home/User/Documents"

# mode 
mode = 0o666

# Path 
path = os.path.join(parent_dir, directory) 

# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# with mode 0o666 
os.mkdir(path, mode) 
print("Directory '%s' created" %directory) 

```



## os.mkdirs()

**Syntax:** os.makedirs(path, mode = 0o777, exist_ok = False)

**Parameter:**
**path**: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
**mode** (optional) : A Integer value representing mode of the newly created directory..If this parameter is omitted then the default value Oo777 is used.
**exist_ok** (optional) : A default value False is used for this parameter. If the target directory already exists an OSError is raised if its value is False otherwise not.

**Return Type:** This method does not return any value.

**Code #1**

```python
# Python program to explain os.makedirs() method  
    
# importing os module  
import os 
  
# Leaf directory 
directory = "ihritik"
  
# Parent Directories 
parent_dir = "/home/User/Documents/GeeksForGeeks/Authors"
  
# Path 
path = os.path.join(parent_dir, directory) 
  
# Create the directory 
# 'ihritik' 
os.makedirs(path) 
print("Directory '%s' created" %directory) 
  
# Directory 'GeeksForGeeks' and 'Authors' will 
# be created too  
# if it does not exists 
  
  
  
# Leaf directory 
directory = "c"
  
# Parent Directories 
parent_dir = "/home/User/Documents/GeeksforGeeks/a/b"
  
# mode 
mode = 0o666
  
path = os.path.join(parent_dir, directory) 
  
# Create the directory 
# 'c' 
   
os.makedirs(path, mode) 
print("Directory '%s' created" %directory) 
  
  
# 'GeeksForGeeks', 'a', and 'b' 
# will also be created if 
# it does not exists 
  
# If any of the intermediate level 
# directory is missing  
# os.makedirs() method will 
# create them 
  
# os.makedirs() method can be  
# used to create a directory tree 
```





## os.chdir()

***Syntax: os.chdir(path)***

**Parameters:**
**path:** A complete path of directory to be changed to new directory path.

**Returns:** Doesn’t return any value



**Code # 1**

```python
# Python3 program to change the  
# directory of file using os.chdir() method 
  
# import os library 
import os 
  
# change the current directory 
# to specified directory 
os.chdir(r"C:\Users\Gfg\Desktop\geeks") 
  
print("Directory changed") 
```



## os.path.exists()

**Syntax:** *os.path.exists(path)*

**Parameter:**
**path**: A path-like object representing a file system path. A path-like object is either a *string* or *bytes* object representing a path.

**Return Type:** This method returns a Boolean value of class *bool*. This method returns *True* if path exists otherwise returns *False*.



**Code #1**

```python
# Python program to explain os.path.exists() method  
    
# importing os module  
import os 
  
# Specify path 
path = '/usr/local/bin/'
  
# Check whether the specified 
# path exists or not 
isExist = os.path.exists(path) 
print(isExist) 
  
  
# Specify path 
path = '/home/User/Desktop/file.txt'
  
# Check whether the specified 
# path exists or not 
isExist = os.path.exists(path) 
print(isExist) 
```



# os.path.dirname()

**Syntax:** *os.path.dirname(path)*

**Parameter:**
**path**: A path-like object representing a file system path.

**Return Type:** This method returns a string value which represents the directory name from the specified path.

```python
# Python program to explain os.path.dirname() method  
    
# importing os.path module  
import os.path 
  
# Path 
path = '/home/User/Documents'
  
# Get the directory name   
# from the specified path 
dirname = os.path.dirname(path) 
  
# Print the directory name   
print(dirname) 
  
  
# Path 
path = '/home/User/Documents/file.txt'
  
# Get the directory name   
# from the specified path 
dirname = os.path.dirname(path) 
  
# Print the directory name   
print(dirname) 
  
  
# Path 
path = 'file.txt'
  
# Get the directory name   
# from the specified path 
dirname = os.path.dirname(path) 
  
# Print the directory name   
print(dirname) 
  
# In the above specified path  
# does not contains any 
# directory so,  
# It will print Nothing
```



# os.environ

`os.environ` in Python is a mapping object that represents the user’s environmental variables. It returns a dictionary having user’s environmental variable as key and their values as value.

`os.environ` behaves like a python dictionary, so all the common dictionary operations like get and set can be performed. We can also modify `os.environ` but any changes will be effective only for the current process where it was assigned and it will not change the value permanently.

**Syntax:** os.environ

**Parameter:** It is a non-callable object. Hence, no parameter is required

**Return Type:** This returns a dictionary representing the user’s environmental variables

```python
# Python program to explain os.environ object  
  
# importing os module  
import os 
import pprint 
  
# Get the list of user's 
# environment variables 
env_var = os.environ 
  
# Print the list of user's 
# environment variables 
print("User's Environment variable:") 
pprint.pprint(dict(env_var), width = 1) 
```



## os.system()

