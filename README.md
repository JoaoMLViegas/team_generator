# **Team Generator**

A terminal-based Python program for generating balanced teams from stored or input player lists. The app includes a menu interface that allows users to add, remove, and view players or teams and to export teams to files.

## **Features**
- Team Generation: Generate teams from stored players (all or a selection) or input new players on the fly.
- Player Management: Add or remove players from stored data, view stored players, and prevent duplicate entries.
- File Management: Save generated teams to files for future reference, view stored teams, and delete unwanted team files.
- Ratings for Balance: Includes the possibility of using a rating system (1-10) for players to ensure balanced team creation.
- Menu Interface: Intuitive menu for navigating program options.

## **Getting Started**
### Prerequisites
- **Python**: Ensure you have Python installed. To check, run: 
``` 
python --version
```

### Installation
1. Clone the repository:  
```
git clone https://github.com/JoaoMLViegas/team_generator.git  
cd team_generator
```
2. Run the app:  
```
python team_generator.py
```

## **Usage**
Upon running, the program will display the Main Menu, providing the following options:  

--- Team Generator Main Menu ---  
1 - Generate Teams Menu  
2 - Manage Players Menu  
3 - Manage Teams Menu  
0 - Exit program  

### **Generate Teams Menu**
Choosing option 1 in the Main Menu will display the following:

--- Generate Teams Menu ---  
1 - Generate teams from stored players  
2 - Generate teams from input players  
0 - Back to Main Menu  

#### Option description
1. Generate teams from stored players: Uses the existing list of stored players to form teams, choosing which players to include.
2. Generate teams from input players: Lets you enter new players and their ratings to create teams without saving them to storage.  
NOTE: In both options, the user will be asked if the players' ratings are to be considered while generating or if the teams are to be completely random.

### **Manage Players Menu**
Choosing option 2 in the Main Menu will display the following:

--- Manage Players Menu ---  
1 - Add to stored players  
2 - Remove from stored players  
3 - List stored players  
0 - Back to Main Menu  

#### Option description
1. Add to stored players: Add new players with ratings (1-10) to the stored player list, ensuring no duplicate entries.
2. Remove from stored players: Remove specific players from storage.
3. List stored players: Displays the list of stored players and their ratings.

### **Manage Teams Menu**
Choosing option 3 in the Main Menu will display the following:

--- Manage Teams Menu ---  
1 - View stored teams  
2 - Remove stored team  
0 - Back to Main Menu  

#### Option description
1. View stored teams: Lists available team files and allows you to view the contents of a selected file.
2. Remove stored team: Lists and allows deletion of unwanted team files from storage.

## **Project Structure**
team_generator/  
├── team_generator.py &emsp;# Main app code with tkinter GUI  
├── players.json &emsp;# File to store player data  
├── teams/ &emsp;# Folder to store generated team files  
├── README.md &emsp;# Project documentation  
└── LICENSE &emsp;# Project license  

## **License**
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
See the [LICENSE](LICENSE) file for more details.
