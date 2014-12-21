//what a boring question and a boring solution! no use at all


class Solution {
public:
    double pow(double x, int n) {
        int i,j,k;
        double returnnum = 1;
        if(n==0)
            return 1;
        else if(n>0)
        {
            while(n>0)
            {

                if(returnnum*x*x == returnnum)
                {
                    if (n%2==1)
                        return returnnum*x;
                    else
                        return returnnum;
                }
                returnnum*=x;
                n--;
            }
        }
        else if ( n< 0)
        {
            while(n<0)
            {

                if(returnnum/x/x == returnnum)
                {
                    if (n%2==1)
                        return returnnum/x;
                    else
                        return returnnum;               
                }
                returnnum = returnnum / x;
                n++;
            }
        }
        return returnnum;
    }
};