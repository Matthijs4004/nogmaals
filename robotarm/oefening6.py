from random import getrandbits
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

for x in range(7):
    robotArm.moveRight()

for x in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()