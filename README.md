# Emoji Battleships
## my-third-project:
- [Live Site](https://emoji-battleships-5ae2f3e29783.herokuapp.com/)
- [Repository](https://github.com/EMPZsolt/my-third-project)

Emoji Battleships is a simple command-line game where players take turns trying to sink each other's ships on a 5x5 grid. The game is played against a computer opponent. The objective is to sink all of the computer's ships before the computer sinks all of your ships.

This is a game that you will want to play over and over again. Battleships is all about of strategy, memory and logic. It's a great game for enhancing your concentration, training your motor skills and improving of your strategic thinking. Everyone from children to adults can play. For the little ones it can sharpen their mind and for the grown ups, you can have pleasant, fun moments, while they can recall their childhood in the meantime.


![A screenshot of this project from a mockup screenshot generator and it represents how responsive the program](./assets/images/responsive.webp)

## Contents
- [How to play](#how-to-play)
- [Design](#design)
     * [Imagery](#imagery)
- [Features](#features)
     * [Existing Features](#existing-features)
     * [Future Features](#future-features)
- [Flow chart](#flow-chart)
- [Technologies Used](#technologies-used)
     * [Languages Used](#languages-used)
     * [Libraries & Programs Used](#libraries--programs-used)
- [Deployment](#deployment)
- [Testing](#testing)
     * [Validation testing](#validation-testing)
     * [Manual testing](#manual-testing)
     * [Bugs](#bugs)
- [Credits](#credits)
     * [Code Used](#code-used)
     * [Content](#content)
     * [Media](#media)
     * [Acknowledgments](#acknowledgments)

## How to play
1. Run the emoji_battleships.py script in your terminal or command prompt.
2. You will be greeted with the welcome message and game description.
3. Enter your name when prompted.
4. The game will display your board (with your ships) and the computer's board (the ships of the machine will be hidden).
5. During your turn, you will be asked to enter the row and column coordinates (either numeric or alphabetic).
6. The game will show the results of your shot and the computer's shot.
7. The game continues until one of the players wins.
8. After the game ends, the final message is displayed.

## Design
### Imagery
- I found the emojis on a public website. I have credited this in the credits section.
- The idea of the board structure I took it from a YouTube video. I have credited this in the credits section.

## Features
### Existing Features
Intro text:
- The game starts with a welcome message and a description (as well as the parameters and rules of the game).
![](assets/images/intro.webp)
     
The playground:    
- A two-player board is created with randomly placed ships.
- The computer's ships are hidden from the player.
- The game awaits for the coordinates.
![](assets/images/boards.webp)

Coordinate input, results and scores summary:
- Start to play against the computer.
- Entering valid coordinates.
- Get the result from our and the computer randomized guess.
- Get a scores summary after each round.
![](assets/images/guess-score_summary.webp)

Input validation:
- You can only choose within the grid.
- Only that input valid which meets the compliance rules.
- If you enter an already used coordinate, the round will repeat.
![](assets/images/errors.webp)

### Future Features
- Multiple player mode option.
- Adjustable board size.
- Different ship sizes and their manual placement.
- Option to exit the game at any time.

## Flow chart
I used Draw.io to create a flow chart of the game separating individual elements and processes of the program with colors and shapes. 

![](assets/images/flow_chart.webp)

## Technologies Used
### Languages Used
Python were used to create this game.
### Libraries & Programs Used
- Git - For version control.
- Github - To save and store the files for the website.
- Heroku - To represent the live program.
- Tiny PNG - To compress images.
- FreeConvert - To compress images in the webp format.
- Am I Responsive? - To show the website image on a range of devices.
- Paint - To cut the images to the right size.
- Draw.io - To create the flow chart

## Deployment
The app was deployed to Heroku using the following steps:
1. Create new app:
- ![](assets/images/heroku_create.webp)
2. Add buildpacks and config VARS:
- ![](assets/images/heroku_vars_buildpacks.webp)
3. Connect Heroku to GitHub
4. Authorise the connection
5. Connect to the correct repository
- ![](assets/images/heroku_deployment.webp)
     
## Testing
Testing took place continuously during the entire construction. I used the print() statement during the build to try out new ideas and prevent or, if necessary, fix problems.
- I tested playing this game in different browsers: Microsoft Edge, Google Chrome, Firefox.
- I tested in my local terminal and the Code Institute Heroku terminal.
- I confirmed that this game results are always correct.
- I confirm that the game process works properly and gives the correct results.
### Validation testing
I pasted run.py into the CI Python Linter and non errors were found.
![](assets/images/ci_python_%20linter.webp)
### Manual testing
The game is thoroughly tested to ensure its functionality and user experience. The test covers various aspects of the game, including board creation, ship placement, gameplay, user interaction, input validation, and win conditions.

| Feature            | Expected Outcome | Testing Performed     | Pass/Fail  |
| :------------      | :------------    | :------------         |   :---:    |
| Board Creation Test| Initialize the board with a given size.| Board is created with the specified size.| Pass|
|                    | Check if the grid is initialized with the correct size and with the correct emoji.| Each cell in the grid is initialized to an empty space.| Pass |
| Ship Placement Test| Place ships randomly on the board.| Ships are placed randomly on the board.| Pass|
|                    | The expected ship number and computer ships are hidden.| The correct number of ships is placed on the board and the computer ships are hidden.| Pass|
|Gameplay Test       | Simulate the game flow and turns with predefined player guesses.| Overall gameplay and user interaction work correctly.| Pass|
|                    | Validate the responses for hits, misses, and errors based on expected behavior.| Game follows the rules and handles guesses accurately.| Pass|
| Player's Score Update Test| Simulate player's successful hits and check if the score is incremented.| Player's score is correctly updated after each hit.| Pass|
| Valid Coordinate Input| Test the function with valid and invalid input to check for correct responses.| Input validation function works as expected.| Pass| 
### Bugs
- First, I created a joint guess list, which resulted in the hits being mixed up and the player could not shoot where the machine had already shoted. That's why I created separate lists to store the previously chosen coordinates of the player and the computer.
- In the first version, after I tried to shoot in the same place as before, the system continued to let the machine play, while I had to repeat. To solve this situation, I needed to modify the game logic to handle repeated guesses from the player and prompt the player to enter a different set of coordinates before allowing the computer to take its turn. So I wrapped the player's input section inside a while True loop. This loop will keep prompting the player to enter new coordinates until they provide a unique set of coordinates that haven't been guessed before. Once the player enters a valid and non-repeated coordinate, it will break out of the loop and proceed with the rest of the game logic, including the computer's turn.
- During my discussion with my mentor, we noticed that I repeatedly wrote the line of code for matching the valid coordinates and the error message for it. Although this did not cause an error in the program, they were completely unnecessary, so two were deleted.
- In the first version, an error slipped into the function that monitors the valid input value and practically all values ​​were accepted, and the result thus became completely irrelevant. Thats why I used the "ord(coordinate.upper()) - ord('A')" solution, so if the input is alphabetic (representing the column coordinate), it converts the letter to a numeric column index. Or if the input is numeric (representing the row coordinate), I used "int(coordinate)" to convert it to an integer. Thus, the coordinate system presented in the Infos section is valid and produces the expected results.
- Furthermore, I encountered an error during the development that the computer did not create the ships, so the player always lost. It turned out that the computer_board.place_ships method in the game function was not working properly due to a typo.

 ## Credits
 ### Code Used
- Some of the code comes from the Code Institute sample project.
 ### Content
- The basic structure comes from the CodeInstitute sample portfolio project.
 ### Media
 - The [emojis](https://unicode.org/emoji/charts/emoji-list.html) is from a public website.
 - The idea of the [board structure](https://www.youtube.com/watch?v=xz9GrOwQ_5E&t=0s) is from this YouTube video
 ### Acknowledgments
 I would like to acknowledge the following people who helped me along the way in completing my second milestone project:
 - My wife, who gave me ideas and supported me through the project.
 - My Mentor, Graeme Taylor, who showed the direction, helped and encouraged me.
 - Thank you to entire Code Isntitute for making my development possible.
