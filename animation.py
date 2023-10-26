from PyQt5.QtWidgets import QApplication, QLineEdit, QPlainTextEdit, QRadioButton, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLabel, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class My2DAnimationWidget(QWidget):
    def __init__(self, file_path):
        super().__init__()
        layout = QVBoxLayout(self)

        # Create a label to display the video
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Create a media player object
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.label)

        # Set the media player's media content
        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media_content)

        # Play the video
        self.media_player.play()


class My3DAnimationWidget(QWidget):
    def __init__(self, file_path):
        super().__init__()
        layout = QVBoxLayout(self)

        # Create a label to display the video
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Create a media player object
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.label)

        # Set the media player's media content
        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media_content)

        # Play the video
        self.media_player.play()
