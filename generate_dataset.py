import numpy as np
import pandas as pd
import os

def generate_phase_shift_dataset(num_points=200, seed=42, save_path="dataset/phase_shift_data.csv"):
    """
    Simulates energy vs phase shift data for two potential types:
    'Attractive' and 'Repulsive'.
    """
    np.random.seed(seed)

    energies = np.linspace(5, 50, num_points)
    data = []

    for E in energies:
        # Attractive potential: phase shift increases with energy then saturates
        phase_attractive = 50 * (1 - np.exp(-E / 15)) + np.random.normal(0, 1)
        # Repulsive potential: phase shift decreases slowly
        phase_repulsive = 60 * np.exp(-E / 30) + np.random.normal(0, 1)

        data.append((E, phase_attractive, "Attractive"))
        data.append((E, phase_repulsive, "Repulsive"))

    df = pd.DataFrame(data, columns=["Energy(MeV)", "PhaseShift(deg)", "PotentialType"])

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Dataset saved to: {save_path}")
    return df

if __name__ == "__main__":
    generate_phase_shift_dataset()
