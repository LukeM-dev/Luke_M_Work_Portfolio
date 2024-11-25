CSV Visualizer

This project is a Python-based application that provides an interactive interface for visualizing data stored in CSV files. Built with Panel, Pandas, and hvPlot, it simplifies the process of exploring and analyzing datasets by offering intuitive controls for customization.
Features
1. Dynamic File Monitoring

    Automatically detects and lists CSV files in a specified folder.
    Updates the file selection list in real time as files are added or removed.

2. Interactive Graph Controls

    Customize plots with user-selectable options for:
        X-axis and Y-axis columns.
        Plot types (scatter, line, bar, area).
        Colors.
    Ensures that selected columns are compatible across all graphs for consistent comparisons.

3. Graph Management

    Load and manage multiple graphs simultaneously.
    Combines individual plots into a unified display.
    Supports updating graphs dynamically as settings are adjusted.

4. Error Handling

    Identifies and logs issues with empty or malformed CSV files.
    Provides a debug pane for detailed feedback during data loading and plotting.

Prerequisites
Required Libraries

    Python 3.8 or higher
    Panel
    Pandas
    hvPlot

To install the required libraries, run:

pip install panel pandas hvplot

Setup Instructions

    Folder Monitoring:
        Place your CSV files in the data/ folder (default folder to monitor).

    Run the Application:
        Execute the script to launch the interactive interface:

        python app.py

    Use the Dashboard:
        Select files using the sidebar.
        Configure graph settings such as axes, plot type, and color.
        View the combined visualization in the main display area.

How It Works

    File Selection:
        Uses a CheckBoxGroup widget to allow selection of one or more CSV files.
        Automatically updates available files every two seconds.

    Graph Control:
        Synchronizes graph settings for all active datasets to ensure consistent visualizations.

    Visualization:
        Combines multiple graphs into a single unified plot using hvPlot.
        Interactive controls enable quick updates without reloading the application.

Benefits

    Easy-to-use interface for exploring CSV datasets.
    Minimal setup required for dynamic file monitoring.
    Supports multiple visualization types for tailored analysis.

Example Use Cases

    Analyzing trends in large datasets.
    Comparing multiple datasets simultaneously.
    Rapid prototyping of data visualization for presentations or reports.