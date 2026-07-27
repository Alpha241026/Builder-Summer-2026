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
    cout << "Enter element to search: ";
    cin >> x;

    int l = 0;
    int u = n - 1;
    int answer = n;

    while (l <= u) {
        int mid = l + (u - l) / 2;   // safer than (l+u)/2

        if (arr[mid] >= x) {
            answer = mid;      // store current candidate
            u = mid - 1;       // search for an earlier one
        }
        else {
            l = mid + 1;       // answer must be on the right
        }
    }

    if (answer == n)
        cout << "Lower Bound does not exist. Returning index " << n;
    else
        cout << "Lower Bound of " << x << " is at index " << answer << " (value = " << arr[answer] << ")";

    return 0;
}