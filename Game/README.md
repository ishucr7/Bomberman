Bomberman game can be run by using any python3 or python
1) python3 gameplay.py
2) python gameplay.py

Basic Controls :--

  Function     key
1)Move left 	a 
2)Move right	d 
3)Move up   	w 
4)Move down 	s 
5)Drop bomb 	b 

It is a simple game where bomberman can be run by the user whereas enemies move randomly on the board. Both of them cannot walk through walls or bricks. Bomberman can drop a bomb which destroys bricks and enemies around it's four direction except the place of bomb itself after 3 seconds .

'/' represents the bricks
'B' represents Bomberman 
'E' represents Enemy
'e' represents the fire of explosion
'X' The walls 

It is implemented using OOP's Principles

Modularity:-
Code has been divided into several modules , which altogether run as if it were a single file code

brick.py     :- It conatains the code for Brick class ,it initialises the bricks on board 
board.py     :- It contains the code for Board class ; it initiliases the arr[x][y]=='W' with where to have walls
bomberman.py :- It contains the code for Bomberman class ; it creates functionality for bomberman's movement
bomb.py      :- It contains the code for Bomb class ; it controls the exexecution of bomb
person.py    :- It contains the code for Person class ; it is parent class for both enemy and bomberman
enemy.py     :- It contains the code for Enemy class ; it contains the functionality which controls the movement of enemy
walls.py     :- It contains the code for Walls class ; it contains the printing part of the game
getchunix.py :- It contains the code for getting char from keyboard without interupt

Inheritance:-
The Enemy and Bomberman classes both inherit Person class
The run class inherits Bomb and Walls class

Polymorphism:-
We have an abstract class Person which contains mak(),moveDown(),moveLeft(),moveRight(),moveUp()

All the functions listed above  except mak() work according to the object which called it , i.e the functions work differently if the object of Enemy calls  or  when the object of Bomberman calls 

Encapsultion:-
The enemymove method is private to its class
__enemymove()
	and hence is accessed by e._Enemy__enemymove()

Bonus Part:--
1) The bomb display the number of seconds left for explosion 
  instead of ‘O’. For example if one second is left then  
  1111   =>    0000  => explosion 
  1111         0000 
2) I have given red color to 'E'(enemy) , 'green' to 'B' bomberman , 'blue' to bricks
