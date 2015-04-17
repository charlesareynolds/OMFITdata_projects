#-*-Python-*-
# Created by creyn at 2015/02/13 10:35

import os.path

print ('running runHypnoToad.py (file:"%s")' % __file__)

idl_files_dir = str(root['SETTINGS']['SETUP']['hypnotoad_location'])
idl_statement = 'hypnotoad'

geqdsk_path = str(root['FILES']['G-EQDSK'])
idl_statement += ', GEQDSK_DIR="' + os.path.dirname(geqdsk_path)+ '"'
idl_statement += ', GEQDSK_FILE="' + os.path.basename(geqdsk_path) + '"'

grid_path = str(root['FILES']['grid'])
idl_statement += ', GRID_DIR="' + os.path.dirname(grid_path) + '"'
idl_statement += ', GRID_FILE="' + os.path.basename(grid_path) + '"'

OMFITx.execute(
    command_line='cd ' + idl_files_dir + ';' +  
                 'module add idl;' + 
                 'idl',
    interactive_input=None,
    ignoreReturnCode=False,
    std_out=None,
    std_err=None,
    quiet=False,
    arguments='-e ' + "'" + idl_statement + "'",
#    arguments='-demo -e ' + idl_statement,
    script=None)

print ('DONE running runHypnoToad.py')
