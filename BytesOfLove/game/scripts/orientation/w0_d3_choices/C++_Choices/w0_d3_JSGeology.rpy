label w0_d3_JSGeology:
    mc "\"Maybe a class on geology.\""
    mc "\"Rocks fascinated me as a kid,\""
    mc "\"Not enough to major in it, but I would love to learn more.\""

    menu w0_d3_GeologyChoice:
        js "\"Really what got you interested in them?\""

        "I got a really close look at one when I was a kid":
            mc "\"When I was a little kid I was playing soccer with my friend one day.\""
            mc "\"We didn’t have a ball so we were playing with a rock,\""
            mc "\"And one thing led to another and the next thing I knew the rock was flying at my face.\""
            js "\"Oh my god!\""
            js "\"Are you okay? What happened?\""
            mc "\"I woke up in the hospital holding the rock.\""
            mc "\"So, I had a lot of time to stare at it.\""
            mc "\"And ever since then, I’ve been fascinated by them.\""
            js "\"Wow! That is such a crazy story!\""
            mc "\"Some of my friends say that I was never the same after the accident,\""
            mc "\"But personally, I think I’ve always been this dumb.\""
            js "\"Hahahaha!\""
            js "\"[mc] you’re so funny!\""

        "My dad is a geologist":
            mc "\"My dad is a geologist, so I guess his passion kinda rubbed off on me.\""
            mc "\"He was always talking about his work and telling me all kinds of facts.\""
            mc "\"He’s the best.\""
            js "\"So you could say...\""

            menu w0_d3_JavaScriptJoke:
                js "\"He rocks?\""

                "Laugh at the joke":
                    $ js_rep = reputation(js_rep,affection_change)
                    mc "{i}*Laughs*{/i} \"Why have I never thought of that?\""
                    mc "\"You’re really funny, you know that?\""
                    js "{i}*Smiles*{/i} \"Thank you, [mc], you’re a good guy.\""

                "Don't laugh at the joke":
                    $ js_rep = reputation(js_rep,-affection_change)
                    mc "\"That was horrible.\""
                    mc "\"You’re trying too hard to be funny, JavaScript.\""
                    js "\"You just don’t know how to be nice, do you?\""
                    mc "\"I’m just being honest.\""
                    mc "\"Would you rather me just pretend you’re funny?\""
                    js "\"Are you just intentionally trying to piss me off?\""
                    js "\"You could just be nice for a change.\""
                    js "\"I hope all your stupid rock classes are full.\""

        "I really like Hank from Breaking Bad":
            mc "\"So I watched Breaking Bad back in high school.\""
            mc "\"And there is this character named Hank, who really likes rocks.\""
            mc "\"He collects them, and I thought that was really interesting,\""
            mc "\"So now it’s a passion of mine too.\""
            js "\"Wow, that is so cool!\""
            js "\"I didn’t know that was a part of Breaking Bad...\""
            js "\"I thought it was just about making meth and stuff.\""
            mc "\"That technically is the plot, but the story encapsulates so much more than that.\""
            mc "\"I would highly recommend you watch it.\""

            menu w0_d3_JSOnePiece:
                js "\"Ah, I would but I am pretty committed to watching One Piece right now.\""

                "One Piece? I prefer two piece swimsuits":
                    $ js_rep = reputation(js_rep,-affection_change)
                    mc "\"One piece? I prefer watching girls in two piece swimsuits...\""
                    js "\"One Piece is an anime, idiot!\""
                    js "\"All you think about is girls!\""

                "I've never heard of One Piece":
                    mc "\"Huh, I’ve never heard of One Piece, what is it-\""

    bsl "\"Hey, can you guys be quiet back there?\""
    bsl "\"You have been talking the whole time.\""
    bsl "\"We will be going to the advising building to pick classes soon,\""
    bsl "\"So wait to talk until we leave the classroom please.\""
    mc "\"Sure, sorry.\""