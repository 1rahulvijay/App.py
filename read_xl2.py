import pandas as pd


def read_file(file_path):
    try:
        # Check the file extension and read the file accordingly
        if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            df = pd.read_excel(file_path)
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            raise ValueError(
                "Unsupported file format. Please provide an Excel (.xlsx, .xls) or CSV (.csv) file."
            )

        return df

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return None


# Example usage:
file_path = "path/to/your/file.xlsx"
data = read_file(file_path)
if data is not None:
    print(data.head())
