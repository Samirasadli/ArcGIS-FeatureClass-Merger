import arcpy
import os

# Define paths to your geodatabases
path1 = r"C:\GIS\Project1\Project1.gdb"
path2 = r"C:\GIS\Project2\Project2.gdb"
output_path = r"C:\GIS\Output\FinalProject.gdb"

# Create output geodatabase if it doesn’t exist
if not arcpy.Exists(output_path):
    arcpy.CreateFileGDB_management(os.path.dirname(output_path), os.path.basename(output_path))

# Set the workspace to the first geodatabase and get a list of feature classes
arcpy.env.workspace = path1
feature_classes1 = arcpy.ListFeatureClasses()

# Set the workspace to the second geodatabase and get a list of feature classes
arcpy.env.workspace = path2
feature_classes2 = arcpy.ListFeatureClasses()

# Function to copy unique feature classes to the output geodatabase
def copy_unique_features(fc_list, src_workspace, dest_workspace):
    arcpy.env.workspace = src_workspace
    for fc in fc_list:
        dest_fc_path = os.path.join(dest_workspace, fc)
        if not arcpy.Exists(dest_fc_path):
            try:
                arcpy.Copy_management(fc, dest_fc_path)
                print(f"Copied {fc} to {dest_workspace}")
            except Exception as e:
                print(f"Error copying {fc}: {e}")

# Copy unique feature classes from both geodatabases to the output geodatabase
print("Copying feature classes from the first geodatabase...")
copy_unique_features(feature_classes1, path1, output_path)

print("Copying feature classes from the second geodatabase...")
copy_unique_features(feature_classes2, path2, output_path)

# Merge common feature classes by appending data from the second geodatabase to the first
arcpy.env.workspace = output_path
for fc in feature_classes1:
    if fc in feature_classes2:
        try:
            print(f"Appending {fc} from {path2} to {output_path}")
            arcpy.Append_management(inputs=os.path.join(path2, fc), target=os.path.join(output_path, fc), schema_type="NO_TEST")
        except Exception as e:
            print(f"Error appending {fc}: {e}")

# Remove duplicate features from the output geodatabase
arcpy.env.workspace = output_path
for fc in arcpy.ListFeatureClasses():
    try:
        print(f"Removing duplicates in {fc}...")
        arcpy.DeleteIdentical_management(in_dataset=fc, fields=["Shape"])  # You can add more fields if needed
    except Exception as e:
        print(f"Error removing duplicates from {fc}: {e}")

print("Merging complete! Duplicates removed.")
