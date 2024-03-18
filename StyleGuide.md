# Bytes of Love: Ren'Py Programming Principles Guide

Welcome to the "Bytes of Love" Ren'Py programming guide. This document aims to provide you with a clear and structured approach to scripting your visual novel. Follow these guidelines to ensure consistency and readability throughout your project.

## Variable Declarations

- **Location for Declarations:** All variables should be declared in the `VisualNovel/UFOSC/game/script.rpy` file.
- **Naming Conventions:** Use underscore casing for variable names (e.g., `rust_normal` instead of `rustNormal`) to maintain consistency.

## Script Structure

- **Weekly Cycle:** Structure your script based on the week day cycle. For example, to edit events on day 1 of week 0, use `w0_d1_[Location]` as a naming convention.
- **Labels:** Use labels to mark the beginning of a scene. Labels work similarly to functions in programming, allowing you to "jump" to different parts of the script. Example:
  ```renpy
  label start:
  	# Your scene code here
  ```
- **Scenes:** Use the `scene` statement to change backgrounds. Note that this is specifically for changing scene backgrounds, not character images.
  - Example of changing a scene:
	```renpy
	scene classroom_day
	```

## Character Interaction and Choices

- **Declaring Characters:** When declaring a new character, add their definition to `VisualNovel/UFOSC/game/script.rpy`.
- **Menus for Choices:** Use the `menu` statement to present choices to the player. Follow each `menu` statement with text-only options.
  - **Note:** You can precede the choices with a line of dialogue, which will be displayed alongside the options, to add context or emotion to the decision-making process.
  - Changing character expressions within choices is allowed. Use the `show` statement with a transition (e.g., `with dissolve`) for visual effects.
  - Example of presenting choices:
	```renpy
  	menu w0_d1_Rust:
          "Before making a choice, the [mc] thinks:" #this is shown under the choices in a text box

          "Mean response":
        		mc "You suck."
	        	show rust_angry with dissolve
	    	"Nice response":
	        	mc "Nice to meet you."
	        	show rust_happy with dissolve
	```
  - **Error Troubleshooting:** If you encounter an `EXPECTED MENU ITEM` error, ensure that commands are placed **inside** the options, similar to the `show` command in the example.

## Variable Usage

- **Dynamic Text:** To make text dynamic based on player choices or actions, declare and use variables accordingly.
  - Example of declaring a variable:
	```renpy
	$ food_item = "bacon"
	```
  - You can then use this variable within your script to dynamically change the text.
  - Example of using a variable:
	```renpy
	mc "I want to eat [food_item]."
	```

## Conditional Content and Choices

### Using If Statements
- **Purpose:** Utilize `if` statements to dynamically alter game content based on variable values. This is especially useful for conditional dialogue options, scene changes, or character interactions.
- **Syntax and Example:**
    ```renpy
    if python_rep > 10:
        # Conditional content here
    ```
- **Application in Choices:**
    - To conditionally display choices, wrap the choice in an `if` statement within a `menu` block.
    - **Example:**
        ```renpy
        menu:
            "This choice always appears."

            if python_rep > 10:
                "This choice only appears if python_rep is greater than 10."
        ```

### Dynamic Choices Based on Variables
- **Adjusting Choices:** Change the text and outcomes of choices dynamically by referencing variables.
- **Example:** Using `python_rep` to influence dialogue options.
    ```renpy
    menu:
        if python_rep < 5:
            "Ask about basic Python concepts.":
                # Outcome for low python_rep
        elif python_rep >= 5:
            "Discuss advanced Python topics.":
                # Outcome for high python_rep
    ```

## File Structure and Organization

- **Big Choices:** For significant choices, create separate files within dedicated folders (e.g., `w1_d1_choices/`, containing `w1_d1_LunchJava`, `w1_d1_LunchPython`, etc.). This approach keeps your project organized and manageable.
- **Small Choices:** Minor choices can be integrated directly into the main script file, avoiding unnecessary file fragmentation.

## Advanced Variable Usage

### Conditionally Modifying Game Flow
- **Scenes and Character Displays:** Use variables like `python_rep` to make decisions about which scenes to display or how characters react.
    ```renpy
    if python_rep > 5:
        scene special_python_classroom
        show character_smiling
    else:
        scene regular_classroom
        show character_neutral
    ```

- **Conditional Interactions:** In sections detailing character interactions, remind scriptwriters to consider the player's relationship status with characters, influenced by variables such as `python_rep`, to adjust dialogue and interactions accordingly.

## Additional Tips

- **Beginner Tips:** Start small and gradually add more complexity to your game as you become more comfortable with Ren'Py's scripting language.
- **Testing:** Regularly test your game to catch and fix errors early in the development process.
- **Community Resources:** Don't hesitate to seek help from the [UFOSC Discord](https://discord.gg/pk9gCXgPRB)! Specifically the [Bytes of Love Channel](https://discord.gg/THrZYamTGH). For people, refer to our main developers: [Lazzy](https://github.com/Xa-el), [Anton](https://github.com/antoncsalvador), [Jason](https://github.com/jasonlin15), or [Mathew](https://github.com/jasonlin15)!

This guide is designed to help beginners navigate the basics of Ren'Py scripting for the "Bytes of Love" project. By adhering to these principles, you'll create a more organized and enjoyable visual novel. Happy coding!

