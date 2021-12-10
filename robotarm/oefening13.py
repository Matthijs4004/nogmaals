from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
i=9
x=1
for b in range(i):
    robotArm.grab()
    for b in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(10):
        robotArm.moveLeft()
    x += 1
    i -= 1
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()