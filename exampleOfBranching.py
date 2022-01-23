#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:57:15 2022

@author: kimberleegray
"""
# given a number of pennies < 100, 
# find the min number of coins to represent them

#Example 81 cents => 81 pennies
# 3 quarters, 1 nickle, 1 penny

# step 1: read the amount gtom the user
a = int(input("Enter the amount: "))
# step 2: divide a by 25 to get the number of quaters and remainder
Quarters = a // 25
remainder = a % 25
# step 3: divide remainder by 10 to get number of dimes and remainder 2
dimes = remainder = remainder // 10 
remainder2 = remainder % 10
# step 4: divide remainder2 by five to get number of nickles and pennies
Nickles = remainder2 // 5
Pennies = remainder2 % 5

if Quarters > 0:
    if Quarters == 1:
        print(Quarters, "Quarter")
    else:
        print(Quarters, "Quarters")

if dimes > 0:
    if dimes == 1:
        print(dimes, "Dime")
    else:
        print(dimes, "Dimes")

if Nickles > 0:
    if Nickles == 1:
        print(Nickles, "Nickle")
    else:
        print(Nickles, "Nickles")

if Pennies > 0:
    if Pennies == 1:
        print(Pennies, "Penny")
    else:
        print(Pennies, "Pennies")





