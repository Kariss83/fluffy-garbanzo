# fluffy-garbanzo
# Escape game MacGyver style
This repo contains all the files you need to run a little game of running through a maze.

## Game rules

You are MacGyver and have to find a way to escape the maze.
The problem is that a guardian is at the end of it and you don't have sufficient power to kill him by hand.
Therefore you have to first pick up all items you find on the maze (seringe, plactic tube and ether) in order to put him
to sleep.
This way you'll be able to escape.

## How to run
This game have been developped to be used with python 3.7, if you run into trouble while trying to run this game make 
sure that you are running the right version of python.

### Getting the repo
First you have to install git by visiting [their website](https://git-scm.com/)

In order to get the repo you have to clone it using git :
`<git clone https://github.com/Kariss83/fluffy-garbanzo.git>`

### Preparing environment
Then you have to prepare a virtualenv in order to get the additional modules you need

#### For Unix systems
Use the following commands:
* (If you don't have yet installed virtualenv):
`<pip3 install virtualenv>`
* Initialize your virtual env:
`<virtualenv -p python3 env>`
* Activate you virtual env:
`<source env/bin/activate>`
	* Normally you should see a *(env)* at the beginning of your command line
* Install the external modules using pip
`<pip3 install -r requirements.txt>`
 
#### For windows
Use the following commands:
* (If you don't have yet installed virtualenv):
`<pip3 install virtualenv>`
* Initialize your virtual env:
`<virtualenv -p $env:python3 env>`
* Activate you virtual env:
`<.env/scripts/activate.ps1>`
	* Normally you should see a *(env)* at the beginning of your command line
* Install the external modules using pip
`<pip3 install -r requirements.txt>`
 


### Running the game
In order to run the game you have to start the file main.py with the following command:
`<python3 main.py>`

## Questions
If you have any questions or wants to contribute feel free to make a PR.

