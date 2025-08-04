class PlayerClass:
    def __init__(self, name, lifes=5):
        self.name = name
        self.max_lifes = lifes
        self.current_lifes = lifes
        self.score = 0
    
    # Increase or decrease player score methods
    def changeScore(self, factor):
        self.score += factor
        return self.score
    
    # Reset score
    def resetScore(self):
        self.score = 0
        return self.score

    # Decrease life
    def decreaseLife(self, factor=-1):
        factor = abs(factor) * -1
        self.current_lifes += factor
        return self.current_lifes

    # Reset lifes
    def resetLifes(self):
        self.current_lifes = self.max_lifes
        return self.current_lifes

# Object test
if __name__ == '__main__':
    playtest_one = Player('playtest1')
    playtest_two = Player('playtest2', lifes=10)

    print(playtest_one.name, playtest_one.score, playtest_one.changeScore(1), playtest_one.changeScore(-3), playtest_one.resetScore())
    print(playtest_two.name, playtest_two.decreaseLife(), playtest_two.decreaseLife(-5), playtest_two.decreaseLife(600), playtest_two.resetLifes())
