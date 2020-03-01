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

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class PlayerModel {
	private static ArrayList<String[]> str = new ArrayList<String[]>();
	private static ArrayList<Player> player = new ArrayList<Player>();
	
	public static void main(String[] args) throws IOException {
		readFiles();
		printData();
	}
	
	/**
	* The readFiles() gets the player data and stores it in the player arraylist
	* @param nothing
	* @return nothing 
	*/
	private static void readFiles() {
		BufferedReader br = null;
		try {
			br = new BufferedReader(new FileReader("2K Player Stats.csv"));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		String s;
		try {
			br.readLine();
			while((s = br.readLine()) != null) {
				String[] x = null; 
				str.add(x = s.split(","));
			}
			for(int i = 0; i < str.size(); i++) {
				player.add(new Player(str.get(i)));
				System.out.println(player.get(i));
			}
			br.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	* The printData() method prints the player data into a csv
	* @param nothing
	* @return nothing 
	*/
	private static void printData() throws IOException {
		BufferedWriter bw = new BufferedWriter(new PrintWriter("PlayerStats.csv"));
		bw.write("ID,Name,Team,PER\n");
		for(int i = 0; i < player.size(); i++) {
			bw.write(player.get(i).toString() + "\n");
		}
		bw.close();
		System.out.println("\nWrite Successful.");
	}
}
