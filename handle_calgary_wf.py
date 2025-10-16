"""
handle_calgary_wf module
The workflow of cleaning and updating Calgary Buildings dataset.
Project Developer: Alireza Adli alireza.adli@mail.concordia.ca
"""

from scrub_layer_class import ScrubLayer
import input_paths_and_layers as paths

# Making folders for the output data layers
paths.create_output_folders(paths.output_paths, paths.output_paths_dir)

cerc_boundary = \
  ScrubLayer(
    paths.qgis_path,
    paths.input_paths['CERC Boundary'],
    'CERC Boundary')

# Initialize the input data layers
nrcan = ScrubLayer(paths.qgis_path, paths.input_paths['NRCan'], 'NRCan')

# Processing the NRCan layer includes fixing its geometries
print('Processing the NRCan layer')
print(nrcan)
nrcan.create_spatial_index()
nrcan.fix_geometries(paths.output_paths['Fixed NRCan'])

# Defining a new layer for the fixed NRCan
nrcan_fixed = \
  ScrubLayer(paths.qgis_path, paths.output_paths['Fixed NRCan'], 'Fixed NRCan')
nrcan_fixed.create_spatial_index()
print(nrcan_fixed)

nrcan_fixed.clip_layer(
  cerc_boundary.layer_path, paths.output_paths['NRCan CERC Fixed'])

nrcan_cerc_fixed = ScrubLayer(
  paths.qgis_path, paths.output_paths['NRCan CERC Fixed'], 'NRCan CERC Fixed')

nrcan_cerc_fixed.create_spatial_index()
print(nrcan_cerc_fixed)

