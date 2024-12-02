import datetime

DB_USR_CONFIG = {
    'host': 'localhost',
    'user': 'std',
    'password': 'Fate_Panel_Kick',
    'database': 'chicagocrime'
}

TABLE_NAMES = {
    'crime': 'crime_records',
    'ward': 'ward_definitions',
    'beat': 'beat_definitions',
    'district': 'district_definitions'
}

DB_COLUMN_NAME_MAP = {
    "crime_records": {
        "ID": "id",
        "Case Number": "case_number",
        "Date": "date",
        "Block": "block",
        "IUCR": "iucr",
        "Primary Type": "primary_type",
        "Description": "description",
        "Location Description": "location_description",
        "Arrest": "arrest",
        "Domestic": "domestic",
        "Beat": "beat",
        "District": "district",
        "Ward": "ward",
        "Community Area": "community_area",
        "FBI Code": "fbi_code",
        "X Coordinate": "x_coordinate",
        "Y Coordinate": "y_coordinate",
        "Year": "year",
        "Updated On": "updated_on",
        "Latitude": "latitude",
        "Longitude": "longitude",
        "Location": "location",  
    }
}

CC_DB_TABLE_DEFINTIONS = {
    "crime_records": {
        "id": {
            "type": "INT",
            "python_type": int,
            "constraints": ["PRIMARY KEY"],
            "csv_column_name": "ID"
        },
        "case_number": {
            "type": "VARCHAR(50)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Case Number"
        },
        "date": {
            "type": "DATETIME",
            "python_type": datetime.datetime,
            "constraints": [],
            "csv_column_name": "Date"
        },
        "block": {
            "type": "TEXT",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Block"
        },
        "iucr": {
            "type": "VARCHAR(10)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "IUCR"
        },
        "primary_type": {
            "type": "TEXT",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Primary Type"
        },
        "description": {
            "type": "TEXT",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Description"
        },
        "location_description": {
            "type": "TEXT",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Location Description"
        },
        "arrest": {
            "type": "BOOLEAN",
            "python_type": bool,
            "constraints": [],
            "csv_column_name": "Arrest"
        },
        "domestic": {
            "type": "BOOLEAN",
            "python_type": bool,
            "constraints": [],
            "csv_column_name": "Domestic"
        },
        "beat": {
            "type": "VARCHAR(10)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Beat"
        },
        "district": {
            "type": "VARCHAR(10)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "District"
        },
        "ward": {
            "type": "INT",
            "python_type": int,
            "constraints": [],
            "csv_column_name": "Ward"
        },
        "community_area": {
            "type": "VARCHAR(50)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Community Area"
        },
        "fbi_code": {
            "type": "VARCHAR(10)",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "FBI Code"
        },
        "x_coordinate": {
            "type": "DOUBLE",
            "python_type": float,
            "constraints": [],
            "csv_column_name": "X Coordinate"
        },
        "y_coordinate": {
            "type": "DOUBLE",
            "python_type": float,
            "constraints": [],
            "csv_column_name": "Y Coordinate"
        },
        "year": {
            "type": "INT",
            "python_type": int,
            "constraints": [],
            "csv_column_name": "Year"
        },
        "updated_on": {
            "type": "DATETIME",
            "python_type": datetime.datetime,
            "constraints": [],
            "csv_column_name": "Updated On"
        },
        "latitude": {
            "type": "DOUBLE",
            "python_type": float,
            "constraints": [],
            "csv_column_name": "Latitude"
        },
        "longitude": {
            "type": "DOUBLE",
            "python_type": float,
            "constraints": [],
            "csv_column_name": "Longitude"
        },
        "location": {
            "type": "TEXT",
            "python_type": str,
            "constraints": [],
            "csv_column_name": "Location"
        },
    }
}
