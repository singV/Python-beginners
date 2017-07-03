# Lesson-1

This lesson talks about managing python environments. We talk about two approaches in this lesson:

1. Using Docker containers
2. Using Virtual Environment

Sample code for both these approach is same.
The code does nothing but displays custom messages based on python version.

## Video tutorial
You can watch the working example of the lesson on youtube <Youtube video link>

# 1. Working with Python Docker Container

## Problems addressed

## Commands

## Further reading

You can further play with docker tools like Dockerfile and docker-compose. We will discuss more about these approach in our coming video series. 

# 2. Working with Python Virtual Environments

## Problem with python environments
Typical way of working on a python project is to install all the required packages using pip.
But what does the default installation does? It install all your packages in your default python's site packages. This works but has the following issues:
1. The environment is not clean for the project. i.e., if you are working on multiple projects, you have bunch of python packages installed at the same location.
2. If you try to freeze your requirements for the current project, the requirements generated will be the list of all python packages installed at your default location.
3. If multiple projects require different versions of a python package, you are in trouble.
4. If you are not logged in as admin, to install a package you have to switch user (with admin access) as pip installs python packages in your system libraries.

To overcome all these issue, virtual environment is used.

## How to use virtual environment:

1. Install virtual environment:
```
sudo pip install virtualenv
```
2. Create a new virtual environment (say venv)
```
virtualenv venv
```
3. Activate the virtual environment
```
source venv/bin/activate
```
4. Install dependencies in requirements.txt using this virtual environment
```
(venv) $ pip install -r requirements.txt
```

You are good to go!! You can check the location for any package installed, it should list the location in your virtual environment, e.g:
```
(venv) $ pytest --version
```
> This is pytest version 3.0.7, imported from /venv/lib/python2.7/site-packages/pytest.pyc
Using terminal, execute any of the project file, like:
```
(venv) $ pytest tests/
```
If you are using pyCharm IDE, you should (must actually) use this virtual environment

> from Preferences->Project Interpreter->Choose venv as project interpreter. You will see only the packages downloaded from requirements.txt are in the list of packages.

After you are done, and want to a new virtual environment, simply use the following command:
```
(venv) $ deactivate
```
This will deactivate your current virtual environment.

### Notes
1. Every time you start a bash prompt, you will have to activate the virtual environment.