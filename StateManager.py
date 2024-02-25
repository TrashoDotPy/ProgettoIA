

class StateManager:
    def __init__(self, currentState):
        self.__currentState = currentState

    def getState(self):
        return self.__currentState
    
    def setState(self, state):
        self.__currentState = state