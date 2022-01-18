# Time:  O(n)
# Space: O(1)

# A password is considered strong if below conditions are all met:
#
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter,
# and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak,
# but "...aa...a..." is strong, assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one change.

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_type_cnt = 3
        if any('a' <= c <= 'z' for c in s):
            missing_type_cnt -= 1
        if any('A' <= c <= 'Z' for c in s):
            missing_type_cnt -= 1
        if any(c.isdigit() for c in s):
            missing_type_cnt -= 1

        total_change_cnt = 0
        one_change_cnt, two_change_cnt, three_change_cnt = 0, 0, 0
        i = 2
        while i < len(s):
            if s[i] == s[i-1] == s[i-2]:
                length = 2
                while i < len(s) and s[i] == s[i-1]:
                    length += 1
                    i += 1
                    
                total_change_cnt += length / 3
                if length % 3 == 0:
                    one_change_cnt += 1
                elif length % 3 == 1:
                    two_change_cnt += 1
                else:
                    three_change_cnt += 1
            else:
                i += 1
        
        if len(s) < 6:
            return max(missing_type_cnt, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_type_cnt, total_change_cnt)
        else:
            delete_cnt = len(s) - 20
            
            total_change_cnt -= min(delete_cnt, one_change_cnt * 1) / 1
            total_change_cnt -= min(max(delete_cnt - one_change_cnt, 0), two_change_cnt * 2) / 2
            total_change_cnt -= min(max(delete_cnt - one_change_cnt - 2 * two_change_cnt, 0), three_change_cnt * 3) / 3
                
            return delete_cnt + max(missing_type_cnt, total_change_cnt)
