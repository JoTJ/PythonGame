import Board, Stone
class Game:
    def __init__(self):
        """Erstellt ein neues Spielfeld für das aktuelle Spiel"""
        self._board = Board.Board()
        self._phaseOfPlayer1 = 1
        self._phaseOfPlayer2 = 1
        self._playerOnTurn = True
        self._status = ""
        self._previousClickedStone = None
        self._player1stonesToSet = 9
        self._player2stonesToSet = 9
        self._numberOfTurnsWithoutMill = 0
        ##Programmlogik

    def getPlayerOnTurn(self):
        """Gibt zurück, welcher Spieler gerade am Zug ist (True: Spieler 1, False: Spieler 2)"""
        return self._playerOnTurn
    
    def getPhaseOfPlayer(self, player):
        """Gibt die aktuelle Phase eines Spielers zurück (True: Spieler 1, False: Spieler 2)"""
        if player:
            return self._phaseOfPlayer1
        else:
           return self._phaseOfPlayer2

    def getStatus(self):
        """Gibt den aktuellen Spielstatus zurück"""
        self._status

    def getBoard(self):
        return self._board

    def handleClick(self, position):
        self._status = ""
        colorOnThisTurn = True if self._playerOnTurn else False
        phaseOnThisTurn = self._phaseOfPlayer1 if self._playerOnTurn else self._phaseOfPlayer2
        phaseOfOtherPlayer = self._phaseOfPlayer2 if self._playerOnTurn else self._phaseOfPlayer1

        
        stoneOnThisTurn = self._board.getStone(position.getRing(),position.getNumber())
        if phaseOnThisTurn==1:
            if stoneOnThisTurn!="":
                self._status == "Feld bereits belegt"
                return
            else:
                stoneOnThisTurn = Stone(position,colorOnThisTurn,self._board)
                self._player1stonesToSet=self._player1stonesToSet-1 if self._playerOnTurn else self._player2stonesToSet=self._player2stonesToSet-1
                if self._player1stonesToSet==0:
                    self._phaseOfPlayer1 = 2
                if self._player2stonesToSet==0:
                    self._phaseOfPlayer2 = 2                            
                         
        elif phaseOnThisTurn==2:
            inputFinished = False
            while not(inputFinished):
                if stoneOnThisTurn=="" or stoneOnThisTurn.color != colorOnThisTurn:
                    self._status = "Es muuss ein eigener Stein, der bewegt werden soll, gewählt werden"
                    return
                else:
                    newPlace = GUI.askForNewPlaceOfStone();
                    selectedStone = self._board.getStone(newPlace)
                    if selectedStone!="":
                        if selectedStone.Color == colorOnThisTurn:
                            #Stein, der beweget werden soll, wrid überschrieben
                            stoneOnThisTurn = selectedStone
                            continue
                        else:
                            return
                    else:
                        if self._board.checkMove(stoneOnThisTurn, newPlace):
                            #Move
                            stoneOnThisTurn.move(newPlace,2)
                            break
                        else:
                            self._status = "In Phase 2 muss ein benachbartes Feld gewählt werden. Wähle erneut einen Stein und dann ein benachbartes Feld"
                            return                    
        elif phaseOnThisTurn == 3:
            inputFinished = False
            while not(inputFinished):
                if stoneOnThisTurn=="" or stoneOnThisTurn.color != colorOnThisTurn:
                    self._status = "Es muuss ein eigener Stein, der bewegt werden soll, gewählt werden"
                    return
                else:
                    newPlace = GUI.askForNewPlaceOfStone();
                    selectedStone = self._board.getStone(newPlace)
                    if selectedStone!="":
                        if selectedStone.Color == colorOnThisTurn:
                            #Stein, der beweget werden soll, wrid überschrieben
                            stoneOnThisTurn = selectedStone
                            continue
                        else:
                            return
                    else:
                        #Move
                        stoneOnThisTurn.move(newPlace,3)
                        inputFinished = True
                        
        if stoneOnThisTurn.isInMill():
            self._numberOfTurnsWithoutMill=0
            allowedToRemove = False
            while not(allowedToRemove):
                positionOfstoneToRemove = GUI.askForStoneToRemove()
                if self._board.getStone(positionOfstoneToRemove)=="":
                    GUI.printWrongMoveMessage("Es muss ein Stein gewählt werden")
                    break;
                stoneToRemove = self._board.getStone(positionOfstoneToRemove)
                if stoneToRemove.getColor()==colorOnThisTurn:
                    GUI.printWrongMoveMessage("Es muss ein gegnerischer Stein gewählt werden")
                if  not(stoneToRemove.IsInMill()):
                    allowedToRemove = True
                    break
                else:
                    if self._board.getNumberOfStonesOutsideFromMills(not(ColorOnThisTurn)==0):
                        allowedToRemove = True
                        break
                    else:
                        GUI.printWrongMoveMessage("Dieser Stein darf nicht entfernt werden")
                    
            self._board.removeStone(stoneToRemove)
            if self._board.numberOfStones(not(colorOnThisTurn))==3:
                self._phaseOfPlayer1=3 if playerOnTurn else self._phaseOfPlayer2=3
            if self._board.numberOfStones(not(colorOnThisTurn))<3:
                self._status = "Spielende"
                #Gewinner ist am Zug
                GUI.endOfGame(self._playerOnTurn)
                
            self._playerOnTurn = not(self._playerOnTurn)
        else:
            self._numberOfTurnsWithoutMill+=1                        
            
        if self._numberOfTurnsWithoutMill >=50:
            GUI.remis("50 Züge ohne Mühle")
            #check for remis
        if self._board.saveBoardConfig():
            GUI.remis("3mal die gleiche Stellung. Unentschieden")                