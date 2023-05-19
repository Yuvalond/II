#include "Example.h"
#include <iostream>

using namespace std;

Example::Example(){
	cout << "Default constructor" << endl;
}

Example::Example(int n){
	this -> n = n;
	cout << "Constructor set" ;
}

Example::Example(const Example& copy){ //конструктор копии 
	n = copy.n;
	arr = new int[n];
	
	for(int i = 0; i < n; i++){
		this -> arr[i] = copy.arr[i];
	}
	cout << endl;
	cout << "Copy constructor" ;
}

void Example::Create(){
	this -> arr = new int[n];
}

Example::~Example(){
	cout << endl;
	cout << "Destructor" ;
	delete[] arr;
}

void Example::Vvod(){
	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}
}

void Example::Metod1(){
	for(int i = 0; i < n; i += 2){
		arr[i] += arr[i + 1];
	}
}

void Example::Metod2(){
	for(int i = 0; i < n; i += 2){
		arr[i] *= arr[i + 1];
	}
}

void Example::Sum(){
	int Sum = 0;
	for(int i = 0; i < n; i++){
		Sum += arr[i];
	}
	cout << endl;
	cout << Sum;
}

void Example::Vivod(){
	cout << endl;
	for (int i = 0; i < n - 1 ; i++){
		cout << arr[i] << "  ";
	}
	cout << arr[n-1];
}
