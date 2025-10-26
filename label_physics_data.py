import pandas as pd
import numpy as np
import os

def add_labels_to_dataset(file_path="dataset/phase_shift_data.csv", save_labeled_path="dataset/labeled_phase_shift.csv"):
    """
    Adds a numerical label column (0=Attractive, 1=Repulsive)
    and creates a derived 'Trend' column to show how phase changes with energy.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}. Run generate_dataset.py first.")

    df = pd.read_csv(file_path)

    # Encode potential types
    df["Label"] = df["PotentialType"].map({"Attractive": 0, "Repulsive": 1})

    # Trend detection (numerical derivative of phase shift)
    df["dPhase_dE"] = np.gradient(df["PhaseShift(deg)"], df["Energy(MeV)"])

    df.to_csv(save_labeled_path, index=False)
    print(f"Labeled dataset saved to: {save_labeled_path}")
    return df

if __name__ == "__main__":
    add_labels_to_dataset()
