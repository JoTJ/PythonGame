class Board:
    def __init__(self):
        """Erstellt ein leeres Spielfeld"""
        pass

    def getStone(position):
        """Gibt den Stein auf dem Feld zurück oder None"""
        pass

    def setStone(stone, position):
        """Fügt den Stein auf die Position ein"""
        pass
        
    def removeStone(positon):
        """Entfernt den Stein an angegebener Position oder wirft eine Exception wenn kein Stein dort ist"""
        pass

    def isMill(position):
        """Prüft, ob sich an angegebener Position eine Mühle befindet"""
        pass

    def checkMove(oldPosition, newPosition, phase):
        """Guckt, ob der Stein von der alten zur neuen Position verschoben werden darf"""
        pass

class Game:
    def __init__(self):
        """Erstellt ein neues Spielfeld für das aktuelle Spiel"""
        self._board = Board()
        self._phaseOfPlayer1 = 1
        self._phaseOfPlayer2 = 1
        self._playerOnTurn = True

        ##Programmlogik

    def getPlayerOnTurn(self):
        """Gibt zurück, welcher Spieler gerade am Zug ist (True: Spieler 1, False: Spieler 2)"""
        return _playerOnTurn
    
    def getPhaseOfPlayer(self, player):
        """Gibt die aktuelle Phase eines Spielers zurück (True: Spieler 1, False: Spieler 2)"""
        if player:
            return _phaseOfPlayer1
        else:
           return _phaseOfPlayer2

    def getStatus(self):
        """Gibt den aktuellen Spielstatus zurück"""

    def getBoard(self):
        return _board

class Stone:
    """Ein Spielstein"""

    def __init__(self, ring, position, color, board):
        """Erstellt einen neuen Stein auf einem der drei Ringe mit Position 1-8 (Uhrzeigersinn von oben links) mit einer Farbe und ein Spielfeld"""
        self._position = position
        self._ring = ring
        self._color = color
        self._board = board
    
    def getColor(self):
        """Gibt die Farbe dieses Steins zurück"""
        return self._color

    def isInMill(self):
        """Prüft, ob dieser Stein in einer Mühle ist"""
        _board.isMill(_position)

    def move(self, newPosition):
        """Bewegt einen Stein, sofern zulässig"""
        if _board.checkMove(self._position, newPosition):
            _board.remove(_position)
            _board.setStone(self, newPosition)
            _position = newPosition


class GUI:
    def drawBoard():
        pass
    
    def printInformation():
        pass

game = Game()
    #Skizze:
    while game.getStatus == "":
            #WaitForClick
            #GetClickedStone
                #resetButton? -> break
            #game.doNextStep(clickedStone)
            #drawBoard
            #printInformation
    #printWinner
    

