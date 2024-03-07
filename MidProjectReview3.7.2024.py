#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
STUD_MM = 8
# use with a robot that:
# - uses the standard wheels known as EV3EducationSetTire
# - wheels are ~12.39 studs apart

wheel2WheelDiam = 12.39 # The space between both wheels (switch up to fix problems)
#stick around this value increase if its turning too short and decrease if it is turning to far. It is finnicky

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, wheel2WheelDiam * STUD_MM) 

# Enable odometry
# Use odometry to drive to specific coordinates (speed,x,y)
mdiff.odometry_start() # starts at (0,0)
for i in range(1):
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 500) #500 mm forward
    mdiff.on_to_coordinates(SpeedRPM(40), -500, 500) #500 mm right
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 500) # backward
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 0) # back to the origin

    mdiff.turn_to_angle(SpeedRPM(40), 90)# Use odometry to rotate in place to 90 degrees

# Disable odometry
mdiff.odometry_stop()