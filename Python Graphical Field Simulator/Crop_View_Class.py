from PyQt4.QtGui import *

import resources

class CropView(QGraphicsView):
    """This class provides a graphics view that has the resources for displaying
       crop status visually"""

    #Constructor
    def __init__(self):
        super().__init__()

    def resources(self, cropType):
        #Get the graphics
        seed = QPixmap(":/{0}_Seed.png".format(cropType))
        seedling = QPixmap(":/{0}_Seedling.png".format(cropType))
        young = QPixmap(":/{0}_Young.png".format(cropType))
        mature = QPixmap(":/{0}_Mature.png".format(cropType))
        old = QPixmap(":/{0}_Old.png".format(cropType))

        cropPictures = [seed, seedling, young, mature, old]

        #Add the graphics to scenes
        self.cropScene = []
        for each in cropPictures:
            self.cropScene.append(QGraphicsScene())
            self.cropScene[-1].addPixmap(each)
        self.setScene(self.cropScene[0]) #Set the initial scene

    def switchScene(self, scene):
        self.setScene(self.cropScenes[scene])

class WheatView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("Wheat")

class PotatoView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("Potato")
