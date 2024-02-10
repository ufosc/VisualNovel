# This will be a template for how further script development will be implemented

# All primarily dialogue files will be stored in the "scripts" directory

# As of this current plan. We will be breaking the script up in chronological order, each week will have its own folder
#with each day being a .rpy file.

# This file will mark the very start of the Bytes of Love story

# As long as any script file has the .rpy extension, you can jump to any label in the script

#Here I create a label "begin"
label begin:
    "this is dialogue from the narrator"

    "[mc]" "this is dialogue from the player character"

    c "this is dialogue from the character C++"

    jump nextWeek #this jump statement will take the game state and move it to the "nextWeek" label in "w1_d1" in the "week1" folder

    return