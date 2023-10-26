from PyQt5.QtWidgets import QApplication, QLineEdit, QPlainTextEdit, QRadioButton, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLabel, QFileDialog
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QRect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from chat import chat_output
from creation import creation_output
from interaction import interaction_output
from learn import learn_output
from note import note_output
from act import act_output

class Productivitee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI App")
        self.setGeometry(100, 100, 1200, 600)
        self.setStyleSheet("background-color: #F2E8CF; color: #101010; font-family: Arial; font-size: 14px;")

        
        def create_btn(text, x, func):
            btn = QRadioButton(text, self)
            btn.move(x, 10)
            btn.clicked.connect(func)
            return btn


        self.chat_btn, self.creation_btn, self.interaction_btn, self.learn_btn, self.note_btn, self.act_btn = \
            [create_btn(t, 100 * i, f) for i, (t, f) in enumerate(zip(
                ["Chat", "Creation", "Interaction", "Learn", "Note", "Act"],
                [self.chat_mode, self.creation_mode, self.interaction_mode, self.learn_mode, self.note_mode, self.act_mode]))]

        self.chat_btn.setChecked(True)
        self.title_label = QLabel("Hello! I am an artificial intelligence trained to help you learn new things. Ask me anything you want.", self, geometry=QRect(0, 50, 1200, 50), alignment=Qt.AlignCenter)
        self.input_textbox, self.submit_btn, self.output_textbox = QPlainTextEdit(self, geometry=QRect(50, 120, 800, 40)), QPushButton("Ask", self, geometry=QRect(880, 120, 100, 40), clicked=self.submit_action), QTextEdit(self, readOnly=True, geometry=QRect(50, 200, 1000, 300))

        def create_action_btn(text, x, func): return QPushButton(text, self, geometry=QRect(x, 540, 100, 40), clicked=func)

        self.new_topic_btn, self.copy_btn, self.history_btn = \
            [create_action_btn(t, 400 + 120 * i, f) for i, (t, f) in enumerate(zip(
                ["New Topic", "Copy", "My History"],
                [self.new_topic_action, self.copy_action, self.history_action]))]

        self.mode = "chat"
        self.chat_mode()

    def submit_action(self):
        user_input = self.input_textbox.toPlainText()
        self.input_textbox.setPlainText("")
        if self.mode == "chat":
            chat_output(self, user_input)
        elif self.mode == "creation":
            creation_output(self, user_input)
        elif self.mode == "interaction":
            interaction_output(user_input)
        elif self.mode == "learn":
            learn_output(user_input)
        elif self.mode == "note":
            note_output(user_input)
        elif self.mode == "act":
            act_output(user_input)

    def new_topic_action(self): pass
    def copy_action(self): pass
    def history_action(self): pass

    def chat_mode(self): self.set_mode('chat')
    def creation_mode(self): self.set_mode('creation')
    def interaction_mode(self): self.set_mode('interaction')
    def learn_mode(self): self.set_mode('learn')
    def note_mode(self): self.set_mode('note')
    def act_mode(self): self.set_mode('act')

    def set_mode(self, mode):
        modes = {
            "chat": ("Hello! I am an artificial intelligence trained to help you learn new things. Ask me anything you want.", "#C9E4E2", "#38A29A"),
            "creation": ("Hello! I am an artificial intelligence trained to help you improve your creativity. What would you like to create today? I can help you create 2D or 3D graphic representations of your ideas.", "#C9E4CA", "#7BA69C"),
            "interaction": ("Hello! I am an artificial intelligence trained to help you manipulate digital content. What would you like to manipulate today? Import a file and give me instructions.", "#F1D1D0", "#E26D5C"),
            "learn": ("Hello! I am an artificial intelligence trained to help you learn about human arts. Give me a topic and I will prepare educational content and exercises to help you become better at what you do.", "#E4D6C9", "#C47B37"),
            "note": ("Hello! I am an artificial intelligence trained to help you organize your ideas. What do you want to work on today?", "#E4E0C9", "#AD9C38"),
            "act": ("Hello! I am an artificial intelligence trained to perform repetitive or complex tasks on your device. Give me instructions.", "#E9D0F1", "#9630B6")
        }
        title, input_bg, submit_bg = modes[mode]

        self.mode = mode
        self.title_label.setText(title)
        self.title_label.setStyleSheet("font: 16pt Arial Rounded MT Bold;")
        self.input_textbox.setStyleSheet(f"background-color: {input_bg}; color: #101010; font: 14pt Arial;")
        self.submit_btn.setText("Ask" if mode == "chat" else "Create" if mode == "creation" else "Modify" if mode == "interaction" else "Teach me" if mode == "learn" else "Save" if mode == "note" else "Act")
        self.submit_btn.setStyleSheet(f"background-color: {submit_bg}; color: #FFFFFF; font: 14pt Arial;")
        self.new_topic_btn.setText(f"New {mode.capitalize()}")
        self.new_topic_btn.setStyleSheet(f"background-color: {submit_bg}; color: #FFFFFF; font: 14pt Arial;")
        self.copy_btn.setText(f"Download {mode.capitalize()}")
        self.copy_btn.setStyleSheet(f"background-color: {submit_bg}; color: #FFFFFF; font: 14pt Arial;")
        self.history_btn.setStyleSheet(f"background-color: {submit_bg}; color: #FFFFFF; font: 14pt Arial;")
        self.output_textbox.setStyleSheet(f"background-color: {input_bg}; color: #101010; font: 14pt Arial;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Productivitee()
