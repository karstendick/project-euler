#include <iostream>
#include <cmath>
#include <climits>

using namespace std;

bool isprime(const int num)
{
	if(num % 2 == 0) return false;
	int n = floor(sqrt(num));
	for(int i=3; i<=n; i+=2)
		if (num % i == 0) return false;
	return true;
}

int main (int argc, char * const argv[]) {
	unsigned long long sum = 2;
	long max = 2000000;
    for(long i=3; i<max; i+=2)
		if(isprime(i))
		{
			sum += i;
			//cout << i << endl;
		}
	cout << "sum:\t" << sum << endl;
	cout << "max:\t" << LONG_MAX << endl;
    return 0;
}
