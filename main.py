import sys
from PySide6.QtWidgets import QApplication
from dotenv import load_dotenv

from src.controllers.MainWindowController import MainWindowController
import qdarktheme

from src.utils.Config import Config

# load environment variables
load_dotenv()
config = Config.get_instance()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowController()
    # setup stylesheet
    qdarktheme.setup_theme("light", default_theme="light")
    window.show()
    sys.exit(app.exec())
