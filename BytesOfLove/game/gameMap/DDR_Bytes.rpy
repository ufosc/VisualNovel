init python:
    from renpy.display.image import Image
    from renpy.display.motion import Transform
    import time
    import random

    # Global game variables
    target_time = 3.8  # Base target time for block interaction
    block_creation_count = 0
    max_block_creation = 10  # Adjusted per difficulty
    gameScore = 0  # Track player score

    # RhythmBlock class definition
    class RhythmBlock:
        def __init__(self, image_path, x, y, speed, transform_name, zoom):
            self.sprite = Image(image_path)
            self.x = x
            self.y = y
            self.speed = speed
            self.transform_name = transform_name
            self.zoom = zoom
            self.hit = False
            self.start_time = time.time()

        @staticmethod
        def difficultyRating(level):
            global target_time, max_block_creation, block_speed, blockrepition

            # Base values for the Easy difficulty
            base_target_time = 3.8
            base_max_blocks = 10
            base_speed = 5
            base_rep_time = 2

            if level == "Easy":
                target_time = base_target_time
                max_block_creation = base_max_blocks
                block_speed = base_speed
                blockrepition = base_rep_time

            elif level == "Medium":
                target_time = base_target_time * 0.8  # 20% faster
                max_block_creation = int(base_max_blocks * 1.2)
                block_speed = base_speed * 1.2
                blockrepition = base_rep_time * 0.6

            elif level == "Hard":
                target_time = base_target_time * 0.6  # 40% faster
                max_block_creation = int(base_max_blocks * 1.5)
                block_speed = base_speed * 1.5
                blockrepition = base_rep_time * 0.3

            else:
                raise ValueError("Invalid difficulty level. Choose 'Easy', 'Medium', or 'Hard'.")

        def get_elapsed_time(self):
            """Calculate the elapsed time since block creation."""
            return time.time() - self.start_time

        def check_hit_timing(self, target_time): 
            """Check if the block is hit within an acceptable time window."""
            time_difference = abs(self.get_elapsed_time() - target_time)
         
            if self.hit:
                return "already_hit"
            if time_difference <= 0.3:
                self.hit = True
                return "perfect"
            elif time_difference <= 0.6:
                self.hit = True
                return "good"
            elif time_difference <= 0.9:
                self.hit = True
                return "bad"
            else:
                return "missed"

    # Subclasses for different block types
    class BurgerBlock(RhythmBlock):
        def __init__(self, x, y, speed):
            super().__init__("DDR_images/burger.png", x, y, speed, move_arrow_1, 0.15)

    class FriesBlock(RhythmBlock):
        def __init__(self, x, y, speed):
            super().__init__("DDR_images/Fries.png", x, y, speed, move_arrow_2, 0.15)

    class SodaBlock(RhythmBlock):
        def __init__(self, x, y, speed):
            super().__init__("DDR_images/Soda.png", x, y, speed, move_arrow_3, 0.15)

    class TendiesBlock(RhythmBlock):
        def __init__(self, x, y, speed):
            super().__init__("DDR_images/tendies.png", x, y, speed, move_arrow_4, 0.12)

    # List to hold active blocks
    active_blocks = []
    block_classes = [BurgerBlock, FriesBlock, SodaBlock, TendiesBlock]

    def random_block_order():
        """Generate and append a random block if creation limit has not been reached."""
        global block_creation_count, max_block_creation, block_speed

        if block_creation_count < max_block_creation:
            chosen_block = random.choice(block_classes)(1100, -50, block_speed)
            active_blocks.append(chosen_block)
            block_creation_count += 1

    def log_key_press(block_name, elapsed_time):
        """Log key press times for debugging purposes."""
        print(f"[DEBUG] Key pressed for {block_name} at {elapsed_time:.2f} seconds after block creation.")

    def handle_block_hit(block_type, target_time): # will need to be modifyed so that it removes the renpy.notify and creates image popups of perfect, good, bad, etc.
        """Register block hits and update the score."""
        global gameScore
        matching_blocks = [block for block in active_blocks if isinstance(block, block_type) and not block.hit]
        if matching_blocks:
            block = matching_blocks[-1]
            elapsed_time = block.get_elapsed_time()
            log_key_press(block.__class__.__name__, elapsed_time)
            result = block.check_hit_timing(target_time)

            if result == "perfect":
                renpy.notify("Perfect!")
                gameScore += 10
            elif result == "good":
                renpy.notify("Good!")
                gameScore += 5
            elif result == "bad":
                renpy.notify("Bad!")
                gameScore += 1
            elif result == "missed":
                renpy.notify("Missed!")
            else:
                renpy.notify("Already hit!")
        
        else:
            renpy.notify(f"No {block_type.__name__} blocks to hit!")



    def sprite_manager(image, xpos, ypos, zoom=1.0):
        """Return a Transform with given image and attributes."""
        return Transform(image, xpos=xpos, ypos=ypos, zoom=zoom)

