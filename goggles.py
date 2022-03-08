#!/usr/bin/env python3

challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]

a = challenge[2][1]
b = challenge[2][0]
c = challenge [3]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print("My ", a, "! ", "The ", b, "they do ", c, "!")

d = trial[2]["goggles"]
e = trial[2]["eyes"]
f = trial[3]

print("My ",d,"!","The ", e,"The do", f,"!")

