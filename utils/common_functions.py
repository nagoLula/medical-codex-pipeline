"""Shared utility functions for the project medical-codex-pipeline."""

# Functions:
# - save to format(df, base_filename): save Dataframe to CSV (and future formats easily) .
# - validate_code_format(code, pattern): helper to validate a regrex pattern(return bool).

from pathlib import Path
import pandas as pd
import logging
from datetime import datetime
import re

def save_to_format(df: pd.DataFrame, base_filename: str) -> None:

    """
    Save a DataFrame to multiple formats (currently CSV).

    Args:
        df (pd.DataFrame): The DataFrame to save.
        base_filename (str): The base filename without extension.

    Returns:
        None
    """
    try:
        # Ensure the output directory exists
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save as CSV
        csv_path = output_dir / f"{base_filename}.csv"
        df.to_csv(csv_path, index=False)
        logging.info(f"DataFrame saved as CSV to {csv_path}")

        # Future formats can be added here (e.g., JSON, Excel)
        # Example for JSON:
        # json_path = output_dir / f"{base_filename}.json"
        # df.to_json(json_path, orient='records', lines=True)
        # logging.info(f"DataFrame saved as JSON to {json_path}")

    except Exception as e:
        logging.error(f"Error saving DataFrame: {e}")
        
            