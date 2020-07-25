# A Study Of Zombie Movements

This repo, demonstrates an solution on zombie movement effects in a grid, and infecting other living creatures( :sheep: )they bite.

### A bit of a background

In a  NxN matrix world. A zombie wakes up in a predefined location(x,y). Point 0,0 being top left.

This zomibe follows a predefined set of movements: "U" up, "D" down, "L" left, "R" right, to travel in the matrix world square of square.
If it sees a creature in that squre it will infect them, and move on. In turn each turned creature, which is a zombie now, starts the same series of moves,
to infect others.

Note Zombies can travel from one edge to another, for example "R" on far right edge, will put them the x:0 of the same row.
The World will come to and end when there is no more newly infected zombies.
Right well designed, well tested, readable, performant code.


## Considered Approaches

### A

Having a DDD and OOP background, I thought of how to model this domain, as follows:
 - Organism as the base class. 
 - Zombie(bites) and Creature(can be infected, and transform into Zombie),
 - Square can contain one or more Organisms.
 - Grid contains Squares, and keeps track of new transforms.
 - ZombieLand where it contains grid.
 And some events to bubble up and keep containers aware of what is happening.
 
 However as the grid size grows bigger this approach gets slower and slower.

### B

Another way I could think of, was to create the data structures, and play with lists and loops and mutiple functions to get the results.
While it works, it is not that readable. so decided to try a third  approach.
 

### C (The Chosen):

This is based on having a minimal set of models, and working with lists, seems to get the best of both approaches, fast enough,
and minimal memory foot-print. 
Within this approach there is a Zombie model, that can move and inspect if it has the same location as creatures.

## Application Input
The input to the application is a json file in the following format:
```json
{
  "size": 4,
  "zombie_start": [2,1],
  "creatures": [[0,1],[1,2],[3,1]],
  "moves": "DLUURR"
}

```
size: defines the the grid size
zombie_start: the location where the zombie wakes up.
creatures: a list of creature locations within the grid.
moves: the path a zombie will follow.

## Install and run:

The only Prerequisite is python 3.8. Just make sure it is in path env variable.

The following command installs python3 virtual env, then runs the application within that env.
It assumes a file called boo.json has the input data in json format, and is in the same location as the start.sh file.
Thia has been developed on OSX.

```
./start.sh
```

If you prefer to run the application directly here is the syntax:

```
(env) ~/zz-dev > python zombie_runner.py -f <file_name.json>
```
If the file_name.json is skipped, the app will look for 'input.json'.

 ## Notes
 * Alternative requirements could be considered : a giant zombie, which occupies more than just one square, and infects other creatures, keeping it's edge traveling properties.
 * Another alternative would be to move the zombie one square at a time.
 


