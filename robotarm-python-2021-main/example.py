from random import getrandbits, randint
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
while True:
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()

    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()