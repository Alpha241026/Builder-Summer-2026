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

    int currentSum=arr[0]; //currentSum = best subarray sum ending at current index
    int bestSum=arr[0]; //bestSum = best subarray sum found so far

    for (int i=0;i<n-1;i++) {
        
        if(arr[i+1]>currentSum+arr[i+1])
            currentSum=arr[i+1];
        else
        currentSum+=arr[i+1];
        
        if(currentSum>bestSum)
            bestSum = currentSum;

    }

    cout << "Sum by maximum subarray: ";
    cout << bestSum;
}








