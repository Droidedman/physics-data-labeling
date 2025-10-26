import pandas as pd

def describe_dataset(file_path="dataset/labeled_phase_shift.csv"):
    """Prints a brief summary of dataset stats."""
    df = pd.read_csv(file_path)
    print("Dataset Summary:")
    print(f"Total samples: {len(df)}")
    print("Class distribution:")
    print(df["PotentialType"].value_counts())
    print("\nPhase Shift Range:")
    print(df["PhaseShift(deg)"].describe())
    return df
