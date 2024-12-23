import csv

def parse_kitty_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # assume first line is header
        
        # Let's assume the file has two columns: PetName, Age
        for row in reader:
            if len(row) < 2:
                print("Found a row that doesn't have enough columns:", row)
                continue
            pet_name, age = row[0], row[1]
            print(f"{pet_name} is {age} years old!")

if __name__ == "__main__":
    # Example usage
    file_path = "sample_pets.csv"
    parse_kitty_csv(file_path)
