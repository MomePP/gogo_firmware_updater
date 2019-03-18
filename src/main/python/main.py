from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtCore import QProcess, QStringListModel
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from fwUpdaterUI import Ui_MainWindow

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def __init__(self, parent=None):
        self.window = QMainWindow()
        
        QWidget.__init__(self.window, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        #? setup click event
        self.ui.pathButton.clicked.connect(self.openFileNameDialog)
        self.ui.pushButton.clicked.connect(self.runFWUpdate)

        #? set statusbar value
        self.ui.progressBar.setRange(0, 100)
    
    def run(self):                              # 2. Implement run()
        
        version = self.build_settings['version']
        self.window.setWindowTitle("GoGo Updater v" + version)
        self.window.show()
        return self.app.exec_()                 # 3. End run() with this line
    
    def insertText(self):
        t = self.ui.label.text()
        self.ui.textEdit.setText(t)
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self.window,"Select new firmware to update", "","Bin Files (*.bin);;All Files (*)", options=options)
        if filePath:
            self.ui.textEdit.setText(filePath)

    def runFWUpdate(self):
        self.ui.progressBar.setValue(0)
        arg_list = []
        fullProgramPath = self.get_resource('hid-flash.exe')
        arg_list.append(self.ui.textEdit.toPlainText())

        proc = QProcess()
        proc.setProgram(fullProgramPath)
        proc.setArguments(arg_list)
        proc.start()
        # proc.start()
        proc.waitForFinished()

        self.ui.progressBar.setValue(100)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)