import arcpy

# Set your workspace (the geodatabase where your feature classes are located)
workspace = r"C:\GIS\YourGeodatabase.gdb"  # Update to your workspace

# Set the source and target feature classes
source_fc = "SourceFeatureClass"  # The feature class to copy data from
target_fc = "TargetFeatureClass"  # The feature class to copy data to

# Set the workspace
arcpy.env.workspace = workspace

# Check if source and target feature classes exist
if not arcpy.Exists(source_fc):
    print(f"Error: Source feature class '{source_fc}' does not exist in the workspace.")
elif not arcpy.Exists(target_fc):
    print(f"Error: Target feature class '{target_fc}' does not exist in the workspace.")
else:
    # Perform the append operation
    try:
        arcpy.management.Append(inputs=source_fc, target=target_fc, schema_type="NO_TEST")
        print(f"Data successfully copied from {source_fc} to {target_fc}!")
    except arcpy.ExecuteError as e:
        print(f"Error executing Append: {e}")
