#include <stdlib.h>
#include <stdio.h>
#include "Example.h"
#include <iostream>

using namespace std;

Example* func(int size){
	Example* objtemp;
	objtemp = new Example(size);
	objtemp -> Create();
	objtemp -> Vvod();
	objtemp -> Metod2();
	return objtemp;
}

int main()
{
	int n;
	cin >> n;
	if(n < 2 || n % 2 != 0){
		cout << n << "?";
	}
	else{
		cout << n << endl;
		Example* obj;
		obj = func(n);
		obj -> Metod1();
		Example* obj2 = new Example(*obj); //создание и присвоенеи
		obj2 -> Metod2();
		obj -> Vivod();
		obj -> Sum();
		obj2 -> Vivod();
		obj2 -> Sum();
		obj2 = obj;
		obj -> Metod1();
		obj2 -> Vivod();
		obj2 -> Sum();
		delete obj;
		delete obj2;
	}
	return(0);
}
