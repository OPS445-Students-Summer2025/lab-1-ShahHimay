#!/usr/bin/env python3

'''Lab 3 Part 4 - Check free disk space on root'''

# Author ID: 118541234



import subprocess



def free_space():

    
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)

    return result.stdout.strip()



if __name__ == '__main__':

    print(free_space())
