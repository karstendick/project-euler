#include <iostream>
#include <cmath>

using namespace std;

const double NUM = 600851475143.0;

bool isprime(const int num);

int main (int argc, char * const argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
	
	int n=floor(sqrt(NUM));
	int ans = 0;
	
	for(int i=3; i<=n; i+=2)
	{
		if(((long long)(NUM) % i == 0) && isprime(i))
			ans = i;
	}
	cout << "Answer:\t" << ans << endl;
	
    return 0;
}

bool isprime(const int num)
{
	if(num % 2 == 0) return false;
	int n = floor(sqrt(num));
	for(int i=3; i<= n; ++i)
		if (num % i == 0) return false;
	return true;
}
