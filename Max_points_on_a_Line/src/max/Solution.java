package max;

import java.util.HashMap;

import com.apple.crypto.provider.HmacMD5;
import com.sun.org.apache.xalan.internal.xsltc.compiler.Template;



public class Solution {
	final int MAX = 9999999;
    public int maxPoints(Point[] points) {
        int returnnum = 0;
        int length1 = points.length;
        
        float array[][] = null;
        
        for(int i = 0; i < length1; i++)
        {
        	for(int j = i; j < length1; j++)
        	{
        		if(i==j)
        			array[i][j]=0;
        		else if(points[i].getX()-points[j].getX() == 0 )
        		{
        			array[i][j] = MAX;
        			array[j][i] = MAX;
        		}
        		else {
					float temp =  (points[i].getY()-points[j].getY())/(points[i].getX()-points[j].getX());
					array[i][j] = temp;
					array[j][i] = temp;
        		}
        	}
        }
        int pointnum[];
    
        for(int i = 0 ; i < length1; i++)
        {
        	HashMap<Float , Integer > hm = new HashMap<Float, Integer>();
        	for(int j = 0; j < length1 ; j++)
        	{
        		int temp = hm.get(array[i][j]);
        		hm.put(array[i][j], temp+1);
        	}
        	hm.values()
        }
        return returnnum;
    }
}
