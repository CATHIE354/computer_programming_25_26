

# Session 2 continuity variables (Rule settings). Do not change these.
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"



correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower

flower2 = {
"id": "flower2",
"sepal_length": 4.9,
"sepal_width": 3.0,
"petal_length": 1.4,
"petal_width": 0.2,
"species": "setosa"
}


# Task 2: Create list of dictionaries
dataset= [flower1,flower2]


# Task 3: Create a for loop to process the dataset
for flower in dataset:
    print(flower["id"], flower["petal_length"], flower["species"])

# Task 4: Use an if-else statement to classify each sample
    if flower["petal_length"] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    if flower[label_key] == positive_label:
        y_true = positive_label
    else:
        y_true = negative_label

    if y_pred == y_true :
        correct += 1
    else :
        wrong += 1

    total +=1

    y_pred_list.append(y_pred)

print(
 f"id={flower['id']} | true={y_true} | pred={y_pred} | "
 f"petal_length={flower['petal_length']}"   
)

accuracy = (correct/total) * 100 if total > 0 else 0.0

print("\n=== session 3 Summary ===")
print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Accuracy (%):", round(accuracy, 2))
print("All predictions:", y_pred_list)