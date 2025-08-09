Social Media’s Affect on Mood — Data Analysis
This repository contains custom Python scripts used to analyze and interpret data for the research paper "Social Media’s Affect on Mood" by Yadav Singh.
The analysis is based on raw data collected as part of a PSYC 201W experimental research study examining the emotional impact of social media content.

📄 Overview
The scripts in this repository automate:

Parsing and cleaning raw participant data.

Calculating Positive and Negative Affect Schedule (PANAS) scores.

Generating descriptive statistics (mean, standard deviation).

Preparing results for integration into the final research paper.

The work follows a reproducible, transparent workflow, ensuring that all calculations can be replicated for peer review or further research.

📊 Research Context
This study investigated whether the emotional valence of social media content influences participants' moods. Mood changes were measured using the PANAS scale before and after exposure to selected content.
The findings contribute to the growing field of social media psychology, with potential implications for digital well-being and content moderation.

⚙️ Features
PANAS Integration: Leverages a panas module to compute positive and negative affect scores.

Automated Statistics: Calculates mean and standard deviation for key variables.

Clean, Reusable Code: Scripts are modular to allow quick re-analysis with different datasets.

CSV Data Input: Works directly with exported survey or lab experiment data.

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yadav412/psyc-201w-data-analysis.git
cd psyc-201w-data-analysis
Install dependencies (preferably in a virtual environment):

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Place your raw data file (CSV) in the repository folder, then run:

bash
Copy
Edit
python analyze.py
Example output:

Positive Affect mean & SD

Negative Affect mean & SD

PANAS change scores

Ready-to-use table outputs for research paper inclusion

📁 Repository Structure
bash
Copy
Edit
.
├── analyze.py          # Main script to run the analysis
├── panas.py            # PANAS scoring functions
├── utils.py            # Helper functions for data cleaning
├── data/               # Folder for raw and processed data
├── results/            # Output tables and statistics
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
📚 Dependencies
pandas — data handling

numpy — statistical calculations

panas — PANAS scoring helper functions (local module in repo)

Install all with:

bash
Copy
Edit
pip install -r requirements.txt

🧪 Example Dataset
A sample dataset (data/sample.csv) is provided to demonstrate expected input format:

participant_id

time (pre or post)

positive_item_scores

negative_item_scores

✏️ Author
Yadav Singh
📧 Contact: GitHub Profile

📜 License
This project is released under the MIT License — see the LICENSE file for details.
