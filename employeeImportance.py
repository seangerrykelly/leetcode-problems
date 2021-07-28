"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        importanceVal = 0
        employeeMap = {}
        selectedEmployee = None
        
        for employee in employees:
            if employee.id == id:
                selectedEmployee = employee
            if employeeMap.get(employee.id) is None:
                employeeMap[employee.id] = employee
                
        employeeQueue = [selectedEmployee]
        
        while employeeQueue:
            currentEmployee = employeeQueue.pop(0)
            if currentEmployee is None:
                continue
            importanceVal += currentEmployee.importance
            for sub in currentEmployee.subordinates:
                employeeQueue.append(employeeMap[sub])
        
        return importanceVal
            
        
        