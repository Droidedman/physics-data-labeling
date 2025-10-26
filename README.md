# physics-data-labeling
Synthetic physics dataset generation, labeling, and visualization pipeline using Python. Simulates energy–phase shift data for nuclear scattering and demonstrates AI-ready data preprocessing, annotation, and analysis workflow.

# Physics Data Labeling

This repository provides a complete **data generation, labeling, and visualization pipeline** for physics datasets.  
It simulates **energy–phase shift data** from simplified nuclear scattering models and prepares it for use in **machine learning or AI-assisted analysis**.

The goal is to demonstrate how a physics researcher can create structured, labeled datasets from theoretical simulations — bridging **scientific modeling** and **data-driven AI workflows**.

---

## 🧠 Background

In nuclear and particle physics, the relationship between **incident energy** and **scattering phase shift** carries crucial information about the potential and interaction type.

This repository reproduces simplified trends for:

- **Attractive potentials:** phase shift increases and saturates with energy.  
- **Repulsive potentials:** phase shift decreases gradually with energy.

The dataset is then **labeled, cleaned, and visualized**, ready for AI model training (e.g., potential classification, regression, or pattern recognition).

---

## 🧩 Features

- Generates synthetic **energy–phase shift datasets**  
- Adds **machine-readable labels (0/1)** for classification tasks  
- Computes **derived numerical features** (`dPhase_dE`)  
- Visualizes labeled data for exploratory analysis  
- Modular, reproducible structure suitable for AI pipelines

---

## 📂 Directory Structure

physics-data-labeling/
│
├── generate_dataset.py # Simulates synthetic phase shift data
├── label_physics_data.py # Adds labels and derived columns
├── visualize_dataset.py # Scatterplots of labeled data
├── utils.py # Summary and statistics
├── main.py # Runs full pipeline
└── dataset/
└── phase_shift_data.csv # Generated dataset

yaml
Copy code

---

## ⚙️ Installation

Requires **Python 3.8+** and the following dependencies:

```bash
pip install numpy pandas matplotlib seaborn
▶️ Running the Full Pipeline
Run the main script to generate, label, summarize, and visualize the dataset:

bash
Copy code
python main.py
It will sequentially:

Generate synthetic energy–phase shift data

Label each data point as “Attractive” or “Repulsive”

Compute derived feature dPhase_dE

Save labeled CSV files in dataset/

Visualize the result

📊 Example Output
1. Generated CSV (dataset/phase_shift_data.csv)
Energy(MeV)	PhaseShift(deg)	PotentialType
5.0	19.8	Attractive
5.0	58.7	Repulsive
10.0	28.3	Attractive
10.0	56.2	Repulsive

2. Labeled CSV (dataset/labeled_phase_shift.csv)
Energy(MeV)	PhaseShift(deg)	PotentialType	Label	dPhase_dE
5.0	19.8	Attractive	0	0.62
5.0	58.7	Repulsive	1	-0.84

3. Visualization
A scatter plot distinguishes Attractive vs. Repulsive phase-shift trends:

scss
Copy code
Phase Shift (deg)
│                 ⚪ Repulsive
│            ⚫ Attractive
│
└────────────────────────── Energy (MeV)
🧰 Functions Overview
Script	Description
generate_dataset.py	Creates synthetic physics dataset
label_physics_data.py	Adds labels and computed columns
visualize_dataset.py	Generates scatter plot visualization
utils.py	Prints dataset summary and stats
main.py	Runs full workflow in sequence

💡 Applications
Pretraining dataset for AI models that classify potential types

Example for supervised learning in physics

Training tool for students learning data labeling and scientific computation

Demonstration of bridging simulation and machine learning

🧮 Example: Extending to AI Training
You can easily adapt this dataset for an ML model, e.g., using scikit-learn:

python
Copy code
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df = pd.read_csv("dataset/labeled_phase_shift.csv")
X = df[["Energy(MeV)", "PhaseShift(deg)", "dPhase_dE"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier().fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
👨‍🔬 Author
Dewang Sukhadare
Ph.D. Candidate — Theoretical Nuclear Physics
Amity University, Mumbai, India

Email: sukhadarewango38@gmail.com

LinkedIn: linkedin.com/in/dewang-sukhadare

⚖️ License
Released under the MIT License (2025) — free for educational and research use with proper attribution.

🧭 Keywords
physics • nuclear-scattering • data-labeling • ai-ready-dataset • machine-learning • pandas • numpy • computational-physics


Would you like me to now generate your **third repo setup (`physics-data-visualization`)**, to show deeper **data analysis + featur
