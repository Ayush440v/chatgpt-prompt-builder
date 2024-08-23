# ChatGPT Prompt Builder

## Overview

The ChatGPT Prompt Builder is a Streamlit application designed to help users generate prompts for ChatGPT based on selected domains, expertise levels, tasks, and specific user requirements. The application provides a user-friendly interface to select options and generate customized prompts.

## Features

- **Domain Selection**: Choose from a variety of domains.
- **Expertise Selection**: Select expertise levels based on the chosen domain.
- **Task Selection**: Choose tasks related to the selected expertise.
- **User Input**: Provide specific requirements to tailor the prompt.
- **Prompt Generation**: Generate a customized prompt based on the selected options and user input.
- **Database Storage**: Store generated prompts in an SQLite database.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ayush440v/chatgpt-prompt-builder.git
    cd chatgpt-prompt-builder
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and navigate to `http://localhost:8501` to access the application.

3. **Follow the steps** in the application to generate a prompt:
    - Select a domain.
    - Select an expertise level.
    - Select a task.
    - Provide specific requirements.
    - Click "Generate Prompt" to see the generated prompt.

## Data Files

- [`data/domain_expertise.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FZ%3A%2FProjects%2Fprompt_builder%2Fdata%2Fdomain_expertise.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "z:\Projects\prompt_builder\data\domain_expertise.json"): JSON file containing domain and expertise data.
- [`data/expertise_tasks.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FZ%3A%2FProjects%2Fprompt_builder%2Fdata%2Fexpertise_tasks.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "z:\Projects\prompt_builder\data\expertise_tasks.json"): JSON file containing expertise and task data.
- `data/prompts.db`: SQLite database file for storing generated prompts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Streamlit for providing an easy-to-use framework for building web applications.
- OpenAI for developing ChatGPT.