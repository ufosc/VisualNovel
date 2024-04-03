default campus_text = False
default bar_text = False
default highway_text = False
default resturant_text = False
default mall_text = False
default frat_text = False
default library_text = False
default stadium_text = False

screen overviewMap:

    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map_images/overview_map.png"

        imagebutton:
            focus_mask True
            xpos 798
            ypos 227
            idle "map_images/campus_idle.png"
            hover "map_images/campus_hover.png"
            action ShowMenu("campusroadmap")
            hovered SetVariable("campus_text", True)
            unhovered SetVariable("campus_text", False)


        imagebutton:
            focus_mask True
            xpos 1545
            ypos 535
            idle "map_images/bar_idle.png"
            hover "map_images/bar_hover.png"
            hovered SetVariable("bar_text", True)
            unhovered SetVariable("bar_text", False)
            action Return()

        imagebutton:
            focus_mask True
            xpos 965
            ypos -5
            idle "map_images/frat_idle.png"
            hover "map_images/frat_hover.png"
            hovered SetVariable("frat_text", True)
            unhovered SetVariable("frat_text", False)
            action Return()

        imagebutton:
            focus_mask True
            xpos -10
            ypos -10
            idle "map_images/highway_idle.png"
            hover "map_images/highway_hover.png"
            hovered SetVariable("highway_text", True)
            unhovered SetVariable("highway_text", False)

            action Return()

        imagebutton:
            focus_mask True
            xpos 1463
            ypos 74
            idle "map_images/library_idle.png"
            hover "map_images/library_hover.png"
            hovered SetVariable("library_text", True)
            unhovered SetVariable("library_text", False)

            action Return()


        imagebutton:
            focus_mask True
            xpos 542
            ypos -5
            idle "map_images/mall_idle.png"
            hover "map_images/mall_hover.png"
            hovered SetVariable("mall_text", True)
            unhovered SetVariable("mall_text", False)

            action Return()

        imagebutton:
            focus_mask True
            xpos 1212
            ypos 671
            idle "map_images/resturant_idle.png"
            hover "map_images/resturant_hover.png"
            hovered SetVariable("resturant_text", True)
            unhovered SetVariable("resturant_text", False)

            action Return()

        imagebutton:
            focus_mask True
            xpos 155
            ypos 515
            idle "map_images/stadium_idle.png"
            hover "map_images/stadium_hover.png"
            hovered SetVariable("stadium_text", True)
            unhovered SetVariable("stadium_text", False)

            action Return()

  

    if campus_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Bytes Campus"

    if library_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Library"

    if mall_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Mall"

    if frat_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Theta Theta Houses"

    if resturant_text:
        window:
            yanchor 0.40

            vbox: 
                xalign 0.5 
                yalign 0.10 
                text "8-Byte Fastfood"

    if bar_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Mothers-OG"

    if stadium_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "Stadium"

    if highway_text:
        window:
            yanchor 0.40

            vbox:
                xalign 0.5 
                yalign 0.10 
                text "I-420 Highway"