label w0_d2_LunchFlirt:
    menu w0_d2_LunchFlirtC:
        "Flirt with Python":
            $ p_rep = reputation(p_rep, -2)

            hide cpp_happy
            show cpp_angry at right
            hide js_smirk
            show js_angry at center
            hide python_pocket_happy
            show python_angry at left
            mc "\"Especially you, Python.\""
            mc "{i}*Winks*{/i}"

            hide python_angry
            show python_angry_talk at left
            p "\"Wow, way to ruin an apology.\""
            p "\"I expected nothing less.\""

            hide python_angry_talk
            show python_angry at left
            hide cpp_angry
            show cpp_angry_talk at right
            c "\"Typical man...\""

            hide cpp_angry_talk
            show cpp_angry at right

        "Flirt with C++":
            $ c_rep = reputation(c_rep, -2)

            hide python_pocket_happy
            show python_angry at left
            hide js_smirk
            show js_angry at center
            hide cpp_happy
            show cpp_angry at right
            mc "\"Especially you, C++.\""
            mc "{i}*Winks*{/i}"

            hide cpp_angry
            show cpp_angry_talk at right
            c "\"Wow, way to ruin an apology.\""
            c "\"I expected nothing less.\""

            hide cpp_angry_talk
            show cpp_angry at right
            hide js_angry
            show js_talk at center
            js "\"What a simp...\""

            hide js_talk
            show js_angry at center

        "Flirt with JavaScript":
            $ js_rep = reputation(js_rep, -2)

            hide python_pocket_happy
            show python_angry at left
            hide cpp_happy
            show cpp_angry at right
            hide js_smirk
            show js_angry at center
            mc "\"Especially you, JavaScript.\""
            mc "{i}*Winks*{/i}"
            hide js_angry
            show js_talk
            js "\"Wow, way to ruin an apology.\""
            js "\"I expected nothing less.\""
            hide js_talk
            show js_angry at center
            hide cpp_angry
            show cpp_talk at right
            c "\"Men...\""
            hide cpp_talk
            show cpp_angry at right

        "Everyone":
            $ p_rep = reputation(p_rep, -6)
            $ js_rep = reputation(js_rep, -6)
            $ c_rep = reputation(c_rep, -6)

            hide python_pocket_happy
            show python_angry at left
            hide cpp_happy
            show cpp_angry at right
            hide js_smirk
            show js_angry at center
            mc "\"Maybe I could get to know all of you really well back at my hotel tonight...\""

            hide cpp_angry
            show cpp_angry_talk at right
            c "\"What the actual fuck is wrong with you.\""
            c "\"That is so disgusting.\""

            hide cpp_angry_talk
            show cpp_angry at right
            hide python_angry
            show python_angry_talk at left
            p "\"I can’t believe you, you are despicable.\""

            hide python_angry_talk
            show python_angry at left
            hide js_angry
            show js_talk
            js "\"I think I might actually throw up...\""

            hide js_talk
            show js_angry

    mc "\"Hmm, I thought that would go differently.\""
    mc "\"Can’t blame me, shooters gotta shoot...\""

    jump w0_d2_AfterLunch