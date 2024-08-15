# https://leetcode.com/problems/duplicate-emails/description/
# Write your MySQL query statement below
SELECT Person.email FROM Person 
GROUP BY Person.email
HAVING COUNT(Person.email) > 1