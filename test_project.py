from unittest.mock import patch
from datetime import datetime
import pytest
import os
from tempfile import NamedTemporaryFile
from project import get_twelve_months_ago, read_from_csv, write_to_csv, incomes

def test_get_twelve_months_ago():
    # Mocking the current date
    with patch('project.tday', datetime(2024, 1, 15)):
        result = get_twelve_months_ago()
        assert result == datetime(2023, 12, 15)

    with patch('project.tday', datetime(2024, 2, 15)):
        result = get_twelve_months_ago()
        assert result == datetime(2023, 2, 15)

    with patch('project.tday', datetime(2024, 3, 15)):
        result = get_twelve_months_ago()
        assert result == datetime(2023, 3, 15)

    with patch('project.tday', datetime(2024, 4, 15)):
        result = get_twelve_months_ago()
        assert result == datetime(2023, 4, 15)
  
    with patch('project.tday', datetime(2024, 12, 15)):
        result = get_twelve_months_ago()
        assert result == datetime(2023, 12, 15)

@pytest.fixture
def temporary_csv_file():
    # Create a temporary CSV file and yield its name
    with NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        yield temp_file.name
        os.remove(temp_file.name)

def test_read_from_csv(temporary_csv_file):
    # Write test data to the temporary file
    test_data = """year,month,amount
2024,7,3501.0
2024,5,7100.0
2024,1,6.0
"""
    with open(temporary_csv_file, mode='w', newline='') as file:
        file.write(test_data)

    # Read the data from the temporary file
    read_from_csv(temporary_csv_file)

    # Check if the 'incomes' dictionary is correctly populated
    expected_incomes = {
        "2024 7": 3501.0,
        "2024 5": 7100.0,
        "2024 1": 6.0,
    }
    assert incomes == expected_incomes

def test_write_to_csv(temporary_csv_file):
    # Populate the 'incomes' dictionary with test data
    test_incomes = {
        "2024 7": 3501.0,
        "2024 5": 7100.0,
        "2024 1": 6.0,
    }
    incomes.update(test_incomes)

    # Write the data to the temporary file
    write_to_csv(temporary_csv_file)

    # Verify if the file content matches the expected output
    expected_data = """year,month,amount
2024,7,3501.0
2024,5,7100.0
2024,1,6.0
"""
    with open(temporary_csv_file, mode='r') as file:
        content = file.read()

    assert content == expected_data