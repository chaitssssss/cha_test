rows = m1_results.fetchall()
print("Fetched rows (first 5):", rows[:5])  # Inspect the first few rows

# Get column names from cursor description
columns = [desc[0] for desc in m1_results.description]
print("Column names:", columns)
print(f"Expected number of columns: {len(columns)}")

# Check if the fetched rows are nested tuples and adjust accordingly
if rows and all(isinstance(row, tuple) for row in rows):
    # If rows are nested tuples with a single element, flatten them
    if len(rows[0]) == 1 and len(columns) > 1:
        rows = [row[0] for row in rows]  # Unpacking if rows are [(x,), (y,), ...]
    elif len(rows[0]) != len(columns):
        logger.error(f"Mismatch in the number of columns: data has {len(rows[0])} columns, expected {len(columns)}.")
        raise ValueError(f"Shape of data does not match the number of columns: {len(rows[0])} vs {len(columns)}")
else:
    logger.error("Fetched rows are not tuples, or are empty.")
    raise ValueError("Fetched rows are not tuples, or are empty.")

# Create DataFrame if shapes match
try:
    data_frame = pd.DataFrame(rows, columns=columns)
    logger.info("DataFrame created successfully with columns: {}".format(data_frame.columns.tolist()))
except ValueError as e:
    logger.error(f"Error creating DataFrame: {e}")
    raise ValueError(f"Could not create DataFrame due to shape mismatch: {e}")
