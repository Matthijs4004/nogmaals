from random import getrandbits, randint
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
i = 0
m = 1
while i < 4:
    for x in range(m):
        robotArm.grab()
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    m += 1
    i += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()