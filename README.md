# Steam Random Picker

## Introduction
Steam Random Picker is a Python-based application that helps you select a game at random from your installed Steam library. This tool is perfect for gamers who have a large collection of games and struggle with choosing what to play next.

## Features
- Fetches your entire owned games library via Steam's API.
- Filters the games to show only those installed on your local machine.
- Randomly picks a game and offers a quick link to launch it.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.x installed on your system.
- Access to your Steam API key and Steam ID.
- Your local path to the Steam libraries.

## Obtaining Your Steam API Key
To use this tool, you will need a Steam API key. Here’s how you can obtain one:
1. Log in to your Steam account through the [Steam Community website](https://steamcommunity.com/).
2. Visit the following URL to register for an API key: [Steam Web API Key Registration](https://steamcommunity.com/dev/apikey).
3. Enter the domain name you will use this API key for, or you can use `localhost` if you are calling the API from your local machine.
4. Agree to the terms of use and click "Register".
5. Store your API key safely, and do not share it publicly.

## Setup
1. Clone the repository to your local machine.
2. Install the necessary Python libraries:
3. Open the `steam_random_picker.py` script and replace `YOUR_STEAM_API_KEY` and `YOUR_STEAM_ID` with the API key and Steam ID you obtained.

## Usage
Run the script using Python:
A graphical interface will appear, and a game will be randomly selected.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests to enhance the functionalities.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
