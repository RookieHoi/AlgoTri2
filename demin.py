import random


def affichage(display):
  print("   0 1 2 3 4 5 6 7 8")
  print("   _________________")
  for i in range(0,9):
    print(i+0, end=" |")
    for j in range(0,9):
      print(display[i][j], end=" ")
    print("")


def calibrage(matrice):
  print("   0 1 2 3 4 5 6 7 8")
  print("   _________________")
  for i in range(0,9):
    print(i+0, end=" |")
    for j in range(0,9):
      print(matrice[i][j], end=" ")
    print("")


matrice = [
    [0,0,0,0,0,0,0,0,0], #Matrice du démineur (là ou les variables son manipulées)
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    
display = [
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",], #Grille d'affichage (Ce que le joueur voit)
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",],
    ["☐","☐","☐","☐","☐","☐","☐","☐","☐",]
    ]

    
gameOver = False
bomb = False


while bomb == False:
    
    for i in range(len(matrice)):
        
        for j in range(len(matrice[i])):
           
            var = random.randint(1,5)
            if(var == 1):
                matrice[i][j] = "b"
                if (i>0 and j>0 and matrice[i-1][j-1]!="b"):
                    matrice[i-1][j-1]+=1
        
                if (j>0 and matrice[i][j-1]!="b"):
                    matrice[i][j-1]+=1

                if (i>0 and matrice[i-1][j]!="b"):
                    matrice[i-1][j]+=1

                if (i<len(matrice)-1 and j<len(matrice)-1 and matrice[i+1][j+1]!="b"):
                    matrice[i+1][j+1]+=1

                if (j<len(matrice)-1 and matrice[i][j+1]!="b"):
                    matrice[i][j+1]+=1

                if (i<len(matrice)-1 and matrice[i+1][j]!="b"):
                    matrice[i+1][j]+=1

                if (i>0 and j<len(matrice)-1 and matrice[i-1][j+1]!="b"):
                    matrice[i-1][j+1]+=1

                if (i<len(matrice)-1 and j>0 and matrice[i+1][j-1]!="b"):
                    matrice[i+1][j-1]+=1
                bomb = True


calibrage(matrice)
print("")


while gameOver == False:

    affichage(display)
    print("")
    x = int(input("choisir une ligne:  "))
    y = int(input("choisir une colonne:  "))
    print("")
    
    if(y in range(len(matrice)) and x in range(len(matrice))):
        
      if(matrice[x][y] == "b"):
          gameOver = True
          display[x][y] = matrice[x][y]
          affichage(display)
            
          print("Game Over")

      else:
        display[x][y] = matrice[x][y]
        print("")