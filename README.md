# UF Visual Novel
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)  ![GitHub issues](https://img.shields.io/github/issues/ufosc/VisualNovel)  ![GitHub](https://img.shields.io/github/license/ufosc/VisualNovel) 
<br/>
A visual novel developed by the UF Open Source Club. Started in the Fall semester 2023, this video game is built and maintained by club members.

## Table of Contents
- [UF Visual Novel](#uf-visual-novel)
  - [Table of Contents](#table-of-contents)
  - [Maintainers](#maintainers)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Resources](#resources)
  - [Contributing](#contributing)
  - [License](#license)
 
## Maintainers
Maintained by the UF Open Source Club, can be contacted via [Discord](https://discord.gg/j9g5dqSVD8)

Current Maintainers: 
- Nicolas Valiente @nickv779
- Wilson Goins @WilsonGoins
- Anton Salvador @antoncsalvador

## Installation

### Prerequisites 
This project requires [Python](ttps://www.python.org/downloads/) and the [Ren'Py](https://www.renpy.org/) SDK to run. You can install them from here
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

### Ren'py Language Basics

- Base Directory: The base directory is the directory that contains all files that are distributed with the game. The base directory is
 ory is named rengygames, and your game is named "HelloWorld", your base directory will be rengygames/HelloWorld.

- Game Directory: The game directory is a directory named "game" inside the base directory. For example, if your base directory is
  renpygames/HelloWorld, your game directory will be renpygames/HelloWorld/game.

- Logical Lines: A script file is broken up into logical lines. A logical line always begins at the start of a line in the file. A
  logical line ends at the end of a line, unless: 
     - The last character on the line is a backslash(\). 
     - The line contains an open parenthesis character((, {, or [), that hasn't been matched by the cooresponding closing parenthesis
       character (), }, or ], respectively). 
     - The end of the line occurs during a string - any string, even with single quotes, as opposed to Python rules. 
     - Once a logical line ends, the next logical lines begins at the start of the next line. 
     - Most statements in the Ren'Py language consist of a single logical line. 

- Indentation: Indentation is the name we give to the space at the start of each logical line that's used to line up Ren'Py statements.
  In Ren'Py, indentation must consist only of spaces.
  Indentation is used to group statements into blocks. A block is a group of lines, and often a group of statements. The rules for dividing a file into blocks are:
  A block is open at the start of a file.
  A new block is started whenever a logical line is indented past the previous logical line.
  All logical lines inside a block must have the same indentation.
  A block ends when a non-empty logical line is encountered with less indentation than the lines in the block.
  Indentation is very important in Ren'Py, as it is in Python, and it can cause syntax or logical errors when it's incorrect. At the same  time, the use of indentation to express the block structure is far simpler than other languages using other delimiters.

 More information can be found at https://www.renpy.org/doc/html/language_basics.html  

## Resources
Here are some additional resources for using and contributing to the project:

- [Bytes of Love Documentation](https://docs.google.com/document/d/1UAgixK7u0OdSegyYB6ZlITFe23ok7GV4MDUKGovdals/edit?usp=sharing)
- [Ren'py Cheat Sheet](https://docs.google.com/document/d/15tTWFoevrGnxqZxlg1_bZifPYbWIxpm_45jp-FGTpGA/edit)
- [Ren'Py Documenation](https://www.renpy.org/doc/html/index.html)
- [Mood Board](https://www.figma.com/file/71HjcR1MImeYLqvirhFNO9/MOOD-BOARD-ANIME-GAME?type=design&node-id=0%3A1&mode=design&t=lBhCu8ZOLgnEFp4m-1)
- [Miro Board](https://miro.com/welcomeonboard/QnRybW9VRlpCQU5nT3R4UGIxejlrRG12ZzdDalFlM01RN2R6MHFlclg0RmRaUzI0UmhZdXBMREZCUGRVU215eXwzNDU4NzY0NTE3ODI5MjgwMjEwfDI=?share_link_id=384176755076)

## Contributing
All contributions are welcome and appreciated, so long as they adhere to the [license](#license).

To contribute, check out the issues for anything that you think you can work on. As always, reach out to any of the maintainers for permission to tackle the issue before working on it. Feel free to ask for any help in setting up the coding environment and for any clarification on issues.

## License
[AGPL 2.0](LICENSE.md) <br/>
