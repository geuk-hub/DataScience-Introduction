class Stack : 
    def __init__(self) :
        self.top = []
    def isEmpty(self) :
        return len(self.top) == 0
    def size(self) :
        return len(self.top)
    def clear(self) :
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self) :
        if not self.isEmpty() :
            return self.top.pop(-1)
    def peek(self) :
        if not self.isEmpty() :
            return self.top[-1]
    def __str__(self) :
        return str(self.top[::-1])

def isValidPos(x,y) :
    if x < 0 or y < 0 or x >= MAZE_LENGTH or y >= MAZE_WIDTH :
        return False
    else :
        return map[x][y] == '0' or map[x][y] == 'E'

def DFS(index) :
    stack =Stack()
    stack.push(index)

    while not stack.isEmpty() :
        here = stack.pop()
        (x,y) = here
        if (map[x][y] == 'E') :
            break
        else : 
            map[x][y] = '.'
            if isValidPos(x, y - 1) :
                stack.push((x, y-1))
            if isValidPos(x, y + 1) :
                stack.push((x, y + 1))
            if isValidPos(x - 1, y) :
                stack.push((x - 1, y))
            if isValidPos(x + 1, y) :
                stack.push((x+1, y))
    if map[x][y] == 'E' :
        return True
    else :
        return False



inputfile = open('input1.txt', 'r')
start_location = inputfile.readlines()
mazefile = open('maze.txt', 'r')
mazefile = mazefile.readlines()
    
for i in range(0, len(start_location)) :
    map = []
    for j in range(1,len(mazefile)) :
        map.append(list(mazefile[j][:20]))

    maze_size = mazefile[0].split()
    MAZE_LENGTH = int(maze_size[0])
    MAZE_WIDTH = int(maze_size[1])
    
    index = start_location[i].split()
    index_2 = [0,0]
    index_2 = int(index[0]), int(index[1])
    index[0], index[1] = int(index[0])-1 , int(index[1])-1
    index = tuple(index)
    result = DFS(index)
    
    if result == False :
        print("{0} 에서 출발 ==>\tX, 실패".format(index_2))
    if result == True :
        print("{0} 에서 출발 ==>\t0, 성공".format(index_2))