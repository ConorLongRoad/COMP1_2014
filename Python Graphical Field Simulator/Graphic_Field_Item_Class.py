from PyQt4.QtGui import *

class FieldItemGraphicsPixmapItem(QGraphicsPixmapItem):
    """This class provides a pixmap item with a preset image for the item"""

    #Constructor
    def __init__(self, graphicsList):
        super().__init__()
        self.availableGraphics = graphicsList
        self.currentGraphic = QPixmap(self.availableGraphics[0])
        self.setPixmap(self.currentGraphic.scaledToWidth(25,1))
        self.setFlag(QGraphicsItem.ItemIsMovable) #Allows us to move the graphics in the scene

    def updateStatus(self):
        pass
