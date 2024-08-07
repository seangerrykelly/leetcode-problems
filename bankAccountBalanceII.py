# https://leetcode.com/problems/bank-account-summary-ii/submissions/1346710823/
# Write your MySQL query statement below
SELECT Users.name AS NAME, sum(Transactions.amount) AS BALANCE 
FROM Transactions
JOIN Users ON Transactions.account = Users.account
GROUP BY Users.name
HAVING BALANCE > 10000