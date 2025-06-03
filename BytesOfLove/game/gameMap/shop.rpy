default cache_cleaner_count = 0
default bought_charm_compiler = False
default bought_cache_cleaner = False
default bought_syntax_spray = False

label shop:
    "Welcome to the Likeability Shop! What would you like to buy?"

    menu:
        "Charm Compiler (+10 to C, Python, Java | -10 Bytecoin)":
            if byte >= 10:
                $ byte -= 10
                $ c_rep = min(c_rep + 10, 100)
                $ p_rep = min(p_rep + 10, 100)
                $ j_rep = min(j_rep + 10, 100)
                $ bought_charm_compiler = True
                "You bought a Charm Compiler!"
            else:
                "You don't have enough Bytecoin."

        "Cache Cleaner (+20 to Java, C | -15 Bytecoin, max 3)":
            if byte >= 15 and cache_cleaner_count < 3:
                $ byte -= 15
                $ j_rep = min(j_rep + 20, 100)
                $ c_rep = min(c_rep + 20, 100)
                $ cache_cleaner_count += 1
                $ bought_cache_cleaner = True
                "You bought a Cache Cleaner!"
            elif cache_cleaner_count >= 3:
                "You've already bought 3 Cache Cleaners."
            else:
                "You don't have enough Bytecoin."

        "Syntax Sugar Spray (+5 to JS, Python, Rust | -5 Bytecoin)":
            if byte >= 5:
                $ byte -= 5
                $ js_rep = min(js_rep + 5, 100)
                $ p_rep = min(p_rep + 5, 100)
                $ r_rep = min(r_rep + 5, 100)
                $ bought_syntax_spray = True
                "You bought Syntax Sugar Spray!"
            else:
                "You don't have enough Bytecoin."

        "Leave Shop":
            jump after_shop

    jump shop 

label after_shop:
    "Thanks for visiting the shop!"
    Return()
