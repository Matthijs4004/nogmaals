from random import getrandbits, randint
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(30):
    robotArm.grab()
    colors = robotArm.scan()
    if colors == "red":
        for x in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(9):
            robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()