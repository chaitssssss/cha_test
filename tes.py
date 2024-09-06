if len(columns) == len(rows[0]):  # Ensure the shape matches
    data_frame = pd.DataFrame(rows, columns=columns)
else:
    logger.error(f"Mismatch in number of columns: expected {len(rows[0])}, got {len(columns)}")
    raise ValueError(f"Shape of data does not match the number of columns: {len(rows[0])} vs {len(columns)}")


logger.info("Printing column names for omni_items_join data:")
logger.info(f"{data_frame.columns.tolist()}")
