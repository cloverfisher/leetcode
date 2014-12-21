public class Solution {
    public int singleNumber(int[] A) {
    	Map<Integer, Integer> map = new HashMap<Integer, Integer>();
      //  HashMap map<int, int>= new HashMap<int,int>();
        for (int i : A)
        {
            try
            {
              int j = map.get(i);  
              map.put(i,j+1);
            }
            catch(Exception e)
            {
                map.put(i,1); 
            }
            if(map.get(i)==3)
                map.remove(i);
        }
        int k = (Integer) map.keySet().toArray()[0];
     
      return k;
    }
}