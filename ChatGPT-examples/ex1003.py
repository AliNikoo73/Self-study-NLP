import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load sample data
data = {
    "Name": ["Ali", "Sara", "John", "Mina"],
    "Age": [25, 30, 22, 28],
    "Score": [88, 92, 85, 90]
}

df = pd.DataFrame(data)
print(df)

# Average age
print("Average Age:", np.mean(df["Age"]))

# Plot scores
plt.bar(df["Name"], df["Score"])
plt.xlabel("Student")
plt.ylabel("Score")
plt.title("Student Scores")
plt.show()


print("---------------------------------------")
#----------


# Practice

# 1. Create a list of 5 numbers and print only the even numbers.
numbers = [107, 258, 377, 48, 55]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

# 2. Make a small dataset with 5 people (name, age, height).
people_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 17, 22, 35, 28],
    "Height": [165, 175, 180, 170, 160]
}
df = pd.DataFrame(people_data)

# - Compute average height.
average_height = np.mean(df["Height"])
print("Average Height:", average_height)

# - Plot a bar chart of their ages.
plt.bar(df["Name"], df["Age"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Ages of People")
plt.show()

# 3. Write a loop to print “Adult” if age ≥ 18, else “Minor”.
for index, row in df.iterrows():
    if row["Age"] >= 18:
        print(row["Name"], "is an Adult.")
    else:
        print(row["Name"], "is a Minor.")


# Take your daily expenses for a week and store them in a list (np array)
expenses = np.array([50, 75, 60, 80, 90, 40, 70])
# Compute total, average, min, max, and visualize them using a bar chart.
total_expenses = np.sum(expenses)
average_expenses = np.mean(expenses)
min_expenses = np.min(expenses)
max_expenses = np.max(expenses)

print("Total Expenses:", total_expenses)
print("Average Expenses:", average_expenses)
print("Min Expenses:", min_expenses)
print("Max Expenses:", max_expenses)

plt.bar(["Total", "Average", "Min", "Max"], [total_expenses, average_expenses, min_expenses, max_expenses])
plt.ylabel("Amount")
plt.title("Weekly Expenses")
plt.show()
