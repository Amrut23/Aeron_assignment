# CSV Plotter

This is a Python application that reads data from a CSV file and generates plots based on the data. It is designed to help visualize data quickly and easily.

## Features
- Reads data from a CSV file.
- Generates plots for data visualization.
- Supports customization of plots (e.g., selecting columns to plot).

## Prerequisites
- Python 3.8 or higher
- Required Python libraries (listed in `requirements.txt`):
  - pandas
  - matplotlib

## Installation
1. Clone or download this repository.
2. Navigate to the `part2_csv_plotter` directory.
3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application
1. Ensure you are in the `part2_csv_plotter` directory.
2. Run the script:
   ```powershell
   python csv_plotter.py
   ```
3. Follow the prompts in the terminal to select the CSV file and columns for plotting.

## Directory Structure
- `csv_plotter.py`: Main script for reading CSV data and generating plots.
- `sample_data.csv`: Example CSV file for testing the application.
- `requirements.txt`: List of required Python libraries.

## Usage
1. Place your CSV file in the `part2_csv_plotter` directory or provide the path to the file when prompted.
2. Run the script and follow the instructions to generate plots.
3. View the generated plots in a new window.

## Notes
- Ensure your CSV file is properly formatted with a header row.
- The application uses `matplotlib` for plotting and `pandas` for data manipulation.

## License
This project is for educational purposes and is not licensed for commercial use.

Additional tools used: **Copilot** (within VS Code and GitHub) assisted with code authoring and suggestions; the base project structure was designed using **Claude** and **Gemini**.