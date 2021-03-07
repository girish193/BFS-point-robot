## Run Code

Open the file "4x4 puzzle with tracking.py" in an IDE (Spyder, VS Code etc) of your choice. All the test cases are given as input and solutions are found in the same python file. Further "nodePath_{*}.txt" files are generated which contains the solution strategy for a given initial and goal states.Also it contains information of other nodes generated (only string representation is mentioned in column major order).

## Description
This code aims at solving 15 puzzle problem with BFS. All the nodes corresponding with different positions of the blank tile are explored until a goal is found.

## Dependencies
* python -version 3
* Numpy
* copy
* time

## Function Descriptions 

## 1) Workspace_check
 
In this functiom the given value is checked to see if it lies in the workspace.  

## 2) Obstacle_Space 

In this function thee given value is checked against obstacles and true is returned if it lies outside obstacle space. Obstacles which are given are C shaped polygon, rounded rectangle, ellipse, circle and polygon.  

## 3) Tree_generation

In this function the initial input values are taken and action sets is called and top, topleft, top right, bottom left, bottom right,bottom, left ,right are performed to generate next set of moves. These values are stored in a list and if  thse values are not valid, they are removed. For each value stored in the search_value list, it is compared with the existing elements in the point database. If the point already exists, the value is not added, otherwise it is added in breadth first manner (BFS) which in turn is accomplished by using the key of the last element incremented by 1 as the new child key. This way the node numbers are added in BFS manner with their values. 

## 5) main_function 

In this function, the initial and goal states are assigned to the node dictionary. 


