import arcpy
import os

# Set the path to the folder containing your .lyrx files (symbology files)
lyrx_folder = r"C:\Users\samir\OneDrive\Masaüstü\New folder (2)\Layers"

# Get the current ArcGIS Pro project
project = arcpy.mp.ArcGISProject("CURRENT")

# Get the active map
active_map = project.activeMap

# Create a dictionary to map the .lyrx layer names to the actual map layer names
layer_name_mapping = {
    "AshaghiTezyiqMovcudPE": "Aşağı təzyiqli mövcud polietilen qaz xətti",
    "AshaghiTezyiqMovcudYeralti": "Aşağı təzyiqli mövcud yeraltı qaz xətti",
    "AshaghiTezyiqMovcudYerustu": "Aşağı təzyiqli mövcud yerüstü qaz xətti",
    "OrtaTezyiqMovcudYeralti": "Orta təzyiqli mövcud yeraltı qaz xətti",
    "Orta təzyiqli mövcud yeraltı qaz xətti": "Orta təzyiqli mövcud yeraltı qaz xətti",
    "Layihələndirilən aşağı təzyiqli yerüstü qaz xətti": "Layihələndirilən aşağı təzyiqli yerüstü qaz xətti",
    "Orta təzyiq layihələndirilən yeraltı qaz xətti": "Orta təzyiq layihələndirilən yeraltı qaz xətti",
    "Orta təzyiqli layihələndirilən yer üstü qaz xətti": "Orta təzyiqli layihələndirilən yer üstü qaz xətti",
    "OrtaTezyiqMovcudPE": "Orta təzyiqli mövcud polietilen qaz xətti",
    "OrtaTezyiqMovcudYerustu": "Orta təzyiqli mövcud yerüstü qaz xətti",
    "QazTenzimleyiciMenteqe": "Qaz tənzimləyici məntəqə",
    "Quraşdırılmış balans sayğacı": "Quraşdırılmış balans sayğacı",
    "Regulator": "Requlyator",
    "Saygac": "Sayğac",
    "YeraltiBaglayiciKlapan": "Yeraltı bağlayıcı klapan",
    "YerustuBaglayiciKlapan": "Yerüstü bağlayıcı klapan",
    "YuksekTezyiqMovcudPE": "Yüksək təzyiqli mövcud polietilen qaz xətti",
    "YuksekTezyiqMovcudYeralti": "Yüksək təzyiqli mövcud yeraltı qaz xətti",
    "YuksekTezyiqMovcudYerustu": "Yüksək təzyiqli mövcud yeraltı qaz xətti",
    "Əlaqələndirici siyirtmə": "Əlaqələndirici siyirtmə"
}

# Loop through all the .lyrx files in the specified folder
for lyrx_file in os.listdir(lyrx_folder):
    if lyrx_file.endswith(".lyrx"):
        # Construct the full path to the .lyrx file
        lyrx_path = os.path.join(lyrx_folder, lyrx_file)

        # Load the symbology from the .lyrx file
        lyrx_layer = arcpy.mp.LayerFile(lyrx_path).listLayers()[0]
        lyrx_layer_name = lyrx_layer.name

        # Map the lyrx layer name to the actual map layer name
        actual_layer_name = layer_name_mapping.get(lyrx_layer_name, lyrx_layer_name)

        # Find the corresponding layer in the active map by name
        existing_layer = None
        for layer in active_map.listLayers():
            if layer.name == actual_layer_name:
                existing_layer = layer
                break

        if existing_layer:
            # Apply the symbology from the .lyrx file to the existing layer
            existing_layer.symbology = lyrx_layer.symbology
            print(f"Updated symbology for layer: {existing_layer.name}")
        else:
            print(f"Layer {actual_layer_name} not found in the active map, skipping.")

# Save the project
project.save()

print("Layer symbology updated successfully!")
