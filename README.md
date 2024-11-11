# **Team Generator**

A terminal-based Python program for generating balanced teams from stored or input player lists. The app includes a menu interface that allows users to add, remove, and view players or teams and to export teams to files.

## **Features**
- Team Generation: Generate teams from stored players or input new players on the fly.
- Player Management: Add or remove players from stored data, view stored players, and prevent duplicate entries.
- File Management: Save generated teams to files for future reference, view stored teams, and delete unwanted team files.
- Ratings for Balance: Includes a rating system (1-10) for players to ensure balanced team creation.
- Menu Interface: Intuitive menu for navigating program options. (in development...) Organize options in 3 sub-menus (Generate teams, Manage Stored Players and Manage Stored Teams)
- (in development...) Add option to generate teams without balance considerations

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
Upon running, the program will display the main menu, providing the following options:  

--- Team Generator Menu ---  
1 - Generate teams from stored players  
2 - Generate teams from input players  
3 - Add to stored players  
4 - Remove from stored players  
5 - List stored players  
6 - View stored teams  
7 - Remove stored team  
0 - Exit program  

### **Menu Options**
0. Exit program: Closes the program.
1. Generate teams from stored players: Uses the existing list of stored players to form balanced teams based on player ratings.
2. Generate teams from input players: Lets you enter new players and their ratings to create teams without saving them to storage.
3. Add to stored players: Add new players with ratings (1-10) to the stored player list, ensuring no duplicate entries.
4. Remove from stored players: Remove specific players from storage.
5. List stored players: Displays the list of stored players and their ratings.
6. View stored teams: Lists available team files and allows you to view the contents of a selected file.
7. Remove stored team: Lists and deletes unwanted team files from storage.

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