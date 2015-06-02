#-*-Python-*-
# Created by creyn at 2015/02/12 11:06

import os.path

print ('running runCOGENT.py (file:"%s")' % __file__)

# Same as runHypntoad.py:
import shutil

def copy_to_other_working(work_path, other_work_dir):
    """other_work_dir can be a complete file name or just a directory,
    just like unix cp.
    """
    shutil.copy(work_path, other_work_dir) 

def move_from_other_working(work_path, other_work_dir):
    """other_work_dir can only be a direcotory.
    """
    work_dir = os.path.dirname(work_path)
    name = os.path.basename (work_path)
    other_work_path = other_work_dir + os.sep + name
    # Have to use the complete work path as destination because every 
    # working OMFIT file is in its own directory:
    shutil.move(other_work_path, work_path) 
# END Same as runHypntoad.py.

# Copy the parm file etc. to a batch-accessible directory and add its batch location:
# NOTE: watch for multiple runs, users, etc.
server_dir = '/global/homes/c/creyn/code/test'
# Below commented out because I don't have permission to write to /scratch1/creyn
#server_dir = root['SETTINGS']['REMOTE_SETUP']['workDir']

parm_file_path = str(root['FILES']['COGENT_parms'])
parm_file_basename = os.path.basename (parm_file_path)
parm_file_server_path = server_dir + os.sep + parm_file_basename
copy_to_other_working(parm_file_path, parm_file_server_path)

coeff_file_path = str(root['FILES']['nodal_COGENT_coefficients'])
coeff_file_basename = os.path.basename (coeff_file_path)
coeff_file_server_path = server_dir + os.sep + coeff_file_basename
copy_to_other_working(coeff_file_path, coeff_file_server_path)

grid_file_path = str(root['FILES']['nodal_grid'])
grid_file_basename = os.path.basename (grid_file_path)
grid_file_server_path = server_dir + os.sep + grid_file_basename
copy_to_other_working(grid_file_path, grid_file_server_path)


# Add the .pbs script:
arguments=str(root['SCRIPTS']['COGENTPBS'])
# Set environment variables in the batch environment:
arguments += ' -v COGENT_PARM_FILE=' + parm_file_server_path
arguments += ', COGENT_COEFF_FILE=' + coeff_file_server_path
arguments += ', COGENT_GRID_FILE=' + grid_file_server_path

#arguments += ' -v COGENT_PARM_FILE=/global/homes/c/creyn/code/test/gam_regression.in_my'

# Below doesn't work because it is on local /tmp which is not 
# available to batch nodes.  /global is, and /scratch1 is on edison.
#arguments += ' -v COGENT_PARM_FILE=' + str(root['FILES']['COGENT_parms'])

OMFITx.execute(
    command_line='qsub',
    interactive_input=None,
    ignoreReturnCode=False,
    std_out=None,
    std_err=None,
    quiet=False,
    arguments=arguments,
    script=None)

# Have to copy each file separately because every 
# working OMFIT file lives in its own directory:
# TODO: copy the resulting files to the plot files dir:
move_from_other_working(root['FILES']['plot_files_dir'], idl_work_dir)

print ('DONE running runCOGENT.py')
