# AI Chatbot for Skill Teaching and Creativity Stimulation

This project is designed to create an AI chatbot capable of teaching various skills and stimulating creativity. The chatbot leverages the OpenAI API for natural language processing and interaction. It is equipped to assist users in a variety of domains, from chat-based learning to creative content generation.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Modes of Operation](#modes-of-operation)
- [Author](#author)
- [Future Potential](#future-potential)

## Project Structure

The project is organized into several Python files, each serving a specific purpose:

- **openai_api.py**: Contains functions to interact with the OpenAI API. It enables the chatbot to generate responses based on user input.

- **config.py**: Defines global configurations and constants, including the OpenAI API key and the OpenAI GPT-3 engine.

- **act.py**: This file handles the "Act" mode, allowing the chatbot to perform actions or tasks based on user instructions.

- **animation.py**: Implements the display of 2D and 3D animations using PyQt5. These animations can be used for creative content or visualization.

- **chat.py**: Manages the "Chat" mode, where the chatbot engages in conversation and provides responses to user queries.

- **creation.py**: Handles the "Creation" mode, enabling users to create various content types, such as audio, images, and videos, with the assistance of the chatbot.

- **gui.py**: This is the graphical user interface for interacting with the chatbot. It provides a user-friendly way to switch between different modes and communicate with the chatbot.

- **interaction.py**: Manages the "Interaction" mode, allowing users to manipulate digital content with the assistance of the chatbot.

- **learn.py**: Handles the "Learn" mode, where the chatbot provides educational content and exercises to help users learn about specific topics or skills.

- **note.py**: This mode, named "Note," assists users in organizing their ideas and creating notes. Users can input note titles and content, and the chatbot helps manage them.

- **main.py**: The main script that initializes the GUI and starts the application.

## Getting Started

To get started with this project, follow these steps:

1. Clone or download the project repository to your local machine.

2. Ensure you have the required dependencies installed, including PyQt5, OpenAI Python, and other libraries used in the project.

3. Configure the `config.py` file by adding your OpenAI API key. Make sure you have access to the GPT-3 engine specified in the configuration.

4. Run the `main.py` script to launch the chatbot interface.

5. Use the interface to switch between different modes (Chat, Creation, Interaction, Learn, Note, Act) and interact with the chatbot based on your requirements.

## Modes of Operation

- **Chat Mode**: This mode allows natural language conversation with the chatbot. It's designed for general chat-based interactions.

- **Creation Mode**: Users can create various content types, such as audio, images, videos, and animations, with the assistance of the chatbot.

- **Interaction Mode**: Users can manipulate digital content with the help of the chatbot. This mode is useful for tasks like editing and modifying files.

- **Learn Mode**: The chatbot provides educational content and exercises to help users learn about specific topics or skills.

- **Note Mode**: Users can create and manage notes and ideas with the chatbot's assistance.

- **Act Mode**: This mode enables the chatbot to perform actions or tasks based on user instructions.

## Author

This project was developed by AMBAZA KIMANUKA Armand.

## Future Potential

The project's future potential includes:

- **Enhanced Learning**: Extending the "Learn" mode to cover a wider range of topics and provide more comprehensive educational materials.

- **Improved Creativity**: Enhancing the "Creation" mode to offer more sophisticated content creation, such as complex animations and artwork.

- **Action Automation**: Developing the "Act" mode further to perform a broader set of actions and tasks, making it more versatile.

- **User Interaction**: Improving the chatbot's ability to understand and respond to user queries, creating a more natural and helpful experience.

Contributions from the open-source community can help unlock the full potential of this project.
