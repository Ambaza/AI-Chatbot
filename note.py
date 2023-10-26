import config

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

def create_note(title: str, content: str) -> Note:
    return Note(title, content)

def note_output(note: Note) -> str:
    return f"{config.APP_NAME}\n\n{str(note)}"

def main():
    while True:
        title = input("Enter the note title: ")
        if title.lower() == "quit":
            print("Goodbye!")
            break

        content = input("Enter the note content: ")
        note = create_note(title, content)
        output = note_output(note)
        print("Note created:")
        print(output)

if __name__ == "__main__":
    main()
