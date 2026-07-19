#include <iostream>

using namespace std;

int main() {
    int size;
    cout << "Enter size of array : ";
    cin >> size;

    int arr[size];
    cout << "Enter size of array : ";
    for (int i=0;i<size;i++) {
        cin >> arr[i];
    }

    int largest = arr[0];
    for (int i=1;i<size;i++) {
        if (arr[i]>largest)
        largest = arr[i];
    }

    cout << "Largest element in array = "<<largest;
}