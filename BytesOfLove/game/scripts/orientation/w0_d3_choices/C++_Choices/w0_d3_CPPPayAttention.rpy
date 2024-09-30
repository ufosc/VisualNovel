label w0_d3_CPPPayAttention:
    scene
    mc "But on the other hand, I should take classes I’m interested in, not what she’s interested in."
    mc "I guess I’ll pay attention to the recommendations."
    bsl "\"So, since it will be all of your first semester, the classes you take are very important.\""
    bsl "\"All of you should definitely try to take Introduction to Programming 1.\""
    mc "Okay, l already knew that one."
    mc "I will have the perfect schedule, nobody can stop me!"
    bsl "\"Then, along with Introduction to Programming 1, you guys will want to take Calculus 1.\""
    bsl "\"That class isn’t super challenging, but you definitely want to do it now.\""
    mc "{i}*Writing vigorously*{/i} Great, so I need to take Introduction to Programming 1 and Calculus 1."
    mc "I hope this semester isn’t too hard..."
    bsl "\"Aside from those two classes,\""
    bsl "\"There aren’t any classes that computer science students NEED to take.\""
    mc "Nice, so I basically don’t have to pay attention anymore..."
    mc "I mean maybe I should, but-"
    js "{i}*Whispers*{/i} \"Hey, [mc]!\""
    mc "{i}*Whispers*{/i} \"Hey, JavaScript.\""
    mc "\"What’s up?\""
    js "\"This is, like, SO boring.\""
    mc "\"Yeah, I get what you mean.\""
    mc "\"But I’m also sort of stressed about getting the right classes, ya know?\""
    js "\"OMG, totally.\""
    js "\"It’s like, SO stressful!\""
    js "\"This is our future, it’s kinda scary...\""
    mc "\"Yeah, but it sounds like we just need to take Introduction to Programming 1 and Calc 1.\""
    mc "\"And other than that, we can pick whatever.\""
    js "\"I wonder what other classes they will have to offer.\""
    mc "\"I hope I can take a super niche-interesting class.\""

    menu w0_d3_JSClasses:
        js "\"Oh yeah? Like what?\""

        "Maybe a class on the history of women's tennis":
            jump w0_d3_JSWomenTennis

        "Maybe a class on how to mitigate women's suffrage":
            jump w0_d3_JSWomenSuffrage

        "Maybe a class on geology":
            jump w0_d3_JSGeology

