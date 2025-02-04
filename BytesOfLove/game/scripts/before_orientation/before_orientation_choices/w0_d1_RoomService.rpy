label w0_d1_RoomService:
    mc "I know, I’ll get room service."
    mc "Nothing beats having fresh food delivered, without the pain of cleaning up afterwards."
    mc "{i}*Looks at the menu*{/i}"

    menu w0_d1_RoomServiceOrder:
        mc "I don’t even know what I want, there are so many options..."

        "Burger":
            $ food_item = "a burger"

        "Mac and Cheese":
            $ food_item = "the mac and cheese"

        "Chicken Fingers":
            $ food_item = "the chicken fingers"
            
        "Pizza":
            $ food_item = "a pizza"

    mc "Yeah, I HAVE to get [food_item]. You can’t go wrong with that."
    $ byte = bytecoin(byte, -15)
    scene hotel_room_night with shorter_fade
    "{i}*5 minutes pass*{/i}"
    mc "I hope this doesn’t take too long, I’m getting pretty hungry here."
    "{i}*You hear a knock on the door*{/i}"
    mc "Oh, thank god."
    "{i}*Opens door*{/i}"
    mc "\"Thanks man, that was fast!\""

jump w0_d1_End
