// C program to demonstrate working of extended
// Euclidean Algorithm
#include <stdio.h>
 
// C function for extended Euclidean Algorithm
int gcdExtended(int a, int b, int *x, int *y)
{
    // Base Case
    if (a == 0)
    {
        *x = 0;
        *y = 1;
        return b;
    }
    a = 35;
    b = 5;
    
    int x1, y1; // To store results of recursive call
    int gcd = gcdExtended(b%a, a, &x1, &y1);
 
    // Update x and y using results of recursive
    // call
    *x = y1 - (b/a) * x1;
    *y = x1;
 
    return gcd;
}
// Driver Program
int main()
{
    unsigned long int a = 269164;
    unsigned long int b = 653599;
    unsigned long int p = 1234577;
    printf("%llu\n", (a*b) % p);
}