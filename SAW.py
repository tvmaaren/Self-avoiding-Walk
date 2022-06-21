import numpy as np
import matplotlib.pyplot as plt

class SAW:
    def __init__(self, N,template="2dsquare", path_coords=[],direction_vectors=None):
        if not ((template==None) ^ (direction_vectors==None)):
            raise Exception("One and only one of template and direction_vectors must be equal to \"None\"")
        if(template=="2dsquare"):
            direction_vectors = [(0,1),(1,0),(0,-1),(-1,0)]
        elif(template=="3dcubic"):
            direction_vectors = [(0,0,1),(0,1,0),(0,0,-1),(0,-1,0),(1,0,0),(-1,0,0)]
        elif(template=="4dcubic"):
            direction_vectors =\
            [(0,0,0,1),(0,0,1,0),(0,0,0,-1),(0,0,-1,0),(0,1,0,0),(0,-1,0,0),(1,0,0,0)\
                    ,(-1,0,0,0)]
        elif(template=="2dhoneycomb"):
            raise NotImplementedError("Template 2dhoneycomb is not implemented yet")
            
            #direction_vectors = [(-1,0,1),(0,1,1),(1,1,0),(1,0,-1),(0,-1,-1),(-1,-1,0)]
        elif(template=="2dtriangle"):
            direction_vectors = [(-1,0,1),(0,1,1),(1,1,0),(1,0,-1),(0,-1,-1),(-1,-1,0)]

        self.direction_vectors = direction_vectors
        self.dimensions = len(direction_vectors[0])
        if(len(path_coords)==0 or path_coords[0]!=(0,)*self.dimensions):
            path_coords.insert(0,(0,)*self.dimensions)
        self.path_coords = path_coords
        self.N = N
        self.template = template
        
        self.visited = np.zeros((2*N+1,)*self.dimensions,dtype =bool)
        self.max_dimensions = np.full((self.dimensions),N)
        self.min_dimensions = np.full((self.dimensions),-N)

        self.visited[(0,)*self.dimensions]=True
        path_coords_transposed = np.array(path_coords).T.tolist()
        self.visited[tuple(path_coords_transposed)]=True
    def append(self,new_coords):
        self.path_coords = np.append(self.path_coords, new_coords,0)
        for new_coord in new_coords:
            #for element,max_dimension,min_dimension in\
            #        zip(new_coord,max_dimensions,min_dimensions):
            for dim in range(self.dimensions):
                if(new_coord[dim]> self.max_dimensions[dim]):
                    self.max_dimensions[dim]+=1
                    #Because we assume that this point is connected to a point
                    #that is in the lattice, we can assume we only need to add
                    #one row
                    self.visited =np.insert(self.visited, [self.max_dimensions[dim]], False,dim)
                if(new_coord[dim]< self.min_dimensions[dim]):
                    self.min_dimensions[dim]-=1
                    self.visited =np.insert(self.visited, [self.min_dimensions[dim]+1], False,dim)
            self.visited[new_coord]=True

                     
        if isinstance(new_coords, int):
            self.N+=1
        else:
            self.N+=len(new_coords)

    def pop(self,n):
        to_be_removed =  np.array(self.path_coords[-n:]).T.tolist()
        self.visited[tuple(to_be_removed)]=False
        self.path_coords = self.path_coords[:-n]
    def go_direction(self, direction):
        if(direction>= len(self.direction_vectors)):
            raise Exception("Direction must be between 0 and {}, thus it can't be {}".format(len(direction_vectors)-1,direction))
        new_coord =tuple([x+y for x,y in zip(self.path_coords[-1],\
                self.direction_vectors[direction])])
        if(self.visited[new_coord]):
            raise Exception("Point {} has already been visited".format(new_coord))
        self.append([new_coord])
        
    def plot_saw(self):
        if self.template == '2dsquare':
            plt.figure()
            ax = plt.axes()
            # Draw SAW
            for i in range(0,len(self.path_coords)-1):
                begin = self.path_coords[i]
                end = self.path_coords[i+1]
                x_range = [begin[0],end[0]]
                y_range = [begin[1],end[1]]
                ax.plot(x_range,y_range,color = 'k')
            # Draw grid
            x = np.array([],dtype = int)
            for i in range(0,len(self.path_coords)):
                x = np.append(x,self.path_coords[i][0])
            x_range = (min(x),max(x))
            
            y = np.array([],dtype = int)
            for i in range(0,len(self.path_coords)):
                y = np.append(y,self.path_coords[i][1])
            y_range = (min(y),max(y))
            
            x_range = np.arange(x_range[0]-1,x_range[1]+2)
            y_range = np.arange(y_range[0]-1,y_range[1]+2)
            data = np.array([[x,y] for x in x_range for y in y_range])
            plt.scatter(data[:, 0], data[:, 1],linewidths=6)
                       
            
        elif self.template == '2dtriangle':
            raise NotImplementedError("Plotting has not been implemented for '2dtriangle' SAW.")
        else:
            raise NotImplementedError("Plotting has not been implemented for {{template} type.")

'''        
g = SAW(1)
g.go_direction(1)
g.go_direction(2)
g.go_direction(1)
g.go_direction(2)
g.go_direction(3)

print(g.path_coords)
g.plot_saw()
'''

s = SAW(10)
s.go_direction(1)
s.go_direction(2)
s.go_direction(1)
s.go_direction(2)
s.go_direction(2)
s.plot_saw()