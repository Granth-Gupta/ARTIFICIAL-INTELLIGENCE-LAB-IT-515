# Experiment 1: Perceptron for binary classification (AND gate)

# Step 1: Data (AND gate)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]


# Step 2: Activation function (step function)
def step(z):
    return 1 if z >= 0 else 0


# Step 3: Predict output for one input
def predict(x, w, b):
    z = w[0] * x[0] + w[1] * x[1] + b
    return step(z)


# Step 4: Perceptron Learning Algorithm
def train(lr, max_epochs):
    w = [0.0, 0.0]   # starting weights
    b = 0.0          # starting bias
    for epoch in range(1, max_epochs + 1):
        errors = 0
        for xi, target in zip(X, y):
            error = target - predict(xi, w, b)
            if error != 0:                      # wrong prediction -> update
                w[0] += lr * error * xi[0]
                w[1] += lr * error * xi[1]
                b += lr * error
                errors += 1
        if errors == 0:                         # all correct -> converged
            return w, b, epoch, True
    return w, b, max_epochs, False


# Step 5: Accuracy
def accuracy(w, b):
    correct = sum(1 for xi, t in zip(X, y) if predict(xi, w, b) == t)
    return correct / len(X) * 100


# Step 6: Effect of learning rate and iterations
print("Learning Rate | Max Iterations | Epochs Used | Converged | Accuracy")
print("-" * 65)
for lr in [0.01, 0.1, 0.5, 1.0]:
    for max_epochs in [1, 2, 5, 10, 50]:
        w, b, used, ok = train(lr, max_epochs)
        print(f"{lr:<13} | {max_epochs:<14} | {used:<11} | {str(ok):<9} | {accuracy(w, b):.0f}%")

# Step 7: Final result with lr = 0.1
w, b, used, ok = train(0.1, 50)
print("\nFinal weights:", w, " Bias:", b, " Epochs:", used)
print("Testing the trained perceptron:")
for xi, t in zip(X, y):
    print(f"Input {xi} -> Predicted {predict(xi, w, b)}, Actual {t}")