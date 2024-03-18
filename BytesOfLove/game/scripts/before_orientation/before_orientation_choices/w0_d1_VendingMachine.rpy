label w0_d1_VendingMachine:
    mc "I think I will go downstairs to the vending machine, I could really go for a Snickers bar and a bag of Doritos right now."
    mc "And, I will save some money, you never know when you will need it."

    scene w0_d1_vending

    "*[mc] walks downstairs to go to find a vending machine*"

    show rust_normal at right with fade

    r "Hey there! My name is Rust! Do you go to UB?"

    menu w0_d1_Rust:
        "Mean response":
            mc "Yeah, I do, my name is [mc]."
            r "Cool, you seem chill, what's your major?"
            mc "Wouldn't you like to know…"
            
            hide rust_normal 
            show rust_angry at right with dissolve

            r "Damn, I was just wondering."
            r "I am computer science, in case you wanted to know mine."
            mc "Oh thanks, I wasn't"
            r "Jeez you don't have to be mean about it, man."
            mc "Whatever."
            hide rust_angry with dissolve
            "*Rust leaves*"

        "Nice response":
            mc "Yeah I do, my name is [mc], nice to meet you! What major are you?"
            r "*Smiles* I am a computer science major, what about you?"
            mc "Oh man, me too! I am hoping to take programming 1 this semester, are you as well?"
            r "Yes, I have some programming experience from highschool, but I am excited to start learning."
            r "We can totally work on projects and study together! It will be really cool."
            mc "Absolutely! We will probably be spending a lot of time together."
            r "Yeah I am excited to become better friends with you."
            r "Well anyway, I have to get back to my room so I can get a good night's sleep."
            r "It was nice to meet you, see you in class!"
            hide rust_normal with dissolve

    "*[mc] stands at the vending machine, thinking about what he wants*"
    mc "Hmm they don't have Doritos, I guess I am only getting a Snickers bar tonight."
    "*gets his snickers bar and heads back up to his room*"

jump w0_d1_End
