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
  'Property Assessment Calgary':
  'C:/Users/a_adli/docker_projects/calgary_gis_oo/input_data/'
  'property_assessment_calgary/property_assessment_calgary.shp',
  'Calgary 209':
  'C:/Users/a_adli/docker_projects/calgary_gis_oo/input_data/'
  'property_assessment_calgary_district_209/'
  'property_assessment_calgary_district_209.shp'
}

# Defining a directory for all the output data layers
output_paths_dir = 'C:/Users/a_adli/docker_projects/calgary_gis_oo/output_data'

# Preparing a bedding for output data layers paths
output_paths = {
  'Fixed Property Assessment Calgary': '',
  'Fixed Calgary 209': '',
}
