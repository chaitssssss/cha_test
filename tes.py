# Correctly unpack if rows are nested tuples with single elements
if all(len(row) == 1 for row in rows):  # Means rows look like [(val1,), (val2,), ...]
    rows = [row[0] for row in rows]  # Unpack the nested tuples

# Create DataFrame if shapes match
if len(columns) == len(rows[0]):
    data_frame = pd.DataFrame(rows, columns=columns)
else:
    logger.error(f"Mismatch in number of columns: expected {len(columns)}, got {len(rows[0])}")
    raise ValueError(f"Shape of data does not match the number of columns: expected {len(columns)}, got {len(rows[0])}")

logger.info(f"DataFrame created with columns: {data_frame.columns.tolist()}")
