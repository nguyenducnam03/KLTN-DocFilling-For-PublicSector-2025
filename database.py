import sqlite3

# --------------- Tạo Database -------------------
def create_database(tag_names):
    # Connect to SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('data.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Remove leading and trailing whitespaces and split the tag_names string into a list
    list_tag_names = [tag.strip() for tag in tag_names.split('\n') if tag.strip()]
    list_tag_names = [tag.replace('#', '') for tag in list_tag_names]
    # Create a table with columns based on tag_names
    create_table_query = f"CREATE TABLE IF NOT EXISTS data ({', '.join([f'{tag} TEXT' for tag in list_tag_names])})"
    cursor.execute(create_table_query)
    # Commit changes
    conn.commit()
    # Close the connection
    conn.close()

# ------------------- Đếm số dòng trong database ------------------
def count_rows():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM data;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    return count


# ---------------- Thêm thông tin vào datase -----------------------------
def insert_value_into_database(data_to_insert):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    columns = ', '.join(data_to_insert.keys())
    print(columns)
    placeholders = ', '.join(['?' for _ in range(len(data_to_insert))])
    print(placeholders)
    sql_query = f"INSERT INTO data ({columns}) VALUES ({placeholders})"
    values = [data_to_insert[key] for key in data_to_insert]
    cursor.execute(sql_query, values)
    conn.commit()
    conn.close()

def update_value_in_database(id, data_to_update):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Construct the SET part of the SQL query
    set_clause = ', '.join([f"{key} = ?" for key in data_to_update.keys()])
    
    # Construct the values to be updated
    values = list(data_to_update.values())
    values.append(id)  # Append the ID for the WHERE clause

    # Construct the SQL query
    sql_query = f"UPDATE data SET {set_clause} WHERE id = ?"

    # Execute the query
    cursor.execute(sql_query, values)
    conn.commit()
    conn.close()


# ------------------- Lấy thông tin tại 1 ô từ database ----------------------------
def get_value(id, key):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    sql_query = f'SELECT {key} FROM data WHERE ID = ?'
    cursor.execute(sql_query, (id,))
    value = cursor.fetchone()[0]
    conn.close()
    return value
    
# ----------------- Lấy thông tin từ nhiều key tại 1 dòng --------------------------
def get_values(id, list_cols, translations):
    list_info = []
    list_miss_keys = []
    list_miss_items = []
    for tag in list_cols:
        key = tag.replace("#","")
        value = get_value(id, key)
        if not value:
            list_miss_keys.append(tag)
            list_miss_items.append(translations[tag])
            list_info.append("Rỗng")
        else:
            list_info.append(value)
    return list_info, list_miss_keys, list_miss_items