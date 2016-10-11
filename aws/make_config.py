import os
import jinja2

# Don't version control private data. 
# Use templates to populate config files and scripts with private data.

config_template = './config_template'
post_install_template = './post_install_template'

# Directory containing files with private data
private_dir='/home/stefan/Documents/aws'

# context is a file containing a dictionary, e.g.
# {
#     'key_name': 'mykey1',
# 	...
# }
context = private_dir+'/cluster_variables'

# Output files. These will contain the private data!
config_fname = private_dir+'/config'
post_install_fname = private_dir+'/post_install.sh'


# http://matthiaseisen.com/pp/patterns/p0198/
def render(fname_tmpl, context):
	path, f1 = os.path.split(fname_tmpl)
	return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(f1).render(context)


f = open(context, 'r')
context = eval(f.read())

tmp = render(config_template, context)
f = open(config_fname, 'w')
f.write(tmp)

tmp = render(post_install_template, context)
f = open(post_install_fname, 'w')
f.write(tmp)
