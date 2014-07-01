from PyQt4.QtGui import *

import Resources

class CropView(QGraphicsView):
    """This class provides a graphical view that has the resources for displaying
       crop status visually"""

    #Constructor
    def __init__(self):
        super().__init__()

    def Resources(self, cropType):
        #Get the graphics
        seed = QPixmap(":/{0}_Seed.png".format(cropType))
        seedling = QPixmap(":/{0}_Seedling.png".format(cropType))
        young = QPixmap(":/{0}_Young.png".format(cropType))
        mature = QPixmap(":/{0}_Mature.png".format(cropType))
        old = QPixmap(":/{0}_Old.png".format(cropType))

        cropPictures = [seed, seedling, young, mature, old]

        #Add the graphics to scenes
        self.cropScenes = []
        for each in cropPictures:
            self.cropScenes.append(QGraphicsScene())
            self.cropScenes[-1].addPixmap(each)
        self.setScene(self.cropScenes[0]) #Set the initial scene

    def switchScene(self, scene):
        self.setScene(self.cropScenes[scene])

class WheatView(CropView):
    def __init__(self):
        super().__init__()
        self.Resources("Wheat")

class PotatoView(CropView):
    def __init__(self):
        super().__init__()
        self.Resources("Potato")
