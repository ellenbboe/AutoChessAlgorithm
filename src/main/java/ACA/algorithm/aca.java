package ACA.algorithm;
import ACA.entity.Location;
import lombok.extern.slf4j.Slf4j;

import java.util.Collection;
import java.util.LinkedList;

@Slf4j
public class aca {
    int[][] maps = new int[10][10];
    int sum = 9;
    int count = 1;

    public Location step(int x,int y)
    {
        if(maps[x][y] == 1)
        {
            count++;
            if(count == sum)
            {
                return new Location(x,y);
            }
            x=x+1;
        }else{
            y=y+1;
        }
        step(x,y);
        return new Location(x,y);
    }

    public void go()
    {
        for(int i = 0;i<maps.length;i++)
        {
            LinkedList<Location> results = new LinkedList<>();
            results.add(step(i,0));
            for(Location a :results)
            {
               log.info(a.toString());
            }
        }
    }

    public static void main(String[] args) {
        aca a = new aca();
        a.maps[9][9]= 1;
        a.maps[5][9]= 1;
        a.go();
    }
}