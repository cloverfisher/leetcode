package max;

import java.util.HashMap;

import com.apple.crypto.provider.HmacMD5;
import com.sun.org.apache.xalan.internal.xsltc.compiler.Template;



public class Solution {
	final static int MAX = 65535;
    public static int maxPoints(Point[] points) {
        int returnnum = 0;
        int length1 = points.length;
        
        if(length1<=2)
            return length1;
        float array[][] = new float[length1][length1];
        
         for(int i = 0;i < length1;i++)
             for(int j = 0; j < length1; j++)
                 array[i][j] = 0;
        
        int assetnum[] = new int[length1];
        for(int i = 0; i < length1; i++)
            assetnum[i] = 1;
        for(int i = 0; i < length1; i++)
        {
//        	if(i>0)
//        		continue;
        	for(int j = i+1; j < length1; j++)
        	{
        		if((points[i].getX()==points[j].getX())&&(points[i].getY()==points[j].getY()  )  )
        		{
        		    array[i][j]=MAX-1;
        		    array[j][i]=MAX-1;
        		    assetnum[i]++;
        		    assetnum[j]++;
        		}
        		else if(points[i].getX()-points[j].getX() == 0 )
        		{
        			array[i][j] = MAX;
        			array[j][i] = MAX;
        		}
        		else {
        			float heihei = points[i].getY()-points[j].getY();
        			float haha = points[i].getX()-points[j].getX();
        			float temp = heihei/haha;
        			System.out.println(temp);
				//	float temp =  (points[i].getY()-points[j].getY())/(points[i].getX()-points[j].getX());
					array[i][j] = temp;
					array[j][i] = temp;
        		}
        	}
        }
        int pointnum[] = new int[length1];
        for(int i = 0 ; i < length1 ; i++)
            pointnum[i] = 0;
    
        for(int i = 0 ; i < length1; i++)
        {
        	HashMap<Float , Integer > hm = new HashMap<Float, Integer>();
        	
        	for(int j = 0; j < length1 ; j++)
        	{
        		if(i==j)
        			continue;
        	    if(array[i][j] == MAX-1)
        	        continue;
        		if(!hm.containsKey(array[i][j]))
        			hm.put(array[i][j], 0);
        		int temp = hm.get(array[i][j]);
        		hm.put(array[i][j], temp+1);
        		if(pointnum[i]<= temp)
        			pointnum[i] = temp+1;
            	   		
        	}
        }
        for(int i = 0 ; i < length1; i++)
        {
        	System.out.println("array:"+pointnum[i] + "asset:"+assetnum[i]);  
        	if(returnnum< pointnum[i]+assetnum[i])
        		returnnum = pointnum[i] + assetnum[i];
        }
        return returnnum;
    }
    
    public static void main(String [ ] args)
    {
    	Point p[] = new Point[9];
    	p[0] = new Point(84, 250);
    	p[1] = new Point(0,0);
    	p[2] = new Point(1,0);
    	p[3] = new Point(0,-70);    	
    	p[4] = new Point(0,-70);
    	p[5] = new Point(1,-1);
    	p[6] = new Point(21,10);
    	p[7] = new Point(42,90);
    	p[8] = new Point(-42,-230);
    	int i = maxPoints(p);
    	System.out.println(i);
    }
}

