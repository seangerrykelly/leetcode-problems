# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/
# Write your MySQL query statement below
SELECT name 
FROM Employee
WHERE id IN (
    SELECT managerId 
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) > 4
)