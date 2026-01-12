import gdal2tiles
import os
from multiprocessing import freeze_support

#default tile size 256

# Simple raster profile generation with depth 9
input_file = 'finalmap_grid_output.tif'  # Input raster file
output_dir = 'output_tiles_test_final/'  # Output directory

# Function to generate tiles

def generate_tiles():
    if os.path.exists(input_file):
        os.makedirs(output_dir, exist_ok=True)
        
        gdal2tiles.generate_tiles(
            input_file, 
            output_dir, 
            zoom='0-6', # Specify zoom levels
            nb_processes=2,
            profile='raster', # Use raster profile
        )
        print("Tile generation completed successfully!")
    else:
        print(f"Error: Input file '{input_file}' not found!")

# Main execution with proper multiprocessing support
if __name__ == '__main__':
    freeze_support()  # Fix for multiprocessing issues
    generate_tiles()
