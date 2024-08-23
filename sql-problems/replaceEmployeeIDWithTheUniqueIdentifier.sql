# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/
# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name FROM EmployeeUNI
RIGHT JOIN Employees
ON EmployeeUNI.id=Employees.id