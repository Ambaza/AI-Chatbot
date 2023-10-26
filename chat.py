from openai_api import call

def chat_output(self, prompt):
    self.output_textbox.append(call(prompt))
