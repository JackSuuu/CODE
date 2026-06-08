import openpyxl

# Load the Excel file into a workbook object
wb = openpyxl.load_workbook('/Users/jack/Downloads/My_Excel_File.xlsx')

# Select the sheet you want to read
sheet = wb['Sheet1']

# Extract a specific row
row_num = 2  # The row number you want to extract
row = sheet[row_num]

# Extract a specific column
col_name = 'A'  # The name of the column you want to extract
col = [cell.value for cell in sheet[col_name]]

# Print the extracted row and column
print('Row {}:'.format(row_num))
for cell in row:
    print(cell.value, end=' ')
print()

print('Column {}:'.format(col_name))
print(col)
