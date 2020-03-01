#    Statramento Kings - A Discord bot for 2K League Analysis
#    Copyright (C) 2020 Christopher Keokot, Kevin Tran, Zain Ali
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import csv
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

players = {}

PER_rank = 0

player_rank_list = []

with open('playerdata.csv', newline='') as playercsvfile:
    playerdata = csv.reader(playercsvfile, delimiter=',')
    for row in playerdata:
        Person_id, Player, Position, Team, Season_Type, GP, Min, FGM, FGA, FGPERCENT, FG3M, FG3A, FG3PERCENT, FTM, FTA, FTPERCENT, OREB, DREB, REB, AST, PF, STL, TOV, BLK, PTS, CareerHighPTS, eFGPERCENT, TSPERCENT, PER = row
        PER_rank += 1 
        players[Person_id] = {"Player": Player, "Position": Position, "Team": Team, "Season_Type": Season_Type, "GP": GP, "Min": Min, "FGM": FGM, "FGA": FGA, "FGPERCENT": FGPERCENT, "FG3M": FG3M, "FG3A": FG3A, "FG3PERCENT": FG3PERCENT, "FTM": FTM, "FTA": FTA, "FTPERCENT": FTPERCENT, "OREB": OREB, "DREB": DREB, "REB": REB, "AST": AST, "PF": PF, "STL": STL, "TOV": TOV, "BLK": BLK, "PTS": PTS, "CareerHighPTS": CareerHighPTS, "eFGPERCENT": eFGPERCENT, "TSPERCENT": TSPERCENT, "PER": PER, "PER_rank": PER_rank}
        player_rank_list.append(str(Player))

teams = {}

TEAM_Rank = 0

team_rank_list = []

with open('teamdata.csv', newline='') as teamcsvfile:
    teamdata = csv.reader(teamcsvfile, delimiter=',')
    for row in teamdata:
        Team, Nickname, Games_Played, Sum_Player_MIN, Team_MIN, Points, Field_Goals, Field_Goals_Attempted, FGPERCENT, Three_Pointers, Three_Pointers_Attempted, THREEPPERCENT, Offensive_Rebounds, Defensive_Rebounds, Normalized_OVR, Rounded_OVR, Assists, Steals, Turnovers, Blocked_Shots, Points1, PT_Differential, Opp_FGM, Opp_FGA, Opp_FGPERCENT, Opp_3PM, Opp_3PA, Opp_3PPERCENT, Opp_OREB, Opp_DREB, Opp_AST, Opp_STL, Opp_TOV, Opp_BLK = row
        TEAM_Rank += 1
        teams[Team] = {"Nickname": Nickname, "Games_Played": Games_Played, "Points": Points, "FGPERCENT": FGPERCENT, "Rounded_OVR": Rounded_OVR, "PT_Differential": PT_Differential, "Opp_FGPERCENT": Opp_FGPERCENT, "TEAM_Rank": TEAM_Rank}
        team_rank_list.append(str(Nickname))

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print()

#@bot.command()
#async def player(ctx, *, player):
#    for Person_id in players:
#        if str(players[str(Person_id)]["Player"]) == str(player):
#            await ctx.send(str(players[str(Person_id)]["Player"]) + 
#            '\nTeam: ' + str(players[str(Person_id)]["Team"]) + 
#            "\nPosition: " + str(players[str(Person_id)]["Position"]) + 
#            "\nRanking: " + str(players[str(Person_id)]["PER_rank"]) + 
#            "\nMinutes Per Game: " + str(int(int(str(players[str(Person_id)]["Min"])) / int(str(players[str(Person_id)]["GP"])))) +
#            "\nPoints Per Game: " + str(int(int(str(players[str(Person_id)]["PTS"])) / int(str(players[str(Person_id)]["GP"])))) +
#            "\nField Goal Percentage: " + str(players[str(Person_id)]["FGPERCENT"]) +
#            "\nRebounds: " + str(players[str(Person_id)]["REB"]) +
#            "\nBlocks: " + str(players[str(Person_id)]["BLK"]) +
#            "\nPER: " + str(players[str(Person_id)]["PER"])
#            )

