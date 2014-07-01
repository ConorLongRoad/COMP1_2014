from graphic_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """This class provides a pixmap item with a preset image for the animal"""

    #Constructor
    def __init__(self, graphicsList):
        super().__init__(graphicsList)

        self.animal = None

    def updateStatus(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.availableGraphics[0]).scaledToWidth(25,1))
        elif self.animal._status == "Poor":
            self.setPixmap(QPixmap(self.availableGraphics[1]).scaledToWidth(25,1))
        elif self.animal._status == "Fine":
            self.setPixmap(QPixmap(self.availableGraphics[2]).scaledToWidth(25,1))
        elif self.animal._status == "Prime":
            self.setPixmap(QPixmap(self.availableGraphics[3]).scaledToWidth(25,1))
