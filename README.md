# Report Processing Project

## Description

This project processes member and payment data to generate reports on membership and payment activity. It performs the following tasks:

1. **Data Loading:** Loads member data from a CSV file and payment data from an Excel file.
2. **Data Cleaning and Transformation:** Cleans and transforms the data, including converting data types and merging datasets.
3. **Report Generation:** Generates reports on total payments per ward and payment activity by group, including member counts and total amounts paid.
4. **Data Export:** Exports the generated reports to Excel files.

## Installation

1. **Install Required Libraries:** Make sure you have the following libraries installed:
2. **Upload Data Files:** Upload your 'Members.csv' and 'PaymentsJan.xlsx' files to your Google Colab environment. Ensure they are accessible via the specified paths in the code.

## Usage

1. **Open the Colab Notebook:** Open the provided Colab notebook.
2. **Update File Paths:** Replace the placeholder file paths with the actual paths to your data files.
3. **Run the Code:** Execute the code cells in the notebook sequentially.
4. **View and Download Reports:** View the generated reports within the notebook. Downloaded reports will be saved in the Colab environment.

## Output

The project generates the following output files:

- `total_payments_per_ward.xlsx`: Contains the total payments made per ward.
- `group_nama_ward_member_size_paid.xlsx`: Contains group-wise payment activity, including total member count, total members paid, and total amount paid.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, please feel free to submit a pull request.

## License

This project is licensed under the MIT License.

## Author

[Your Name]
