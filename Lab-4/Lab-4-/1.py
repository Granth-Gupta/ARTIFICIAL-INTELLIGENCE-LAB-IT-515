import math
from collections import defaultdict
from typing import List, Tuple, Dict
 
class MemorizationLearner:
    """Simple learner that stores training examples and answers queries by lookup"""
    
    def __init__(self):
        self.table = {}  # Dictionary to store mark -> grade mapping
    
    def build_table(self, marks: List[int], grades: List[str]):
        """Build the memorization table from training data"""     
        for index in range(len(marks)):
            self.table[marks[index]] = grades[index] 
        
        print("\nTraining Table Built:")
        print("-" * 40)
        print("Marks | Grade")
        print("-" * 40)
        for mark, grade in sorted(self.table.items()):
            print(f"{mark:5} | {grade}")
        print("-" * 40)
    
    def query(self, mark: int) -> str:
        """Answer a query by looking up in the memorization table"""
        if mark in self.table:
            return self.table[mark]
        else:
            return "UNKNOWN (Never seen in training data)"
    
    def answer_queries(self, queries: List[int]):
        """Answer multiple queries"""
        print("\nAnswering Queries:")
        print("-" * 40)
        for q in queries:
            result = self.query(q)
            status = "✓ Found" if result != "UNKNOWN (Never seen in training data)" else "✗ Not Found"
            print(f"Query: Marks = {q:2} → Grade = {result:30} [{status}]")
        print("-" * 40)
        
        print("\nWhat can the learner do?")
        print("• The learner can ONLY answer queries for marks it has seen in training")
        # print("• For unseen marks (like 65), it cannot determine the grade")
        # print("• This is a simple lookup-based approach with NO generalization capability")
  
if __name__ == "__main__":
    
    memorizer = MemorizationLearner()
    
    # Training data
    marks = [45, 52, 61, 73, 88]
    grades = ['D', 'C', 'C', 'B', 'A']
    queries = [61, 45, 65]
    
    # Build and query
    memorizer.build_table(marks, grades)
    memorizer.answer_queries(queries)

