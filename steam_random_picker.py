import tkinter as tk
import random
import requests
import webbrowser
import os
import re
import threading

# Replace these with your own Steam API key and Steam ID
STEAM_API_KEY = 'YOUR_STEAM_API_KEY'
STEAM_ID = 'YOUR_STEAM_ID'
STEAM_LIBRARY_FOLDERS_PATH = r'D:\Steam\steamapps\libraryfolders.vdf'

def fetch_steam_library():
    url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={STEAM_ID}&format=json&include_appinfo=true'
    response = requests.get(url)
    data = response.json()
    games = [{'name': game['name'], 'appid': game['appid']} for game in data['response']['games']]
    return games

def get_library_paths():
    with open(STEAM_LIBRARY_FOLDERS_PATH, 'r') as file:
        content = file.read()
    
    library_paths = re.findall(r'\"path\"\s+\"(.*?)\"', content)
    library_paths = [path.replace('\\\\', '\\') for path in library_paths]
    return library_paths

def get_installed_games():
    library_paths = get_library_paths()
    installed_game_ids = set()

    for path in library_paths:
        steamapps_path = os.path.join(path, 'steamapps')
        if os.path.exists(steamapps_path):
            for file in os.listdir(steamapps_path):
                if file.startswith('appmanifest_') and file.endswith('.acf'):
                    app_id = int(file.split('_')[1].split('.')[0])
                    installed_game_ids.add(app_id)
    
    return installed_game_ids

def pick_random_game():
    games = fetch_steam_library()
    installed_game_ids = get_installed_games()
    
    installed_games = [game for game in games if game['appid'] in installed_game_ids]
    if not installed_games:
        return None, []
    random_game = random.choice(installed_games)
    
    return random_game, installed_games

def show_result():
    random_game, installed_games = pick_random_game()
    if random_game is None:
        print("No installed games found.")
        return

    def open_game():
        # Launch the game using the Steam URL protocol
        steam_url = f"steam://run/{random_game['appid']}"
        webbrowser.open(steam_url)
        root.after(3000, show_picked_game)  # Ensure this runs in the main thread after a delay to allow game to start

    def show_picked_game():
        label.config(text="Congratulations!")
        result_label.config(text=f"The picked game is:\n{random_game['name']}")
        dynamic_label.config(text="")
        stop_cycling.set()  # Stop the cycling of game names

    # Create the main window
    root = tk.Tk()
    root.title("Random Game Picker")

    # Create and place the labels
    label = tk.Label(root, text="Picking random game", font=("Helvetica", 16))
    label.pack(pady=10)

    dynamic_label = tk.Label(root, text="", font=("Helvetica", 14))
    dynamic_label.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=10)

    # Set the size of the popup window
    root.geometry("400x250")

    stop_cycling = threading.Event()

    def update_text():
        if not stop_cycling.is_set():
            random_game_title = random.choice(installed_games)['name']
            dynamic_label.config(text=random_game_title)
            root.update()
            root.after(100, update_text)  # Continue updating text every 100 ms

    # Start the game picking process
    root.after(1000, update_text)
    threading.Thread(target=open_game).start()  # Start the game opening in a new thread

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    show_result()
