#include <iostream>
#include <cmath>

using namespace std;

bool ispalindrome(int n)
{
	int a[6];
	int i;
	for(i=0; i<6; ++i)
	{
		a[i] = n % 10;
		n /= 10;
	}
	for(i=0; i<6; ++i)
	{
		if(a[i] != a[5-i])
			return false;
	}
	return true;
}

int main (int argc, char * const argv[]) {
    int ans=0, n=0;
	int ansi, ansj;
	
	for(int i=100; i<1000; ++i)
		for(int j=100; j<1000; ++j)
		{
			n = i*j;
			if((n > ans) && ispalindrome(n))
			{
				ans = n;
				ansi = i;
				ansj = j;
			}
		}
	cout << "Answer:\t" << ans << " = " << ansi << " * " << ansj << endl;
    return 0;
}
