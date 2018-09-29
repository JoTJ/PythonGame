class Position:
    def __init__(self,ring,number):
        self._ring = ring
        self._number = number
        
    def getNumber(self):
        return self._number
    
    def getRing(self):
        return self._ring