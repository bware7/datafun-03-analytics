# datafun-03-project

## Overview

This project demonstrates the following capabilities:

1. Fetching web data using the `requests` module.
2. Processing data using Python collections such as lists, dictionaries, and sets.
3. Saving the processed data into different file formats, including text files, CSV, and JSON.

It showcases how to interact with web data, manipulate it in memory, and export it for further use.

## Project Structure

- **binware_analytics.py**: Main script that orchestrates data fetching, processing, and file creation.
- **utils_binware.py**: A utility module with reusable functions for the project.
- **binware_project_setup.py**: A module for project setup, including folder creation.
- **data/**: A folder where fetched data and processed results are saved.
  - **data-txt/**: Folder for text data files.
  - **data-csv/**: Folder for CSV data files.
  - **data-excel/**: Folder for Excel data files.
  - **data-json/**: Folder for JSON data files.

## Prerequisites

- Python 3.10 or higher is recommended.
- `requests`, `openpyxl`, and `xlrd` packages are required.

## Create Project Virtual Environment

On Windows, create a project virtual environment in the `.venv` folder. Use the following commands:

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

## Running the Project

1. Activate the virtual environment using the command provided above.
2. Run the main script to fetch, process, and save data:

python binware_analytics.py

## Project Output

- The script will create four folders within the `data` directory: `data-txt`, `data-csv`, `data-excel`, and `data-json`.
- It will fetch data from the specified URLs and save them in the respective folders:
  - `data-txt/data.txt`
  - `data-csv/data.csv`
  - `data-excel/data.xls`
  - `data-json/data.json`
- After fetching the data, the script processes the files and generates the following output files in the same directories:
  - `data-txt/results_txt.txt`: Contains the total word count and unique word count from the text file.
  - `data-csv/results_csv.txt`: Shows the average "Ladder score" calculated from the CSV data.
  - `data-excel/results_excel.txt`: Displays the total sum of values in a specific column from the Excel file.
  - `data-json/results_json.txt`: Lists the names of astronauts currently in space as retrieved from the JSON data.