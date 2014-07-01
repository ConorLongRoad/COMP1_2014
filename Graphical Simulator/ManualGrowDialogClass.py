from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """This class provides a dialog window to ask for light and water"""

    #Constructor
    def __init__(self):
        super().__init__()

        self.waterSpinbox = QSpinBox()
        self.lightSpinbox = QSpinBox()

        self.waterSpinbox.setRange(0,10)
        self.lightSpinbox.setRange(0,10)

        self.waterSpinbox.setSuffix(" Water")
        self.lightSpinbox.setSuffix(" Light")

        self.waterSpinbox.setValue(1)
        self.lightSpinbox.setValue(1)

        self.submitButton = QPushButton("Enter value")

        self.dialogLayout = QVBoxLayout()
        self.dialogLayout.addWidget(self.lightSpinbox)
        self.dialogLayout.addWidget(self.waterSpinbox)
        self.dialogLayout.addWidget(self.submitButton)

        self.setLayout(self.dialogLayout)

        #Connections
        self.submitButton.clicked.connect(self.close)

    def values(self):
        return int(self.lightSpinbox.value()), int(self.waterSpinbox.value())
