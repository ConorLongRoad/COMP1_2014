from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """This class provides a dialog window to ask for light and water values"""

    #Constructor
    def __init__(self):
        super().__init__()

        self.waterSpinBox = QSpinBox()
        self.lightSpinBox = QSpinBox()

        self.waterSpinBox.setRange(1,10)
        self.lightSpinBox.setRange(1,10)

        self.waterSpinBox.setSuffix(" Water")
        self.lightSpinBox.setSuffix(" Light")

        self.waterSpinBox.setValue(1)
        self.lightSpinBox.setValue(1)

        self.submitButton = QPushButton("Enter Values")

        self.dialogLayout = QVBoxLayout()
        self.dialogLayout.addWidget(self.lightSpinBox)
        self.dialogLayout.addWidget(self.waterSpinBox)
        self.dialogLayout.addWidget(self.submitButton)

        self.setLayout(self.dialogLayout)

        #Connection
        self.submitButton.clicked.connect(self.close)

    def values(self):
        return int(self.lightSpinBox.value()), int(self.waterSpinBox.value())
