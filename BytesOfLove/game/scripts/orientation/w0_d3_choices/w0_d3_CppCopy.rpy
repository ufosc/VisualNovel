label w0_d3_CppCopy:
    show cpp_normal at left
    show python_pocket at right
    mc "\"Definitely no reason to stress myself out, C++ will have me covered.\""
    mc "\"You know, I’m actually getting kind of sleepy…\""

    scene breakout_room with longer_fade

    hide cpp_normal
    hide python_pocket
    show python_pocket_happy
    p "\"HEY, [mc]!\"" with hpunch
    p "\"Are you coming? Everyone is going to the administrative building to pick their classes.\""

    hide python_pocket_happy
    show python_pocket
    mc "{i}Sleepy and confused.{/i} \"Woah, what happened?\""
    mc "\"I swear I was listening to the breakout leader talk about Calc 1, and that’s the last thing I remember…\""
    
    hide python_pocket
    show python_pocket_happy
    p "\"Yeah, you fell asleep like 20 minutes ago, LOL.\""
    p "\"JavaScript was going to wake you up, but we figured you needed the sleep.\""
    p "\"We thought you might’ve had a late night again…\""
    
    hide python_pocket_happy
    show python_pocket
    mc "\"Haha, no. I fell asleep as soon as I got home last night.\""
    mc "\"I’m not sure why I’m so tired.\""
    
    hide python_pocket
    show python_pocket_happy
    p "\"Well, you said you wanted the college experience.\""
    p "\"Falling asleep in class definitely puts you on the right track.\""
    
    hide python_pocket_happy
    show python_pocket
    mc "\"Haha, you’re right, my dreams are coming true already!\""
    mc "\"Wait, where is everyone else?\""

    hide python_pocket
    show python_pocket_happy
    p "\"They left already, C++ insisted on being first in line to get her classes.\""
    p "\"And C++’s panicking made JavaScript scared, so she left too.\""

    hide python_pocket_happy
    show python_pocket
    mc "\"Well thanks for staying behind to wake me up.\""
    mc "\"Aren’t you worried about missing registration too?\""

    hide python_pocket
    show python_pocket_happy
    p "\"No, not really.\""
    p "\"I figure it will all work out, so I’m not stressing about it.\""
    p "\"With all these freshmen, there will definitely be space for everyone in Programming 1…\""

    hide python_pocket_happy
    show python_pocket
    mc "\"Wow, that is pretty chill of you, Python.\""
    mc "\"That’s a good outlook, you’re probably right.\""
    hide python_pocket
    show python_pocket_happy

    menu w0_d3_PreparingToPickClasses:
        p "\"Also, I can catch you up on what you missed while you were asleep.\""

        "Give a friendly compliment":
            $ r_rep = reputation(r_rep, int(affection_change * 0.5))
            hide python_pocket_happy
            show python_pocket
            mc "\"Also, I really like your hair today, it looks good.\""

            hide python_pocket
            show python_pocket_happy
            p "\"Thank you!\""
            p "\"I like your outfit today, you have good style.\""

            hide python_pocket_happy
            show python_pocket
            mc "{i}*Blushing*{/i} \"Thanks!\""
            mc "\"Anywho…\""
            mc "\"We should probably get going now, so that we don’t completely miss registration.\""
           
            hide python_pocket
            show python_pocket_happy
            p "\"Okay, good idea.\""

            hide python_pocket_happy with dissolve

        "Give an offensive compliment":
            $ r_rep = reputation(r_rep, int(-affection_change * 0.5))
            hide python_pocket_happy
            show python_pocket
            mc "\"Anywho…\""

            hide python_pocket
            show python_angry
            mc "\"I bet you get a lot of guys looking at you dressed like that.\""
            mc "\"I doubt there are many women on campus hotter than you.\""

            hide python_angry
            show python_angry_talk
            p "\"Uhm… thanks?\""
            p "\"We should get going.\""

            hide python_angry_talk
            show python_angry
            mc "\"Wait, did you hear what I said?\""

            hide python_angry
            show python_angry_talk
            p "\"Uh, yeah I did…\""

            hide python_angry_talk
            show python_angry
            mc "\"You’re right, we should get going.\""
            mc "\"Sorry…\""

            hide python_angry with dissolve

        "Head to registration":
            hide python_pocket_happy
            show python_pocket

            mc "\"Anywho…\""
            mc "\"We should probably get going now, so that we don’t completely miss registration.\""

            hide python_pocket
            show python_pocket_happy
            p "\"Okay, good idea.\""

            hide python_pocket_happy with dissolve

    jump w0_d3_Registration