# Transitions
define fadehold = Fade(0.5, 1.0, 0.5)

# Characters
define r = Character("Rust")
define p = Character("Python")
define c = Character("C++")
define j = Character("Java")
define u = Character("???")

# Backgrounds
image bg lecturehall = "backgrounds/bg lecturehall.jpg"
image bg black = "backgrounds/bg black.jpg"

# Screens
image mine_sweeper = "images/mine_sweeper.png"

#Audio

# The game starts here.

label start:
    # PROLOUGUE

    "Welcome to Bytes of Love! A visual novel currently being developed by the University of Florida's Open Source Club!"
    "This is an educational dating simulator where you romance programming languages that are represented as anime-style characters while learning about multiple programming languages."
    "If you have any questions or comments about the project, please reach out to anyone in the \"Maintainers\" section of the GitHub!"
    
    $ mc = renpy.input("Your name: ").strip()

    "Your name is [mc]."

    jump w0_d1
