# Pytest Project for Python Gently Explained Exercises

![Python Version](https://img.shields.io/badge/Python-3.7-green)
![Pytest Version](https://img.shields.io/badge/Pytest-7.1.2-green)

Setting up a Python project for Al Sweigart's exercises
[Python Programming Exercises, Gently Explained](https://inventwithpython.com/pythongently/).

## Project Setup

If you don't have already you need to install **Python >= 3.7** and set up a 
virtual environment. This can be done with Python's `venv` command.

After you cloned the repository, use `cd` to navigate to the directory
containing this repository. Then you can start creating your virtual
environment.

### Virtual Environment

Run the following commands inside the directory containing this repository to
create and activate the virtual environment.

#### Create the virtual environment with name `gently_explained`

On **Windows**
```bat
C:\...> python -m venv gently_explained
```

---

On **Linux/macOS**
```bash
$ python -m venv gently_explained
```

#### Activate the virtual environment after creation

After activation you will see `(gently_explained)` in front of the prompt on
the command line to indicate that you are in the virtual environment.

On **Windows**
```bat
C:\...> %cd%\gently_explained\Scripts\activate.bat
```

---

On **Linux/macOS**
```bash
$ source gently_explained/bin/activate
```

#### Deactivate the virtual environment after you are finished

On **Windows**
```bat
(gently_explained) C:\...> deactivate
```

---

On **Linux/macOS**
```bash
(gently_explained) $ deactivate 
```

#### Install required packages

After you activate the virtual environment run the following command to
install all required packages:

On **Windows**
```bat
(gently_explained) C:\...> pip install -r requirements.txt
```

---

On **Linux/macOS**
```bash
(gently_explained) $ pip install -r requirements.txt
```

This will install all required packages into your virtual environment.

## Run Pytest

Now you are all set to solve the exercises.
You can run the unit tests for each exercise by calling the corresponding
unit test script with `pytest`.

On **Windows**
```bat
(gently_explained) C:\...> pytest tests\test_<exercise>.py
```

---

On **Linux/macOS**
```bash
(gently_explained) $ pytest tests/test_<exercise>.py
```

Simply replace `<exercise>` with the name of the exercise script you are working with.
