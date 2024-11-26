import datetime


DB_USR_CONFIG = {
    'host': 'localhost',
    'user': 'std',
    'password': 'Fate_Panel_Kick',
    'database': 'chicagocrime'
}

CC_DB_TABLE_DEFINTIONS = {
    "crime_records": {
        "id": {"type": "INT", "python_type": int, "constraints": ["PRIMARY KEY"]},
        "case_number": {"type": "VARCHAR(50)", "python_type": str, "constraints": []},
        "date": {"type": "DATETIME", "python_type": datetime.datetime, "constraints": []},  
        "block": {"type": "TEXT", "python_type": str, "constraints": []},
        "iucr": {"type": "VARCHAR(10)", "python_type": str, "constraints": []},
        "primary_type": {"type": "TEXT", "python_type": str, "constraints": []},
        "description": {"type": "TEXT", "python_type": str, "constraints": []},
        "location_description": {"type": "TEXT", "python_type": str, "constraints": []},
        "arrest": {"type": "BOOLEAN", "python_type": bool, "constraints": []},
        "domestic": {"type": "BOOLEAN", "python_type": bool, "constraints": []},
        "beat": {"type": "VARCHAR(10)", "python_type": str, "constraints": []},
        "district": {"type": "VARCHAR(10)", "python_type": str, "constraints": []},
        "ward": {"type": "INT", "python_type": int, "constraints": []},
        "community_area": {"type": "VARCHAR(50)", "python_type": str, "constraints": []},
        "fbi_code": {"type": "VARCHAR(10)", "python_type": str, "constraints": []},
        "x_coordinate": {"type": "DOUBLE", "python_type": float, "constraints": []},
        "y_coordinate": {"type": "DOUBLE", "python_type": float, "constraints": []},
        "year": {"type": "INT", "python_type": int, "constraints": []},
        "updated_on": {"type": "DATETIME", "python_type": datetime.datetime, "constraints": []},
        "latitude": {"type": "DOUBLE", "python_type": float, "constraints": []},
        "longitude": {"type": "DOUBLE", "python_type": float, "constraints": []},
        "location": {"type": "TEXT", "python_type": str, "constraints": []},
    }
}