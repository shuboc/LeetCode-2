// Time:  O(n * C(n - 1, c - 1)), n is length of str, c is unique count of pattern,
//                                there are H(n - c, c - 1) = C(n - 1, c - 1) possible splits of string,
//                                and each one costs O(n) to check if it matches the word pattern.
// Space: O(n + c) 

class Solution {
public:
    bool wordPatternMatch(string pattern, string str) {
        unordered_map<string, char> w2p;
        unordered_map<char, string> p2w;
        return match(pattern, str, 0, 0, &w2p, &p2w);
    }

    bool match(const string &pattern, const string &str,
               const int i, const int j,
               unordered_map<string, char>* w2p,
               unordered_map<char, string>* p2w) {

        bool is_match = false;
        if (i == pattern.length() && j == str.length()) {
            is_match = true;
        } else if (i < pattern.length() && j < str.length()) {
            const char p = pattern[i];
            if (p2w->count(p)) {
                const auto& w = (*p2w)[p];
                if (w == str.substr(j, w.length())) {  // Match pattern.
                    is_match = match(pattern, str, i + 1, j + w.length(), w2p, p2w);
                }  // Else return false.
            } else {
                for (int k = j; k < str.length() && !is_match; ++k) {
                    const string w = str.substr(j, k - j + 1);
                    if (!w2p->count(w)) {
                        // Build mapping. Space: O(n + c)
                        (*w2p)[w] = p, (*p2w)[p] = w;
                        is_match = match(pattern, str, i + 1, k + 1, w2p, p2w);
                        w2p->erase(w), p2w->erase(p);
                    }  // Else try longer word.
                }
            }
        }
        return is_match;
    }
};
