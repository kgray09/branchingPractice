#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# Created on Thu Jan 13 21:57:15 2022

# @author: kimberleegray
userChange = int(input())

dollars = userChange // 100
remainder1 = userChange % 100

quarters = remainder1 // 25
remainder2 = remainder1 % 25

dimes = remainder2 // 10
remainder3 = remainder2 % 10

nickles = remainder3 // 5
remainder4 = remainder3 % 5

pennies = remainder4 // 1

if userChange == 0:
    print("No change")

if dollars > 0:
    if dollars == 1:
        print(dollars, "Dollar")
    else:
        print(dollars, "Dollars")

if quarters > 0:
    if quarters == 1:
        print(quarters, "Quarter")
    else:
        print(quarters, "Quarters")
        
if dimes > 0:
    if dimes == 1:
        print(dimes, "Dime")
    else:
        print(dimes, "Dimes")
        
if nickles > 0:
    if nickles == 1:
        print(nickles, "Nickel")
    else:
        print(nickles, "Nickels")

if pennies > 0:
    if pennies == 1:
        print(pennies, "Penny")
    else:
        print(pennies, "Pennies")


