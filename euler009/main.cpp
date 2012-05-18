#include <iostream>
using namespace std;

int main (int argc, char * const argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
	int a,b,c;
	int ans;
	for(int m=1; m<=1000; ++m)
		for(int n=m+1; n<=1000; ++n)
		{
			a = 2*m*n;
			b = n*n - m*m;
			c = m*m + n*n;
			if(a+b+c == 1000)
			{
				cout << "a=" << a << ", b=" << b << ", c=" << c << endl;
				ans = a*b*c;
			}
		}
	std::cout << "Answer:\t" << ans << std::endl;
	
    return 0;
}
