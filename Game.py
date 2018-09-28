import Board, Stone, Player
class Game:
    def __init__(self):
        """Erstellt ein neues Spielfeld für das aktuelle Spiel"""
        self._board = Board.Board()
        self._playerOnTurn = 1
        self._previousClickedStone = None
        self._numberOfTurnsWithoutMill = 0
        self._player1 = Player.Player("white",self._board)
        self._player2 = Player.Player("black",self._board)

    def getPlayerOnTurn(self):
        """Gibt zurück, welcher Spieler gerade am Zug ist (True: Spieler 1, False: Spieler 2)"""
        return self._playerOnTurn
    
    def getPhaseOfPlayer(self, playerNumber):
        """Gibt die aktuelle Phase eines Spielers zurück (1: Spieler 1, 2: Spieler 2)"""
        if playerNumber == 1:
            self_player1.getPhase()
        else:
            self_player2.getPhase()
        
    def getStatus(self,playerNumber):
        """Gibt den aktuellen Status eines Spielers zurück (1: Spieler 1, 2: Spieler 2)"""
        if playerNumber == 1:
            self._player1.getStatus()
        else:
            self._player2.getStatus()
        
    def getBoard(self):
        return self._board

    def handleClick(self):
        GUI.printPlayerOnTurn(playerOnTurn)        
        
        # Informationen über den Zug holen
        if playerOnTurn == 1:
            actualPlayer = self._player1
            actualColor = "white"
        else:
            actualPlayer = self._player2
            actualColor = "black"
        actualPhase = actualPlayer.getPhase()
        
        #Zug in Phase 2 möglich?
        if actualPhase == 2:
            if self._board.everythingBlocked(actualColor):
                GUI.Message("Kein Zug möglich. Passe.")
                time.sleep(5)
                self._changeTurn()
                return
            
        #Phase 1 - setzen
        if actualPhase == 1:
            GUI.Message("Wähle Feld, um Stein zu platzieren")
            clickAccepted = False
            while not(clickAccepted):
                positionToSet = GUI.GetClick()
                #Gültige Eingabe
                if (self._board.checkMove(positionToSet,1)):
                    clickAccepted = True
                    newStone = Stone.Stone(positionToSet,actualColor,self._board)
                    continue
                #Ungültige Eingabe
                else:
                    GUI.Message("Ungültiges Feld. Wähle Feld, um Stein zu platzieren")
            
            #neuen Stein setzen
            self._board.setStone(Stone.Stone(positionToSet,actualColor,self._board))
            affectedPosition = positionToSet
        
        #Phase 2/3 - ziehen
        else:
            #gültige Eingabe holen
            GUI.Message("Wähle Stein, der bewegt werden soll")
            firstClickAccepted = False
            bothClicksAAccepted = False
            while not(bothClicksAAccepted):
                while not(firstClickAccepted):
                    positionFrom = GUI.GetClick()
                    #Ungültiger 1. Click
                    if self._board.checkOccupancy()!=actualColor:
                        GUI.Message("Du musst einen eigenen Stein wählen.")
                        continue
                    #Gültiger 1. Click
                    else:
                        firstClickAccepted = True
                
                #Nachricht für 2. Click
                if (actualPhase == 2):
                    GUI.Message("Wähle neue Position des Steins")
                else:
                    GUI.Message("Wähle neue Position des Steins. Du darfst Springen")
                
                positionTo = GUI.GetClick()
                #Gültiger 2.Click
                if (self._board.checkMove(positionFrom,positionTo,actualPhase)):
                    affectedPosition = positionTo
                    break
                #Ungültiger 2. Click. Starte wieder beim ersten Click (evtl kein gültiger 2.Click möglich)
                else:
                    GUI.Message("Wähle Stein, der bewegt werden soll")
                    firstClickAccepted = False
         
        ###    
        #Zug ausführen
        
        #Stein von alter Position entfernen (durch Zug) - in Phase 2 oder 3 
        if actualPhase!=1:
            newStone = Stone.Stone(positionTo,actualColor,self._board)
            self._board.removeStone(positionFrom)
        self._board.setStone(newStone)
        
        #Auf Mühle prüfen
        if self._board.isMill(affectedPosition):
            
            #Anzahl Züge ohne Mühle zurücksetzen
            self._numberOfTurnsWithoutMill = 0
            
            #Stein entfernen
            GUI.Message("Stein entfernen")
            clickAccepted = False
            while not(clickAccepted):
                positionToRemove = GUI.GetClick()
                
                #Stein muss Farbe des Gegners haben (wird in board.checkRemoveability geprüft)
                if actualColor == "white":
                    otherColor = "black"
                else:
                    otherColor = "white"
                #Prüfen, ob Stein entfernt werden darf
                if self._board.checkRemoveability(positionToRemove,otherColor):
                    clickAccepted = True
                    #Stein nun entfernen
                    self._board.removeStone(positionToRemove)
                #Falsche Wahl mitteilen
                else:
                    GUI.Message("Es muss ein gegnerischer Stein gewählt werden, der sich nicht in einer Mühle befindet (wenn der Gegner nicht nur Mühlen hat)")

        #Keine Mühle
        else:
            #Anzahl Züge ohne Mühle erhöhen
            self._numberOfTurnsWithoutMill += 1
        
        
        ###Daten aktualisieren
        #Anzahl gesetzter Steine aktualisieren
        if actualPhase == 1:
            actualPlayer.increaseStonesSet()
        ChangeTurn()
        self._board.saveBoardConfig()
        #Auf Ende überprüfen
        self.CheckGameGoesOn()
        
    def CheckGameGoesOn(self):
        #Züge ohne Mühle
        if self._numberOfTurnsWithoutMill >= 50:
            self._player1.setStatus("Remis. 50 Züge ohne Mühle")            
            self._player2.setStatus("Remis. 50 Züge ohne Mühle")
            GUI.EndGame()
        #Gleiche Stellung
        if self._board.getNumberOfActualBoardConfig >= 3:
            self._player1.setStatus("Remis. 3x gleiche Stellung")            
            self._player2.setStatus("Remis. 3x gleiche Stellung")
            GUI.EndGame()
        #Niederlage Spieler 1
        if self._player1.getStonesInGame < 3:
            self._player1.setStatus("Verloren")            
            self._player2.setStatus("Gewonnen")
            GUI.EndGame()
        #Niederlage Spieler 2
        if self._player2.getStonesInGame < 3:
            self._player2.setStatus("Verloren")            
            self._player1.setStatus("Gewonnen")
            GUI.EndGame()

                
    def changeTurn(self):
        if self._playerOnTurn = 1:
            self._playerOnTurn = 2
        else:
            self._playerOnTurn = 1
            
    