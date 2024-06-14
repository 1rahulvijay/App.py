import os
import sys
import win32com.client

def refresh_excel_data(file_path):
    try:
        if not os.path.isfile(file_path):
            print(f"Error: File not found - {file_path}")
            return

        # Start an instance of Excel
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = False  # Set to True if you want to see the Excel UI

        # Open the workbook
        workbook = excel.Workbooks.Open(file_path)

        # Refresh all data connections
        workbook.RefreshAll()

        # Wait for all refreshes to complete
        while excel.CalculationState != 0:
            pass

        # Save and close the workbook
        workbook.Save()
        workbook.Close()

        # Quit the Excel application
        excel.Quit()

        print("Excel data refresh completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'excel' in locals():
            excel.Quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_excel_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    refresh_excel_data(file_path)
