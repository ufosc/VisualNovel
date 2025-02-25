init python:
    from renpy.display.image import Image
    from renpy.display.motion import Transform
    import random
    def click_counter():
        global click
        global start_time
        if click ==0:
            start_time = True
        click +=1


transform fish_caught:
    xalign 0.47
    yalign 1.1
    linear 5.0 yalign 0.3

screen fish_Game:
    frame:
        xsize 1920
        ysize 1080
        background "Fishing_images/Fishing_background.jpg"
    key "K_SPACE" action If(count_clicks, Function(click_counter), NullAction())
    text "Clicks: [click] Time left: [countdown]" align(.25,.25)
    if not count_clicks:
        #Placeholder images not for final product
        if 20<=click <=50:
            add Transform("Fishing_images/flopper.jpg") at fish_caught
        elif 51<=click <=100:
            add Transform("Fishing_images/shield_fish.jpg") at fish_caught
        elif 101<=click <=150:
            add Transform("Fishing_images/midas.jpg", zoom =.5) at fish_caught
        elif 151<=click <=250:
            add Transform("Fishing_images/mythic.jpg") at fish_caught
        elif click>250:
            add Transform("Fishing_images/Benjy.png") at fish_caught
        else:
            text "Noob" align(.5,.5)
    if start_time:
        timer 1.0 action If(countdown>0, SetVariable("countdown",countdown -1), SetVariable("count_clicks", False)) repeat countdown > 0
default start_time = False
default click =0
default count_clicks = True
default countdown =20

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
            textbutton "Start" action [Show("fish_Game"), Hide("instructions_Fishing")]