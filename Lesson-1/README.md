# Lesson-1

This lesson talks about managing python environments. We talk about two approaches in this lesson:

1. Using Docker containers
2. Using Virtual Environment

Sample code for both these approach is same.
The code does nothing but displays custom messages based on python version.

## Video tutorial
You can watch the working example of the lesson on youtube:

[Lesson-1: Part 1](https://www.youtube.com/watch?v=QG84l1yMh-s&t=43s)

[Lesson-1: Part 2](https://www.youtube.com/watch?v=FSLr4ZJIUco&t=10s)


# 1. Working with Python Docker Container

## Problems addressed

What problems are we addressing here:

1. Suppose you want to work on a python project with python version 3 but do not want to install/upgrade python on your machine
2. You want a use and throw environment where you are just checking a python code (to check its compatibility with a certain python version). For this you do not want to install multiple python version on your machine and its required dependencies.
3. You are learning python, using python for experimentation purpose.

The solution to all these problems is docker containers. Docker containers help you to create a throwable virtual environment where you can run your applications without installing python or any required dependency on your machine.

## Running a docker container

**Prerequisites:** 

Docker should be installed on your machine, if you don't have it, download it from [Docker site](https://www.docker.com/) and follow the instructions for your OS.

**Command:**

`docker run --it --name my-python-app -v "$(pwd)":/root/ python:3 /bin/bash`

Arguments explained:

`run` : Finds a docker image on your machine, if not available, downloads it from [Docker Hub](https://hub.docker.com/) and then run a container from that image.

`--it` : Start container in an interactive Bash session (/bin/bash)

`--name` : name of your container

`-v` : Volume to be mounted from your Host machine to your container

**python:3** : is the name of the image followed by tag (python version 3.6.1 is currently tagged as 3)

To exit from container:


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