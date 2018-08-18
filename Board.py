import Math, Stone
class Board:
    def __init__(self):
        """Erstellt ein leeres Spielfeld"""
        self._stoneArray = [[""]*8]*3

    def getStone(self, position):
        """Gibt den Stein auf dem Feld zurück oder None"""
        return self._stoneArray[position.getRing()][position.getNumber()]

    def setStone(self,stone, position):
        """Fügt den Stein auf die Position ein"""
        self._stoneArray[position.getRing()][position.getNumber()]=stone
        
    def removeStone(self,position):
        """Entfernt den Stein an angegebener Position oder wirft eine Exception wenn kein Stein dort ist"""
        if self._stoneArray[position.getRing()][position.getNumber()]!="":
            self._stoneArray[position.getRing()][position.getNumber()]=""
        else:
            #TODO
            pass

    def isMill(self, position):
        """Prüft, ob sich an angegebener Position eine Mühle befindet"""
        result = False
        color = (self.getStone(position)).getColor()
        if position%2==1:
            result = result or (self._stoneArray[position.getRing()][position.getNumber()-1 %8]==color and self._stoneArray[position.getRing()][position.getNumber()+1 %8]==color)
            result = result or (self._stoneArray[position.getRing()-1 %3][position.getNumber()]==color and self._stoneArray[position.getRing()+1 %3][position.getNumber()]==color)
        else:
            result = result or (self._stoneArray[position.getRing()][position.getNumber()-2 %8]==color and self._stoneArray[position.getRing()][position.getNumber()-1 %8]==color)
            result = result or (self._stoneArray[position.getRing()][position.getNumber()+1 %8]==color and self._stoneArray[position.getRing()][position.getNumber()+2 %8]==color)
        return result
    

    def checkMove(self,oldPosition, newPosition, phase):
        """Guckt, ob der Stein von der alten zur neuen Position verschoben werden darf"""
        if phase ==1 or phase==3:
            if self._stoneArray[newPosition.getRing()][newPosition.getNumber()]=="":
                return True
            else:
                return False
        elif phase==2:
            numberDistance = abs(oldPosition.getNumber()-newPosition.getNumber())
            ringDistance = abs(oldPosition.retRing()-newPosition.getRing())
            if ringDistance ==0 and (numberDistance==1 or numberDistance==7):
                return True
            if ringDistance ==1 and numberDistance==0:
                return True 
            return False

    def numberOfStones(self,color):
        counter = 0
        for i in range (0,2):
            for j in range (0,7):
                if self._stoneArray[i][j]!="":
                    if self._stoneArray[i][j].getColor == color:
                        counter+=1
        return counter

    def saveBoardConfig(self):
        #speichert den aktuellen Zustand des Bretts ab und prüft, ob dieser schon zweimal erreicht wurde. In dem Fall True, sonst False
        #TODO
        pass               