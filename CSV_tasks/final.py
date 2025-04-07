import csv
import os

def read_existing_data(file_path):
    if not os.path.exists(file_path):
        return set()

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        return {tuple(row) for row in reader}

def group_by_data(file_path, column_name):
    grouped_data = {}

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        if column_name not in header:
            print(f"{column_name} not found..!!")
            return  

        column_index = header.index(column_name)

        for row in reader:
            title = row[column_index].replace("/", "_")

            if title not in grouped_data:
                grouped_data[title] = []
            grouped_data[title].append(row)

    output_folder = f"{column_name}_Files"
    os.makedirs(output_folder, exist_ok=True)

    for title, rows in grouped_data.items():
        column_filename = os.path.join(output_folder, f"{title}.csv")
        existing_data = read_existing_data(column_filename)
        new_rows = [row for row in rows if tuple(row) not in existing_data]

        if new_rows:
            with open(column_filename, "a", newline="") as file:
                writer = csv.writer(file)
                if not existing_data:  
                    writer.writerow(header)

                writer.writerows(new_rows)

            print(f"New data appended to '{column_filename}'")
        else:
            print(f"No new data for '{title}', skipping update.")

path = "organizations-100demo.csv"
group_by_data(path, "Country")
group_by_data(path, "Founded")
group_by_data(path, "Industry")