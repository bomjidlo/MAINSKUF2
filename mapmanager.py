class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)
        self.startNew()
        self.addBlock((0, 10, 0))
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setTag('at', str(position))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def startNew(self):
        self.land = render.attachNewNode('Land')
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line  = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                        if z0 == 1:
                            self.block.setColor(0,1,0, 1)
                        elif z0 == 2:
                            self.block.setColor(1,0,0,1)
                        elif z0 == 3:
                            self.block.setColor(0,0,1,1)
                        
                    x+= 1
                y +=1
    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def findBlocks(self, pos):
        return self.land.findAllMatches('=at='+str(pos))
    def findHighestEmpty(self,pos):
        x,y,z  = pos
        z =1
        while not self.isEmpty((x,y,z)):
            z+=1
        return(x,y,z)
    def clear(self):
        self.land.removeNode()
        self.startNew()


