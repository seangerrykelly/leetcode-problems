# https://leetcode.com/problems/classes-more-than-5-students/description/
# Write your MySQL query statement below
SELECT class FROM Courses
GROUP BY class
HAVING COUNT(class) > 4