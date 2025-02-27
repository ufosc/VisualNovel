label w0_d2_LunchFlirt:
    menu w0_d2_LunchFlirtC:
        "Flirt with Python":
            $ p_rep = reputation(p_rep, -affection_change)
            mc "\"Especially you Python.\""
            mc "{i}Winks{/i}"
            hide python_pocket
            show python_pocket_happy at left
            p "\"Wow, way to ruin an apology.\""
            p "\"I expected nothing less.\""
            hide python_pocket_happy
            show python_pocket at left
            hide cpp_normal
            show cpp_talk at right
            c "\"Typical man...\""
            hide cpp_talk
            show cpp_normal at right
        "Flirt with C++":
            $ c_rep = reputation(c_rep, -affection_change)
            mc "\"Especially you C++.\""
            mc "{i}Winks{/i}"
            hide cpp_normal
            show cpp_talk at right
            c "\"Wow, way to ruin an apology.\""
            c "\"I expected nothing less.\""
            hide cpp_talk
            show cpp_normal at right
            hide js_normal
            show js_talk
            js "\"What a simp...\""
            hide js_talk
            show js_normal

        "Flirt with JavaScript":
            $ js_rep = reputation(js_rep, -affection_change)
            mc "\"Especially you JavaScript.\""
            mc "{i}Winks{/i}"
            hide js_normal
            show js_talk
            js "\"Wow, way to ruin an apology.\""
            js "\"I expected nothing less.\""
            hide js_talk
            show js_normal
            hide cpp_normal
            show cpp_talk at right
            c "\"Men...\""
            hide cpp_talk
            show cpp_normal at right

        "Everyone":
            $ p_rep = reputation(p_rep, -affection_change *3)
            $ js_rep = reputation(js_rep, -affection_change * 3)
            $ c_rep = reputation(c_rep, -affection_change * 3)
            mc "\"Maybe I could get to know all of you really well back at my hotel tonight...\""
            hide cpp_normal
            show cpp_talk at right
            c "\"What the actual fuck is wrong with you.\""
            c "\"That is so disgusting.\""
            hide cpp_talk
            show cpp_normal at right
            hide python_pocket
            show python_angry_talk at left
            p "\"I can’t believe you, you are despicable.\""
            hide python_angry_talk
            show python_angry at left
            hide js_normal
            show js_talk
            js "\"I think I might actually throw up...\""
            hide js_talk
            show js_normal

    mc "\"Hmm, I thought that would go differently.\""
    mc "\"Can’t blame me, shooters gotta shoot...\""

    jump w0_d2_AfterLunch
