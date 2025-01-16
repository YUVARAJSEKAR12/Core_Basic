import pandas as pd

def get_customers_in_time_range(start_time, end_time):
    # Read data from Excel file
    df = pd.read_excel('TestData/Monday_Power_Consumption_Data.xlsx')

    # Filter data based on time range
    filtered_df = df[(df['Time'] >= start_time) & (df['Time'] <= end_time)]

    # Calculate total number of customers
    total_customers = filtered_df['Power Consumption (Watts)'].sum()

    return total_customers


# Example usage
#excel_file =str(input('Enter the excel_file name '))
start_time = input("Enter start time (HH:MM): ")
end_time = input("Enter end time (HH:MM): ")

total_customers = get_customers_in_time_range(start_time, end_time)

print(f"Total customers between {start_time} and {end_time}: {total_customers}")