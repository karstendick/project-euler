#include <iostream>

int main (int argc, char * const argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
	long int max = 4000000;
	long int fi = 1, fii = 2;
	long int sum = 0;
	long int new_fi = 0, new_fii = 0;
	
	while(fi <= max && fii<=max)
	{
		if(fi % 2 == 0)
			sum += fi;
		if(fii % 2 == 0)
			sum += fii;
		
		new_fi = fi + fii;
		new_fii = fii + new_fi;
		
		fi = new_fi;
		fii = new_fii;
	}
	
	std::cout << "Answer:\t" << sum << std::endl;
	
    return 0;
}
