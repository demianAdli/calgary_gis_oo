"""
input_paths_and_layers module
Project Developer: Alireza Adli alireza.adli@concordia.ca
"""
import os


def create_output_folders(paths_dict, output_dir):
  for path in paths_dict.keys():
    new_folder = path.lower().replace(' ', '_')
    output_path = output_dir + '/' + new_folder
    os.mkdir(output_path)
    if path[-1] != 's':
      paths_dict[path] = output_path + f'/{new_folder}.shp'
    else:
      paths_dict[path] = output_path


# Application's path
qgis_path = 'C:/Program Files/QGIS 3.34.1/apps/qgis'

# Gathering input data layers paths
input_paths = {
  'NRCan':
  'C:/Users/a_adli/PycharmProjects/mtl_gis_oo/input_data/nrcan/'
  'Autobuilding_QC_VILLE_MONTREAL.shp',
  'GeoIndex':
  'C:/Users/a_adli/PycharmProjects/mtl_gis_oo/input_data/'
  'Geoindex_81670/mamh_usage_predo_2022_s_poly.shp',
  'Property Assessment':
  'C:/Users/a_adli/PycharmProjects/mtl_gis_oo/input_data/'
  'property_assessment/uniteevaluationfonciere.shp',
  'CERC Boundary':
  'C:/Users/a_adli/PycharmProjects/mtl_gis_oo/input_data/'
  'cerc_district_111/layer_111.shp'
}

# Defining a directory for all the output data layers
output_paths_dir = \
  'C:/Users/a_adli/PycharmProjects/mtl_gis_oo/' \
  'output_data'

# Preparing a bedding for output data layers paths
output_paths = {
  'Fixed NRCan': '',
  'NRCan CERC Fixed': '',
  'Fixed GeoIndex': '',
  'Clipped Fixed GeoIndex': '',
  'CERC Property Assessment': '',
  'Splitted CERC NRCans': '',
  'Pairwise Clipped Property Assessment Partitions': '',
  'Pairwise Clipped Merged Property Assessment': '',
  'Property Assessment and NRCan': '',
  'Property Assessment and NRCan and GeoIndex': '',
  'Deleted Duplicates Layer': '',
  'Single Parts Layer': ''
}
