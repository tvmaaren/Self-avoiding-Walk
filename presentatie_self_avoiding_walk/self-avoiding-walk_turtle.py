import numpy as np
import turtle as t

screen = t.Screen()
screen.clear()
screen.screensize(200,200)
screen.setworldcoordinates(-250,-250,350,250)

alex=t.Turtle()
alex.shape("turtle")
alex.speed(1000)

n=14
visited = np.zeros((2*n+1,2*n+1,2*n+1),dtype =bool)

def set_back_color(turtle_enter):
    if((turtle_enter-alex.heading())%360==0):
        alex.pencolor(0,0,0)
    else:
        alex.pencolor(1,1,1)
    return None

def go(x,y,z,stap,visited,n,even,turtle_enter):
    if(visited[x,y,z]):
        return 0 #ga terug
    elif stap==n:
        return 1
    visited[x,y,z] = True

    count = 0
    if(even):
        alex.forward(20)
        
        count+= go(x+1,y+1,z,stap+1,visited,n, not even, alex.heading())

        alex.left(180)
        set_back_color(turtle_enter)
        alex.forward(20)
        alex.right(60)
        alex.pencolor(0,0,0)
        alex.forward(20)
        turtle_leave = alex.heading()
        alex.right(120)
       
        count+= go(x-1,y,z+1,stap+1,visited,n, not even,turtle_leave)
        
        alex.right(60)
        set_back_color(turtle_enter)
        alex.forward(20)
        alex.right(60)
        alex.pencolor(0,0,0)
        alex.forward(20)
        turtle_leave = alex.heading()
        alex.left(120)
        count+= go(x,y-1,z-1,stap+1,visited,n, not even,turtle_leave)
        alex.left(60)
        set_back_color(turtle_enter)
        alex.forward(20)
        alex.right(60)
        alex.pencolor(0,0,0)

    else:
        alex.right(180)
        alex.forward(20)
        turtle_leave = alex.heading()
        alex.right(180)

        count+= go(x-1,y-1,z,stap+1,visited,n, not even,turtle_leave)

        set_back_color(turtle_enter)
        alex.forward(20)
        alex.right(60)
        alex.pencolor(0,0,0)
        alex.forward(20)
        turtle_leave = alex.heading()
        alex.left(60)

        count+= go(x+1,y,z-1,stap+1,visited,n, not even,turtle_leave)

        alex.left(120)
        set_back_color(turtle_enter)
        alex.forward(20)
        alex.pencolor(0,0,0)
        alex.right(60)
        alex.forward(20)
        turtle_leave = alex.heading()
        alex.right(60)
        
        count+= go(x,y+1,z+1,stap+1,visited,n, not even,turtle_leave)

        alex.right(120)
        set_back_color(turtle_enter)
        alex.forward(20)
        alex.pencolor(0,0,0)
        alex.left(120)
    visited[x,y,z] = False
    return count


print(go(0,0,0,0,visited,n,True,0))

