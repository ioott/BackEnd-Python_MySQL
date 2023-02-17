import csv


def export_csv(file_path, report):
    with open(file_path, mode="w") as file:
        csv_writer = csv.writer(file)

        for transaction in report:
            csv_writer.writerow(transaction)
