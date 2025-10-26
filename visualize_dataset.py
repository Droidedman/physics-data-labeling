import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_phase_shift_data(file_path="dataset/labeled_phase_shift.csv"):
    """
    Visualizes labeled phase shift data by potential type.
    """
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Energy(MeV)",
        y="PhaseShift(deg)",
        hue="PotentialType",
        style="PotentialType",
        s=50,
        edgecolor="black"
    )
    plt.title("Phase Shift vs Energy (Labeled Dataset)")
    plt.xlabel("Energy (MeV)")
    plt.ylabel("Phase Shift (degrees)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_phase_shift_data()
