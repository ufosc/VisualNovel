label w0_d3_CppCopy:
    mc "\"Definitely no reason to stress myself out, C++ will have me covered.\""
    mc "\"You know, I’m actually getting kind of sleepy…\""
    # insert transition to empty classroom

    p "\"HEY, [mc]!\""
    p "\"Are you coming? Everyone is going to the administrative building to pick their classes.\""
    mc "{i}Sleepy and confused.{/i} \"Woah, what happened?\""
    mc "\"I swear I was listening to the breakout leader talk about Calc 1, and that’s the last thing I remember…\""
    p "\"Yeah, you fell asleep like 20 minutes ago, LOL.\""
    p "\"JavaScript was going to wake you up, but we figured you needed the sleep.\""
    p "\"We thought you might’ve had a late night again…\""
    mc "\"Haha, no. I fell asleep as soon as I got home last night.\""
    mc "\"I’m not sure why I’m so tired.\""
    p "\"Well, you said you wanted the college experience.\""
    p "\"Falling asleep in class definitely puts you on the right track.\""
    mc "\"Haha, you’re right, my dreams are coming true already!\""
    mc "\"Wait, where is everyone else?\""
    p "\"They left already, C++ insisted on being first in line to get her classes.\""
    p "\"And C++’s panicking made JavaScript scared, so she left too.\""
    mc "\"Well thanks for staying behind to wake me up.\""
    mc "\"Aren’t you worried about missing registration too?\""
    p "\"No, not really.\""
    p "\"I figure it will all work out, so I’m not stressing about it.\""
    p "\"With all these freshmen, there will definitely be space for everyone in Programming 1…\""
    mc "\"Wow, that is pretty chill of you, Python.\""
    mc "\"That’s a good outlook, you’re probably right.\""

    menu w0_d3_PreparingToPickClasses:
        p "\"Also, I can catch you up on what you missed while you were asleep.\""

        "Give a friendly compliment":
            # affects python positively
            mc "\"Also, I really like your hair today, it looks good.\""
            p "\"Thank you!\""
            p "\"I like your outfit today, you have good style.\""
            mc "{i}Blushing{/i} \"Thanks!\""
            mc "\"Anywho…\'"
            mc "\"We should probably get going now, so that we don’t completely miss registration.\""
            p "\"Okay, good idea.\""

        "Give a bold compliment":
            #affects python negatively 
            mc "\"Anywho…\""
            mc "\"I bet you get a lot of guys looking at you dressed like that.\""
            mc "\"I doubt there are many women on campus hotter than you.\""
            p "\"Uhm… thanks?\""
            p "\"We should get going.\""
            mc "\"Wait, did you hear what I said?\""
            p "\"Uh, yeah I did…\""
            mc "\"You’re right, we should get going.\""
            mc "\"Sorry…\""

        "Head to registration":
            mc "\"Anywho…\""
            mc "\"We should probably get going now, so that we don’t completely miss registration.\""
            p "\"Okay, good idea.\""





