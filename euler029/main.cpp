#include <iostream>
#include <cmath>
#include <set>
#include <cfloat>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class factored_int
{
public:
	factored_int(int n)
	{
		//int max = n;
		int i=2;
		
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
	}
	
	void pow(int e)
	{
		for(int i=0; i<exps.size(); ++i)
			exps[i] *= e;
	}
	
	string tostring() const
	{
		string str = "";
		stringstream ss(stringstream::in | stringstream::out);
		for(int i=0; i<primes.size(); ++i)
			ss << primes[i] << "^" << exps[i] << ",";
		str = ss.str();
		return str;
	}
private:
	vector<int> primes;
	vector<int> exps;
};

int main (int argc, char * const argv[]) {
	set<string> S;
	vector<string> V;
	//long double n=0;
	//int count = 0;
	
	cout << "Max size:\t" << S.max_size() << endl;
	
	for(int a=2; a<=100; ++a)
		for(int b=2; b<=100; ++b)
		{
			factored_int fa(a);
			fa.pow(b);
			string str = fa.tostring();
			
			S.insert(str);
			V.push_back(str);
			//cout << a << "^" << b << "=\t" << str << endl;
			if(str == "") cin >> str;
		}
	
	cout << "Answer:\t" << S.size() << endl;
	S.insert("2^2,");
	cout << "New size:\t" << S.size() << endl;
	cout << "Max size:\t" << S.max_size() << endl;
	
	cout << "Vector size:\t" << V.size() << endl;
	sort(V.begin(), V.end());
	vector<string>::iterator it;
	it = unique(V.begin(), V.end());
	V.resize(it-V.begin());
	cout << "Vector size:\t" << V.size() << endl;
	
	//cout << "LDBL_MAX:\t" << LDBL_MAX << endl;
	
    return 0;
}
