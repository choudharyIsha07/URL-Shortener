#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ishac123
#
# Created:     26-03-2023
# Copyright:   (c) ishac123 2023
# Licence:     <your licence>
#-----------------------------------------------------------------------------

import pyshorteners

link = input("enter the link: ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)