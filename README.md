# Shop Inventory Project - Board Games

The task was to create an app that allows a shop keeper to keep track of the items within their inventory. This project uses board games as the shop items. 

## Installation

To run the files enter the following into terminal:

```bash
createdb board_games

psql -d board_games -f db/board_games.sql

python3 console.py
```

## Usage

The app allows you to view, add, edit, and delete both the board games and the manufacturers of said board games. To view more details about an individual game or manufacturer, select its underlined name within the list. The app also shows when an item is low or out of stock. 
