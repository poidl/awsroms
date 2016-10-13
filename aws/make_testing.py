"""Make cloudfront script to manage a single EC2 testing instance"""

import fill_templates as ft

TEMPLATE = './templates/ec2_testing_template'

# Directory containing files with private data
PRIVATE_DIR = '/home/stefan/Documents/aws'

VARS = PRIVATE_DIR+'/testing_variables.json'

# Output files. These will contain the private data!
OUTPUT_FILE = PRIVATE_DIR+'/ec2_testing.sh'

ft.fill(VARS, TEMPLATE, OUTPUT_FILE)
