# Fetch all results
rows = m1_results.fetchall()
print("Fetched rows:", rows)  # Print all rows for inspection

# Get column names from cursor description
columns = [desc[0] for desc in m1_results.description]
print("Column names:", columns)

# Check if rows are indeed tuples and not empty
if rows and isinstance(rows, list) and all(isinstance(row, tuple) for row in rows):
    if len(rows[0]) == len(columns):  # Ensure the shape matches exactly
        # Create DataFrame safely
        try:
            data_frame = pd.DataFrame(rows, columns=columns)
            logger.info("DataFrame created successfully with columns: {}".format(data_frame.columns.tolist()))
        except ValueError as e:
            logger.error(f"Error creating DataFrame: {e}")
            raise ValueError(f"Could not create DataFrame due to shape mismatch: {e}")
    else:
        logger.error(f"Mismatch in the number of columns: data has {len(rows[0])} columns, expected {len(columns)}.")
        raise ValueError(f"Shape of data does not match the number of columns: {len(rows[0])} vs {len(columns)}")
else:
    logger.error("Fetched rows are not tuples, or are empty.")
    raise ValueError("Fetched rows are not tuples, or are empty.")