# Transform definitions
transform move_arrow_1:
    xalign 0.425
    linear config.screen_height / 800.0 * target_time yalign 1.5
    repeat

transform move_arrow_2:
    xalign 0.515
    linear config.screen_height / 800.0 * target_time yalign 1.5
    repeat

transform move_arrow_3:
    xalign 0.6
    linear config.screen_height / 800.0 * target_time yalign 1.5
    repeat

transform move_arrow_4:
    xalign 0.68
    linear config.screen_height / 800.0 * target_time yalign 1.5
    repeat



# Screens for the game
screen instructions_DDR:
    frame:
        xsize 800
        ysize 700
        align (0.5, 0.5)
        background "#333333"
        padding (20, 20)
        vbox:
            null height 10
            spacing 20
            text "Welcome to the DDR-style Rhythm Game!" color "#FFFFFF" size 40
            text "Instructions:" color "#FFFFFF" size 30
            for instruction in [
                "1. Watch as blocks fall from the top of the screen.",
                "2. Press the corresponding arrow keys when the blocks reach the target zone.",
                "3. Hit the keys with perfect timing to score the most points!",
                "4. Try to score as many points as you can."
            ]:
                text instruction color "#FFFFFF" size 25
            null height 20
            text "Choose your difficulty:" color "#FFFFFF" size 30 align (0.5, 0.5)
        
            null height 20
            hbox:
                spacing 100
                align((0.5, 0.5))
                textbutton "Easy" action [Function(RhythmBlock.difficultyRating, "Easy"), Hide("instructions_DDR"), Show("DDRgame")]
                textbutton "Medium" action [Function(RhythmBlock.difficultyRating, "Medium"), Hide("instructions_DDR"), Show("DDRgame")]
                textbutton "Hard" action [Function(RhythmBlock.difficultyRating, "Hard"), Hide("instructions_DDR"), Show("DDRgame")]

screen DDRgame:
    frame:
        xsize 1920
        ysize 1000
        background "map_images/Food_bytes#2.jpg"
        add sprite_manager("DDR_images/scaleBackground.png", 90, -5)
        for xpos in [1100, 950, 800, 650, 500]:
            add sprite_manager("DDR_images/straight-line.png", xpos, -50)

        for block in active_blocks:
            add block.sprite at block.transform_name zoom block.zoom

        text "Score: [gameScore]" xpos 20 ypos 20 color "#FFFFFF" size 40

        for xpos in [760, 915, 1065, 1215]:
            add sprite_manager("DDR_images/zone.png", xpos, 900, zoom=0.10)

        key "K_LEFT" action Function(handle_block_hit, BurgerBlock, target_time)
        key "K_UP" action Function(handle_block_hit, FriesBlock, target_time)
        key "K_DOWN" action Function(handle_block_hit, SodaBlock, target_time)
        key "K_RIGHT" action Function(handle_block_hit, TendiesBlock, target_time)

        if block_creation_count >= max_block_creation:
            timer 6.0 action Show("score_results", transition=dissolve, layer="overlay")

    timer blockrepition action Function(random_block_order) repeat True

screen score_results:
    frame:
        xsize 1000
        ysize 1000
        align (0.5, 0.5)
        background "#333333"
        padding (20, 20)
        vbox:
            spacing 20
            align (0.5, 0.5)
            text "Final Score: [gameScore]" color "#FFFFFF" size 40 align (0.5, 0.5)
            text "Thank you for playing!" color "#FFFFFF" size 30 align (0.5, 0.5)
            textbutton "Leave" action [Hide('score_results'), Show('overviewMap')] align (0.5, 0.5)
