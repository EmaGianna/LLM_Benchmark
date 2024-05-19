import os

def create_db_from_csv_prompts(path_dir):
    """
    The function `create_db_from_csv_prompts` reads CSV files from a directory, creates a DataFrame for
    each file, and stores the data in a SQLite database using the table name derived from the file name.
    
    :param path_dir: The `path_dir` parameter in the `create_db_from_csv_prompts` function is the
    directory path where the CSV files are located. This function reads each CSV file in the specified
    directory, creates a DataFrame from the data in the CSV file, and then stores the data in a SQLite
    database table
    """
    files = os.listdir(path_dir)
    for file in files:
      if '.csv' in file:
        print(file)
        tbl_name = file.split('.')[0]
        df = pd.read_csv(os.path.join(path_dir, file), sep=';')
        print(df)
        df.to_sql(tbl_name, con, if_exists='replace', index=False)