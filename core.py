import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_clean_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Missing file: {filepath}")
    
    df = pd.read_csv(filepath)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount", "Date"]).sort_values("Date")
    return df

def generate_metrics(df):
    total_spent = np.sum(df["Amount"].to_numpy())
    mean_tx = np.mean(df["Amount"].to_numpy())
    median_tx = np.median(df["Amount"].to_numpy())
    by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    
    print("\n========== Financial Summary ==========")
    print(f"Total Spent:         ${total_spent:.2f}")
    print(f"Average Transaction: ${mean_tx:.2f}")
    print(f"Median Transaction:  ${median_tx:.2f}")
    print("\n--- Spending by Category ---")
    print(by_category.to_string())
    print("=======================================\n")
    return by_category

def export_charts(df, by_category, output_filename="expense_summary.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    ax1.bar(by_category.index, by_category.values, color="#2b5c8f", edgecolor="#111111")
    ax1.set_title("Total Spend by Category", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Amount ($)")
    ax1.tick_params(axis="x", rotation=30)
    ax1.grid(axis="y", linestyle="--", alpha=0.5)

    daily_spend = df.groupby("Date")["Amount"].sum()
    ax2.plot(daily_spend.index, daily_spend.values, marker="o", color="#d95f02", linewidth=2)
    ax2.set_title("Spending Trend Over Time", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Amount ($)")
    ax2.tick_params(axis="x", rotation=30)
    ax2.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    print(f"Visual report saved to: {output_filename}")
    plt.show()

if __name__ == "__main__":
    csv_file = "expenses.csv"
    data = load_and_clean_data(csv_file)
    cat_summary = generate_metrics(data)
    export_charts(data, cat_summary)