import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads sales data from a CSV and performs initial cleaning steps.

    Args:
        file_path (str): The full path to the sales data CSV file.

    Returns:
        pd.DataFrame: The cleaned DataFrame, or None if the file is not found.
    """
    try:
        # Load the data
        df = pd.read_csv(file_path)

        # Drop rows that are completely empty
        df.dropna(how="all", inplace=True)


        # Drop the header row that may appear in the middle of the data
        df = df[df['Order ID'].str[0:2] != 'Or']

        # Return the cleaned DataFrame
        return df
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the path.")
        return None

