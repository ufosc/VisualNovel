init python:
    from renpy.display.image import Image
    from renpy.display.motion import Transform
    import random

    class Fish:
        def __init__(self, image_path, x, y, zoom, transform):
            self.image = Image(image_path)
            self.x = x
            self.y = y
            self.zoom = zoom
            self.transform = transform

        def get_transform(self):
            return Transform(self.image, xalign=0.0, ypos=self.y, zoom=self.zoom)

    
    # Generate multiple fish dynamically
    fish_list = []
    def spawn_fish():
        if random.randint(1, 2) == 1:
            img = "Fishing_images/Fish_right.png"
            transform = left_to_right
        else:
            img = "Fishing_images/Fish_left.png"
            transform = right_to_left
        fish_list.append(Fish(img, 0, random.randint(400, 900), 0.5, transform))

# Transforms for fish
transform left_to_right:
    xalign -0.2
    linear 6.0 xalign 1.2

transform right_to_left:
    xalign 1.2
    linear 6.0 xalign -0.2

screen fish_Game:
    frame:
        xsize 1920
        ysize 1080
        background "Fishing_images/Fishing_background.jpg"
        if (len(fish_list) < 21):
            timer 2 action Function(spawn_fish) repeat True
        for fish in fish_list:
                add fish.get_transform() at fish_caught
                

screen instructions_Fishing:
    frame:
        xsize 800
        ysize 700
        align (0.5, 0.5)
        background "#333333"
        padding (20, 20)
        vbox:
            null height 10
            spacing 20
            text "Welcome to the Fishing Game!" color "#FFFFFF" size 40
            text "Instructions:" color "#FFFFFF" size 30
            for instruction in [
                "1. Use your mouse to control the fishing rod.",
                "2. Catch the fish that swim across the screen.",
                "3. Avoid catching non-fish",
                "4. Try to score as many points as you can."
            ]:
                text instruction color "#FFFFFF" size 25
            null height 20
            textbutton "Start" action [Show("fish_Game")]
        
        

