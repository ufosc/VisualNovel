# Bytes of Love
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)  ![GitHub issues](https://img.shields.io/github/issues/ufosc/VisualNovel)  ![GitHub](https://img.shields.io/github/license/ufosc/VisualNovel) 
<br/>

A visual novel developed by the UF Open Source Club. Started in the Fall 2023, this game is built and maintained by club members.

## Table of Contents
- [Team Members](#team-members)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)
 
## Team Members
The project is currently maintained by the UF Open Source Club, can be contacted via [Discord](https://discord.gg/j9g5dqSVD8).

The lead team members in charge of the project are as follows. Reach out to any of them via Discord with questions regarding the project. Click the names of the Tech Leads if you wish to send an email as your preferred form of communication.

Tech Leads: 
- (@WilsonGoins) [Wilson Goins](mailto:wilson.goins@ufl.edu), Script Writer
- (@RyderKeeny) [Ryder Keeny](mailto:ryder.keeny@ufl.edu), Story Lead
- (@nickv779) [Nicolas Valiente](mailto:nvaliente@ufl.edu), Product Manager

Lead Contributors:
- (@Xa-el) Xael Font, Lead Ren'Py Developer
- (@JMalegni) Joseph Malegni, Product Manager
- (@Myrtte) Edward Roshko, Script Writer

## Installation

### Prerequisites 
This project requires [Python](ttps://www.python.org/downloads/) and the [Ren'Py](https://www.renpy.org/) SDK to run. You can install them from here:
- Python (Latest): https://www.python.org/downloads/
- Ren'Py (8.1.1 or greater): https://www.renpy.org/latest.html

### Setup

Once you have downloaded the Ren'py SDK, extract it into your project directory. 

Now, you can fork the repository and clone it into the root directory of the SDK using this command using ssh or http:

In the ```renpy.8.1.1-sdk``` folder.

SSH
        
        git clone git@github.com:user/VisualNovel.git 

HTTP

        git clone https://github.com/user/VisualNovel.git

You can start up the Ren'Py launcher by launching ```renpy.exe``` in the ```renpy.8.1.1-sdk``` directory. If you are a Mac user, launch via ```renpy``` instead of ```renpy.exe```. Once the launcher opens, the project should show up in the projects tab as UFOSC.

If the project is not showing up you need to set the project directory manually. This is done by navigating to ``` preferences``` located under the Launch Project button on the botton right. 

Then under ```Project Directory```, update the project directory to ```renpy-8.1.1-sdk/VisualNovel``` or the parent folder that UFOSC is located in.

The program and games file can be edited in the ```scripts.py``` file in the UFOSC folder. 

## Resources
Here are some additional resources for using and contributing to the project:

- [Bytes of Love Documentation](https://docs.google.com/document/d/1UAgixK7u0OdSegyYB6ZlITFe23ok7GV4MDUKGovdals/edit?usp=sharing)
- [Ren'py Cheat Sheet](https://docs.google.com/document/d/15tTWFoevrGnxqZxlg1_bZifPYbWIxpm_45jp-FGTpGA/edit)
- [Ren'Py Documenation](https://www.renpy.org/doc/html/index.html)
- [Mood Board](https://www.figma.com/file/71HjcR1MImeYLqvirhFNO9/MOOD-BOARD-ANIME-GAME?type=design&node-id=0%3A1&mode=design&t=lBhCu8ZOLgnEFp4m-1)
- [Miro Board](https://miro.com/welcomeonboard/QnRybW9VRlpCQU5nT3R4UGIxejlrRG12ZzdDalFlM01RN2R6MHFlclg0RmRaUzI0UmhZdXBMREZCUGRVU215eXwzNDU4NzY0NTE3ODI5MjgwMjEwfDI=?share_link_id=384176755076)

## Contributing
All contributions are welcome and appreciated, so long as they adhere to the [license](#license).

To contribute, check out the issues for anything that you think you can work on. As always, reach out to any of the Tech Leads or Lead Contributors for permission to tackle the issue before working on it. Feel free to ask for any help in setting up the coding environment and for any clarification on issues.

Review the Bytes of Love Documentation for any information regarding the gam's ideas, progress, and next steps. For edit access, reach out to Nicolas Valiente for approval; you must request the access in person during Casual Coding sessions.

# Bytes of Love: Ren'Py Programming Principles Guide

Welcome to the "Bytes of Love" Ren'Py programming guide. This document aims to provide you with a clear and structured approach to scripting your visual novel. Follow these guidelines to ensure consistency and readability throughout your project.

## Variable Declarations

- **Location for Declarations:** All variables should be declared in the `VisualNovel/UFOSC/game/script.rpy` file.
- **Naming Conventions:** Use underscore casing for variable names (e.g., `rust_normal` instead of `rustNormal`) to maintain consistency.

## Script Structure

- **Weekly Cycle:** Structure your script based on the week day cycle. For example, to edit events on day 1 of week 0, use `w0_d1_...` as a naming convention.
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
  - Changing character expressions within choices is allowed. Use the `show` statement with a transition (e.g., `with dissolve`) for visual effects.
  - Example of presenting choices:
	```renpy
	menu w0_d1_Rust:
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

## Additional Tips

- **Beginner Tips:** Start small and gradually add more complexity to your game as you become more comfortable with Ren'Py's scripting language.
- **Testing:** Regularly test your game to catch and fix errors early in the development process.
- **Community Resources:** Don't hesitate to seek help from the UFOSC Discord! Specifically Lazzy, Anton, Ryder, or Mathew!

This guide is designed to help beginners navigate the basics of Ren'Py scripting for the "Bytes of Love" project. By adhering to these principles, you'll create a more organized and enjoyable visual novel. Happy coding!

## License
[AGPL 2.0](LICENSE.md) <br/>
e
