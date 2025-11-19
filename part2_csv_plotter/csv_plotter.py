"""
Python CSV Plotter - Part 2 of AI Intern Assignment
A Python script that loads a CSV file, lets the user choose 2 columns
for X and Y axes, and plots the data as a line chart or bar graph.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def load_csv(filename):
    """Load CSV file and return DataFrame"""
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File '{filename}' is empty.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

def display_columns(df):
    """Display available columns to the user"""
    print("\nAvailable columns:")
    print("-" * 50)
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    print("-" * 50)

def get_column_choice(df, axis_name):
    """Get user's column choice for X or Y axis"""
    while True:
        try:
            choice = input(f"\nSelect column number for {axis_name} axis: ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(df.columns):
                selected_col = df.columns[choice_num - 1]
                print(f"Selected: {selected_col}")
                return selected_col
            else:
                print(f"Please enter a number between 1 and {len(df.columns)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)

def get_graph_type():
    """Get user's choice for graph type"""
    while True:
        print("\nSelect graph type:")
        print("1. Line Chart")
        print("2. Bar Graph")
        
        try:
            choice = input("Enter your choice (1 or 2): ").strip()
            
            if choice == '1':
                return 'line'
            elif choice == '2':
                return 'bar'
            else:
                print("Please enter 1 for Line Chart or 2 for Bar Graph")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)

def plot_data(df, x_col, y_col, graph_type):
    """Plot the data using matplotlib"""
    try:
        # Convert to numeric if possible
        x_data = pd.to_numeric(df[x_col], errors='coerce')
        y_data = pd.to_numeric(df[y_col], errors='coerce')
        
        # Check if conversion was successful
        if x_data.isna().all():
            print(f"Warning: Column '{x_col}' could not be converted to numeric. Using as categorical.")
            x_data = df[x_col]
        
        if y_data.isna().all():
            print(f"Warning: Column '{y_col}' could not be converted to numeric. Using as categorical.")
            y_data = df[y_col]
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        
        if graph_type == 'line':
            plt.plot(x_data, y_data, marker='o', linewidth=2, markersize=6)
            plt.title(f'Line Chart: {y_col} vs {x_col}', fontsize=14, fontweight='bold')
        else:  # bar graph
            plt.bar(x_data, y_data, color='steelblue', alpha=0.7)
            plt.title(f'Bar Graph: {y_col} vs {x_col}', fontsize=14, fontweight='bold')
        
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Rotate x-axis labels if they're long
        if len(str(x_data.iloc[0])) > 10:
            plt.xticks(rotation=45, ha='right')
        
        plt.show()
        
        print("\nGraph displayed successfully!")
        
    except Exception as e:
        print(f"Error plotting data: {e}")
        sys.exit(1)

def main():
    """Main function to run the CSV plotter"""
    print("=" * 60)
    print("Python CSV Plotter")
    print("=" * 60)
    
    # Get CSV file path
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = input("Enter the path to your CSV file: ").strip().strip('"').strip("'")
    
    # Check if file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' does not exist.")
        sys.exit(1)
    
    # Load CSV
    print(f"\nLoading CSV file: {csv_file}")
    df = load_csv(csv_file)
    
    print(f"\nCSV file loaded successfully!")
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    
    # Display columns
    display_columns(df)
    
    # Get column choices
    x_column = get_column_choice(df, "X")
    y_column = get_column_choice(df, "Y")
    
    # Get graph type
    graph_type = get_graph_type()
    
    # Plot the data
    print(f"\nPlotting {graph_type} graph...")
    plot_data(df, x_column, y_column, graph_type)

if __name__ == "__main__":
    main()

