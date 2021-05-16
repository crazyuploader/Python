#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


class IOString(object):
    def __init__(self):
        self.string = ""

    def GetString(self):
        self.string = str(input("Enter String: "))
    
    def PrintString(self):
        print(self.string.upper())


st = IOString()
st.GetString()
st.PrintString()
