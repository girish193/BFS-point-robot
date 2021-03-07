#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
import time

def workspace_check(x_new,y_new): 
    
    """
        
        In this functiom the given value is checked to see if it lies in the workspace
        
        Parameters
        ----------
        x_new: X coordinate of given input 
        y_new: Y coordinate of given input 
        
        Returns
        -------
        True  : If the input lies inside workspace
        False : If the input lies outside workspace
        
    """
    
    if(x_new >= 0) and (y_new >= 0) and (x_new <= 400) and (y_new <= 300):
        return True
    else: 
        return False
    
def obstacle_space(x_new,y_new):
        
    """
        
        In this functiom the given value is checked to see if it lies in the obstacle space
        
        Parameters
        ----------
        x_new: X coordinate of given input 
        y_new: Y coordinate of given input 
        
        Returns
        -------
        True  : If the input lies outside obstacle space
        False : If the input lies inside obstacle space
        
    """
    
    flag1, flag2, flag3, flag4, flag5 = (True, True, True, True, True)
    
    # For Circle
    if ((x_new - 90)**2 + (y_new - 70)**2 - 35**2 <= 0):
        flag1 = False
        
    # For Ellipse
    if (((x_new - 246)/60)**2 + ((y_new - 145)/30)**2 -1 <= 0):
        flag2 = False
        
    # For C-shape
    if ((x_new >= 200) and (x_new <= 230) and (y_new >= 230) and (y_new <= 280)):
        if ((x_new > 210) and (y_new > 240) and (y_new < 270)):
            flag3 = True
        else:
            flag3 = False
    
    # For rotated rectangle
    x1, y1 = (48, 108)
    x2, y2 = (x1 - 20*np.cos(11*np.pi/36), y1 + 20*np.sin(11*np.pi/36))
    x4, y4 = (x1 + 150*np.cos(7*np.pi/36), y1 + 150*np.sin(7*np.pi/36))
    x3, y3 = (x4 - 20*np.cos(11*np.pi/36), y4 + 20*np.sin(11*np.pi/36))
    
    l_12 = lambda x, y : (y2 - y1)/(x2 - x1)*(x - x1) - (y - y1)  
    l_23 = lambda x, y : (y3 - y2)/(x3 - x2)*(x - x2) - (y - y2)
    l_34 = lambda x, y : (y4 - y3)/(x4 - x3)*(x - x3) - (y - y3)
    l_41 = lambda x, y : (y1 - y4)/(x1 - x4)*(x - x4) - (y - y4)
    
    if ((l_12(0, 0)*l_12(x_new, y_new) <= 0) and (l_23(0, 0)*l_23(x_new, y_new) >= 0) and         (l_34(0, 0)*l_34(x_new, y_new) >= 0) and (l_41(0, 0)*l_41(x_new, y_new) <= 0)):
        
        flag4 = False
        
    # For 6-sided irregular polygon
    x5, y5 = (328, 63)
    x6, y6 = (x5 - 60*np.cos(np.pi/4), y5 + 60*np.sin(np.pi/4))
    x7, y7 = (x6 + 56*np.cos(np.pi/4), y6 + 56*np.sin(np.pi/4))
    x8, y8 = (354, 138)
    x10, y10 = (x5 + 75*np.cos(np.pi/4), y5 + 75*np.sin(np.pi/4))
    x9, y9 = (x10, y10 + 55)
    
    l_56 = lambda x, y : (y6 - y5)/(x6 - x5)*(x - x5) - (y - y5)  
    l_67 = lambda x, y : (y7 - y6)/(x7 - x6)*(x - x6) - (y - y6)
    l_78 = lambda x, y : (y8 - y7)/(x8 - x7)*(x - x7) - (y - y7)
    l_89 = lambda x, y : (y9 - y8)/(x9 - x8)*(x - x8) - (y - y8)  
    l_105 = lambda x, y : (y5 - y10)/(x5 - x10)*(x - x10) - (y - y10)
    
    if ((l_56(0, 0)*l_56(x_new, y_new) <= 0) and (l_67(0, 0)*l_67(x_new, y_new) <= 0) and         x_new <= x10 and (l_105(0, 0)*l_105(x_new, y_new) >= 0)):
        
        if ((l_78(0, 0)*l_78(x_new, y_new) < 0) and (l_89(0, 0)*l_89(x_new, y_new) > 0)):
            flag5 = True
        
        else:
            flag5 = False
            
    flag = flag1 and flag2 and flag3 and flag4 and flag5
    
    return flag   
    
