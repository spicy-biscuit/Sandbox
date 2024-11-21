#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "hello world!\n";
    cout << "type your name: \n";
    string x;
    getline(cin, x);
    cout << "\n" << x << "\n";
    return 0;
}