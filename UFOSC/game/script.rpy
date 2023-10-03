#Characters
define python = Character("Python")

#Backgrounds

#Audio


# The game starts here.

label start:


    return


screen input_screen():
    window:
        has hbox


        input allow()

        input length(10)

        input default "While (numMines > 0) {
        numMines += 1
        GenerateMine()
        }"
        



