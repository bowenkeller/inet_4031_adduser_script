# Add Users Ubuntu Script

##Program Description

This program contains a script that is able to automate the addition of new users to an Ubuntu system. Manually a user would use the adduser command and follow prompts to add a new user to the system, and this program automates the same process, allowing batches of users to be added simultaneously.

##Program Operation

In order to operate this script, navigate to the directory containing it, and create a .input file containing the users you would like to add. Make sure you have Python installed and either execute permissions for the create-users.py file, or the ability to modify execute permissions for the file.

### Input File Format

This program can take text input files containing user information to be added. The file should contain users separated by newlines, their information delimited by colons as follows username:password:lastname:firstname:groups. The group field may be left empty with '-', contain a single group, or be further delimited with commas as follows 'group01,group02,group05'.

### Command Execution

If the file is not already executable, run the command 'chmod +x create-users.py' at the command line, then at the command line run sudo ./create-users.py < yourfilename.input

### "Dry Run"

If you choose to perform a dry run, the script will print out all of the commands it would run had you chosen to actually run the script. Helpful for ensuring commands look correct to prevent mistakes. To perform a dry run, comment out all three of the 'os.system(cmd)' lines. 
