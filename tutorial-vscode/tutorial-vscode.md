
## [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) Notes

Start VS Code in a folder, that folder becomes your "workspace"

### Python interpreter

1. Open **Command Palette** (Ctrl+Shift+P)
2. Type **Python: Select Interpreter**

A .vscode directory will appear with a seting.json and in it "python.pythonPath"

### Running source files

- Press **Run Python File in Terminal** play button in the top-right side of the editor
- Right-click anywhere in the editor window and select Run Python File in Terminal (which saves the file automatically)
- Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. This command is convenient for testing just a part of a file.
- From the Command Palette (Ctrl+Shift+P), select the Python: Start REPL command to open a REPL terminal for the currently selected Python interpreter. In the REPL, you can then enter and run lines of code one at a time

### Debugger

**TIP:** Press `F9` to set a breakpoint

Press `F5` to start debugging

You can fuck around in the **Python Debug Console**

### Packages

1. CREATE VIRTUAL ENVIROMENT 

**Why:** Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library. This means if application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run. [[Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html#introduction)]

```shell
python3 -m venv [name_of_enviroment]
```
Activate virtual enviroment

```shell
source [name_of_enviroment]/bin/activate
```

2. Select your new environment by using the **Python: Select Interpreter** command from the Command Palette

3. Install packages

```bash
apt-get install python3-tk # Probably already installed

# To install a python package
pip install [package]
```

4. Type `deactivate` to deactivate the virtual environment.
