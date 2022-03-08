#!/usr/bin/env python3

import shutil #imports the shutil module
import os # imports the os module

def main():    #defining the main program function

    os.chdir('/home/student/mycode') #changes the current directory to the /mycode/ folder
    
    shutil.move('raynor.obj', 'ceph_storage/') #moves the file 'raynor.obj' to the /ceph_storage/ folder
    
    xname = input('What is the new name for kerrigan.obj? ') #prompts the user for input to rename 'kerrigan.obj'
    
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #moves the newly renamed 'kerrigan.obj' to the /ceph_                                                                       storage/ folder under the new name
main() #closes the main function
