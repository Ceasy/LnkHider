Shortcut Manager is a simple and efficient way to manage shortcuts on your desktop.
With Shortcut Manager, you can hide and show your shortcuts with a single hotkey. This will keep your desktop
clutter-free and organized.

1. Features

* Hide and show shortcuts with a single hotkey
* Store shortcuts in a designated folder
* Customize hotkey and folder location through config file


2. Requirements

* Windows XP or later
* .NET Framework 4.0 or later


3. Installation

1. Download the repository as a zip file from GitHub
2. Extract the zip file to your local machine
3. Navigate to the extracted folder and install the required libraries

$ cd Shortcut-Manager
$ pip install -r requirements.txt


4. Usage

1) Run the LnkHider.exe file

2) By default, the hotkey is set to Ctrl + Windows. You can change the hotkey in the config.ini file.

[Settings]
lnks_path = C:\Users\Public\Documents\Links
hotkey = ctrl+win

3) The shortcuts will be stored in the folder C:\Users\Public\Documents\Links by default.
You can change the folder location in the config.ini file.


5. Troubleshooting
If you encounter any issues while using Shortcut Manager, please report them on the GitHub repository.
The development team will do their best to resolve the issue as soon as possible.

6. License
Shortcut Manager is licensed under the MIT License. See the LICENSE file for more information.

Author: Alexey Fedotov.
Date: 2023-29-01
