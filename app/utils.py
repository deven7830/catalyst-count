import csv
from django.core.exceptions import ValidationError


chunk_size = 1024  # Adjust the chunk size as needed
decoded_data = ""
def process_chunk(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            while True:
                chunk = csvfile.read(chunk_size)
                if not chunk:
                    break
                decoded_data += chunk.decode('utf-8')
    except FileNotFoundError:
        raise ValidationError('CSV file not found.')
    except csv.Error:
        raise ValidationError('Error occurred while reading the CSV file.')