# PROJECT OVERVIEW

## installation virtual environment

1. To setup the necessary virtual environment (**venv**), run [`setup.ps1`](setup.ps1) in your powershell terminal.

    ### open terminal:

    ![](instructions\open_terminal.gif)
    ![](https://github.com/Shergotty/create_py_venv_public/tree/main/instructions/open_terminal.gif)

If Python is not installed, Python version 3.10.7 will be downloaded ([Python](https://www.python.org/downloads/)) and the installer will be executed. Please install Python in order to setup the virtual environment and make sure you add your python installation folder to PATH (Checkbox at the end of installation). IF Python has to be installed, reboot your system in order to write your new systemvariable to your registry.

### run [`setup.ps1`](setup.ps1) 

```{ps}
.\setup.ps1
```

![](instructions\install_requirements.gif)
![](https://github.com/Shergotty/create_py_venv_public/tree/main/instructions/install_requirements.gif)
    
## venv is activated

![](instructions\ready.gif)
![](https://github.com/Shergotty/create_py_venv_public/tree/main/instructions/ready.gif)

---
## uninstall virtual environment

1. To unsintall the **venv**, run [`uninstall.ps1`](uninstall.ps1) in your powershell terminal.

```{ps}
.\uninstall.ps1
```