label w0_d3_JSWomenSuffrage:
    $ js_rep = reputation(js_rep,-2)
    mc "\"Maybe a class on how to mitigate women’s suffrage.\""
    mc "\"I am very passionate about the issues women face,\""
    mc "\"And I hate to hear that they are still suffering...\""
    js "\"Oh, really?\""
    js "\"Are you sure you aren’t just saying that because you think it’ll impress me?\""
    mc "\"Nope! I really am against women’s suffrage!\""
    mc "\"You won’t find many guys like me\""
    c "\"Oh. My. God.\""
    c "\"...Do you not know what suffrage means?\""
    mc "\"Uhhh, what do YOU think it means?\""
    c "\"Suffrage is a group of people’s right to vote.\""
    c "\"So when you say that you want to mitigate women’s suffrage...\""

    menu w0_d3_WomenSuffrageDecision:
        c "\"You are really saying that you don’t want women to vote.\""

        "Double Down":
            $ js_rep = reputation(js_rep,-2)
            $ c_rep = reputation(c_rep,-2)
            mc "\"That’s exactly what I want!\""
            mc "\"I’m glad we’re on the same page now.\""
            mc "\"And you know what else? I think that-\""

        "Admit your mistake":
            $ js_rep = reputation(js_rep,2)
            mc "\"Ohhhh, I didn’t realize that.\""
            mc "\"I was wondering why people looked at me weird when I said that before...\""
            js "\"LMAO\""
            c "\"You’re so stupid...\""

    bsl "\"Hey, can you guys be quiet back there?\""
    bsl "\"You have been talking the whole time.\""
    bsl "\"We will be going to the advising building to pick classes soon,\""
    bsl "\"So wait to talk until we leave the classroom please.\""
    mc "\"Sure, sorry.\""