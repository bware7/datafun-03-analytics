"""
Module: Python With Bin - Project Folder Automation

Module 2 Project
"""

import pathlib
import time

#####################################
# Global Variables
#####################################

# Project and data paths
project_path = pathlib.Path.cwd()
data_path = project_path.joinpath('data')

# Ensure the data directory exists
data_path.mkdir(exist_ok=True)

# Lists
tools_used: list = ["Git", "GitHub", "Python", "VS Code"]
regions = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Functions
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    """
    Create folders for each year.

    Arguments:
    start_year - The starting year of the range.
    end_year - The ending year of the range.
    """
    print(f"Creating folders for years {start_year} to {end_year}...")
    for year in range(start_year, end_year + 1):
        year_path = data_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        print(f"Folder created: {year_path}")

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    """
    Create folders from a list of names.

    Arguments:
    folder_list - A list of folder names to be created.
    to_lowercase - Convert folder names to lowercase if True.
    remove_spaces - Replace spaces with underscores in folder names if True.
    """
    print("Creating folders from the provided list...")
    for name in folder_list:
        original_name = name
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "_")
        folder_path = data_path.joinpath(name)
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path} (Original: '{original_name}')")

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    """
    Create folders with a given prefix for each name in a list.

    Arguments:
    folder_list - A list of folder names to be prefixed and created.
    prefix - The prefix to be added to each folder name.
    """
    print(f"Creating folders with prefix '{prefix}'...")
    for name in folder_list:
        prefixed_name = f"{prefix}{name}"
        folder_path = data_path.joinpath(prefixed_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path}")

def create_folders_periodically(duration_seconds: int, interval_seconds: int = 5) -> None:
    """
    Create a series of folders periodically over a specified duration.

    Arguments:
    duration_seconds - The total duration over which folders will be created.
    interval_seconds - The interval between folder creation in seconds.
    """
    print(f"Creating folders every {interval_seconds} seconds for a total duration of {duration_seconds} seconds...")
    start_time = time.time()
    folder_count = 0
    while (time.time() - start_time) < duration_seconds:
        folder_count += 1
        folder_path = data_path.joinpath(f"periodic_folder_{folder_count}")
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path}")
        time.sleep(interval_seconds)
    print(f"Finished creating {folder_count} folders.")

#####################################
# Byline Function
#####################################

def get_byline() -> str:
    """
    Return a byline with summary.
    """
    byline = f"""
    -------------------------------------------------
     Python With Bin: Project Folder Automation
    -------------------------------------------------
    Project Path: {project_path}
    Data Path: {data_path}
    Tools Used: {tools_used}
    Regions for Folders: {regions}
    Available Functions:
        - create_folders_for_range(start_year, end_year)
        - create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False)
        - create_prefixed_folders(folder_list, prefix)
        - create_folders_periodically(duration_seconds, interval_seconds=5)
    """
    return byline

#####################################
# Main Function
#####################################

def main() -> None:
    """
    Main function.
    """
    print(get_byline())

    # Demonstrating folder creation for a range of years
    create_folders_for_range(2020, 2023)

    # Demonstrating folder creation from a list with optional parameters
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # Demonstrating folder creation with a prefix
    create_prefixed_folders(tools_used, prefix="tool-")

    # Demonstrating periodic folder creation
    create_folders_periodically(duration_seconds=15, interval_seconds=5)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()