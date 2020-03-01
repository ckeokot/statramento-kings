![Statramento Kings Logo](/logo.jpg)

# Statramento Kings
Statramento Kings is a Discord bot created for NBA 2K League statistics and analysis. This project was created during SacHacks 2020 and won 1st Place for the Sacramento Kings Track.

# Motivation
The Sacramento Kings Track for SacHacks 2020 was all about analyzing player and team data from the NBA 2k League. More specifically, the goal was to create a player model that ranks all 126 league players, as well as a team model that ranks all 21 teams. In addition to this, another goal was to look specifically at Kings Guard Gaming and determine what were the team's biggest strengths, weaknesses, and so forth.

The decision to make a bot on Discord came from the idea that a community for the NBA 2K League could be built on Discord. Also, a Discord bot that displayed statistics and analysis would be much more useful for players and coaches in the NBA 2K League compared to a website.

# Screenshots
![Player Stats Screenshot](/screenshot_2.png)

![Team Stats Screenshot](/screenshot_1.png)

# How It Works
![How It Works Flowchart](/flowchart.png)

1. NBA 2K League player and team statistics are read from a .xlsx file by Player.java and PlayerModel.java
2. The player model and team model calculations are done in Java and are written to playerdata.csv and teamdata.csv
3. The csv files and main.py are uploaded to a Google Cloud Platform Virtual Machine instance
4. main.py reads from the csv files and outputs analysis based on user commands using discord.py

# Built With
* [Java](https://www.java.com/) - Player model and team model calculations
* [Python](https://www.python.org/) - Backend
* [discord.py](https://github.com/Rapptz/discord.py) - API wrapper for Discord in Python
* [Google Cloud Platform](https://cloud.google.com/) - Virtual Machine instance

# Authors
* **Christopher Keokot** - Python Backend, Google Cloud Platform Virtual Machine, discord.py Frontend - [ckeokot](https://github.com/ckeokot)
* **Kevin Tran** - Java Backend
* **Zain Ali** - Design

# License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/ckeokot/statramento-kings/blob/master/LICENSE.md) file for details.
