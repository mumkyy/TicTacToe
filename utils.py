class Screen:
    def __init__(self,size=(3,3),grid=False,grid_dimensions=(0,0),grid_size=(0,0)):
        self.size = size
        self.grid = grid
        self.grid_dimensions = grid_dimensions
        self.grid_size = grid_size
        self.x = size[0]
        self.y = size[1]
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for k in range(self.x):
                self.screen[i].append('   ')
        if grid:
            self.add_grid(grid_dimensions,grid_size)
                
    def add_stuff(self,stuff,x,y):
       for row in range(len(stuff)):
        for item in range(len(stuff[row])):
            self.screen[y+row][x+item] = " " + stuff[row][item] + " "
                
    def add_grid(self,grid_dimensions,grid_size):
        width_between= grid_size[0]//grid_dimensions[0]
        height_between = grid_size[1]//grid_dimensions[1]
        horizontal = grid_dimensions[0]-1
        vertical = grid_dimensions[1]-1
        hline = ['.'*grid_size[0]]
        vline = [['.'] for x in range(grid_size[1])]
        for x in range(1,horizontal+1):
            self.add_stuff(hline,0,height_between*x)
        for y in range(1,vertical+1):
            self.add_stuff(vline,width_between*y,0)

    def clear_screen(self):
        self.screen.clear()
        for i in range(self.y):
            self.screen.append([])
            for k in range(self.x):
                self.screen[i].append('')
    
    def print_screen(self):
        print("."*(3*(self.x)+2))
        for x in self.screen:
            print(".",end = '')
            for y in x:
                print(y, end="")
            print(".")
        print("."*(3*(self.x)+2))