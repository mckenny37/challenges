class Solution {
public:
    int getSum(int a, int b) {
        while(b != 0)
        {        
            int tmp = ((a & b & 0xffffffff) << 1); // limited to 32 bits
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
};