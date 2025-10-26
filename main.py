from generate_dataset import generate_phase_shift_dataset
from label_physics_data import add_labels_to_dataset
from visualize_dataset import visualize_phase_shift_data
from utils import describe_dataset

def main():
    print("=== Generating Synthetic Physics Dataset ===")
    generate_phase_shift_dataset(num_points=200)

    print("=== Adding Labels and Derived Columns ===")
    add_labels_to_dataset()

    print("=== Dataset Summary ===")
    describe_dataset()

    print("=== Visualizing Results ===")
    visualize_phase_shift_data()

if __name__ == "__main__":
    main()
