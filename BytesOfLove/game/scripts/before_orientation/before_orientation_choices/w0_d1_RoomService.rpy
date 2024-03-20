label w0_d1_RoomService:
    mc "I know, I will get room service, nothing beats hotel room service."
    mc "People bring me fresh hot food, and I don't even have to do dishes."

    menu w0_d1_RoomServiceOrder:
        mc "*Looking at menu* Well I don't even know what I want, there are so many options…"

        "Burger":
            $ food_item = "burger"

        "Mac and Cheese":
            $ food_item = "mac and cheese"

        "Chicken Fingers":
            $ food_item = "chicken fingers"
            
        "Pizza":
            $ food_item = "pizza"

    mc "Yeah, I HAVE to get [food_item], you can't go wrong with that."
    scene w0_d1_hotel with shorter_fade
    "*5 minutes pass*"
    mc "I hope this doesn't take too long I am getting pretty hungry here."
    "*Knock on door*"
    mc "Oh man, thank goodness."
    "*Opens door*"
    mc "Thank you man, that was so fast!"

jump w0_d1_End
