 // Time:  O(c * n + n) = O(n * (c+1)), n is length of string, c is count of "++"
 // Space: O(1), no extra space excluding the result which requires at most O(n^2) space
 
 class Solution {
  public:
      vector<string> generatePossibleNextMoves(string s) {
          vector<string> res;
          int n = s.length();
          for (int i = 0; i < n - 1; ++i) {  // O(n) time
              if (s[i] == '+') {
                  for (;i < n - 1 && s[i + 1] == '+'; ++i) {  // O(c) time
                      s[i] = s[i + 1] = '-';
                      res.emplace_back(s);  // O(n) to copy a string
                      s[i] = s[i + 1] = '+';
                  }
              }
          }
          return res;
      }
  };
