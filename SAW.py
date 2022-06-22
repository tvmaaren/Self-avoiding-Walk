import numpy as np
import matplotlib.pyplot as plt

class SAW:
    #template:          The template lattice that will be used. Possible values are
    #                   "2dsquare","3dcubic","4dcubic","2dhoneycomb","2dtriangle" and None.
    #                   When not using a template set this to None
    #direction_vectors: List of direction vectors for the lattice. When using a template this
    #                   must be None
    def __init__(self,template="2dsquare",direction_vectors=None):

        #One and only one of template and direction_vectors must be equal to None. If  they would
        #both be None, then the class has no information on lattice it should have, but if they would
        #both be unequal to None, the two variables could contain conflicting information.
        if not ((template==None) ^ (direction_vectors==None)):
            raise Exception("One and only one of template and direction_vectors must be equal to \"None\"")

        #Goes through al the templates and sets the direction_vectors. The order of the directions goes
        #counter-clockwise for the 2d lattices.
        if(template=="2dsquare"):
            direction_vectors = [(1,0),(0,1),(-1,0),(0,-1)]
        elif(template=="3dcubic"):
            direction_vectors = [(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(1,0,0),(-1,0,0)]
        elif(template=="4dcubic"):
            direction_vectors =\
            [(0,0,1,0),(0,0,0,1),(0,0,-1,0),(0,0,0,-1),(0,1,0,0),(0,-1,0,0),(1,0,0,0)\
                    ,(-1,0,0,0)]
        elif(template=="2dhoneycomb"):
            raise NotImplementedError("Template 2dhoneycomb is not implemented yet")
        elif(template=="2dtriangle"):
            #The direction_vectors for the 2dtriangle are the same as how they where
            #described in the report
            direction_vectors = [(1,1,0),(0,1,1),(-1,0,1),(-1,-1,0),(0,-1,-1),(1,0,-1)]
        elif(template!=None):
            raise Exception("Template \"{}\" does not exist".format(template))

        #Stores the information provided to the __init__ function in the class
        self.direction_vectors = direction_vectors
        self.directions = len(direction_vectors)
        self.dimensions = len(direction_vectors[0])
        self.path_coords = [(0,)*self.dimensions]#The path should always start at th origin
        self.template = template

        #self.visited is a multidimensional numpy array that has coordinates as index. For each
        #coordinate it gives a True if the path passes through that point and a false otherwise.
        self.visited = np.zeros((2*10+1,)*self.dimensions,dtype =bool)

        #For each dimension it gives the maximum and minimum coordinate. In the beginning this
        #is 10 and -10, because this is how the self.visited array is defined.
        self.max_dimensions = np.full((self.dimensions),10)
        self.min_dimensions = np.full((self.dimensions),-10)

        self.visited[(0,)*self.dimensions]=True #The origin must always be visited

                     

    #remove n steps at the end of the walk
    #n:     The amount of steps that will be removed
    def pop(self,n):

        #makes sure the origin alwes gets preserved
        if(n> len(self.path_coords)-1):
            raise Exception("It is illegal to remove the origin")

        to_be_removed =  np.array(self.path_coords[-n:]).T.tolist()
        self.visited[tuple(to_be_removed)]=False
        self.path_coords = self.path_coords[:-n]

    #Take a step in a given direction
    #direction:     Is an index of direction_vectors. It is the direction of the step
    def go_direction(self, direction):

        #check if it is a valid direction
        if(direction>= self.directions):
            raise Exception("Direction must be between 0 and {}, thus it can't be {}".format(self.directions-1,direction))

        #Add the corresponding direction vector to the head of walk
        new_coord =tuple([x+y for x,y in zip(self.path_coords[-1],\
                self.direction_vectors[direction])])
        
        #Enlarge the the grid if new_coord false outside of it
        for dim in range(self.dimensions):
            if(new_coord[dim]> self.max_dimensions[dim]):
                #it assumes that new_coord is connected to a point inside of the grid,
                #thus it only has to make the max_dimension one bigger.
                self.max_dimensions[dim]+=1
                self.visited =np.insert(self.visited, [self.max_dimensions[dim]], False,dim)
            if(new_coord[dim]< self.min_dimensions[dim]):
                #it assumes that new_coord is connected to a point inside of the grid,
                #thus it only has to make the min_dimension one smaller.
                self.min_dimensions[dim]-=1
                self.visited =np.insert(self.visited, [self.min_dimensions[dim]+1], False,dim)

        #Checks if the new point has already been visited
        if(self.visited[new_coord]):
            raise Exception("Point {} has already been visited".format(new_coord))

        #add new_coord to path_coords
        self.path_coords = np.append(self.path_coords, [new_coord],0)

        self.visited[new_coord]=True

    #Calculate the possible walks of specified length
    #N:  The length of a walk.
    def possible_walks(self,N):
        
        #If it already is a walk of length N, there is
        #only one possibility
        if(len(self.path_coords)-1==N):
            return 1
        
        #If the length of the walk is bigger than N
        #there are no possibilities
        elif(len(self.path_coords)-1>=N):
            return 0

        count = 0 #possibility counter

        #Tries every direction from the current point
        for direction in range(self.directions):
            try:
                #This will lead to an error if that point already has been visited
                self.go_direction(direction)

                #If no error occures it counts the possible walks from this point
                count+= self.possible_walks(N)

                #Goes back to the point that it started at
                self.pop(1)
            except:
                pass
        return count
            
    def plot(self):
        if self.template == '2dsquare':
            # Setting correct graph size.
            fig = plt.figure(dpi=300)
            ax = fig.add_subplot(111)
            ax.axis('off')
            ax.set_aspect('equal')
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
            plt.scatter(data[:, 0], data[:, 1],linewidths=3, color = 'k')
            plt.scatter(0,0, color = 'r',linewidths=3)
               
        elif self.template == '2dtriangle':
            fig = plt.figure(dpi=300)
            ax = fig.add_subplot(111)
            ax.axis('off')
            ax.set_aspect('equal')
            # Draw SAW
            start = (0,0)
            y_range = x_range = np.array([0])
            for i in range(0,len(self.path_coords)-1):
                diff = self.path_coords[i+1] - self.path_coords[i]
                if np.allclose(diff, self.direction_vectors[0]):
                    end = (start[0] + 1, start[1] + 0)
                    x_range = np.append(x_range, x_range[-1] + 2)
                    
                elif np.allclose(diff, self.direction_vectors[1]):
                    end = (start[0] + 0.5, start[1] + 0.5*np.sqrt(3))
                    x_range = np.append(x_range, x_range[-1] + 1)
                    y_range = np.append(y_range, y_range[-1] + 1)
                    
                elif np.allclose(diff, self.direction_vectors[2]):
                    end = (start[0] - 0.5, start[1] + 0.5*np.sqrt(3))
                    x_range = np.append(x_range, x_range[-1] - 1)
                    y_range = np.append(y_range, y_range[-1] + 1)
                    
                elif np.allclose(diff, self.direction_vectors[3]):
                    end = (start[0] - 1, start[1])
                    x_range = np.append(x_range, x_range[-1] - 2)
                    
                elif np.allclose(diff, self.direction_vectors[4]):
                    end = (start[0] - 0.5, start[1] - 0.5*np.sqrt(3))
                    x_range = np.append(x_range, x_range[-1] - 1)
                    y_range = np.append(y_range, y_range[-1] - 1)
                    
                else:
                    end = (start[0] + 0.5, start[1] - 0.5*np.sqrt(3))
                    x_range = np.append(x_range, x_range[-1] + 1)
                    y_range = np.append(y_range, y_range[-1] - 1)
                    
                ax.plot([start[0],end[0]],[start[1],end[1]],color = 'k')
                start = end
            
            # Draw grid    
            x_min = min(x_range)-1
            x_max = max(x_range)+1
            y_min = min(y_range)-1
            y_max = max(y_range)+1
            
            for i in range(y_min,y_max+1):
                if i % 2 == 0:
                    x_range = np.array([0.5*x for x in range(x_min,x_max+1) if x % 2 == 0])
                    
                else:
                    x_range = np.array([0.5*x for x in range(x_min,x_max+1) if x % 2 == 1])
                    
                data = np.array([[x,i*0.5*np.sqrt(3)] for x in x_range])
                plt.scatter(data[:, 0], data[:, 1],linewidths=3, color = 'k')
            
            plt.scatter(0,0, color = 'r',linewidths=3)
            
        else:
            raise NotImplementedError("Plotting has not been implemented for {} type.".format(self.template))
        plt.show()
