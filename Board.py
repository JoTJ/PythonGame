import Math, Stone, Position
class Board:
    def __init__(self):
        """Erstellt ein leeres Spielfeld und ein Dictonary"""
        self._stoneArray = [[""]*8]*3
        self._dict = {}

    #---------------------
    def isMill(self, position):
        """Prüft, ob sich an angegebener Position eine Mühle befindet"""
        result = False
        color = (self.getStone(position)).getColor()
 
        #Klammern ergänzt
        if position.getNumber()%2==1:  #Mittelsteine mit Nummern 1,3,5,7
            result = (self._stoneArray[(position.getRing()+1)%3][position.getNumber()]==color      
                     and self._stoneArray[(position.getRing()-1)%3][position.getNumber()]==color)    #ringübergreifende Mühle
                     or                                                                            #oder
                     (self._stoneArray[position.getRing()] [(position.getNumber()+1)%8)]
                     and (self._stoneArray[position.getRing()] [(position.getNumber()-1)%8)])        #Mühle mit benachbarten Ecksteinen
            
        else:                          #Ecksteine mit Nummern 0,2,4,6
            result = (self._stoneArray[(position.getRing()][(position.getNumber()-1)%8]==color
                     and self._stoneArray[(position.getRing()][(position.getNumber()-2)%8]==color)    #gegen den Uhrzeigersinn
                     or
                     (self._stoneArray[(position.getRing()][(position.getNumber()+1)%8]==color
                     and self._stoneArray[(position.getRing()][(position.getNumber()+2)%8]==color)    #im Uhrzeigersinn
    
    def checkOccupancy(self, position):
        if self._stoneArray[position.getRing()][position.getNumber()]=="":
            return ""
        else return self._stoneArray[position.getRing()][position.getNumber()].getColor()

    def checkRemoveability(self, position, color):
        if color != self.getStone(position).getColor():
            return False
        if not(self.isMill(position)):
            return True
        else:
            color = self.checkOccupancy(position)
            positionsOfColor = getPositionsOfColor()
            result = True;
            for position in positionsOfColor:
                if not(self.isMill(position)):
                    result False
                    break
            return result
            
    def getPositionsOfColor(self, color):
        positions = []
        for i in range (0,2):
            for j in range (0,7):
                if self._stoneArray[i][j].getColor() == color:
                    positons.append(Position.Position(i,j))
        return positions
        
    def everythingBlocked(self, color):
        positionsOfColor = getPositionsOfColor()
        allPositions = [""]*24
        for i in range (0,2):
            for j in range (0,7):
                allPostions[8*i+j] = Positon.Positon(i,j)
        
        #Idee: prüfe für alle Positionen, an denen sich Steine der Farbe befinden, ob ein Zug (Phase 2) an irgendeine andere Position möglich ist
        for position in positonsOfColor:
            for possiblePosition in allPositions:
                if (self.checkMove(position,possiblePosition,2)):
                    return False #möglicher Zug gefunden
        return True
        
    def getStone(self, position):
        """Gibt den Stein auf dem Feld zurück oder None"""
        return self._stoneArray[position.getRing()][position.getNumber()]

    def setStone(self,stone):
        """Fügt den Stein auf die Position ein"""
        position = stone.getPosition()
        self._stoneArray[position.getRing()][position.getNumber()]=stone
        
    def removeStone(self,position):
        """Entfernt den Stein an angegebener Position oder wirft eine Exception wenn kein Stein dort ist"""
        if self._stoneArray[position.getRing()][position.getNumber()]!="":
            self._stoneArray[position.getRing()][position.getNumber()]=""
        else:
            #TODO
            pass
    #---------------------
                                          
    def checkMove(self,oldPosition=None, newPosition, phase):     #=None, falls bei Setzphase keine alte Position angegeben
        """Prüft, ob der Stein auf ausgewähltes Feld kann"""
        if phase ==1 or phase==3:  #Phase 1 --> Setzen bzw. Phase 3--> Springen
            if self._stoneArray[newPosition.getRing()][newPosition.getNumber()]=="":    #nur prüfen, ob Feld frei
                return True
            else:
                return False
                                          
        elif phase==2:     #Phase 2 --> Zielen
            numberDistance = abs(oldPosition.getNumber()-newPosition.getNumber())
            ringDistance = abs(oldPosition.getRing()-newPosition.getRing())
                                          
            if ringDistance ==0 and (numberDistance==1 or numberDistance==7): #benachbartes Feld auf Ring
                return True
            if oldposition.getRing()%2==1 and ringDistance ==1 and numberDistance==0:     #ringübergreifend benachbartes Feld
                return True 
            return False

    #------------------------                                          
                                            
    def numberOfStones(self,color):
        counter = 0
        for i in range (0,2):
            for j in range (0,7):
                if self._stoneArray[i][j]!="":
                    if self._stoneArray[i][j].getColor == color:
                        counter+=1
        return counter
                                          
    #--------------------------
    def calculateConfigString(self):
        configString = ""
        for i in range (0,2):
            for j in range (0,7):
                if or i in range (0,2):
            for j in range (0,7):
                if self._stoneArray[i][j]!="black":
                    configString = configString + "X"
                elif self._stoneArray[i][j]!="white":
                    configString = configString + "O"
                else:
                    configString = configString + "-"
        return configString
    
    def getNumberOfActualBoardConfig(self):
        return self._dict[self.calculateConfigString()]                     
                   
    def saveBoardConfig(self):
        #speichert den aktuellen Zustand des Bretts ab und prüft, ob dieser schon zweimal erreicht wurde. In dem Fall True, sonst False
        configString = self.calculateConfigString()
        #configString als Schlüssel, Anuzahl der Vorkommen als Wert
        if configString in self._dict:
            self._dict[configString] = self._dict[configString]+1
        else:
            self._dict[configString] = 1