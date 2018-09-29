import math, Stone, Player, Position, GUI
class Board:
    def __init__(self):
        """Erstellt ein leeres Spielfeld und ein Dictonary"""
        self._stoneArray = [[None]*8,[None]*8,[None]*8]
        self._dict = {}

    #---------------------
    def isMill(self, position):
        """Prüft, ob sich an angegebener Position eine Mühle befindet"""
        color = (self.getStone(position)).getColor()
 
        #Klammern ergänzt
        if (((position.getNumber())%2)==1):  #Mittelsteine mit Nummern 1,3,5,7
            if ((self._stoneArray[(position.getRing()+1)%3][position.getNumber()]!=None) and (self._stoneArray[(position.getRing()-1)%3][position.getNumber()]!=None)):
                if ((self._stoneArray[(position.getRing()+1)%3][position.getNumber()].getColor()==color) and (self._stoneArray[(position.getRing()-1)%3][position.getNumber()].getColor()==color)):    #ringübergreifende Mühle
                    return True
                                                                                            #oder
            if ((self._stoneArray[position.getRing()][(position.getNumber()+1)%8]!=None) and (self._stoneArray[position.getRing()][(position.getNumber()-1)%8]!=None)):
                if ((self._stoneArray[position.getRing()][(position.getNumber()+1)%8].getColor()==color) and (self._stoneArray[position.getRing()][(position.getNumber()-1)%8].getColor()==color)):        #Mühle mit benachbarten Ecksteinen
                    return True
        
        else:                          #Ecksteine mit Nummern 0,2,4,6
            if ((self._stoneArray[position.getRing()][(position.getNumber()-1)%8]!=None) and (self._stoneArray[position.getRing()][(position.getNumber()-2)%8]!=None)):
                if ((self._stoneArray[position.getRing()][(position.getNumber()-1)%8].getColor()==color) and (self._stoneArray[position.getRing()][(position.getNumber()-2)%8].getColor()==color)):      #gegen den Uhrzeigersinn
                    return True 
                    
            if ((self._stoneArray[position.getRing()][(position.getNumber()+1)%8]!=None) and (self._stoneArray[position.getRing()][(position.getNumber()+2)%8]!=None)):        
                if ((self._stoneArray[position.getRing()][(position.getNumber()+1)%8].getColor()==color)
                     and self._stoneArray[position.getRing()][(position.getNumber()+2)%8].getColor()==color):    #im Uhrzeigersinn
                    return True
        
        return False
        
    def checkOccupancy(self, position):
        if self._stoneArray[position.getRing()][position.getNumber()]==None:
            return None
        else:
            return self._stoneArray[position.getRing()][position.getNumber()].getColor()

    def checkRemoveability(self, position, color):
        if self.getStone(position)==None:
            return False
        if color != self.getStone(position).getColor():
            return False
        if not(self.isMill(position)):
            return True
        else:
            color = self.checkOccupancy(position)
            positionsOfColor = getPositionsOfColor(color)
            result = True;
            for position in positionsOfColor:
                if not(self.isMill(position)):
                    result = False
                    break
            return result
            
    def getPositionsOfColor(self, color):
        positions = []
        for i in range (0,2):
            for j in range (0,7):
                if self._stoneArray[i][j]!=None:
                    if self._stoneArray[i][j].getColor() == color:
                        positions.append(Position.Position(i,j))
        return positions
        
    def everythingBlocked(self, color):
        positionsOfColor = self.getPositionsOfColor(color)
        allPositions = [None]*24
        for i in range(0,3):
            for j in range(0,8):
                allPositions[8*i+j] = Position.Position(i,j)
        
        #Idee: prüfe für alle Positionen, an denen sich Steine der Farbe befinden, ob ein Zug (Phase 2) an irgendeine andere Position möglich ist
        for position in positionsOfColor:
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
        """Entfernt den Stein an angegebener Position falls vorhanden"""
        self._stoneArray[position.getRing()][position.getNumber()]=None
                                          
    def checkMove(self,oldPosition, newPosition, phase):     #=None, falls bei Setzphase keine alte Position angegeben
        """Prüft, ob der Stein auf ausgewähltes Feld kann"""
        if phase ==1 or phase==3:  #Phase 1 --> Setzen bzw. Phase 3--> Springen
            if self._stoneArray[newPosition.getRing()][newPosition.getNumber()]==None:    #nur prüfen, ob Feld frei
                return True
            else:
                return False
                                          
        elif phase==2:     #Phase 2 --> Zielen
            numberDistance = abs(oldPosition.getNumber()-newPosition.getNumber())
            ringDistance = abs(oldPosition.getRing()-newPosition.getRing())
            
            #check new field is None
            if self._stoneArray[newPosition.getRing()][newPosition.getNumber()]!=None:
                return False                              
            if ringDistance ==0 and (numberDistance==1 or numberDistance==7): #benachbartes Feld auf Ring
                return True
            if ringDistance ==1 and numberDistance==0:     #ringübergreifend benachbartes Feld
                return True 
            return False

    #------------------------                                          
                                            
    def numberOfStones(self,color):
        counter = 0
        for i in range(0,3):
            for j in range(0,8):
                if self._stoneArray[i][j]!=None:
                    if self._stoneArray[i][j].getColor() == color:
                        counter+=1
        return counter
                                          
    #--------------------------
    def calculateConfigString(self):
        configString = ""
        for i in range(0,3):
            for j in range(0,8):
                if self._stoneArray[i][j] == None:
                    configString = configString + "-"
                elif self._stoneArray[i][j].getColor()=="black":
                    configString = configString + "X"
                elif self._stoneArray[i][j].getColor()=="white":
                    configString = configString + "O"
                    
        print(configString)
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