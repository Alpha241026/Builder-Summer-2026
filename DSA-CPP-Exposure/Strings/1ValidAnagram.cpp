#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1,s2;
    cout << "Enter first string: ";
    cin >> s1;
    cout << "Enter second string: ";
    cin >> s2;

    if(s1.length() != s2.length()){
        cout << "Not Anagrams";
        return 0;
    }

    int freq[26]={0};
    for(int i=0;i<s1.size();i++) {
        freq[s1[i]-'a']++;
        freq[s2[i]-'a']--;
    }

    int count = 0; 

    for(int i = 0; i < 26; i++) {
        if(freq[i] != 0) {
            cout << "Not Anagrams";
            return 0;
        }
    }

    cout << "Anagrams";

    return 0;
}