#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cout << "Enter size of array: ";
    cin >> n;

    string arr[n];

    cout << "Enter list of words: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    string prefix = "";

    for (int i = 0; i < arr[0].size(); i++) {

        for (int j = 1; j < n; j++) {

            if (i >= arr[j].size() || arr[0][i] != arr[j][i]) {
                cout << "Longest Common Prefix = " << prefix;
                return 0;
            }

        }

        prefix += arr[0][i];
    }

    cout << "Longest Common Prefix = " << prefix;

    return 0;
}