@bot.command()
async def player(ctx, *, player):
    """!player player_name to search up a player's statistics"""
    for Person_id in players:
        if str(players[str(Person_id)]["Player"]) == str(player):
            embed = discord.Embed(title=str(players[str(Person_id)]["Player"]))
            if str(players[str(Person_id)]["Player"]) == "Bp":
                embed.set_thumbnail(url='https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600209.png')
            if str(players[str(Person_id)]["Player"]) == "worthingcolt":
                embed.set_thumbnail(url='https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600056.png')
            embed.add_field(name='Team: ', value=str(players[str(Person_id)]["Team"]), inline=False)
            embed.add_field(name="Position: ", value=str(players[str(Person_id)]["Position"]), inline=False)
            embed.add_field(name="Ranking: ", value=str(players[str(Person_id)]["PER_rank"]), inline=False)
            embed.add_field(name='Minutes Per Game: ', value=str(int(int(str(players[str(Person_id)]["Min"])) / int(str(players[str(Person_id)]["GP"])))), inline=False)
            embed.add_field(name='Points Per Game: ', value=str(int(int(str(players[str(Person_id)]["PTS"])) / int(str(players[str(Person_id)]["GP"])))), inline=False)
            embed.add_field(name='Field Goal Percentage: ', value=str(players[str(Person_id)]["FGPERCENT"]), inline=False)
            embed.add_field(name="Rebounds: ", value=str(players[str(Person_id)]["REB"]), inline=False)
            embed.add_field(name="Blocks: ", value=str(players[str(Person_id)]["BLK"]), inline=False)
            embed.add_field(name="PER: ", value=str(players[str(Person_id)]["PER"]), inline=False)
            await ctx.send(embed=embed)

@bot.command()
async def playerrankings(ctx, *, top):
    """!playerrankings X to get the top X players"""
    embed = discord.Embed(title="Player Rankings by PER")
    for n in range(int(top)):
        embed.add_field(name=str(n+1), value=str(player_rank_list[n]), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def teamrankings(ctx, *, top):
    """!teamrankings X to get the top X teams"""
    embed = discord.Embed(title="Team Rankings by OVR")
    for n in range(int(top)):
        embed.add_field(name=str(n+1), value=str(team_rank_list[n]), inline=False)
    await ctx.send(embed=embed)



@bot.command()
async def team(ctx, *, team):
    """!team team_name to search up a team's statistics"""
    for Team in teams:
        if str(teams[str(Team)]["Nickname"]) == str(team):
            embed = discord.Embed(title=str(teams[str(Team)]["Nickname"]))
            if str(teams[str(Team)]["Nickname"]) == "Kings Guard Gaming":
                embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1212461523706101761/chRjVpD5_400x400.jpg')
                embed.set_image(url='https://drive.google.com/uc?id=113ttB3Bveyl3pzE8zeCyGrUy80cmbwYf')
            embed.add_field(name="Ranking: ", value=str(teams[str(Team)]["TEAM_Rank"]), inline=False)
            embed.add_field(name='Points Per Game: ', value=str(int(int(str(teams[str(Team)]["Points"])) / int(str(teams[str(Team)]["Games_Played"])))), inline=False)
            embed.add_field(name="Field Goal Percentage: ", value=str(teams[str(Team)]["FGPERCENT"]), inline=False)
            embed.add_field(name="Point Differential: ", value=str(teams[str(Team)]["PT_Differential"]), inline=False)
            embed.add_field(name="Opponent Field Goal Percentage: ", value=str(teams[str(Team)]["Opp_FGPERCENT"]), inline=False)
            await ctx.send(embed=embed)

#FILL IN YOUR BOT TOKEN
TOKEN = ''

bot.run(TOKEN)