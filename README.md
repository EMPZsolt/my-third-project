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
- [Deployment and Local Development](#deployment-and-local-development)  
     * [Deployment](#deployment)
     * [Local Deployment](#local-development)
          * [How to Fork](#how-to-fork)
          * [How to Clone](#how-to-clone)
- [Testing](#testing)
     * [Bugs](#bugs)
     * [W3C Validator](#w3c-validator)
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
- Intro text:
     - The game starts with a welcome message and a description (as well as the parameters and rules of the game).
     ![](assets/images/intro.webp)
     
- The playground:    
     - A two-player board is created with randomly placed ships.
     - The computer's ships are hidden from the player.
     - The game awaits for the coordinates.
     ![](assets/images/boards.webp)

- Coordinate input, results and scores summary:
     - Start to play against the computer.
     - Entering valid coordinates.
     - Get the result from our and the computer randomized guess.
     - Get a scores summary after each round.
     ![](assets/images/guess-score_summary.webp)
- Input validation:
     - You can only choose within the grid.
     - Only that input valid which meets the compliance rules.
     - If you enter an already used coordinate, the round will repeat.
     ![](assets/images/errors.webp)
### Future Features
- Multiple player mode option.
- Adjustable board size.
- Different ship sizes and their manual placement.
- Option to exit the game at any time

## Flow chart
- I used Draw.io to create a flow chart of the game separating individual elements and processes of the program with colors and shapes. 

- ![](assets/images/flow_chart.webp)

## Technologies Used
### Languages Used
Python were used to create this program.
### Libraries & Programs Used
Git - For version control.
Github - To save and store the files for the website.
Heroku - To represent the live program.
Tiny PNG - To compress images.
FreeConvert - To compress images in the webp format.
Am I Responsive? - To show the website image on a range of devices.
Paint - To cut the images to the right size.
Draw.io - To create the flow chart

## Deployment and Local Development
### Deployment
The site is deployed using GitHub Pages. Visit the deployed site [here][def]. To deploy using GitHub pages:
 1. Login or Sign Up to GitHub.
 2. Open the project repository.
 3. Click on "Settings" on the navigation bar under the repository title.
 4. Click on "Pages" in the left hand navigation panel.
 5. Under "Source", choose which branch to deploy. This should be Main for newer repositories (older repositories may still use Master).
 6. Choose which folder to deploy from, usually "/root".
 7. Click "Save", then wait for it to be deployed. It can take some time for the page to be fully deployed.
 8. Your URL will be displayed above "Source".
### Local Development
#### How to Fork
To fork the repository:
1. Log in (or sign up) to Github.
2. Go to the repository for this project, kera-cudmore/Bully-Book-Club.
3. Click the Fork button in the top right corner.
#### How to Clone
To clone the Bully-Book-Club repository:
Log in (or sign up) to GitHub.
Go to the repository for this project, kera-cudmore/Bully-Book-Club.
Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
## Testing
Testing took place continuously during the entire construction. I used Chrome's developer tools during the build to try out new ideas and prevent or, if necessary, fix problems.
During the development, I used Google's developer tools to ensure everything worked as expected, to successfully discover bugs, determine their origin, and fix them.
- I tested playing this game in different browsers: Microsoft Edge, Google Chrome, Firefox.
- I confirmed that this game results are always correct.
- I confirmed that this project is responsive, functions on all standard screen sizes using the devtools device toolbar.
- I confirmed that the header, game options, game results and the footer are all readable and easy to understand.
### Bugs
- The first time I changed the font, the text hung over one of the buttons in the game options. This is how I increased the original size settings of the buttons.
- At first, I did not notice that the name of the score collector on both displays was "Your scores". Only after a few tests did the mistyping become apparent.
- When I decided to put a versus text between the two displays, I couldn't manage to keep it centered and responsive. Then I created a wrapper div for the game zone and set display to flex , flex-direction to row and justify-content to center . 
- The JavaScript code did not want to work before the first run. When I reviewed the code, I found a typo in the constants.
- With the appearance of the scissors symbol, the display size always became a little smaller. I solved the problem by resizing the image.
- In the checkWinner function, I found a typo on the first look. I wrote the names of all the symbols in capital letters, when they should have been in small letters. Fortunately, it showed up during the first round of checks, so it didn't cause any problems when testing the game.
### W3C Validator
The W3C validator was used to validate the HTML. It was also used to validate CSS in the style.css file.
- No errors were returned when passing through the official [W3C HTML Validator](./assets/images/html-validator.webp)
- No errors were found when passing through the official [CSS Validator](./assets/images/css-validator.webp)

 ## Credits
 ### Code Used
 The constant elements, the event listeners for the buttons and the playGame function come from the CodeInstitute sample portfolio project.!!!!!!!!!!!
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
