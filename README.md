# ArcGIS-FeatureClass-Merger

This repository contains a Python script designed to merge two different ArcGIS geodatabases while ensuring that duplicate features are removed. It automates the process of combining datasets, copying unique feature classes to a new geodatabase, and handling common feature classes by appending data and eliminating duplicates.

## Key Features

- **Automated Merging:** The script automatically merges feature classes from two geodatabases into a new output geodatabase.
- **Duplicate Removal:** Identifies and removes duplicate features based on their geometry (and optionally other attributes).
- **Customizable Paths:** Paths to the geodatabases can be easily modified to suit different projects.

## Usage

1. Modify the paths in the script (`path1`, `path2`, and `output_path`) to point to your specific geodatabases.
2. Run the script in an ArcGIS environment with Python support.
3. The output will be a merged geodatabase with duplicate features removed, ready for further analysis.
