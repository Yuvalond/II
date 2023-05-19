#ifndef EXAMPLE_H
#define EXAMPLE_H

class Example{
private:
	int* arr;
	int n; 
public:
	Example();
	Example(int n); 
	Example(const Example& copy); 
	~Example(); 
	void Vvod(); 
	void Metod1();
	void Metod2(); 
	void Sum(); 
	
	void Vivod(); 
	void Create(); 
};
#endif