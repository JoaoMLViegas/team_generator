import random
import json
import os
import re

# File for storing players and ratings
PLAYERS_FILE = "players.json"

def main_menu():
    stored_players = load_players()
    
    while True:
        print("\n--- Team Generator Main Menu ---")
        print("1 - Generate Teams Menu")
        print("2 - Manage Players Menu")
        print("3 - Manage Teams Menu")
        print("0 - Exit program")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            generate_teams_menu(stored_players)
        elif choice == "2":
            manage_players_menu(stored_players)
        elif choice == "3":
            manage_teams_menu()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Loads players from the file in descending order of rating
def load_players():
    try:
        with open(PLAYERS_FILE, "r") as file:
            players = json.load(file)
            players.sort(key=lambda x: x["rating"], reverse=True)
            return players
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    
def save_players(players):
    with open(PLAYERS_FILE, "w") as file:
        json.dump(players, file)


# Generate Teams

def generate_teams_menu(stored_players):
    while True:
        print("\n--- Generate Teams Menu ---")
        print("1 - Generate teams from stored players")
        print("2 - Generate teams from input players")
        print("0 - Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            generate_from_stored(stored_players)
        elif choice == "2":
            generate_from_input()
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")

def generate_from_stored(stored_players):
    if not stored_players:
        print("No stored players available. Please add players first.")
        return
    
    selected_players = player_selection(stored_players)

    balanced = validate_yes_no("Do you want to balance the teams using the players' ratings? (y/n): ")
    team_generator_aux(selected_players, balanced)

def player_selection(stored_players):
    selected_players = []

    list_stored_players(stored_players)
    
    while True:
        selection_input = input("Enter the numbers of the players you want to include (e.g., '1, 3, 5-7'), or press Enter to select all: ")

        if not selection_input:  # If input is empty, select all players
            selected_players = stored_players
            break

        # Validate and parse the input
        try:
            ranges = selection_input.split(',')
            for range_str in ranges:
                # Check for a single number or a range (e.g., '1' or '1-3')
                match = re.match(r"(\d+)(-(\d+))?", range_str.strip())
                if not match:
                    raise ValueError("Invalid input format")

                start = int(match.group(1)) - 1  # Convert to 0-indexed
                end = int(match.group(3)) - 1 if match.group(3) else start

                if start < 0 or end < 0 or start >= len(stored_players) or end >= len(stored_players) or start > end:
                    raise ValueError("Index out of range")
                
                # Add the selected players to the list
                selected_players.extend(stored_players[start:end+1])

            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
    
    return selected_players

def generate_from_input():
    players = []
    balanced = validate_yes_no("Do you want to balance the teams using the players' ratings? (y/n): ")
    
    if balanced:
        print("Enter player names and ratings (type '0' as name to finish).")
    else:
        print("Enter player names (type '0' as name to finish).")

    while True:
        player_name = input("Player name: ")
        if player_name == "0":
            break
        if any(p["name"] == player_name for p in players):
            print(f"{player_name} is already in the list.")
            continue

        if balanced:
            while True:
                try:
                    rating = int(input(f"Enter a rating for {player_name} (1-10): "))
                    if 1 <= rating <= 10:
                        players.append({"name": player_name, "rating": rating})  # Use list append
                        break
                    else:
                        print("Rating must be between 1 and 10.")
                except ValueError:
                    print("Please enter a valid number for the rating.")
        else:
            players.append({"name": player_name})  # Use list append

    if not players:
        print("No players entered.")
        return

    while True:
        team_generator_aux(players, balanced)
        if not validate_yes_no("Do you want to generate teams again using the same players? (y/n): "):
            break



# Manage Players

def manage_players_menu(stored_players):
    while True:
        print("\n--- Manage Players Menu ---")
        print("1 - Add to stored players")
        print("2 - Remove from stored players")
        print("3 - List stored players")
        print("0 - Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_players(stored_players)
        elif choice == "2":
            remove_player(stored_players)
        elif choice == "3":
            list_stored_players(stored_players)
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")

def add_players(stored_players):
    print("Enter player names and ratings (type '0' as name to finish):")
    while True:
        player = input("Player name: ")
        if player == "0":
            break
        if any(p["name"] == player for p in stored_players):
            print(f"{player} is already in stored players.")
        else:
            while True:
                try:
                    rating = int(input(f"Enter a rating for {player} (1-10): "))
                    if 1 <= rating <= 10:
                        break
                    else:
                        print("Rating must be between 1 and 10.")
                except ValueError:
                    print("Please enter a valid number for the rating.")
            stored_players.append({"name": player, "rating": rating})
            print(f"{player} with rating {rating} added to stored players.")
    save_players(stored_players)

def remove_player(stored_players):
    if not stored_players:
        print("No players to remove.")
        return
    player_name = input("Enter the player name to remove (type '0' to cancel): ")
    if player_name == "0":
        return
    player = next((p for p in stored_players if p["name"] == player_name), None)
    if player:
        stored_players.remove(player)
        save_players(stored_players)
        print(f"{player_name} removed from stored players.")
    else:
        print(f"{player_name} not found in stored players.")

def list_stored_players(stored_players):
    if not stored_players:
        print("No players stored.")
    else:
        print("\nStored Players (sorted by rating):")
        # Note that the players were already loaded by rating
        padding = " "
        for i in range(len(stored_players)):
            if i == 9:
                padding = ""
            print(f"{padding}{i+1}. {stored_players[i]['name']} (Rating: {stored_players[i]['rating']})")



# Manage Teams

def manage_teams_menu():
    while True:
        print("\n--- Manage Teams Menu ---")
        print("1 - View stored teams")
        print("2 - Remove stored team")
        print("0 - Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            visualize_stored_teams()
        elif choice == "2":
            remove_stored_team()
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")

def visualize_stored_teams():
    team_files = [f for f in os.listdir("teams/") if f.endswith(".txt")]
    if not team_files:
        print("No stored team files found.")
        return
    
    print("Available team files:")
    for i, file in enumerate(team_files, start=1):
        print(f"{i} - {file}")
    
    try:
        choice = int(input("Enter the number of the file to view (0 to cancel): "))
        if choice == 0:
            return
        selected_file = team_files[choice - 1]
        with open(os.path.join("teams", selected_file), "r") as file:
            print(f"\nContents of {selected_file}:")
            print(file.read())
    except (IndexError, ValueError):
        print("Invalid choice. Returning to main menu.")

def remove_stored_team():
    team_files = [f for f in os.listdir() if f.endswith(".txt")]
    if not team_files:
        print("No stored team files found.")
        return

    print("Available team files:")
    for i, file in enumerate(team_files, start=1):
        print(f"{i} - {file}")

    try:
        choice = int(input("Enter the number of the file to delete (0 to cancel): "))
        if choice == 0:
            return
        selected_file = team_files[choice - 1]
        os.remove(selected_file)
        print(f"{selected_file} has been deleted.")
    except (IndexError, ValueError):
        print("Invalid choice. Returning to main menu.")
    except OSError as e:
        print(f"Error deleting file: {e}")


# Team Generation

def team_generator(n_teams, players, balanced):

    if balanced: # Generate balanced teams by the players' ratings

        # Function to determine rating group (0-10)
        def get_rating_group(rating):
            return min(10, int((rating + 0.5) // 1))  # Ensures correct bucket allocation

        # Group players by rating
        rating_groups = {}
        for player in players:
            group = get_rating_group(player["rating"])
            rating_groups.setdefault(group, []).append(player)

        # Shuffle players within each rating group
        for group in rating_groups.values():
            random.shuffle(group)

        # Bring back together all players in descending order of rating groups
        sorted_players = [player for rating in sorted(rating_groups.keys(), reverse=True) for player in rating_groups[rating]]

        # Distribute players across teams
        teams = [[] for _ in range(n_teams)]
        team_ratings = [0] * n_teams

        for player in sorted_players:
            min_team_index = team_ratings.index(min(team_ratings))
            teams[min_team_index].append(player)
            team_ratings[min_team_index] += player["rating"]

    else: # Generate teams randomly
        random.shuffle(players)
        teams = [players[i::n_teams] for i in range(n_teams)]

    return teams

def team_generator_aux(players, balanced):
    while True:
        try:
            n_teams = int(input("How many teams do you want? "))
            if n_teams > len(players):
                print("Number of teams cannot exceed number of players.")
            else:
                teams = team_generator(n_teams, players, balanced)
                pretty_print(teams, balanced)
                if validate_yes_no("Do you want to export the teams to a file? (y/n): "):
                    export_teams(teams, balanced)
                break
        except ValueError:
            print("Please enter a valid number.")

def pretty_print(teams, balanced):
    for i, team in enumerate(teams, start=1):
        if balanced:
            print(f"Team {i} (Average Rating: {round(sum(player['rating'] for player in team)/len(team),1)}):")
        else:
            print(f"Team {i}:")
        for player in team:
            if balanced:
                print(f" - {player['name']} (Rating: {player['rating']})")
            else:
                print(f" - {player['name']}")
        print("")

def export_teams(teams, balanced):
    filename = input("Enter the filename to save teams (e.g., teams.txt): ")
    filename = sanitize_filename(filename)
    with open(f"teams/{filename}", "w") as file:
        for i, team in enumerate(teams, start=1):
            if balanced:
                file.write(f"Team {i} (Average Rating: {round(sum(player['rating'] for player in team)/len(team),1)}):\n")
            else:
                file.write(f"Team {i}:\n")
            for player in team:
                if balanced:
                    file.write(f" - {player['name']} (Rating: {player['rating']})\n")
                else:
                    file.write(f" - {player['name']}\n")
            file.write("\n")
    print(f"Teams exported to {filename}.")

def sanitize_filename(filename, default="teams.txt"):
    filename = filename.strip()  # Remove extra spaces

    # If no filename is given, use a default
    if not filename:
        return default

    # Auto-add .txt if missing
    if not filename.lower().endswith(".txt"):
        filename += ".txt"

    # Remove invalid characters for Windows
    filename = re.sub(r'[\\/:*?"<>|]', '', filename)

    return filename

def validate_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        print("Please enter 'y' or 'n'.")



# Start program
main_menu()
