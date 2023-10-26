from gui import Productivitee
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    ex = Productivitee()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
