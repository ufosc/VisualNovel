label w0_d3_JSWomenSuffrage:
    $ js_rep = reputation(js_rep,-affection_change)

    hide js_talk
    show js_normal
    mc "\"Maybe a class on how to mitigate women’s suffrage.\""
    mc "\"I am very passionate about the issues women face,\""
    mc "\"And I hate to hear that they are still suffering...\""

    hide js_normal
    show js_talk
    js "\"Oh, really?\""
    js "\"Are you sure you aren’t just saying that because you think it’ll impress me?\""

    hide js_talk
    show js_normal
    mc "\"Nope! I really am against women’s suffrage!\""
    mc "\"You won’t find many guys like me...\""

    hide js_normal
    show js_normal at left
    show cpp_angry_talk at right with dissolve
    c "\"Oh. My. God.\""
    c "\"...Do you NOT know what suffrage means?\""

    hide cpp_angry_talk
    show cpp_angry at right
    mc "\"Uhhh, what do YOU think it means?\""

    hide cpp_angry
    show cpp_angry_talk at right
    c "\"Suffrage is a group of people’s right to vote.\""
    c "\"So when you say that you want to mitigate women’s suffrage...\""

    menu w0_d3_WomenSuffrageDecision:
        c "\"You are really saying that you don’t want women to vote.\""

        "Double Down":
            $ js_rep = reputation(js_rep,-affection_change)
            $ c_rep = reputation(c_rep,-affection_change)

            hide cpp_angry_talk
            show cpp_angry at right
            hide js_normal
            show js_angry at left
            mc "\"That’s exactly what I want!\""
            mc "\"I’m glad we’re on the same page now.\""
            mc "\"And you know what else? I think that-\""

        "Admit your mistake":
            $ js_rep = reputation(js_rep,affection_change)

            hide cpp_angry_talk
            show cpp_angry at right
            mc "\"Ohhhh, I didn’t realize that.\""

            hide js_normal
            show js_smirk at left
            hide cpp_angry
            show cpp_normal at right
            mc "\"I was wondering why people looked at me weird when I said that before...\""

            hide js_smirk
            show js_blush at left
            js "\"LMAO\""

            hide cpp_normal
            show cpp_happy at right
            c "\"You’re so stupid...\""
            hide js_blush
            show js_smirk at left

    show bsl_normal with dissolve
    show bsl_talk
    bsl "\"Hey, can you guys be quiet back there?\""
    bsl "\"You have been talking the whole time.\""
    bsl "\"We will be going to the advising building to pick classes soon,\""
    bsl "\"So wait to talk until we leave the classroom please.\""
    hide bsl_talk
    show bsl_normal
    mc "\"Sure, sorry.\""
    jump w0_d3_Registration