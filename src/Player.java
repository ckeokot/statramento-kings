/*
    Statramento Kings - A Discord bot for 2K League Analysis
    Copyright (C) 2020 Christopher Keokot, Kevin Tran, Zain Ali

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

public class Player {
	private int id;
	private String name;
	private String team;
	private int min; //Minutes played
	
	private int fgm; //Field goal make
	private int fga; //Field goal attempts
	private double fgp; //Field goal %
	
	private int fg3m; //3 Point makes
	private int fg3a; //3 Point attempts
	private double fg3p; //3 Point %
	
	private int ftm; //Free throw makes
	private int fta; // Free throw attempts
	private double ftp; //Free throw %
	
	private int oreb; //Offensive rebounds
	private int dreb; //Defensive rebounds
	private int reb; //Rebounds
	private int ast; //Assists
	private int pf; //Personal fouls
	private int stl; //Steals
	private int to; //Turnovers
	private int blk; //Blocks
	private int pts; //Points
	
	private double per; //Player Efficiency Rating
	
	
	
	//Player Constructor 
	public Player(String[] s){
		id = Integer.parseInt(s[0]);
		name = s[1];
		team = s[2];
		min = Integer.parseInt(s[5]);
		fgm = Integer.parseInt(s[6]);
		fga = Integer.parseInt(s[7]);
		fgp = Double.parseDouble(s[8]);
		fg3m = Integer.parseInt(s[9]);
		fg3a = Integer.parseInt(s[10]);
		fg3p = Double.parseDouble(s[11]);
		ftm = Integer.parseInt(s[12]);
		fta = Integer.parseInt(s[13]);
		ftp = Double.parseDouble(s[14]);
		oreb = Integer.parseInt(s[15]);
		dreb = Integer.parseInt(s[16]);
		reb = Integer.parseInt(s[17]);
		ast = Integer.parseInt(s[18]);
		pf = Integer.parseInt(s[19]);
		stl = Integer.parseInt(s[20]);
		to = Integer.parseInt(s[21]);
		blk = Integer.parseInt(s[22]);
		pts = Integer.parseInt(s[23]);
		
		calcPer();
	}
	
	/**
	* The calcPer() method calculates the PER of the player
	* @param nothing
	* @return nothing 
	*/
	private void calcPer() {
		per = (fgm*85.910) + (stl*53.897) + (fg3m*51.757) + (ftm*46.845) + (blk*39.190) + (oreb*39.190) + (ast*34.677) + (dreb*14.707);
		per -= ((pf*17.174) + ((fta-ftm)*20.091) + ((fga-fgm)*39.190) + (to*53.897));
		per *= (1/(double)min);
	}
	
	/**
	* The toString() method prints the id, name, team, and PER of the player
	* @param nothing
	* @return String 
	*/
	public String toString() {
		//return id + " " + name + " " + team + " " + min + " " + fgm + " " + fga + " " + fgp + " " + fg3m + " " + fg3a + " " + fg3p + " " + ftm + " " + fta + " " + ftp + " " + oreb + " " + dreb + " " + reb + " " + ast + " " +pf + " " + stl + " " + to + " " + blk + " " + pts;
		return id + "," + name + "," + team  + "," + per;
	}
}
