"""Use templates to populate config files and scripts with private data.
    Don't version control private data."""

import os
import json
import jinja2

CONFIG_TEMPLATE = './config_template'
POST_INSTALL_TEMPLATE = './post_install_template'

# Directory containing files with private data
PRIVATE_DIR = '/home/stefan/Documents/aws'

# context is a file containing a dictionary, e.g.
# {
#     'key_name': 'mykey1',
# 	...
# }
VARS = PRIVATE_DIR+'/cluster_variables.json'

# Output files. These will contain the private data!
CONFIG_FNAME = PRIVATE_DIR+'/config'
POST_INSTALL_FNAME = PRIVATE_DIR+'/post_install.sh'


# render() is copied from http://matthiaseisen.com/pp/patterns/p0198/
def render(fname_tmpl, context):
    """render fills a template file with values from a dict."""
    path, basename = os.path.split(fname_tmpl)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(basename).render(context)


FILE = open(VARS, 'r')

VARS_DICT = json.load(FILE)

TMP = render(CONFIG_TEMPLATE, VARS_DICT)
FP = open(CONFIG_FNAME, 'w')
FP.write(TMP)

TMP = render(POST_INSTALL_TEMPLATE, VARS_DICT)
FP = open(POST_INSTALL_FNAME, 'w')
FP.write(TMP)
