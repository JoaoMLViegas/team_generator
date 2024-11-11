import random #keep for future use (generating teams without balance considerations)
import json
import os

# File for storing players and ratings
PLAYERS_FILE = "players.json"

def load_players():
    try:
        with open(PLAYERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_players(players):
    with open(PLAYERS_FILE, "w") as file:
        json.dump(players, file)

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

def list_stored_players(stored_players):
    if not stored_players:
        print("No players stored.")
    else:
        print("Stored Players:")
        for player in stored_players:
            print(f" - {player['name']} (Rating: {player['rating']})")

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

def team_generator(n_teams, players):
    sorted_players = sorted(players, key=lambda x: x["rating"], reverse=True)
    teams = [[] for _ in range(n_teams)]
    team_ratings = [0] * n_teams

    for player in sorted_players:
        min_team_index = team_ratings.index(min(team_ratings))
        teams[min_team_index].append(player)
        team_ratings[min_team_index] += player["rating"]

    return teams

def pretty_print(teams):
    for i, team in enumerate(teams, start=1):
        print(f"Team {i} (Total Rating: {sum(player['rating'] for player in team)}):")
        for player in team:
            print(f" - {player['name']} (Rating: {player['rating']})")
        print("")

def export_teams(teams):
    filename = input("Enter the filename to save teams (e.g., teams.txt): ")
    with open(f"teams/{filename}", "w") as file:
        for i, team in enumerate(teams, start=1):
            file.write(f"Team {i} (Total Rating: {sum(player['rating'] for player in team)}):\n")
            for player in team:
                file.write(f" - {player['name']} (Rating: {player['rating']})\n")
            file.write("\n")
    print(f"Teams exported to {filename}.")

def validate_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ("y", "n"):
            return response
        print("Please enter 'y' or 'n'.")

def main_menu():
    stored_players = load_players()
    
    while True:
        print("\n--- Team Generator Menu ---")
        print("1 - Generate teams from stored players")
        print("2 - Generate teams from input players")
        print("3 - Add to stored players")
        print("4 - Remove from stored players")
        print("5 - List stored players")
        print("6 - View stored teams")
        print("7 - Remove stored team")
        print("0 - Exit program")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            generate_from_stored(stored_players)
        elif choice == "2":
            generate_from_input()
        elif choice == "3":
            add_players(stored_players)
        elif choice == "4":
            remove_player(stored_players)
        elif choice == "5":
            list_stored_players(stored_players)
        elif choice == "6":
            visualize_stored_teams()
        elif choice == "7":
            remove_stored_team()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def generate_from_stored(stored_players):
    if not stored_players:
        print("No stored players available. Please add players first.")
        return
    while True:
        try:
            n_teams = int(input("How many teams do you want? "))
            if n_teams > len(stored_players):
                print("Number of teams cannot exceed number of players.")
            else:
                teams = team_generator(n_teams, stored_players.copy())
                pretty_print(teams)
                export_choice = validate_yes_no("Do you want to export teams to a file? (y/n): ")
                if export_choice == 'y':
                    export_teams(teams)
                break
        except ValueError:
            print("Please enter a valid number.")

def generate_from_input():
    players = set()
    print("Enter player names and ratings (type '0' as name to finish):")
    while True:
        player_name = input("Player name: ")
        if player_name == "0":
            break
        if any(p["name"] == player_name for p in players):
            print(f"{player_name} is already in the list.")
            continue

        while True:
            try:
                rating = int(input(f"Enter a rating for {player_name} (1-10): "))
                if 1 <= rating <= 10:
                    players.add({"name": player_name, "rating": rating})
                    break
                else:
                    print("Rating must be between 1 and 10.")
            except ValueError:
                print("Please enter a valid number for the rating.")

    if not players:
        print("No players entered.")
        return

    players = list(players)  # Convert set back to list for team generation
    while True:
        try:
            n_teams = int(input("How many teams do you want? "))
            if n_teams > len(players):
                print("Number of teams cannot exceed number of players.")
            else:
                teams = team_generator(n_teams, players)
                pretty_print(teams)
                export_choice = validate_yes_no("Do you want to export teams to a file? (y/n): ")
                if export_choice == 'y':
                    export_teams(teams)
                break
        except ValueError:
            print("Please enter a valid number.")

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
        with open(selected_file, "r") as file:
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

# Start program
main_menu()
