# **Team Generator**

A terminal-based Python program for generating balanced teams from stored or input player lists. The app includes a menu interface that allows users to add, remove, and view players or teams and to export teams to files.

## **Features**
- Advanced Player Selection: Quickly choose participants from your roster using individual numbers or ranges (e.g., 1, 3, 5-10).
- Fair-Play Balancing: Uses a Jittered Greedy Algorithm to ensure teams are balanced by skill level while providing variety between generations.
- Player Roster Management: Add, remove, and view players with persistent storage in a human-readable JSON format.
- Team Export: Save generated lineups to .txt files with automatic folder management and filename sanitisation.
- Clean CLI Interface: Simple, numbered menus for easy navigation.

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
2. Generate teams from input players: Let's you enter new players and their ratings to create teams without saving them to storage.  
<br>NOTE: In both options, the user will be asked whether the players' ratings should be considered when generating or if the teams should be completely random.

### **Manage Players Menu**
Choosing option 2 in the Main Menu will display the following:

--- Manage Players Menu ---  
1 - Add to stored players  
2 - Remove from stored players  
3 - List stored players  
0 - Back to Main Menu  

#### Option description
1. Add to stored players: Add new players with ratings (1.0-10.0) to the stored player list, ensuring no duplicate entries.
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

## Technical Details
### The Balancing Algorithm
To ensure teams are fair but not identical every time you generate them, the app uses a Jittered Greedy Assignment:
1. Jitter: A random value between $\pm 0.4$ is temporarily added to each player's rating. This allows players with similar skill levels to occasionally swap "rank" positions.
2. Sort: Players are sorted by this jittered rating.
3. Greedy Assignment: The algorithm iterates through the sorted list and assigns the next player to whichever team currently has the lowest total rating.

### Data Storage
- Players: Stored in players.json with a 2-space indentation for easy manual editing if needed.
- Teams: Exported to the /teams directory. The program automatically creates this folder if it doesn't exist.

## **Project Structure**
```
team_generator/  
├── team_generator.py  # Main application logic  
├── players.json       # File to store player data  
├── teams/             # Directory to store generated team files  
├── README.md          # Documentation  
└── LICENSE            # License  
```

## **License**
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
See the [LICENSE](LICENSE) file for more details.
