import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#  Hypothesis Test Code (Two-Sample T-Test) 


# Loading the dataset
file_name = "Mental_Health_and_Social_Media_Balance_Dataset.csv"
df = pd.read_csv("E:/Mental_Health_and_Social_Media_Balance_Dataset.csv")



# Filter data for the two groups we want to compare
group_male = df[df['Gender'] == 'Male']['Happiness_Index(1-10)']
group_female = df[df['Gender'] == 'Female']['Happiness_Index(1-10)']

# Observed difference in means
observed_diff = group_male.mean() - group_female.mean()

# ----------------------------------------------------------------------
# 2. PERMUTATION TEST
# ----------------------------------------------------------------------

n_iterations = 5000  # Number of times to shuffle the data
combined_data = np.concatenate([group_male.values, group_female.values])
n_male = len(group_male)
n_female = len(group_female)
permutation_diffs = []

print(f"Starting Permutation Test with {n_iterations} iterations...")

for i in range(n_iterations):
    # Randomly shuffle the combined data
    np.random.shuffle(combined_data)
    
    # Split the shuffled data into two new groups of the original size
    perm_male = combined_data[:n_male]
    perm_female = combined_data[n_male:]
    
    # Calculate the difference in means for this permutation
    perm_diff = perm_male.mean() - perm_female.mean()
    
    permutation_diffs.append(perm_diff)

# ----------------------------------------------------------------------
# 3. RESULTS AND P-VALUE CALCULATION
# ----------------------------------------------------------------------

# Convert to numpy array for p-value calculation
permutation_diffs = np.array(permutation_diffs)

# P-value (Two-sided test): proportion of differences as extreme as the observed difference
# We check how many simulated differences are greater than or equal to the absolute observed difference
p_value = np.sum(np.abs(permutation_diffs) >= np.abs(observed_diff)) / n_iterations

print("\n--- Hypothesis Test Results ---")
print(f"Observed Difference (Male Mean - Female Mean): {observed_diff:.4f}")
print(f"P-Value (Two-sided Permutation Test): {p_value:.4f}")

# Determine conclusion
alpha = 0.05
if p_value < alpha:
    conclusion = "Reject the Null Hypothesis: There is a statistically significant difference in mean happiness between Male and Female participants."
else:
    conclusion = "Fail to Reject the Null Hypothesis: There is no statistically significant difference in mean happiness between Male and Female participants."

print("\nConclusion (at alpha = 0.05):")
print(conclusion)

# ----------------------------------------------------------------------
# 4. VISUALIZATION
# ----------------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.hist(permutation_diffs, bins=50, edgecolor='black', alpha=0.7, 
         label='Permutation Distribution of Mean Differences')
plt.axvline(observed_diff, color='red', linestyle='dashed', linewidth=2, 
            label=f'Observed Difference: {observed_diff:.3f}')
plt.axvline(-observed_diff, color='red', linestyle='dashed', linewidth=2) # Mark the symmetrical boundary for two-sided test

plt.title('Permutation Test: Mean Happiness Difference (Male - Female)', fontsize=14)
plt.xlabel('Difference in Mean Happiness Index ($\mu_{Male} - \mu_{Female}$)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()



'''
from above tests of Hypotheisis is that H0 or null hypothesis is that the mean happeniess of male is equal to the happeniess index of female and the Alternative is Ha Alternative hypotheisis in which we try to reject the null hypotheisis but we fail because the p-value is 0.9840 which is extremly high then alpha value which is 0.5 so we fail to reject null hypoyheisis and the male and female happeniess is eqaul which is proved by permutation test


'''

