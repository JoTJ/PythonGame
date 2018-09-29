import Board, Player, Position
class Stone:
    """Ein Spielstein"""

    def __init__(self, position, color, board):
        """Erstellt einen neuen Stein auf einem der drei Ringe mit Position 1-8 (Uhrzeigersinn von oben links) mit einer Farbe und ein Spielfeld"""
        self._position = position
        self._color = color
        self._board = board
    
    def getColor(self): 
        """Gibt die Farbe dieses Steins zurück"""
        return self._color

    def isInMill(self):
        """Prüft, ob dieser Stein in einer Mühle ist"""
        self._board.isMill(self._position)
        
    def getPosition(self):
        return self._position
#
#    def move(self, newPosition, phase):
#        """Bewegt einen Stein, sofern zulässig"""
#        if self._board.checkMove(self._position, newPosition, phase):
#            self._board.remove(self._position)
#            self._board.setStone(self, newPosition)
#            self._position = newPosition
#        else:
#            #TODO
