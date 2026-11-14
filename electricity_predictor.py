
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TARIFF = 6

def predict_usage():
    try:
        data = pd.read_csv("usage.csv")

        data["Month"] = pd.to_numeric(data["Month"], errors="coerce")
        data["Units"] = pd.to_numeric(data["Units"], errors="coerce")
        data = data.dropna(subset=["Month", "Units"])

        print("\nElectricity Usage Summary")
        print(data)

        if len(data) < 2:
            print("Error: At least 2 months of data are required.")
            return

        months = data["Month"].values
        units = data["Units"].values

        slope, intercept = np.polyfit(months, units, 1)

        predicted = slope * months + intercept

        ss_total = np.sum((units - np.mean(units)) ** 2)
        ss_residual = np.sum((units - predicted) ** 2)

        r2 = 1 - ss_residual / ss_total if ss_total != 0 else 0

        future_month = float(input("\nEnter future month: "))

        predicted_units = slope * future_month + intercept
        bill = predicted_units * TARIFF

        print("\n--- Prediction Result ---")
        print(f"Slope: {slope:.2f}")
        print(f"Intercept: {intercept:.2f}")
        print(f"R2 Score: {r2:.2f}")
        print(f"Predicted Units: {predicted_units:.2f}")
        print(f"Estimated Bill: Rs. {bill:.2f}")

        plt.scatter(months, units, label="Actual Usage")

        x = np.linspace(min(months), max(months) + 2, 100)
        y = slope * x + intercept

        plt.plot(x, y, label="Regression Line")
        plt.scatter(future_month, predicted_units,
                    marker="*", s=150, label="Prediction")

        plt.xlabel("Month")
        plt.ylabel("Electricity Units")
        plt.title("Electricity Usage Prediction")
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Error: usage.csv file not found.")
    except ValueError:
        print("Error: Please enter a valid month.")
    except Exception as e:
        print("Error:", e)


while True:
    print("\n1. Predict Electricity Usage")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        predict_usage()
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
      
