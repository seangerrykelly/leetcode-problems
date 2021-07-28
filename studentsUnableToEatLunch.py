class Solution(object):
    
    def removeStudentFromQueue(self, queue):
        queue.pop(0)
    
    def sendStudentToEnd(self, queue):
        student = queue.pop(0)
        queue.append(student)
    
    def removeSandwich(self, stack):
        stack.pop(0)
    
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        stubbornStudents = len(students)
        cycleTracker = 0
        
        while True:
            
            if len(sandwiches) == 0 or len(students) == 0:
                break
            
            if cycleTracker == len(students):
                break
            
            currStudent = students[0]
            currSandwich = sandwiches[0]
            
            if currStudent == currSandwich:
                self.removeStudentFromQueue(students)
                self.removeSandwich(sandwiches)
                stubbornStudents -= 1
                cycleTracker = 0
            else:
                cycleTracker += 1
                self.sendStudentToEnd(students)
            
        return stubbornStudents