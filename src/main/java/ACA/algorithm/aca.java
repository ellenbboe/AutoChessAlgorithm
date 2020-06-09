package ACA.algorithm;

import ACA.entity.Location;

import java.util.LinkedList;

public class aca {
    int[][] maps = new int[10][10];
    LinkedList<Location> results = new LinkedList<>();
    int sum = 9;
    int count = 1;




    public Location step(int x,int y)
    {
        if(maps[x][y] == 1)
        {
            count++;
            x=x+1;
        }else{
            y=y+1;
        }
        step(x,y);
        return new Location(x,y);
    }
}