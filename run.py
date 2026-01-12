import gdal2tiles
import os
from multiprocessing import freeze_support

# Simple raster profile generation with depth 9
input_file = 'finalmap_grid_output.tif'
output_dir = 'output_tiles_test_final/'

def generate_tiles():
    if os.path.exists(input_file):
        os.makedirs(output_dir, exist_ok=True)
        
        gdal2tiles.generate_tiles(
            input_file, 
            output_dir, 
            zoom='0-6',
            nb_processes=2,
            profile='raster',
        )
        print("Tile generation completed successfully!")
    else:
        print(f"Error: Input file '{input_file}' not found!")

# Main execution with proper multiprocessing support
if __name__ == '__main__':
    freeze_support()  # Fix for multiprocessing issues
    generate_tiles()
