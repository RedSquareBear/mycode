#!/usr/bin/env python3

loginsuccess = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "- - - - -] Loaded" in line:
            loginsuccess += 1

print("The number of successful log in attempts is: ", loginsuccess)
