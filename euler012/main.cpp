#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int funky_sigma(int n)
{
	int res = 0;
	for(int i=1; i<=n; ++i)
	{
		int inner_sum = 0;
		for(int j=1; j<=i; ++j)
		{
			inner_sum += cos(2*M_PI*j*n/i);
		}
		res += inner_sum/i;
	}
	return res;
}

unsigned long long int triangle(unsigned long long int n)
{
	return n * (n+1) /2;
}

unsigned long long int old_sigma(unsigned long long int n)
{
	int res=0;
	for(int i=1; i<=n; ++i)
		if(n%i == 0)
			++res;
	return res;
}

unsigned long long int sigma(unsigned long long int n)
{
	vector<unsigned long long int> primes;
	vector<unsigned long long int> exps;
	unsigned long long int i=2;
	
	while(n>1)
	{
		if(n % i == 0)
		{
			if(primes.empty())
			{
				primes.push_back(i);
				exps.push_back(1);
				n /= i;
				--i;
			}
			else
			{
				if(primes.back() == i)
					exps.back() += 1;
				else
				{
					primes.push_back(i);
					exps.push_back(1);
				}
				n /= i;
				--i;
			}
		}
		++i;
	}
	
	unsigned long long int res = 1;
	for(i=0; i<exps.size(); ++i)
	{
		res *= (exps[i]+1);
	}
	return res;
}

int main (int argc, char * const argv[]) {
    const unsigned long long int MAX = 100000;
	const unsigned long long int TARGET = 500;
	unsigned long long int i;
	unsigned long long int t;
	unsigned long long int s;
	unsigned long long int maxs = 0;
	for(i=1; i<=MAX; ++i)
	{
		t=triangle(i);
		s=sigma(t);
		if(s>maxs)
		{
			maxs = s;
			cout << i << ":\t\t" << t << "\t\t" << maxs << endl;
		}
		if(i%1000 == 0)
			cout << i << ":\t\t" << t << "\t\t" << s << endl;
		if(s > TARGET)
		{
			cout << "Found it!\n";
			cout << i << ":\t\t" << t << "\t\t" << s << endl;
			return 0;
		}
	}
	
    return 0;
}
