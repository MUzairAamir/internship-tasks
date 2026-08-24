#include<stdio.h>
#include<iostream>
#include<cmath>

using namespace std;

void prime(int number) {
	int count = 0;
	int counter =0;
	do{
	
	if (number < 2) {
		cout << "this is not a prime number1";
		count++;
	}
	else {
		for (int i = 2; i <= sqrt(number); i++) {
			if (number % i == 0) {
				
				count++;
			}
		}
		
		}
		
		if (count == 0) {
			cout << number << " is a prime number\n";
			number--;
			counter++;
			cout<< " now checking this number :"<< number <<endl;
		  }
		  if(count>0){
		cout<<"this is not a prime number:"<< number<< endl;
		if(counter>0){
			count=0;
			number--;
		}
		if(counter==0){
			break;
		
		}	
		}
	}while(number>2);
if(counter>0){
	  cout<<"total prime numbers from 0 to your number is :"<<counter;
}	

}
int main() {
	int prime_number = 0;
	cout << "enter the number : ";
	cin >> prime_number;
	prime(prime_number);

}

