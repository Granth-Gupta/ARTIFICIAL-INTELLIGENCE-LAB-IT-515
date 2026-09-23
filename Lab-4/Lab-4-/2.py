import math
from collections import defaultdict
from typing import List, Tuple, Dict

class KNearestNeighbour:
    """k-Nearest Neighbour classifier using Euclidean distance"""
    
    def __init__(self):
        self.training_data = []  # List of (point_dict, class_label)
    
    def add_training_point(self, name: str, x1: float, x2: float, class_label: str):
        """Add a training point"""
        self.training_data.append({
            'name': name,
            'x1': x1,
            'x2': x2,
            'class': class_label
        })
    
    def euclidean_distance(self, p1: Tuple[float, float], 
                          p2: Tuple[float, float]) -> float:
        """Calculate Euclidean distance between two points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def classify(self, test_point: Tuple[float, float], k: int) -> str:
        """Classify test point using k-NN"""
        distances = []
        
        # Calculate distance from test point to all training points
        for point in self.training_data:
            train_coords = (point['x1'], point['x2'])
            dist = self.euclidean_distance(test_point, train_coords)
            distances.append({
                'point': point['name'],
                'distance': dist,
                'class': point['class']
            })
        
        distances.sort(key=lambda x: x['distance'])
        
        return distances
    
    def predict(self, test_point: Tuple[float, float], k: int) -> Tuple[str, List]:
        """Predict class for test point"""
        distances = self.classify(test_point, k)
        
        k_nearest = distances[:k]
        
        # Count classes
        class_count = defaultdict(int)
        for neighbor in k_nearest:
            class_count[neighbor['class']] += 1
        
        # Determine predicted class
        predicted_class = max(class_count, key=class_count.get)
        
        return predicted_class, distances
    
if __name__ == "__main__":
    knn = KNearestNeighbour()
    
    training_points = [
        ('P1', 1, 2, 'A'),
        ('P2', 2, 3, 'A'),
        ('P3', 3, 3, 'B'),
        ('P4', 6, 5, 'B'),
        ('P5', 7, 7, 'B'),
    ]
    
    print("\nTraining Data:")
    print("-" * 50)
    print("Point | x1 | x2 | Class")
    print("-" * 50)
    for name, x1, x2, class_label in training_points:
        knn.add_training_point(name, x1, x2, class_label)
        print(f"{name:5} | {x1:2} | {x2:2} | {class_label}")
    print("-" * 50)
    
    test_point = (3, 4)
    print(f"\nTest Point: {test_point}")
    print()
    
    print("Distances from Test Point:")
    print("-" * 50)
    predicted_k1, all_distances = knn.predict(test_point, k=1)
    
    for item in all_distances:
        print(f"{item['point']} → Distance = {item['distance']:.4f}, Class = {item['class']}")
    
    print("-" * 50)
    print(f"\nPrediction for k=1: Class = {predicted_k1}")
    
    predicted_k3, _ = knn.predict(test_point, k=3)
    print(f"Prediction for k=3: Class = {predicted_k3}")