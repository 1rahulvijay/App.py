def read_excel_custom(file_path, header_row):
    try:
        print(f"Reading file: {file_path} with header row: {header_row}")
        df = pd.read_excel(file_path, header=header_row)
        print(f"DataFrame shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

# Use the custom function
df_custom = read_excel_custom('your_file.xlsx', header_row=2)
if df_custom is not None:
    print(df_custom)
