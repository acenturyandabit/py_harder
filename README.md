# Python part 2: Functions, classes and more!

To make this tutorial a little more coherent, we are going to build a mini gladiator ring game in Python.

A bit of a warning: Much of the code here is template code only and won't work if you directly copy-paste it into python. If you want to just get stuff going, see the `gladiator.py` file in this same repository.
## 1 A quick revision: Variables, arrays, loops
To start off, let's write a program that makes a 20x20 grid filled with the character `'.'`. Think you're up to it?

<details>
  <summary>Show me the answer</summary>
  
    grid = []
    for i in range(20):
        row = []
        for j in range(20):
            row.append('.')
        grid.append(row)
</details>

Great! Now you have a grid of `'.'`'s. This will be the layout of our gladiator ring.

## 2 Top down design
When coding, there are two ways to make things: top down, which means doing the overall structure first; and bottom up, which means focusing on the nitty gritty first. Top down allows you to understand everything you're trying to do so you don't get lost when the project gets really complex. So let's try doing that now.

We'll need the following rough parts:

```python

ring = MAKE the ring

while player is alive:
    GET player move
    UPDATE player
    UPDATE gladiators
    MAKE new gladiators
    SHOW grid

SHOW score
```

Notice here that I have two big types of things: one is nouns like `player` or `gladiator`; the other is verbs like `GET` or `UPDATE` or `SHOW`. We make the distinction between nouns and verbs in grammar, and we also do so in coding. 

We've met nouns before: they are our variables. But what of our verbs?

## 3 Functions
Functions are verbs, inasmuch as they do things to other things. You're probably already familiar with a few functions, like `print`. Functions typically have regular brackets (the curved ones) to indicate they are fractions:

```
function()
list = []
dictionary = {}
```

Now, if we think about verbs, some verbs have objects attached to them. For example, I kick a BALL. I can also kick a number of other things; in that sense, we know that the ball is separate to the kick, and we may need to specify what we want to kick. 

In functions, the objects that we are acting on are called `arguments`. An additional quirk of functions is that they can produce a result, known as a `return value`. A typical function looks like this:

```
pot = makePot(clay);
smashPot(pot); # this one has no result, except maybe a loud crash.
```

So what kind of functions will we need for our gladiator game? What might they need as arguments? What values would they need to return?

<details>
  <summary>Show me the answer</summary>

    ring = makeRing(size)
    move = getMove()
    updatePlayer (move, ring)
    updateGladiators (ring)
    display (ring)

</details>

Functions are made up of smaller actions. For example, the set of commands we used at the start is just enough to create a ring. 

    grid = []
    for i in range(20):
        row = []
        for j in range(20):
            row.push('.')
        grid.push(row)


## 4 Classes
Now, our high level design looks pretty simple, but that's just because we haven't dived deeper yet. When we look at our ring more closely, what does it actually contain?
- The player
- The ring itself
- The gladiators

We could keep those variables separate, or we could lump them together in one single variable like we did in our high level design. Doing this makes an object (in python, this is called a `class`). Inside a class, we can keep both variables and functions. 

Let's start with a class for the player first:

```python
class player:
    x = # something
    y = # something
    grid = # something
    hp = 10
    score = 0
    def move():
        moveCompleted = False
        while moveCompleted == False:
            deltaX = 0
            deltaY = 0
            validMove = False
            while validMove == False:
                print ("Make a move by pressing W,A,S,D and then pressing enter. If you attempt to move onto an enemy, it will receive damage.")
                move = input()
                validMove = True
                if move == "W":
                    deltaY = -1
                elif move == "S":
                    deltaY = 1
                elif move == "A":
                    deltaX = -1
                elif move == "D":
                    deltaX = 1
                else:
                    print ("That's not a valid move. Try again.")
                    validMove = False
            
            # handle the move 
            for [all other gladiators]:
                if gladiator.x = x+deltaX and gladiator.y = y+deltaY:
                    gladiator.takeHit()
                    score = score + 1
                    print ("Wham! The gladiator falls to your feet.")
                    moveCompleted = True
            if not moveCompleted:
                if x+deltaX >= 0 and x+deltaX < grid.width and y+deltaY >= 0 and y.deltaY < grid.height:
                    x=x+deltaX
                    y=y+deltaY
                    print ("You moved to "+str(x)+"," +str(y))
                    moveCompleted = True
                else:
                    print ("You can't move there!")
    def takeHit():
        hp = hp - 1
        if hp==0:
            print("Oh no! You died! Your score was " + str(score) ".")
            exit()
    
```

## 5 Inheritance
Now, we can also write a class for the gladiator. But wait! It's very similar to the player. We notice that gladiators and players are both people in our ring. So let's create a base class called `person`:

```python
class person:
    x = # something
    y = # something
    hp = # something
    grid = # something
    def move():
        # Both the player and the gladiator move, but they move differently. We put this option here so that it can be filled in differently by the different subclasses that derive from person.
        pass
    def takeHit():
        # Same goes for this.
```

And then we can create two subclasses from the person class:
```python
class player(person):
    def move():
        # what we had before
        pass
    def takeHit():
        # see above
        pass 

class gladiator(person):
    def move():
        # it uses coding and algorithms to make it move (whoa buzzwords)
        pass
    def takeHit():
        # RIP
        pass
```

## 6 Instantiation
Grappling (get it?) with the idea of a gladiator, we come to realise that we'll need multiple gladiators, but we only have one class! Luckily, there is a way to get over that: instantiation. Classes are more like templates; so we need to instantiate them to get instances of the (template) class. We can do this by calling the class as a function:

```python
player = player()
gladiator1 = gladiator()
```
and so on. 

When we instantiate a class, a special function is called in the class, if we have defined it: the `__init__` function. We can declare it like this:

```python
class player(person):
    def __init__(self,grid):
        # The "self" parameter is a special parameter that refers to this specific instance of the class.
        self.x=grid.width/2
        self.y=grid.height/2
        self.hp=10
        self.grid=grid # Save the grid so we can access it later.
    # other functions go here

class gladiator(person):
    def __init__(self,grid):
        # The "self" parameter is a special parameter that refers to this specific instance of the class.
        self.x=# a random x
        self.y=# a random y
        self.hp=10
        self.grid=grid # Save the grid so we can access it later.
    # other functions go here

```

## 7 Libraries
Ok, we're almost at the end. But we still have a few difficult holes to fill. For example, how exactly are we going to get a random x value for the gladiator's spawn point?

The answer is libraries. Libraries are collections of functions that have been done for you, so you can focus on actual useful stuff. But python won't automatically fetch all the functions in the world for us! We need to tell python to specifically import a library, so that we can use it. 

```python
import random
import math

aRandomNumber = random.random()
aRandomInteger = math.floor(aRandomNumber()*100)
```

And that's all the bits and pieces you'll need! The rest of the gladiator game is left as an exercise to the reader... or you could check out the `gladiator.py` file in this repository.

