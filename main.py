import sys
from PySide6.QtWidgets import QApplication
from dotenv import load_dotenv
from src.controllers.MainWindowController import MainWindowController
import qdarktheme

#load environment variables
load_dotenv()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowController()
    # setup stylesheet
    qdarktheme.setup_theme("auto", default_theme="dark")
    window.show()
    sys.exit(app.exec())