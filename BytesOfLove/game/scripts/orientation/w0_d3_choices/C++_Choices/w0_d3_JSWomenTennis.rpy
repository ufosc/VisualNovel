label w0_d3_JSWomenTennis:
    mc "\"Maybe a class on the history of women’s tennis.\""
    mc "\"Tennis has always been an interest of mine,\""
    mc "\"And I don’t think the great female tennis players get talked about enough...\""
    js "\"OMG, I totally agree!\""
    js "\"I actually played tennis in high school, so I love tennis.\""

    menu w0_d3_FavoriteTennisPlayer:
        js "\"Who's your favorite player??\""

        "Steffi Graf":
            $ js_rep = reputation(js_rep,affection_change)
            mc "\"Steffi Graf, for sure!\""
            mc "\"She is one of the greatest of all time.\""
            js "\"Oh yea, I do like her.\""
            js "\"Personally, I am a Serena Williams fan.\""
            js "\"Her dominance and longevity is unmatched.\""
            mc "\"Fair enough, I definitely think she’s the GOAT.\""
            mc "\"But Graf is still one of my favorites.\""
            js "\"And also-\""
            c "\"Hey, can you guys be quiet?\""
            c "\"I am trying to hear what the breakout leader is saying,\""
            c "\"And you guys have been talking the entire time.\""
            mc "\"Sorry!\""

        "Billie Jean King":
            $ js_rep = reputation(js_rep,affection_change)
            mc "\"Billie Jean King, for sure!\""
            mc "\"She is one of the greatest of all time.\""
            mc "\"And I loved seeing Emma Stone play her in ‘Battle of the Sexes’.\""
            js "\"Oh yea, I do like her.\""
            js "\"Personally I am a Serena Williams fan.\""
            js "\"Her dominance and longevity is unmatched.\""
            mc "\"Fair enough, I definitely think she’s the GOAT.\""
            mc "\"But Jean is still one of my favorites.\""
            js "\"And also-\""
            c "\"Hey, can you guys be quiet?\""
            c "\"I am trying to hear what the breakout leader is saying,\""
            c "\"And you guys have been talking literally the whole time.\""
            mc "\"Sorry!\""

        "Ada Lovelace":
            $ js_rep = reputation(js_rep,-affection_change)
            mc "\"Ada Lovelace, for sure!\""
            mc "\"She is one of the greatest of all time.\""
            js "\"Hm, I’m not sure I know her...\""
            js "\"Are you sure that-\""
            c "\"Hey, first of all you guys are being so loud, so you need to be quiet.\""
            c "\"Second, Ada Lovelace isn’t even a tennis player...\""
            c "\"She was one of the first female programmers.\""
            c "\"Lovelace is most famous for her work on Babbage’s Analytical Engine.\""
            c "\"A lot of people consider her to be the first programmer.\""
            js "{i}*Quieter than before*{/i} \"Oh, wow. I had no idea.\""
            js "\"That is pretty interesting, I love hearing about the great women of history.\""
            mc "\"Oh yeah, she is amazing.\""
            mc "\"I have always been a big fan of hers.\""
            js "\"Wait, didn’t you think she was a tennis player?\""
            mc "\"Uhhhh...\""
            mc "\"Is that what happened?\""
            mc "\"I’m not sure I remember that...\""
            js "\"Yep, that is definitely what you said!\""
            js "\"And then you tried to pretend that you knew she was the first programmer!\""
            js "\"So first you lied about liking women’s tennis,\""
            js "\"Then you lied about knowing who Lovelace was!\""

            menu w0_d3_LovelaceChoice:
                mc "\"Hm, I definitely can see why you would think that...\""

                "Allow me to explain what actually happened":
                    $ js_rep = reputation(js_rep,-affection_change)
                    mc "\"But, allow me to explain what actually happened.\""
                    mc "\"...\""
                    mc "\"Okay, I thought you would interrupt me, so I actually didn’t think of anything...\""
                    mc "\"I mean I did know her name-\""
                    js "\"OMG, there’s actually no way...\""
                    c "\"Typical.\""

                "I'm sorry for lying":
                    $ js_rep = reputation(js_rep,affection_change)
                    mc "\"I’m sorry for lying about liking tennis and knowing Ada Lovelace.\""
                    mc "\"That wasn’t cool of me.\""
                    mc "\"I just wanted to be able to relate to you since I remembered you liked tennis.\""
                    js "\"Aww, it’s okay, I get it.\""
                    js "\"It was kinda funny, lol.\""

    bsl "\"Hey, can you guys be quiet back there?\""
    bsl "\"You have been talking the whole time.\""
    bsl "\"We will be going to the advising building to pick classes soon,\""
    bsl "\"So wait to talk until we leave the classroom please.\""
    mc "\"Sure, sorry.\""