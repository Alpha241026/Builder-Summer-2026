#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter size of array: ";
    cin >> n;

    int arr[n];
    cout << "Enter array elements: ";
    for (int i=0;i<n;i++) {
        cin >> arr[i];
    }

    int temp = 0;

    for (int i=0,j=0;j<n;j++) {
        if(arr[j]!=0) {
            arr[i]=arr[j];
            i++;
        }
        temp=0;
    }

    cout << "Rearranged array with zeros in the end: ";
    for (int i=0;i<n;i++) {
        cout << arr[i];
    }
}

