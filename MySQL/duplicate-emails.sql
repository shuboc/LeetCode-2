# Time:  O(n^2)
# Space: O(n)
#
# Write a SQL query to find all duplicate emails in a table named Person.
#
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# For example, your query should return the following for the above table:
#
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# Note: All emails are in lowercase.
#

# Write your MySQL query statement below
SELECT Email FROM Person GROUP BY Email HAVING COUNT(*) > 1
