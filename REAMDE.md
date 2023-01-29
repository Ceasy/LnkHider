
# Shortcut Manager
Shortcut Manager is a simple and efficient way to manage shortcuts on your desktop. With Shortcut Manager, you can hide and show your shortcuts with a single hotkey. This will keep your desktop clutter-free and organized.

# Features
Hide and show shortcuts with a single hotkey
Store shortcuts in a designated folder
Customize hotkey and folder location through config file
# Requirements
Python 3.x
Keyboard library
ConfigParser library
Shutil library
# Installation
Clone the repository to your local machine
shell
Copy code
$ git clone https://github.com/[your_username]/Shortcut-Manager.git
Navigate to the cloned repository and install the required libraries
shell
Copy code
$ cd Shortcut-Manager
$ pip install -r requirements.txt
# Usage
Run the main.py file
css
Copy code
$ python main.py
By default, the hotkey is set to Ctrl + Windows. You can change the hotkey in the config.ini file.
makefile
Copy code
[Settings]
lnks_path = C:\Users\Public\Documents\Links
hotkey = ctrl+win
The shortcuts will be stored in the folder C:\Users\Public\Documents\Links by default. You can change the folder location in the config.ini file.
# Contributing
If you would like to contribute to the project, please follow these guidelines:

Fork the repository
Create a new branch for your changes
Commit your changes with clear and concise commit messages
Open a pull request and explain your changes
# License
Shortcut Manager is released under the MIT License.