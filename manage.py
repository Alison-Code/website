#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2016 Michal Cihar <michal@cihar.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmaweb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
print("Hello World")
def employee(str):
    print("Employee")
    
    
    try:
    while (1):
        print("\nWELCOME TO SHIVANG's CALCULATOR")
        print("ENTER YOUR FIRST NUMBER")
        var1 = int(input())
        print("WHAT DO YOU WANT TO DO")
        print("+" ,"-" ,"/" , "*")
        var3 = input()
        print("ENTER YOUR SECOND NUMBER")
        var2 = int(input())

        if var3=="+":
            print("Your ans is" , var1 + var2)

        elif var3=="-":
            print("Your ans is" , var1-var2)

        elif var3=="/":
            print("Your ans is" , var1 / var2)

        else:
            print("Your ans is" ,var1 * var2)

except Exception as e:
    print("Please write correctly")
        
    
