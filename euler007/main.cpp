#include <iostream>
#include <cmath>
using namespace std;

bool isprime(const int num)
{
	if(num % 2 == 0) return false;
	int n = ceil(sqrt(num));
	for(int i=3; i<= n; i+=2)
		if (num % i == 0) return false;
	return true;
}

int main (int argc, char * const argv[]) {
	
	//long int p = 0;
	int pcount = 1;
	for(long int i=3; i<2000000000; i+=2)
	{
		if(isprime(i))
		{
			++pcount;
			if(pcount == 10001)
			{
				cout << "10001st prime:\t" << i << endl;
				return 0;
			}
		}
	}
	cout << "pcount:\t" << pcount << endl;
    return 0;
}
