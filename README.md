# A Study Of Zombie Movements

This repo, demonstrates an approach on zombie movements in a grid, and infecting creatures they hunt.

## Approaches
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
 Another way I could think of , was to create the data structures, and anf play with lists and loops, to get the results.
 This would have been probably very fast, but not that readable. Given the challenge does not mention any performance preference. I decided to go for a third approach.
 

### C (The Chosen):

Having a minimal set of objects, and work with lists, seems to get the best of both approaches, fast enough,
and minimal memory foot print compared to approach one.
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

Prerequisite is python 3.8. Just make sure it is in path env variable.

The following command installs python3 virtual env, then runs the application within that env.
It assumes a file called boo.json has the input data in json format, and is in the same location as the start.sh file.

```
./start.sh
```

If you prefer to run the application directly here is the syntax:

```
python zombie_runner.py -f <file_name.json>
```
If the file_name.json is skipped, the app will look for 'input.json'.

 


