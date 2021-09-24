from random import getrandbits, randint
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

while True:
    robotArm.grab()
    for x in range(9):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()