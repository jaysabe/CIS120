#******************************************************************************
# Author:           Jay Abegglen, Robert Grays
# Lab:              2
# Date:             10/03/2023
# Description:      This program takes in current temperature and pressure readings
#                   from user, does some calculations, then returns average readings
# Input:            (What the program asks for, and the data type, e.g. string)
# Output:           (Summary of messages displayed by the program)
# Sources:          Lab 1 specifications
#                   Module 2
#******************************************************************************

from datetime import datetime


def get_temperature():
    temp = float(input("What is the current temperature? "))
    return temp


def get_temperature_final():
    temperature_final = float(input("What is the final temperature? "))
    return temperature_final


def get_minutes():
    minutes = float(input("How many minutes passed? "))
    return minutes


def calc_rate(temperature_final, temperature_initial, minutes):
    temperature_rate = temperature_final - temperature_initial
    temperature_rate /= minutes
    return round(temperature_rate)


def print_all(temperature_final, temperature_initial, rate):
    print("Current time: " + datetime.now().strftime("%X"))
    print("The current temperature is " + str(temperature_initial))
    print("The final temperature is " + str(temperature_final))
    print("Rate of change in temperature: ", format(rate, ".2f"))


def main():
    temperature_initial = get_temperature()
    temperature_final = get_temperature_final()
    minutes = get_minutes()
    rate = calc_rate(temperature_final, temperature_initial, minutes)
    print_all(temperature_final, temperature_initial, rate)


if __name__ == '__main__':
    main()
