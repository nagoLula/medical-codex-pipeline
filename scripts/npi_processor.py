def main():
    print("Starting NPI Processing...")
    
    #Load source data
    source_data = load_npi_data("input/NPI.csv") # type: ignore
    print(f"Loaded {len(source_data)} records from source data.")
    #clean and process data
    clean_data = clean_npi_data:(source_data) # type: ignore
    print(f"Cleaned data contains {len(clean_data)} records after processing.")
    
    


