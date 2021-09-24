from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
x = 1
i = 1
while i < 4:
    for m in range(1):
        robotArm.grab()
        for m in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for m in range(10):
            robotArm.moveLeft()
        
    if i == 4:
        break
    x += 1
    if x == 8:
        break        
i += 1
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()