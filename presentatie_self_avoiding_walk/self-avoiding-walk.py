import numpy as np

n=14
visited = np.zeros((2*n+1,2*n+1,2*n+1),dtype =bool)

def go(x,y,z,stap,visited,n,even):
    if(visited[x,y,z]):
        return 0 #ga terug
    elif stap==n:
        return 1
    visited[x,y,z] = True
    count = 0
    if(even):
        count+= go(x+1,y+1,z,stap+1,visited,n, not even)
        count+= go(x-1,y,z+1,stap+1,visited,n, not even)
        count+= go(x,y-1,z-1,stap+1,visited,n, not even)
    else:
        count+= go(x-1,y-1,z,stap+1,visited,n, not even)
        count+= go(x+1,y,z-1,stap+1,visited,n, not even)
        count+= go(x,y+1,z+1,stap+1,visited,n, not even)
    visited[x,y,z] = False
    return count
print(go(0,0,0,0,visited,n,True))
