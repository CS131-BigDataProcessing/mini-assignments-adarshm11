#!/bin/bash

# Activity 1

echo "\nThe time and date are: $(date)\n"

echo "Let's see who is logged into the system:\n$(who)\n"

echo "For $USER, the home directory is $HOME\n"


# Activity 2

NAME=$1
MONEY=$2

echo "My name is $NAME and I have \$$MONEY in my wallet.\n"


# Activity 3

mathvar1=$[1+5]
mathvar2=$[mathvar1*20]
mathvar3=$[10]
mathvar4=$[mathvar1*(mathvar2+mathvar3)]

echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4.\n"


# Activity 4

floating=$(echo "scale=3; 4.5/1.7" | bc)

echo "Our floating variable is $floating\n"

