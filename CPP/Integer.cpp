/*
Developed by: Vidhi Subudhi
On Sept 2024
Email ID: mailtovidhisubudhi@gmail.com


Basic Integer class that converts primitive int data into object (here it is Integer)
and various functionalities like converting object -> primitive, string to -> object and vice versa
string -> int and vice-versa.

Learning outcome: Use of various Constructor, Understanding static and non-static member functions
*/

#include<iostream>
#include<cstdlib>

using namespace std;

class Integer
{
	private:
		int val;	//A filed to store data 
		
		//Private member function that can be used only inside the class
		//The function given below reverse a string
		static void rev(char *s)
		{
			int len = 0;			//To store number of characters in the string
			char temp;				//A temporary variable used during character swapping
			while(s[len] != '\0')	// Loop to find out string length
			{
				len++;
			}
			
			//Desired swapping logic to alter position of characters in the string
			for(int i=0; i<=len/2; i++)
			{
				temp = s[i];
				s[i] = s[len-1-i];
				s[len-1-i] = temp;
			}
		}
	public:
		Integer()					//Default Constructor
		{
			val = 0;
		}	
		Integer(int n)				//Parameterized Constructor
		{
			val = n;
		}
		Integer(Integer& n)			//Copy Constructor
		{
			val = n.val;
		}
		
		int parseInt()				//Returns primitive int
		{
			return val;
		}
		char *toString()			//Returns string conversion of data
		{
			char *str;
			int i = 0;
			int temp = val;
			str = (char *)malloc(7 * sizeof(char)); //Dynamically allocating mermory for the string output
			
			while(temp > 0)
			{
				str[i] = (temp%10) + 48;	//ASCII minus 48 will give the numeric value
				temp = temp/10;
				i++;
			}
			str[i] = '\0';			//NULL character (\0) must be at the end of the string
			rev(str);
			return str;
		}
		
		//Static method to the same as above
		static char *toString(int n)	
		{
		    char *str;
			int i = 0;
			str = (char *)malloc(7 * sizeof(char));
			
			while(n > 0)
			{
				str[i] = (n%10) + 48;
				n = n/10;
				i++;
			}
			str[i] = '\0';
			rev(str);
			return str;
		}
};

int main()
{
	Integer p(274);		//Creating Object
	cout<<"Number is "<<p.parseInt()<<endl;	//Calling methods
	cout<<"Numbre in string is "<<p.toString()<<endl;
	cout<<"Converted to string is "<<Integer::toString(563)<<endl;
	return 0;
}
