import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Correlation and Regression part

# Loading the dataset
file_name = "Mental_Health_and_Social_Media_Balance_Dataset.csv"
df = pd.read_csv("E:/Mental_Health_and_Social_Media_Balance_Dataset.csv")

# Define variables
X = df['Daily_Screen_Time(hrs)']
Y = df['Happiness_Index(1-10)']

# --- A. Correlation ---
print("--- A. Correlation Analysis (Pearson's r) ---")
# Calculate the correlation matrix
correlation_matrix = np.corrcoef(X, Y)
# The correlation coefficient (r) is the off-diagonal element
r = correlation_matrix[0, 1]
print(f"Pearson Correlation Coefficient (r) between Daily Screen Time and Happiness Index: {r:.4f}")

# --- B. Simple Linear Regression (Y = mX + c) ---
print("\n--- B. Simple Linear Regression (Y = mX + c) ---")

# Fit the linear model using polyfit (degree 1 for linear)
# Returns [slope (m), intercept (c)]
slope, intercept = np.polyfit(X, Y, 1)

print(f"Regression Equation: Happiness Index = {slope:.4f} * Daily Screen Time + {intercept:.4f}")


'''
Explaination for Correlation: The Correlation  we find is -0.7052 which shows a high strenght and connection between Screen time and Happeniess
and do not forget that it is negative which mean that the relationship is inverse and spending more time in screen making the index of Happeniess lower and negative correlation is a strong eviedence for  it


Explaination for the Regression: so in the Result we found from Regression the "m" shows the slop and the "X" shows the Daily screen time and c the Happeniess index and what it tells us is that the more we spent time on screen or for every hour we spent in screen the predicted Happeniess index decrease by 0.62 points which is a practical impact of Screen time on Happeniess because the Happeniess depends on the screen time because the more   

'''


# VIsualization of Correlation by scotter plot



X = df['Daily_Screen_Time(hrs)']
Y = df['Happiness_Index(1-10)']

# Calculate correlation (r) to include in the title
r = np.corrcoef(X, Y)[0, 1]


plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='darkblue', alpha=0.6, label='Data Points')
plt.title(f'Correlation between Daily Screen Time and Happiness Index (r = {r:.4f})', fontsize=14)
plt.xlabel('Daily Screen Time (hrs)', fontsize=12)
plt.ylabel('Happiness Index (1-10)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.show()


# Visualization of Regression by scotter plot


X = df['Daily_Screen_Time(hrs)']
Y = df['Happiness_Index(1-10)']

# --- Calculate Regression Parameters ---
# Fit the linear model using numpy.polyfit (degree 1)
slope, intercept = np.polyfit(X, Y, 1)
r = np.corrcoef(X, Y)[0, 1]


plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='darkblue', alpha=0.6, label='Data Points')

# Plot the Regression Line: Y = mX + c
regression_line_y = slope * X + intercept
plt.plot(X, regression_line_y, color='red', linewidth=2, 
         label=f'Regression Line: Y = {slope:.2f}X + {intercept:.2f}')

plt.title('Simple Linear Regression: Happiness Index vs. Daily Screen Time', fontsize=14)
plt.xlabel('Daily Screen Time (hrs)', fontsize=12)
plt.ylabel('Happiness Index (1-10)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.show()