def tree_generation(node_index,track): 
        
        """
        
        In this function, new child nodes are generated for a given parent node and later added to the tree.
        
        Note: Here, duplicacy of node generated is checked and only then added !
                
        Parameters
        ----------
        node_index   : int type and accounts for current node number.
        track        : list type and contains path of each node generated.
        
        
        Returns
        -------
        None
        
        """
        
        x_pt = list(node.values())[node_index][0]
        y_pt = list(node.values())[node_index][1]
              
        x1, y1 = (x_pt, y_pt+1)   # top    
        x2, y2 = (x_pt, y_pt-1)   # bottom
        x3, y3 = (x_pt+1, y_pt)   # right
        x4, y4 = (x_pt-1, y_pt)   # left
        x5, y5 = (x_pt-1, y_pt+1) # top_left
        x6, y6 = (x_pt+1, y_pt+1) # top_right
        x7, y7 = (x_pt-1, y_pt-1) # bottom_left
        x8, y8 = (x_pt+1, y_pt-1) # bottom_right

        search_value_old=[(x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6), (x7,y7), (x8,y8)]
        search_value = []
        is_valid = True
        
        for i,j in search_value_old: 
            is_valid = workspace_check(i,j) and obstacle_space(i,j)
            if (is_valid == True): 
                search_value.append((i,j))
            
        child_key= list(node.keys())[-1]+1
        parent_track = track[node_index]

        for x,y in search_value: 
            point_database = list(node.values())
            if(all((x,y) != (i,j) for i,j in point_database)):
                    node.update({child_key:(x,y)})
                    child_track = ''
                    child_track = parent_track + ' -> ' + str(child_key) 
                    track.append(child_track)
                    child_key +=1
        
print('Enter start location, X_start (x coordinate): ')
s1 = int(input())
print('\nEnter start location, Y_start (y coordinate): ')
s2 = int(input())

if (workspace_check(s1, s2) == False):
    print('\n\nStart Point not in Workspace\n\n')
    sys.exit('Exiting ....')
    
if (obstacle_space(s1, s2) == False):
    print('\n\nStart Point is in Obstacle Space\n\n')
    sys.exit('Exiting ....')
    
print('\nEnter end location, X_end (x coordinate): ')
e1 = int(input())
print('\nEnter end location, Y_end (y coordinate): ')
e2 = int(input())

if (workspace_check(e1, e2) == False):
    print('\n\nEnd Point not in Workspace\n\n')
    sys.exit('Exiting ....')
    
if (obstacle_space(e1, e2) == False):
    print('\n\nEnd Point is in Obstacle Space\n\n')
    sys.exit('Exiting ....')
    
start = (s1, s2)
end = (e1, e2)

node_index = 0 
node = {node_index: start}
track= []
track.append('0')

start_time = time.time()

### BFS Tree Generation
print('\n\nSolving.........')
while(node[node_index] != end):
    tree_generation(node_index,track)
    node_index += 1 

end_time = time.time()
total_time = (end_time - start_time)/60
print('\n\nRequired Trajectory Found !!!')
print('\n\n Time taken: {0:1.3f} min'.format(total_time))

# Node Exploration
x_explore = []
y_explore = []
pts = list(node.values())
    
fname1 = './Node_Exploration.txt'
myfile1 = open(fname1,"w")
myfile1.write('X \t Y\n')

for x, y in pts:
    x_explore.append(x)
    y_explore.append(y)
    myfile1.write('{0} \t {1}\n'.format(x, y))
    
myfile1.close()

# Optimal Path
### Writing the solution trajectory to an Output File
x_solution = []
y_solution = []
sol = track[node_index]
sol = sol.split(' -> ')
    
fname2 = './Solution_Path.txt'
myfile2 = open(fname2,"w")
myfile2.write('Time taken to solve:\t{0:1.3f} minutes\n'.format(total_time))
myfile2.write('Required Solution trajectory\n')
myfile2.write('\nX \t Y\n')

for i in sol:
    index = int(i)
    x = node[index][0]
    y = node[index][1]
    x_solution.append(x)
    y_solution.append(y)
    myfile2.write('{0} \t {1}\n'.format(x, y))
    
myfile2.close()

### Visualization starts from here

plt.style.use('seaborn-pastel')

fig = plt.figure()

ax = plt.axes(xlim = (0, 400), ylim = (0, 300)) # Defining Workspace limits

# For Plotting Circle
x_circle = np.linspace(55, 125, 2000)
y_circle1 = 70 + (35**2 - (x_circle - 90)**2)**0.5
y_circle2 = 70 - (35**2 - (x_circle - 90)**2)**0.5
ax.plot(x_circle, y_circle1, 'b.', markersize = 0.15)
ax.plot(x_circle, y_circle2, 'b.', markersize = 0.15)

