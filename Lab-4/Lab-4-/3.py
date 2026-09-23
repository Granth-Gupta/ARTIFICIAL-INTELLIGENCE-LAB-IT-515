import math
from collections import defaultdict
from typing import List, Tuple, Dict

class NaiveBayesClassifier:
    """Naive Bayes classifier for categorical data"""
    
    def __init__(self):
        self.training_data = []
        self.class_counts = defaultdict(int)
        self.attribute_values = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.total_samples = 0
    
    def add_training_example(self, outlook: str, temperature: str, play: str):
        """Add a training example"""
        self.training_data.append({
            'Outlook': outlook,
            'Temperature': temperature,
            'Play': play
        })
        self.class_counts[play] += 1
        self.total_samples += 1
    
    def calculate_probabilities(self):
        """Calculate prior and conditional probabilities"""
        # Count attribute values for each class
        for example in self.training_data:
            play_class = example['Play']
            outlook = example['Outlook']
            temperature = example['Temperature']
            
            self.attribute_values[play_class]['Outlook'][outlook] += 1
            self.attribute_values[play_class]['Temperature'][temperature] += 1
    
    def get_prior_probability(self, class_label: str) -> float:
        """P(Class)"""
        return self.class_counts[class_label] / self.total_samples
    
    def get_conditional_probability(self, attribute: str, value: str, 
                                   class_label: str) -> float:
        """P(Attribute=value | Class) using Laplace smoothing"""
        count = self.attribute_values[class_label][attribute].get(value, 0)
        total = sum(self.attribute_values[class_label][attribute].values())
        unique_values = len(self.attribute_values[class_label][attribute])
        
        return (count + 1) / (total + unique_values)
    
    def classify(self, outlook: str, temperature: str) -> Dict:
        """Classify using Naive Bayes"""
        results = {}
        
        for class_label in self.class_counts.keys():
            prior = self.get_prior_probability(class_label)
            
            p_outlook = self.get_conditional_probability('Outlook', outlook, class_label)
            p_temperature = self.get_conditional_probability('Temperature', temperature, class_label)
            
            score = prior * p_outlook * p_temperature
            
            results[class_label] = {
                'prior': prior,
                'p_outlook': p_outlook,
                'p_temperature': p_temperature,
                'score': score
            }
        
        return results
    
if __name__ == "__main__":
    nb = NaiveBayesClassifier()
    
    # Training data
    training_data_nb = [
        ('Sunny', 'Hot', 'No'),
        ('Sunny', 'Hot', 'No'),
        ('Overcast', 'Hot', 'Yes'),
        ('Rainy', 'Mild', 'Yes'),
        ('Rainy', 'Cool', 'Yes'),
        ('Rainy', 'Cool', 'No'),
        ('Overcast', 'Cool', 'Yes'),
        ('Sunny', 'Mild', 'No'),
        ('Sunny', 'Cool', 'Yes'),
        ('Rainy', 'Mild', 'Yes'),
    ]

    for i, (outlook, temp, play) in enumerate(training_data_nb, 1):
        nb.add_training_example(outlook, temp, play)
    
    nb.calculate_probabilities()
    
    outlook_query = input("Enter Outlook (Sunny/Overcast/Rainy): ").strip()
    temperature_query = input("Enter Temperature (Hot/Mild/Cool): ").strip()
    
    print(f"\nNew Day: Outlook = {outlook_query}, Temperature = {temperature_query}")
    print("-" * 50)
    
    results = nb.classify(outlook_query, temperature_query)
    
    for class_label, scores in results.items():
        print(f"\nPlay = {class_label}:")
        print(f"  Prior P(Play = {class_label}) = {scores['prior']:.4f}")
        print(f"  P(Outlook = {outlook_query} | {class_label}) = {scores['p_outlook']:.4f}")
        print(f"  P(Temperature = {temperature_query} | {class_label}) = {scores['p_temperature']:.4f}")
        print(f"  Score = {scores['prior']:.4f} × {scores['p_outlook']:.4f} × {scores['p_temperature']:.4f} = {scores['score']:.6f}")
    
    predicted_class = max(results, key=lambda x: results[x]['score'])
    print(f"\nPrediction: Play = {predicted_class}")