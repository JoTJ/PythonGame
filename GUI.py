import Board, Stone, Player, Position, Game, GUI, os
class GUI:
    def __init__(self):
        self._game = True
    def message(self,messageText):
        print(messageText)
        
    def printPlayerOnTurn(self,player):
        print("Spieler am Zug: "+str(player))
        
    def getClick(self):
        ring = int(input("Ring: "))
        number = int(input("Number: "))
        return Position.Position(ring, number)
        
    def endGame(self,text):
        print("endgame "+ text)
        self._game = False
        input("Warte...")
        
    def main(self):
        self._gameObj = Game.Game(self)
        GUI()
        while (self._game):
            self.printBoard()
            self._gameObj.doTurn()

    def getStringOfStone(self,i,j):
        board = self._gameObj.getBoard()
        if board.getStone(Position.Position(i,j))==None:
            return "-"
        stone = board.getStone(Position.Position(i,j))
        if stone.getColor()=='white':
            return "O"
        else:
            return "X"
                 
    def printBoard(self):
# =============================================================================
         os.system('cls')
         print(self.getStringOfStone(0,0)+" "*14+self.getStringOfStone(0,1)+" "*14+self.getStringOfStone(0,2))
         print(" ")
         print("  "*3+self.getStringOfStone(1,0)+" "*8+self.getStringOfStone(1,1)+" "*8+self.getStringOfStone(1,2))
         print(" ")
         print(" "*10+self.getStringOfStone(2,0)+" "*4+self.getStringOfStone(2,1)+" "*4+self.getStringOfStone(2,2))
         print(" ")
         print(self.getStringOfStone(0,7)+" "*4+self.getStringOfStone(1,7)+" "*4+self.getStringOfStone(2,7)+" "*9+self.getStringOfStone(2,3)+" "*4+self.getStringOfStone(1,3)+" "*4+self.getStringOfStone(0,3))
         print(" ")
         print(" "*10+self.getStringOfStone(2,6)+" "*4+self.getStringOfStone(2,5)+" "*4+self.getStringOfStone(2,4))
         print(" ")
         print("  "*3+self.getStringOfStone(1,6)+" "*8+self.getStringOfStone(1,5)+" "*8+self.getStringOfStone(1,4))
         print(" ")
         print(self.getStringOfStone(0,6)+" "*14+self.getStringOfStone(0,5)+" "*14+self.getStringOfStone(0,4))
         

#         for i in range (0,2):
#             for j in range (0,7):
#                 if board.getStone(Position.Position(i,j))==None:
#                     stringToPring = "-"
#                 elif board.getStone(Position.Position(i,j)).getColor()=="white":
#                     stringToPring = "O"
#                 else:
#                     stringToPring = "X"
#                 lineToPrint += " "*(i+1)*
# =============================================================================

    if __name__=="__main__":
        guiObj = GUI.GUI()
        guiObj.main()
        