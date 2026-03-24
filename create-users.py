#!/usr/bin/python3

# INET4031
# Bowen Keller
# Creates users on Ubuntu systems
# March 23rd, 2026

#OS and SYS are used to interface with the system, RE is useful for character checking
import os
import re
import sys


def main():
    for line in sys.stdin:

        #Checking for # at the beginning of user input line
        #If # is present, set's match to True
        match = re.match("^#",line)

        #Splitting input line in a list as delimited by colons
        fields = line.strip().split(':')

        #Check if match from earlier is True, indicating the line is to be skipped
	#Then checks if the list of fields from the input line has five fields, any more or less would create errors
	#If either match is True or the number of fields is not five, then skip this user line
        if match or len(fields) != 5:
            continue

        #Creates pointers to the first four fields, naming them accordingly
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #The fifth field contains the groups the user is to be added into
	#Splits the field as delimited by commas into a list of groups for them to be added to
        groups = fields[4].split(',')

        #Print to show that this user made it past error checks earlier in the loop
        print("==> Creating account for %s..." % (username))
        #Building Ubuntu command, '%s'  fields replaced by gecos and username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #First time running command, uncomment print so you can see the constructed commands
	#After that, you can uncomment the os.system line, which will pass the command to the system
        print(cmd)
        os.system(cmd)

        #Shows the username is being passed correctly here
        print("==> Setting the password for %s..." % (username))
        #Creates a command for setting the user's password. echo repeats the password so that it can be confirmed
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #As above, the first time you run the program, uncomment the print to see what commands will be run
	#After that, uncomment the os.system to actually enter the commands
        print(cmd)
        os.system(cmd)

        for group in groups:
            #Looks for groups, if none then continues, else adds the user to the groups, looping until complete
	    #Again, uncomment print to check, os.system to actually run
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
