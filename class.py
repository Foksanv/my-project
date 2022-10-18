import random


class Player:
    def __init__(self, name, team, score):
        self.name = name
        self.team = team
        self.score = score

    def play(self):
        num = random.randint(1, 11)
        self.score += num
        
    def scream(self):
        print(f'i am {self.name} from {self.team})
