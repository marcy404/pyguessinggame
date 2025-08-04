class HostClass:
    def __init__(self):
        self.generateNumber()
    
    # Number Generator
    def generateNumber(self):
        from random import randint
        self.number = randint(1, 100)
        return self.number

    # Check answer --> basically PHP's cute spaceship operator
    def checkAnswer(self, answer):
        if answer > self.number:
            return 1
        
        if answer < self.number:
            return -1
        
        return 0

if __name__ == '__main__':
    testhost = Host()

    print(testhost.number, testhost.generateNumber(), testhost.generateNumber(), testhost.generateNumber())
    print(testhost.checkAnswer(5), testhost.checkAnswer(110), testhost.checkAnswer(testhost.generateNumber()))