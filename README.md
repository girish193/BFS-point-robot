## Run Code

Open the file "BFS_point.py" in an IDE (Spyder, VS Code etc) of your choice. Enter valid input such that point does not lie in obstacle space or outside of workspace. For invalid inputs it exits with invalid input prompt. The video visualization can be found in Point_Robot_Visualization.mp4 .   

## Description
This code aims at implementing BFS for a point robot to solve a given map. All the nodes corresponding with different points (x,y) on the map are explored until a goal is found.

## Dependencies
* python -version 3
* numpy
* sys
* matplotlib
* time

## Function Descriptions 

## 1) Workspace_check
 
In this functiom the given value is checked to see if it lies in the workspace.  

## 2) Obstacle_Space 

In this function thee given value is checked against obstacles and true is returned if it lies outside obstacle space. Obstacles which are given are C shaped polygon, rounded rectangle, ellipse, circle and polygon.  

## 3) Tree_generation

In this function the initial input values are taken and action sets is called and top, topleft, top right, bottom left, bottom right,bottom, left ,right are performed to generate next set of moves. These values are stored in a list and if  thse values are not valid, they are removed. For each value stored in the search_value list, it is compared with the existing elements in the point database. If the point already exists, the value is not added, otherwise it is added in breadth first manner (BFS) which in turn is accomplished by using the key of the last element incremented by 1 as the new child key. This way the node numbers are added in BFS manner with their values. 

##  NOTE : 

Outside of the above function definitions, the initial and goal states are assigned to the node dictionary. Following this tree generation function is called and node dictionary is updated. From the updated node dictionary solution track is obtained and plotted. It takes around 100 minutes (Intel(R) Core(TM) i5-9300HF CPU @ 2.4GHz, RAM = 8GB) to find optimal path using BFS for start point (0,0) and end point (400,300).

Using Matplotlib, animation is generated. Firstly, animation for node exploration is generated and followed by optimal path trajectory's animation. 150 frames for node exploration and 50 frames for solution trajectory are used as default values for the animation. The resulting animation is also stored in Point_Robot_Visualization.mp4 file. 



