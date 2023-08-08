from modelview import (QIcon,  MainWindow)
from recource_utils import resource_path, os, sys
from PyQt5.QtWidgets import QApplication
                
if __name__ == "__main__":
    def cleanup():
        if os.path.exists(resource_path("images\\temp.png")):
            os.remove(resource_path("images\\temp.png"))

    app = QApplication(sys.argv)
    with open(resource_path("style\\style.qss"), "r") as style_file:
        style= style_file.read()
    app.setWindowIcon(QIcon(resource_path("images\\icon.png")))
    app.setStyleSheet(style)
    app.aboutToQuit.connect(cleanup)
    window = MainWindow()
    window.setFixedSize(1500, 800)
    window.show()

    sys.exit(app.exec())