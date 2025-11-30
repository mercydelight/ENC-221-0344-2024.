#include <iostream>
using namespace std;

 // Define the Roommate class
class Roommate {
public:
    string name;
    int age;
    string gender;
    string height;
    string complexion;
    string hobby;
};

    // To print all details

int main() {
    Roommate mate;
    mate.name="shanice";
    mate.age= 20;
    mate.gender="female";
    mate.height="169";
    mate.complexion="dark";
    mate.hobby="singing";
    
    cout << "Roommate Details\n";
    cout << "Name: " << mate.name << endl;
    cout << "Age: " << mate.age << endl;
    cout << "Gender: " << mate.gender << endl;
    cout << "Height: " << mate.height << endl;
    cout << "Complexion: " << mate.complexion << endl;
    cout << "Hobby: " << mate.hobby << endl;

    return 0;
};
