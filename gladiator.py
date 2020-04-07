import math
import random

class Person:
    x=0
    y=0
    def move(self):
        # Both the player and the gladiator move, but they move differently. We put this option here so that it can be filled in differently by the different subclasses that derive from person.
        pass
    def takeHit(self):
        # Same goes for this.
        pass


class Player (Person):
    def __init__(self, grid):
        self.x = math.floor(grid.width/2)
        self.y = math.floor(grid.height/2)
        self.grid = grid
        self.hp = 10
        self.score = 0
        self.type = "Player"

    def move(self):
        moveCompleted = False
        while moveCompleted == False:
            deltaX = 0
            deltaY = 0
            validMove = False
            while validMove == False:
                print ("Make a move by pressing one of w,a,s,d and then pressing enter. If you attempt to move onto an enemy, it will receive damage.")
                move = input()
                validMove = True
                if move == "w":
                    deltaY = -1
                elif move == "s":
                    deltaY = 1
                elif move == "a":
                    deltaX = -1
                elif move == "d":
                    deltaX = 1
                else:
                    print ("That's not a valid move. Try again.")
                    validMove = False
            
            # handle the move 
            if self.x+deltaX >= 0 and self.x+deltaX < self.grid.width and self.y+deltaY >= 0 and self.y+deltaY < self.grid.height:
                for entity in self.grid.entities:
                    if entity.x == self.x+deltaX and entity.y == self.y+deltaY:
                        entity.takeHit()
                        self.score = self.score + 1
                        print ("Wham! The gladiator falls to your feet.")
                        moveCompleted = True
                if not moveCompleted:
                    self.x=self.x+deltaX
                    self.y=self.y+deltaY
                    print ("You moved to "+str(self.x)+"," +str(self.y))
                    moveCompleted = True
            else:
                print ("You can't move there!")

    def takeHit(self):
        self.hp = self.hp - 1
        if self.hp==0:
            print("Oh no! You died! Your score was " + str(self.score) + ".")
            exit()
        else:
            print("A gladiator hit you! You have {} health remaining...".format(self.hp))

class Gladiator(Person):
    def __init__(self, grid):
        spawnOK = False
        # a potential bug here if there are no spaces for gladiators to spawn. What will happen then? How can we fix it?
        while spawnOK == False:
            spawnOK = True
            self.x = math.floor(random.random()*grid.width)
            self.y = math.floor(random.random()*grid.height)
            for entity in grid.entities:
                if entity.x == self.x and entity.y == self.y:
                    spawnOK = False 
        print ("A gladiator appears on {}, {}!".format(self.x, self.y)) # another way of more quickly putting variables into strings.
        self.type="Gladiator"
        self.grid = grid
        self.hp = 10
        self.score = 0
    
    def move(self):
        # make a random move north, south, east or west, hitting any entity in our way
        moveCompleted = False
        moveTries = 5 # 5 maximum tries, in case there is no room for the gladiator to go
        while moveCompleted == False and moveTries > 0:
            moveTries = moveTries - 1
            moveDirection = math.floor(random.random()*4)
            deltaXs=[0,-1,0,1]
            deltaYs=[-1,0,1,0]
            deltaX = deltaXs[moveDirection]
            deltaY = deltaYs[moveDirection]
            
            # handle the move
            if self.x+deltaX >= 0 and self.x+deltaX < self.grid.width and self.y+deltaY >= 0 and self.y+deltaY < self.grid.height:
                squareClear = True 
                for entity in self.grid.entities:
                    if entity.x == self.x+deltaX and entity.y == self.y+deltaY:
                        if entity.type=="Player":
                            entity.takeHit()
                            moveCompleted = True
                        else:
                            squareClear = False
                if not moveCompleted and squareClear:
                    self.x=self.x+deltaX
                    self.y=self.y+deltaY
                    moveCompleted = True

    def takeHit(self):
        # RIP
        self.grid.removeEntity(self)


class Grid():
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.entities=[]
        self.entities.append(Player(self))
        self.turnCount = 0
    
    def draw(self):
        grid = []
        # add 2 so we can put a wall around our ring.
        for i in range(self.height+2):
            row = []
            for j in range(self.width+2):
                charToPush='.'
                if i == 0 or j == 0 or i == self.height+1 or j == self.height+1:
                    charToPush = '#'
                row.append(charToPush)
            grid.append(row)
        
        for entity in self.entities:
            grid[entity.y+1][entity.x+1]=entity.type[0]

        # actually draw it
        for i in range(self.height+2):
            print ("".join(grid[i]))
            # join each cell in each row, separated by nothing (""), and print it.

    def removeEntity(self,theEntity):
        # remove a gladiator
        self.entities.remove(theEntity)

    def run(self):
        while (1):
            self.draw()
            self.turnCount= self.turnCount+1
            for spawnTries in range(1,math.ceil(self.turnCount/5)):
                if (random.random()>0.5):
                    self.entities.append(Gladiator(self))
            for entity in self.entities:
                entity.move()

grid = Grid(10,10)
grid.run()