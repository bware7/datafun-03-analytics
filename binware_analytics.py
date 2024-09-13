"""
This project demonstrates:

1. Fetching web data using the `requests` module.
2. Processing data with Python collections like lists, dictionaries, and sets.
3. Saving processed data in text, CSV, and JSON formats.

It showcases how to interact with web data, manipulate it in memory, and export it for further use.

-- Bin Ware
"""

# Standard library imports
import csv
import json
import pathlib
import statistics

# External library imports (requires virtual environment)
import requests
import openpyxl  # For Excel file processing
import xlrd     # For reading .xls files directly


# Local module imports
import utils_binware
import binware_project_setup

#####################################
# Fetch and Write Functions
#####################################

def fetch_and_write_txt_data(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from a URL and write it to a text file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the file to save the data.
    - url (str): The URL from which to fetch the text data.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch text data: {e}")

def fetch_and_write_csv_data(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from a URL and write it to a CSV file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the file to save the data.
    - url (str): The URL from which to fetch the CSV data.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch CSV data: {e}")

def fetch_and_write_json_data(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch JSON data from a URL and write it to a JSON file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the file to save the data.
    - url (str): The URL from which to fetch the JSON data.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.RequestException as e:
        print(f"Failed to fetch JSON data: {e}")

def fetch_and_write_excel_data(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from a URL and write it to an Excel file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the file to save the data.
    - url (str): The URL from which to fetch the Excel data.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.RequestException as e:
        print(f"Failed to fetch Excel data: {e}")

#####################################
# Write Functions
#####################################

def write_txt_file(folder_name: str, filename: str, data: str) -> None:
    """
    Write text data to a file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the text file.
    - data (str): The text data to write to the file.

    """
    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        print(f"Text data saved to {file_path}")
    except IOError as e:
        print(f"Error writing text file {file_path}: {e}")

def write_csv_file(folder_name: str, filename: str, data: str) -> None:
    """
    Write CSV data to a file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the CSV file.
    - data (str): The CSV data to write to the file.

    """
    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        print(f"CSV data saved to {file_path}")
    except IOError as e:
        print(f"Error writing CSV file {file_path}: {e}")

def write_json_file(folder_name: str, filename: str, data: dict) -> None:
    """
    Write JSON data to a file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the JSON file.
    - data (dict): The JSON data to write to the file.

    """
    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")
    except IOError as e:
        print(f"Error writing JSON file {file_path}: {e}")

def write_excel_file(folder_name: str, filename: str, data: bytes) -> None:
    """
    Write binary Excel data to a file.

    Parameters:
    - folder_name (str): The name of the folder where the file will be saved.
    - filename (str): The name of the Excel file.
    - data (bytes): The binary Excel data to write to the file.

    """
    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with file_path.open('wb') as file:
            file.write(data)
        print(f"Excel data saved to {file_path}")
    except IOError as e:
        print(f"Error writing Excel file {file_path}: {e}")

#####################################
# Process Functions
#####################################

def process_txt_file(folder_name: str, input_filename: str, output_filename: str) -> None:
    """
    Process text data to count total and unique words.

    Parameters:
    - folder_name (str): The name of the folder containing the input file.
    - input_filename (str): The name of the input text file.
    - output_filename (str): The name of the output file to save results.

    """
    file_path = pathlib.Path(folder_name) / input_filename
    try:
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
        # Basic text processing
        words = text.lower().split()
        word_count = len(words)
        unique_words = set(words)
        unique_word_count = len(unique_words)
        # Save results
        output_path = pathlib.Path(folder_name) / output_filename
        with output_path.open('w', encoding='utf-8') as file:
            file.write(f"Total Words: {word_count}\n")
            file.write(f"Unique Words: {unique_word_count}\n")
        print(f"Text data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error processing text file {file_path}: {e}")

def process_csv_file(folder_name: str, input_filename: str, output_filename: str) -> None:
    """
    Process CSV data to calculate the average 'Ladder score'.

    Parameters:
    - folder_name (str): The name of the folder containing the input file.
    - input_filename (str): The name of the input CSV file.
    - output_filename (str): The name of the output file to save results.

    """
    file_path = pathlib.Path(folder_name) / input_filename
    data = []
    try:
        with file_path.open('r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        # Extract 'Ladder score' values
        scores = [float(row['Ladder score']) for row in data if 'Ladder score' in row and row['Ladder score']]
        if scores:
            average_score = statistics.mean(scores)
        else:
            average_score = 0.0
        # Save results
        output_path = pathlib.Path(folder_name) / output_filename
        with output_path.open('w', encoding='utf-8') as file:
            file.write(f"Average Ladder Score: {average_score}\n")
        print(f"CSV data processed and results saved to {output_path}")
    except (IOError, KeyError, ValueError) as e:
        print(f"Error processing CSV file {file_path}: {e}")

def process_json_file(folder_name: str, input_filename: str, output_filename: str) -> None:
    """
    Process JSON data to list astronauts currently in space.

    Parameters:
    - folder_name (str): The name of the folder containing the input file.
    - input_filename (str): The name of the input JSON file.
    - output_filename (str): The name of the output file to save results.

    """
    file_path = pathlib.Path(folder_name) / input_filename
    try:
        with file_path.open('r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        # Extract astronaut names
        astronauts = [person['name'] for person in data.get('people', [])]
        # Save results
        output_path = pathlib.Path(folder_name) / output_filename
        with output_path.open('w', encoding='utf-8') as file:
            file.write("Astronauts Currently in Space:\n")
            for astronaut in astronauts:
                file.write(f"- {astronaut}\n")
        print(f"JSON data processed and results saved to {output_path}")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error processing JSON file {file_path}: {e}")

def process_excel_file(folder_name: str, input_filename: str, output_filename: str) -> None:
    """
    Process Excel data to sum values in a specific column using xlrd.

    Parameters:
    - folder_name (str): The name of the folder containing the input file.
    - input_filename (str): The name of the input Excel file.
    - output_filename (str): The name of the output file to save results.

    """
    file_path = pathlib.Path(folder_name) / input_filename
    try:
        # Open the workbook using xlrd
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)  # Assuming data is in the first sheet
        total = 0
        # Iterate over rows, starting from the second row (index 1) if the first row is header
        for row_idx in range(1, sheet.nrows):
            cell_value = sheet.cell_value(row_idx, 1)  # Assuming values are in the second column (index 1)
            if isinstance(cell_value, (int, float)):
                total += cell_value
        # Save results
        output_path = pathlib.Path(folder_name) / output_filename
        with output_path.open('w', encoding='utf-8') as file:
            file.write(f"Total Value from Excel Data: {total}\n")
        print(f"Excel data processed and results saved to {output_path}")
    except Exception as e:
        print(f"Error processing Excel file {file_path}: {e}")


#####################################
# Main Function
#####################################

def main() -> None:
    """
    Main function to demonstrate module capabilities.

    Fetches data from various sources, processes it, and writes the results.

    """
    print(utils_binware.get_byline())

    # Create necessary data folders
    data_folders = ['data-txt', 'data-csv', 'data-excel', 'data-json']
    binware_project_setup.create_folders_from_list(data_folders, to_lowercase=True)

    # URLs and file names
    txt_url = 'http://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Fetch and write data
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Process data
    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_excel.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
