import board
class Player:
    """Ein Spieler"""
    def __init__(self, color, board):
        self._stonesSet = 0
        self._status  = ""
        self._color = color
        self._board = board
    
    def getStonesInGame(self):
        return self._board.numberOfStones(self._color)
        
    def increaseStonesSet(self):
        self._stonesSet() += 1
    
    def getStonesSet(self):
        return self._stonesSet
    
    def setStatus(self,status):
        self._status = status

    def getStatus(self,status):
        return self._status
        
    def getColor(self):
        return self._color
    
    def getPhase(self):
        if self._stonesSet < 9:
            return 1
        else:
            if self._numberOfStones > 3:
                return 2
            else:
                return 3
            
    def numberOfStones(self):
        self._board.numberOfStones(self._color)