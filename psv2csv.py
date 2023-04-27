import csv
import glob

# Retrieve a list of all PSV files in the current directory
psv_files = glob.glob('*.psv')

# Process each PSV file
for psv_file in psv_files:
    # Construct the name of the output CSV file by replacing the file extension
    csv_file = psv_file.replace('.psv', '.csv')

    # Open the PSV file for reading
    with open(psv_file) as input_file:
        csv_reader = csv.reader(input_file, delimiter='|')

        # Create a new CSV file for writing
        with open(csv_file, mode='w', newline='') as output_file:
            csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Write the header row to the CSV file
            header_row = next(csv_reader)
            csv_writer.writerow(header_row)

            # Write each row from the PSV file to the CSV file
            for row in csv_reader:
                csv_writer.writerow(row)