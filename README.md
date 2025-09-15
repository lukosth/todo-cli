# 📝 todo-cli: Your Simple Command-Line To-Do App

![todo-cli](https://img.shields.io/badge/todo--cli-v1.0.0-blue.svg) ![Python](https://img.shields.io/badge/Python-3.6%2B-yellow.svg) ![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen.svg)

Welcome to **todo-cli**, a straightforward command-line To-Do application crafted with Python. This app allows you to manage your tasks efficiently by adding, completing, and deleting them with ease. With local JSON storage, it's perfect for minimalists who appreciate the simplicity of the terminal.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [JSON Storage](#json-storage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list.
- **Complete Tasks**: Mark tasks as completed with a simple command.
- **Delete Tasks**: Remove tasks that you no longer need.
- **Local JSON Storage**: Store your tasks in a JSON file for easy access and modification.
- **Minimalist Design**: Focus on your tasks without distractions.

## Installation

To get started with todo-cli, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lukosth/todo-cli.git
   cd todo-cli
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.6 or higher installed. You can install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   You can download the latest release [here](https://github.com/lukosth/todo-cli/releases). Make sure to execute the downloaded file to run the application.

## Usage

Once you have installed todo-cli, you can start using it right away. Open your terminal and navigate to the directory where you cloned the repository. Then, run the following command:

```bash
python todo.py
```

You will see a simple interface guiding you through the available commands.

## Commands

Here are the primary commands you can use with todo-cli:

- **Add a Task**:
  ```bash
  add "Task description"
  ```

- **Complete a Task**:
  ```bash
  complete TASK_ID
  ```

- **Delete a Task**:
  ```bash
  delete TASK_ID
  ```

- **List All Tasks**:
  ```bash
  list
  ```

- **Help**:
  ```bash
  help
  ```

## JSON Storage

todo-cli uses a local JSON file to store your tasks. This allows for easy access and modification of your to-do list. The JSON file is located in the same directory as the application. You can edit this file directly if needed, but it's recommended to use the app's commands for consistency.

## Contributing

We welcome contributions to todo-cli! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push to your branch.
5. Create a pull request.

Your contributions help make todo-cli better for everyone.

## License

todo-cli is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit.

## Contact

For any questions or feedback, please reach out:

- **GitHub**: [lukosth](https://github.com/lukosth)
- **Email**: lukosth@example.com

Thank you for checking out todo-cli! We hope it helps you stay organized and productive. Don't forget to visit the [Releases](https://github.com/lukosth/todo-cli/releases) section for updates and new features. 

![Terminal App](https://images.unsplash.com/photo-1517436079788-9d8b1c40a0c2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fHRlcm1pbmFsJTIwYXBwfGVufDB8fHx8MTYzNjYyMTI5Ng&ixlib=rb-1.2.1&q=80&w=1080)

---

Happy Task Management! 🗂️