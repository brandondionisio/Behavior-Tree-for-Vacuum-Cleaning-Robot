# Behavior-Tree-for-Vacuum-Cleaning-Robot
Implementation for a behavior tree dictating the functionality of a vacuum cleaning robot (simple reflex agent).

## Title

CS 131 HW 01 - Behavior Trees

## Author

Brandon Dionisio

## Behavior Tree

![image](https://github.com/brandondionisio/Behavior-Tree-for-Vacuum-Cleaning-Robot/assets/145251710/f2c288e3-1dec-461e-8845-98fe7ae15eba)

## Notes

Initially prompts the user for a starting battery level for the robot

Prompts the user to determine spot cleaning

Prompts the user to determine general cleaning

Dusty cleaning has a 20% chance of occurring at every call

Terminates once battery level reaches 0%

Terminates if the user turns off the robot after each call of do nothing
