//
//  main.cpp
//  Basic Calculator Using Function
//
//  Created by Farhan Niloy on 3/8/23.
//

#include <iostream>
#include <cmath>

using namespace std;

double calcFunction (double a, double b, char op);

int main(int argc, const char * argv[]) {
    double a{}, b{};
    char choice{};

    cout<< "Please Input two numbers and an operator! " <<endl;
    cout<<"Number 1: ";
    cin>> a;
    cout<<"Number 2: ";
    cin>> b;
    cout<< "Action: (+ - * /  ^ Q (quit) ) ";
    cin>>choice;
    
    while (choice != 'Q' || 'q') {
        
        cout<<"result: " <<calcFunction(a, b, choice) <<endl;
        
        double a{}, b{};
        int  choice = '+';

        cout<< "Please Input two numbers and an operator! " <<endl;
        cout<<"Number 1: ";
        cin>> a;
        cout<<"Number 2: ";
        cin>> b;
        cout<< "Action: (+ - * /  ^ Q (quit) ) ";
        cin>>choice;
        
    }
    
    
    return 0;
}

double calcFunction (double a, double b, char op) {
    
    double result{};
    
    
    if (op == '+') {
        result = a+b;
    }
    else if (op == '-') {
        result = a-b;
    }
    else if (op == '*') {
        result = a*b;
    }
    else if (op == '/') {
        result = a/b;
    }
    else if (op == '^') {
        result = pow(a,b);
    } else {
        cout<<"Please enter valid operations! ";
    }
    
    
    
    return result;
    
};
