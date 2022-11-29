#include<iostream>
using namespace std;

int main()
{
	int n;
	
	cout << "Enter your n's value: " << endl;
	cin >> n;
	
	cout << "C" << n << "H" << 2*n <<endl;
	
	switch (n)
	{
		case 1: cout << "Methane" <<endl;
				break;
		case 2: cout << "Ethane" <<endl;
				break;
		case 3: cout << "Prop" <<endl;
				break;
		case 4: cout << "Butane" <<endl;
				break;
		case 5: cout << "Pentane" <<endl;
				break;
		case 6: cout << "Hexane" <<endl;
				break;
		case 7: cout << "Heptane" <<endl;
				break;
		case 8: cout << "Octane" <<endl;
				break;
		case 9: cout << "Nonane" <<endl;
				break;
		case 10: cout << "Decane" <<endl;
				break;
		case 11: cout << "UnDecane" << endl;
				break;
		case 12: cout << "DoDecane"<< endl;
				break;		
	}
	return 0;
}
