#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter size of sorted array: ";
    cin >> n;

    int arr[n];
    cout << "Enter array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int x;
    cout << "Enter element to find insert position for : ";
    cin >> x;

    int l = 0;
    int u = n - 1;
    int answer = n;

    while (l <= u) {
        int mid = l + (u - l) / 2;   

        if (arr[mid] >= x) {
            answer = mid;      
            u = mid - 1;       
        }
        else {
            l = mid + 1;       
        }
    }

    cout << " Search Insert Position = " << answer;

    return 0;
}