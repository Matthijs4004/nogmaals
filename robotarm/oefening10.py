from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
i = 0
m = 9
n = 8
while i < 5:
    robotArm.grab()
    for x in range(m):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(n):
        robotArm.moveLeft()
    i += 1
    m -= 2
    n -= 2
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()