#include <iostream>

int main (int argc, char * const argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
	int n=0;
	for(int i=1; i<1000; ++i)
	{
		if(i % 3 == 0)
			n += i;
		else if(i % 5 == 0)
			n += i;
	}
	std::cout << "Answer:\t" << n << std::endl;
	std::cin >> n;
    return 0;
}