# For Plotting Ellipse
x_ellipse = np.linspace(186, 306, 2000)
y_ellipse1 = 145 + 30*(1 - ((x_ellipse - 246)/60)**2)**0.5
y_ellipse2 = 145 - 30*(1 - ((x_ellipse - 246)/60)**2)**0.5
ax.plot(x_ellipse, y_ellipse1, 'b.', markersize = 0.15)
ax.plot(x_ellipse, y_ellipse2, 'b.', markersize = 0.15)

# For C-Shape (assuming uniform thickness)
ax.axhline(y = 280, xmin = 0.50, xmax = 0.575, color = 'blue')
ax.axvline(x = 200, ymin = 23/30, ymax = 14/15, color = 'blue')
ax.axhline(y = 230, xmin = 0.50, xmax = 0.575, color = 'blue')
ax.axvline(x = 230, ymin = 23/30, ymax = 0.80, color = 'blue')
ax.axhline(y = 240, xmin = 0.525, xmax = 0.575, color = 'blue')
ax.axvline(x = 210, ymin = 0.8, ymax = 0.9, color = 'blue')
ax.axhline(y = 270, xmin = 0.525, xmax = 0.575, color = 'blue')
ax.axvline(x = 230, ymin = 0.9, ymax = 14/15, color = 'blue')

# For rotated rectangle 
x1, y1 = (48, 108)
x2, y2 = (x1 - 20*np.cos(11*np.pi/36), y1 + 20*np.sin(11*np.pi/36))
x4, y4 = (x1 + 150*np.cos(7*np.pi/36), y1 + 150*np.sin(7*np.pi/36))
x3, y3 = (x4 - 20*np.cos(11*np.pi/36), y4 + 20*np.sin(11*np.pi/36))
ax.plot([x1, x2], [y1, y2], 'b-')
ax.plot([x2, x3], [y2, y3], 'b-')
ax.plot([x3, x4], [y3, y4], 'b-')
ax.plot([x1, x4], [y1, y4], 'b-')

# For 6-sided irregular polygon
x5, y5 = (328, 63)
x6, y6 = (x5 - 60*np.cos(np.pi/4), y5 + 60*np.sin(np.pi/4))
x7, y7 = (x6 + 56*np.cos(np.pi/4), y6 + 56*np.sin(np.pi/4))
x8, y8 = (354, 138)
x10, y10 = (x5 + 75*np.cos(np.pi/4), y5 + 75*np.sin(np.pi/4))
x9, y9 = (x10, y10 + 55)
ax.plot([x5, x6], [y5, y6], 'b-')
ax.plot([x6, x7], [y6, y7], 'b-')
ax.plot([x7, x8], [y7, y8], 'b-')
ax.plot([x8, x9], [y8, y9], 'b-')
ax.plot([x9, x10], [y9, y10], 'b-')
ax.plot([x5, x10], [y5, y10], 'b-')

new_node, = ax.plot([], [], 'y.', alpha = 0.1) 

solution_trajectory, = ax.plot([], [], 'r*') 

def animate(frame_number):
        
    """
        
        In this function, animation is carried out. 
                
        Parameters
        ----------
        frame_number : int type, here frame number serves as an index for the images  
        
        
        Returns
        -------
        None
        
    """
    
    frame_diff = total_frames - frame_number
          
    if(frame_diff > solution_traj_frames + 1): # will run for frame_number = [0, 148]
        first = 0
        last = step1*(frame_number+1)
        x = x_explore[first:last]
        y = y_explore[first:last]
        new_node.set_data(x, y)
        new_node.set_markersize(1)
        return new_node,

    elif(frame_diff == solution_traj_frames + 1): # will run for frame_number = 149 only
        x = x_explore
        y = y_explore
        new_node.set_data(x, y)
        new_node.set_markersize(1)
        return new_node,
    
    elif(frame_diff < solution_traj_frames + 1 and frame_diff > 1):  # will run for frame_number = [150, 198]
        first = 0
        last = step2*(frame_number - (node_explore_frames - 1))
        x = x_solution[first:last]
        y = y_solution[first:last]  
        solution_trajectory.set_data(x, y)
        solution_trajectory.set_markersize(1.5)
        return solution_trajectory,
        
    else: # will run for frame_number = 199 only
        x = x_solution
        y = y_solution   
        solution_trajectory.set_data(x, y)
        solution_trajectory.set_markersize(1.5)
        return solution_trajectory,

node_explore_frames = 150
solution_traj_frames = 50  
total_frames = node_explore_frames + solution_traj_frames

step1 = int(len(x_explore)/node_explore_frames)
step2 = int(len(x_solution)/solution_traj_frames)

animation = FuncAnimation(fig, animate, frames = total_frames, interval = 20, blit = True, repeat = False)

animation.save('./Point_Robot_Visualization.mp4', dpi = 600)

plt.title('Point Robot Visualization')

plt.show()

