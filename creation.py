import chat
import pydub

from openai_api import call

from animation import My2DAnimationWidget, My3DAnimationWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

def creation_output(self, user_input):
    if user_input.startswith("/audio"):
        play_audio_file(self, user_input)

    elif user_input.startswith("/image"):
        show_image_file(self, user_input)

    elif user_input.startswith("/video"):
        play_normal_video_file(self, user_input)

    elif user_input.startswith("/2D"):
        show_2d_animation_file(self, user_input)

    elif user_input.startswith("/3D"):
        show_3d_animation_file(user_input)

    else:
        self.output_textbox.append("Invalid input.")


def play_audio_file(self, user_input):

    # Define prompt to send to GPT-3
    prompt = "Analyze this user prompt and generate a precise description of an audio that can be generated from your answer: " + user_input[7:]

    # Generate audio prompt using GPT-3
    response = call(prompt)
    secondCall = call(response)
    audio_url = secondCall.strip()

    # Download the generated audio file
    audio_data = pydub.AudioSegment.from_file(audio_url, format="mp3")
    audio_file = "generated_audio.mp3"
    audio_data.export(audio_file, format="mp3")

    # Play the generated audio
    media = QMediaPlayer()
    media.setMedia(QMediaContent(QUrl.fromLocalFile(audio_file)))
    media.play()

    # Output generated audio file as a URL that can be used to download the file
    self.output_textbox.setPlainText(audio_url)


def show_image_file(self, user_prompt):
    if user_prompt.startswith("/image"):
        # Generate prompt for GPT3 to describe the image
        gpt3_prompt = "Analyze this user prompt and generate a precise description of an image that can be generated on your answer : " + user_prompt[6:]
        # Call GPT3 to get the precise description of the image
        response = call(gpt3_prompt)
        # Extract new image prompt from GPT3 response
        new_image_prompt = call(response).strip()
        
        image_data = response
        if ".png" in image_data:
            image_url = image_data[image_data.index("https"):image_data.index(".png")+4]
        else:
            # handle the error or display an error message
            print("Error: Image URL not found")
            return
    else:
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg)")
        if not file_path:
            return
        image_url = file_path
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    # Display image in a read-only textbox
    self.output_textbox.setReadOnly(True)
    self.output_textbox.setHtml(f'<img src="{image_url}" width="100%"/>')
    self.output_textbox.setReadOnly(False)
    # Create a new zone for displaying the image using PIL
    self.image_zone = QLabel(self)
    self.image_zone.setGeometry(10, 50, 400, 400)  # set the size and position of the zone
    img_pil = image.resize((400, 400))  # resize the image to fit the zone
    img_tk = ImageTk.PhotoImage(img_pil)
    self.image_zone.setPixmap(img_tk)
    self.image_zone.show()


def play_normal_video_file(self, user_input):
    file_path, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.wmv)")
    if file_path:
        media = QMediaPlayer()
        media.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        media.setVideoOutput(self.output_textbox)
        media.play()


def show_2d_animation_file(self, user_input):
    file_path, _ = QFileDialog.getOpenFileName(self, "Open 2D Animation File", "", "Video Files (*.mp4 *.avi *.wmv)")
    if file_path:
        widget = My2DAnimationWidget(file_path)
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setWidget(widget)
        self.output_textbox.setReadOnly(False)


def show_3d_animation_file(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Open 3D Animation File", "", "Video Files (*.mp4 *.avi *.wmv)")
    if file_path:
        widget = My3DAnimationWidget(file_path)
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setWidget(widget)
        self.output_textbox.setReadOnly(False)


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = creation_output(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
