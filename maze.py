import random
from collections import deque
#from termcolor import colored



def bfs_maze(maze,start):
    print_maze(maze)
    print('')
    curr = start
    q = deque()
    q.append(curr)
    visited = [[ False for i in range(len(maze[0]))] for i in range(len(maze))]
    visited[curr[0]][curr[1]] = True
    path = {}
    path[start[0],start[1]] = 'n'
    while len(q) != 0:
        curr = q.popleft()
        visited[curr[0]][curr[1]] = True
        x = curr[0]
        y = curr[1]

        if maze[x][y] == 'G':
            print('Path Found')
            shortest_path(maze,(x,y),path,(start[0],start[1]))
            break
        #maze,x,y,visited,path,curr,q):
        visit_or_append(maze,x,y+1,visited,path,curr,q)
        visit_or_append(maze,x+1,y,visited,path,curr,q)
        visit_or_append(maze,x,y-1,visited,path,curr,q)
        visit_or_append(maze,x-1,y,visited,path,curr,q)
        
    
    print_maze(maze)
    return(maze)
   
def visit_or_append(maze,x,y,visited,path,curr,q):
    
    if x < 0 or y < 0:
        return
    if x >= len(maze) or y >= len(maze[0]):
        return
    if maze[x][y] == 'W':
        visited[x][y] == True

    elif visited[x][y] != True:
        visited[x][y] = True
        path[x,y] = curr
        q.append([x,y])
       

###########Adds the shortest path from start to goal to graph
def shortest_path(maze,end_index,path,start_index):
    step = path[end_index]
    while(step != [start_index[0],start_index[1]]):
        maze[step[0]][step[1]] = 'o'
        step = path[step[0],step[1]]
        
###########Prints current maze
def print_maze(maze):
    if (False):
        wall_color = 'green'
        for i in range(len(maze[0])+2):
            print(colored('W ',color= wall_color,),end='')
        print('')
        for i in maze:
            print(colored('W ',color= wall_color,),end='')
            for j in i:
                if j == 'W':
                    print(colored('W ',color= wall_color,),end='')
                elif j == 'o':
                    print(colored('o ',color= 'blue',),end='')
                elif j == 'S':
                    print(colored('S ',color= 'yellow',),end='')
                elif j == 'G':
                    print(colored('G ',color= 'yellow',),end='')
                else:
                    print(j,end=' ')
            print(colored('W ',color= wall_color,),end='')
            print('')
               
        for i in range(len(maze[0])+2):
            print(colored('W ',color= wall_color),end='')
    if(True):
        for i in range(len(maze[0])+2):
            print('W ',end='')
        print('')
        for i in maze:
            print('W ',end='')
            for j in i:
                if j == 'W':
                    print('W ',end='')
                elif j == 'o':
                    print('o ',end='')
                elif j == 'S':
                    print('S ',end='')
                elif j == 'G':
                    print('G ',end='')
                else:
                    print(j,end=' ')
            print('W ',end='')
            print('')
                
        for i in range(len(maze[0])+2):
            print('W ',end='')
        


       
########## Generate random maze
def generate_maze(r,c):
    maze = [[0 for i in range(c)] for j in range(r)]
    for i in maze:
        for j in range(len(i)):
            x =  random.randint(1,10)
            if x == 1 or x == 2 or x == 3:
                i[j] = 'W'
            else:
                i[j] = '.'
    while(True):
        
        startx = random.randint(0,r-1)
        starty = random.randint(0,c-1)
        if maze[startx][starty]!= 'W':
            maze[startx][starty] = 'S'
            break

    while(True):
        endx = random.randint(0,r-1)
        endy = random.randint(0,c-1)

        if (endx == startx and endy == starty) and maze[endx][endy]!= 'W':
            continue
        maze[endx][endy] = 'G'
        break
    return (maze,[startx,starty])


while(True):
    try:
        x = int(input("Enter the number of rows in the maze: "))
        y = int(input("Enter the number of columns in the maze: "))
        break
    except ValueError:
        print('Only enter integers for the columns/rows')
        continue
        

maze , start = generate_maze(x,y)
maze = bfs_maze(maze,start)
 