"""Make config and post_install.sh files"""

import fill_templates as ft

# Directory containing files with private data
PRIVATE_DIR = '/home/stefan/Documents/aws'

# json variables
VARS = PRIVATE_DIR+'/cluster_variables.json'

# make the config file

TEMPLATE = './templates/config_template'
OUTPUT_FILE = PRIVATE_DIR+'/config'
ft.fill(VARS, TEMPLATE, OUTPUT_FILE)

# # make the post_install file

# TEMPLATE = './templates/post_install_template'
# OUTPUT_FILE = PRIVATE_DIR+'/post_install.sh'
# ft.fill(VARS, TEMPLATE, OUTPUT_FILE)
