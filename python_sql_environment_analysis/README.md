Environmental Data Query and Visualization

This project is a Python-based application designed to query and visualize environmental condition data stored in a relational database. It offers a structured and efficient way to manage, analyze, and display datasets, such as temperature, relative humidity, and dew point, across various locations.
Features

    Database Integration:
        Supports a relational database schema for managing environmental data.
        Tables include EnvironData for sensor readings and LocationMap for mapping location metadata.

    Dynamic Queries:
        Provides flexible querying capabilities to extract specific datasets for analysis.
        Ensures efficient data handling, ideal for large datasets.

    Customizable Visualization:
        Integrates data visualization tools to graph and analyze trends.
        Designed for generating insights into environmental conditions across different locations.

Database Schema
Tables

    EnvironData:
        Stores environmental readings with columns for:
            entry_no: Sequential entry number.
            entry_datetime: Timestamp for each reading.
            temp_F: Temperature in Fahrenheit.
            rh_percent: Relative humidity percentage.
            dew_point_F: Dew point in Fahrenheit.

    LocationMap:
        Maps location_id to descriptive metadata about measurement locations.

Sample Location Mapping
Location ID	Description
21999191	Outdoors – Courtyard Door Overhang
21611332	Tub Room 2041
21611333	Hallway 600 on Linen Room Door Frame
Prerequisites

    Python 3.8 or higher.
    Required Python libraries:
        Pandas
        Matplotlib or other visualization libraries as specified.
        MySQL connector for database interaction.
    MySQL or compatible relational database system.

Setup Instructions

    Database Configuration:
        Edit the USR_CONFIG dictionary in DB_Constants.py to reflect your database credentials:
            host: Database host (default is localhost).
            user: Database username.
            password: Database password.

    Database Initialization:
        Use the TABLE_TEMPLATES in DB_Constants.py to create the necessary tables in your database.

    Run the Application:
        Execute the script in the Jupyter Notebook (Environ_Data_Query_and_Visualization.ipynb) to query and visualize data.

How It Works

    Connects to a database and retrieves environmental data.
    Maps retrieved data to locations for contextual understanding.
    Visualizes data in user-friendly plots for analysis.

Benefits

    Offers structured database management for environmental data.
    Enables real-time querying and analysis.
    Ideal for projects requiring location-specific environmental insights.