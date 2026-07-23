#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter size of sorted array: ";
    cin >> n;

    int arr[n];
    cout << "Enter array elements: ";
    for (int i=0;i<n;i++) {
        cin >> arr[i];
    }

    int x;
    cout << "Enter element to search: ";
    cin >> x;

    int mid,l=0,u=n-1,found=0;

    while (l<=u && found==0) {
        
        mid = (l+u)/2;

        if (arr[mid]==x) {
            found = 1;
            break;
        }
        else if (x>arr[mid])
            l = mid+1;
        else
            u = mid-1;

        
    }

    if(found==1)
    cout<<x<<" found at index "<< mid;
    else
    cout<<x<<" not found in array";
}