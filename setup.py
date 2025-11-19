"""
Setup script to install dependencies for both parts of the assignment.
Run this script to install all required packages.
"""

import subprocess
import sys
import os

def install_requirements(filepath):
    """Install requirements from a requirements.txt file"""
    try:
        print(f"\nInstalling requirements from {filepath}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", filepath])
        print(f"✓ Successfully installed requirements from {filepath}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements from {filepath}: {e}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("AI Intern Assignment - Setup Script")
    print("=" * 60)
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Part 1: File Upload Portal
    part1_req = os.path.join(script_dir, "part1_file_upload", "requirements.txt")
    if os.path.exists(part1_req):
        install_requirements(part1_req)
    else:
        print(f"Warning: {part1_req} not found")
    
    # Part 2: CSV Plotter
    part2_req = os.path.join(script_dir, "part2_csv_plotter", "requirements.txt")
    if os.path.exists(part2_req):
        install_requirements(part2_req)
    else:
        print(f"Warning: {part2_req} not found")
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. For File Upload Portal: No additional setup required")
    print("2. For CSV Plotter: Ready to use with any CSV file")
    print("3. See README.md for detailed usage instructions")

if __name__ == "__main__":
    main()

