#-*-Python-*-
# Created by creyn at 2015/004/17 08:36

import os.path

print ('running run_cogent_grid.py (file:"%s")' % __file__)

idl_files_dir = str(root['SCRIPTS']['cogent_grid location'])
idl_statement = 'cogent_grid'

#grid_path = str(root['FILES']['grid'])
#idl_statement += ', GRID_DIR="' + os.path.dirname(grid_path) + '"'
#idl_statement += ', GRID_FILE="' + os.path.basename(grid_path) + '"'

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

print ('DONE running run_cogent_grid.py')
