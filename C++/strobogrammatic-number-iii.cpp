// Time:  O(5^(n/2))
// Space: O(n)

class Solution {
public:
    int strobogrammaticInRange(string low, string high) {
        int count = countStrobogrammaticUntil(high, false) -
                    countStrobogrammaticUntil(low, false) +
                    isStrobogrammatic(low);
        return count >= 0 ? count : 0;
    }

    int countStrobogrammaticUntil(string num, bool can_start_with_0) {
        if (can_start_with_0 && cache.find(num) != cache.end()) {
            return cache[num];
        }

        int count = 0;
        if (num.length() == 1) {
            for (const auto& c : {'0', '1', '8'}) {
                if (num.front() >= c) {
                    ++count;
                }
            }
            cache[num] = count;
            return count;
        }
        
        for (const auto& kvp : lookup) {
            if (can_start_with_0 || kvp.first != '0') { 
                if (num.front() > kvp.first) {
                    if (num.length() == 2) {  // num is like "21"
                        ++count;
                    } else {  // num is like "201"
                        count += countStrobogrammaticUntil(string(num.length() - 2, '9'), true);
                    }
                } else if (num.front() == kvp.first) {
                    if (num.length() == 2) {  // num is like 12".
                        count += num.back() >= kvp.second;
                    } else {
                        if (num.back() >= kvp.second) {  // num is like "102".
                            count += countStrobogrammaticUntil(getMid(num), true);
                        } else if (getMid(num) != string(num.length() - 2, '0')) {  // num is like "110".
                            count += countStrobogrammaticUntil(getMid(num), true) -
                                     isStrobogrammatic(getMid(num));
                        }
                    }
                }
            }
        }

        if (!can_start_with_0) { // Sum up each length.
            for (int i = num.length() - 1; i > 0; --i) {
                count += countStrobogrammaticByLength(i);
            }
        } else {
            cache[num] = count;
        }

        return count;
    }

    string getMid(const string& num) {
        return num.substr(1, num.length() - 2);
    }

    int countStrobogrammaticByLength(int n) {
        switch (n) {
            case 1:
                return 3;  // "0", "1", "8"
            case 2:
                return 4;  // "11", "69", "88", "96"
            case 3:
                return 4 * 3;  // "101", "111", "181", ...
            default:
                return 5 * countStrobogrammaticByLength(n - 2);
        }
    }

    bool isStrobogrammatic(const string& num) {
        const int n = num.size();
        for (int i = 0; i <= n - 1 - i; ++i) {
            const auto it = lookup.find(num[n - 1 - i]);
            if (it == lookup.end() || num[i] != it->second) {
                return false;
            }
        }
        return true;
    }

private:
    const unordered_map<char, char> lookup{{'0', '0'}, {'1', '1'},
                                           {'6', '9'}, {'8', '8'}, 
                                           {'9', '6'}};
    unordered_map<string, int> cache;
};
