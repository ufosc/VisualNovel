label w0_d3_JSGeology:
    hide js_talk
    show js_smirk
    mc "\"Maybe a class on geology.\""
    mc "\"Rocks fascinated me as a kid,\""
    mc "\"Not enough to major in it, but I would love to learn more.\""
    hide js_smirk
    show js_talk

    menu w0_d3_GeologyChoice:
        js "\"Really what got you interested in them?\""

        "I got a really close look at one when I was a kid":
            hide js_talk
            show js_smirk
            mc "\"When I was a little kid I was playing soccer with my friend one day.\""
            mc "\"We didn’t have a ball so we were playing with a rock,\""
            mc "\"And one thing led to another and the next thing I knew the rock was flying at my face.\""
            
            hide js_smirk
            show js_talk
            js "\"Oh my god!\""
            js "\"Are you okay? What happened?\""

            hide js_talk
            show js_smirk
            mc "\"I woke up in the hospital holding the rock.\""
            mc "\"So, I had a lot of time to look at it.\""
            mc "\"And ever since then, I’ve been fascinated by them.\""

            hide js_smirk
            show js_talk
            js "\"Wow! That is such a crazy story!\""

            hide js_talk
            show js_smirk
            mc "\"Some of my friends say that I was never the same after the accident,\""
            mc "\"But personally, I think I’ve always been this dumb.\""

            hide js_smirk
            show js_blush
            js "\"Hahahaha!\""
            js "\"[mc], you’re so funny!\""
            hide js_blush
            show js_normal

        "My dad is a geologist":
            hide js_talk
            show js_smirk
            mc "\"My dad is a geologist, so I guess his passion kinda rubbed off on me.\""
            mc "\"He was always talking about his work and telling me all kinds of facts.\""
            mc "\"He’s the best.\""

            hide js_smirk
            show js_talk
            js "\"So you could say...\""
            hide js_talk
            show js_smirk

            menu w0_d3_JavaScriptJoke:
                js "\"He {i}rocks{i}?\""

                "Laugh at the joke":
                    $ js_rep = reputation(js_rep,affection_change)

                    mc "{i}*Laughs*{/i} \"Why have I never thought of that?\""
                    mc "\"You’re really funny, you know that?\""

                    hide js_smirk
                    show js_blush
                    js "{i}*Smiles*{/i} \"Thank you, [mc], you’re a good guy.\""
                    hide js_blush
                    show js_normal

                "Don't laugh at the joke":
                    $ js_rep = reputation(js_rep,-affection_change)

                    hide js_smirk
                    show js_angry
                    mc "\"That was horrible.\""
                    mc "\"You’re trying too hard to be funny, JavaScript.\""

                    hide js_angry
                    show js_talk
                    js "\"You just don’t know how to be nice, do you?\""

                    hide js_talk
                    show js_angry
                    mc "\"I’m just being honest.\""
                    mc "\"Would you rather me just pretend you’re funny?\""

                    hide js_angry
                    show js_talk
                    js "\"Are you just intentionally trying to piss me off?\""
                    js "\"You could just be nice for a change.\""
                    js "\"I hope all your stupid rock classes are full.\""
                    hide js_talk
                    show js_angry

        "I really like Hank from Breaking Bad":

            hide js_talk
            show js_smirk
            mc "\"So I watched Breaking Bad back in high school.\""
            mc "\"And there is this character named Hank, who really likes rocks.\""
            mc "\"Or, minerals, I should say...\""
            mc "\"He collects them, and I thought that was really interesting,\""
            mc "\"So now it’s a passion of mine too.\""

            hide js_smirk
            show js_talk
            js "\"Wow, that is so cool!\""
            js "\"I didn’t know that was a part of Breaking Bad...\""
            js "\"I thought it was just about making meth and stuff.\""

            hide js_talk
            show js_smirk
            mc "\"That technically is the plot, but the story encapsulates so much more than that.\""
            mc "\"I would highly recommend you watch it.\""
            hide js_smirk
            show js_talk

            menu w0_d3_JSOnePiece:
                js "\"Ah, I would but I am pretty committed to watching One Piece right now.\""

                "One Piece? I prefer two piece swimsuits":
                    $ js_rep = reputation(js_rep,-affection_change)

                    hide js_talk
                    show js_angry
                    mc "\"One piece? I prefer watching girls in two piece swimsuits...\""

                    hide js_angry
                    show js_talk
                    js "\"One Piece is an anime, idiot!\""
                    js "\"All you think about is girls!\""
                    hide js_talk
                    show js_angry

                "I've never heard of One Piece":
                    hide js_talk
                    show js_smirk
                    mc "\"Huh, I’ve never heard of One Piece, what is it-\""
                    hide js_smirk
                    show js_normal

    hide js_normal
    show js_normal at left
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