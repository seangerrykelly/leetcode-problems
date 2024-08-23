# https://leetcode.com/problems/swap-salary/description/
# Write your MySQL query statement below
UPDATE Salary 
SET 
    sex = CASE
            WHEN sex = 'm' THEN 'f'
            WHEN sex = 'f' THEN 'm'
            ELSE sex
          END
WHERE sex = 'm' OR sex = 'f'