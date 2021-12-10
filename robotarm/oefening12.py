
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
i=9
for x in range(9):
    robotArm.grab()
    colors = robotArm.scan()
    if colors == "red":
        for x in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(i):
            robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    i -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()