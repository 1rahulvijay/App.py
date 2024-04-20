def submit(self):
    file1_path = self.file1_entry.get()
    file2_path = self.file2_entry.get()
    password = self.password_entry.get()
    text_column1 = self.text_column1_entry.get()
    text_column2 = self.text_column2_entry.get()

    if not all([file1_path, file2_path, password]):
        logging.error("Missing input fields")  # Log missing input error
        messagebox.showerror("Error", "Please fill in all fields.")
        return None

        # Start a new thread to perform the data processing and network operation
        threading.Thread(
            target=self.process_data_and_fetch,
            args=(file1_path, file2_path, password, text_column1, text_column2),
        ).start()


def process_data_and_fetch(
    self, file1_path, file2_path, password, text_column1, text_column2
):
    try:
        # Instantiate AnotherClass and pass the logger instance to it
        another_instance = AnotherClass(self.logger)
        # Pass file paths to AnotherClass for processing
        another_instance.do_something(file1_path, file2_path)

        # Simulate data processing (replace with your actual logic)
        output = f"File 1 Path: {file1_path}\nFile 2 Path: {file2_path}\nPassword: {password}\nText Column 1: {text_column1}\nText Column 2: {text_column2}"
        logging.info(output)  # Log simulated data processing

        # Perform the network operation here
        # For demonstration, let's just sleep for a few seconds
        import time

        time.sleep(5)
        logging.info("Data fetched from server")  # Log the completion

        # Show completion message
        messagebox.showinfo(
            "Process completed", "Data processing completed successfully!"
        )
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
