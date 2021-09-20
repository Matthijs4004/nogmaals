# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # Hier vult iemand het aantal geld dat hij/zij moeten betalen
payed = int(float(input('Payed amount: ')) * 100) # Hier vult iemand het aantal geld dat hij/zij al betaald heeft
change = payed - toPay # Wisselgeld wordt door deze formule berekent

if change > 0: # Als er geen wisselgeld is dan doet het programma niks en als dat het er wel is gaat het verder met de while loop
  coinValue = 500 # Als er wisselgeld is begint het programma met het vragen naar de 500 cent
  
  while change > 0 and coinValue > 0: # Als change groter is dan 0 en coinValue groter is dan 0 dan voert het programma de while loop uit
    nrCoins = change // coinValue # change wordt gedeeld door coinValue en daarna afgerond naar een heel getal dat het dichtst bij zit

    if nrCoins > 0: # Als nrCoins groter is dan 0 dan gaat hij door met de statements die onder de if-statement staan
      print('Return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Hier print het programma het maximale aantal coins wat je van een bepaald aantal centen kan terug vragen
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Het programma vraagt hier een aantal coins die je wilt terug hebben van een bepaalde waarde centen
      change -= nrCoinsReturned * coinValue # Het einde van de while loop

# Hieronder staan alle waardes van de geld munten die in het systeem staan
    if coinValue == 500:
      vijfh = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 300 
    elif coinValue == 300:
      drieh = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 200
    elif coinValue == 200:
      tweeh = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 50
    elif coinValue == 50:
      vijftig = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 20
    elif coinValue == 20:
      twintig = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 10
    elif coinValue == 10:
      tien = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 5
    elif coinValue == 5:
      vijf = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 2
    elif coinValue == 2:
      twee = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 1
    else:
      een = nrCoinsReturned," coins of ",coinValue, " cents"
      coinValue = 0

if change > 0: # Als change groter is dan 0 dan heb je niet genoeg wisselgeld gekregen en dan print het programma hoeveel je nog zou moeten krijgen
  print("Not all change has been returned")
  print('Change not returned: ', str(change) + ' cents')
else:
  print('Done.')
  print()
  print(vijfh)
  print(drieh)
  print(tweeh)
  print(vijftig)
  print(twintig)
  print(tien)
  print(vijf)
  print(twee)
  print(een)