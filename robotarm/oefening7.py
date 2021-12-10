from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
i = 1
x = 6
while i < 4:
    for x in range(x):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for i in range(2):
        robotArm.moveRight()

    x += 1
    if x == 7:
        i == False
    i += 1  


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()