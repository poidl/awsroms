"""Use templates to populate config files and scripts with private data.
    Don't version control private data."""

import os
import json
import jinja2

# render() is copied from http://matthiaseisen.com/pp/patterns/p0198/
def render(fname_tmpl, context):
    """render fills a template file with values from a dict."""
    path, basename = os.path.split(fname_tmpl)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(basename).render(context)

def fill(varsjson, templ_fname, output_fname):
    """Read json variable data, fill it in the template and write result to file."""
    # varsjson is a file containing a json object, e.g.
    # {
    #   "key_name": "mykey1",
    #   ...
    # }
    file = open(varsjson, 'r')

    vars_dict = json.load(file)

    tmp = render(templ_fname, vars_dict)
    file = open(output_fname, 'w')
    file.write(tmp)
