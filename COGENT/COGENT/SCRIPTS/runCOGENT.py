#-*-Python-*-
# Created by creyn at 2015/02/12 11:06

import os.path

print ('running runCOGENT.py (file:"%s")' % __file__)

# Same as runHypntoad.py:
import shutil
import os
import os.path

def copy_to_other_work_dir(work_path, other_work_dir):
    work_path = str(work_path)
    other_work_dir = str(other_work_dir)
    assert os.path.isdir(other_work_dir), other_work_dir
    shutil.copy(work_path, other_work_dir) 

def move_from_other_work_dir(work_path, other_work_dir):
    work_path = str(work_path)
    other_work_dir = str(other_work_dir)
    assert os.path.isdir(other_work_dir), other_work_dir
    file_name = os.path.basename(work_path)
    other_work_path = os.path.join(other_work_dir, file_name)
    # Have to use the complete work path as destination because every 
    # working OMFIT file is in its own directory:
    shutil.move(other_work_path, work_path) 

def remove_from_other_work_dir(work_path, other_work_dir):
    work_path = str(work_path)
    other_work_dir = str(other_work_dir)
    assert os.path.isdir(other_work_dir), other_work_dir
    file_name = os.path.basename(work_path)
    other_work_path = os.path.join(other_work_dir, file_name)
    os.remove(other_work_path) 
# END Same as runHypntoad.py.

# Copy the parm file etc. to a batch-accessible directory and add its batch location:
# NOTE: watch for multiple runs, users, etc.
server_name = root['SETTINGS']['REMOTE_SETUP']['serverPicker']
server_dir = SERVER[server_name]['workDir']
parm_file_path = str(root['FILES']['COGENT_parms'])
copy_to_other_work_dir(parm_file_path, server_dir)
copy_to_other_work_dir(str(root['FILES']['nodal_COGENT_Coefficients']), server_dir)
copy_to_other_work_dir(str(root['FILES']['nodal_grid']), server_dir)


# Add the .pbs script:
arguments=str(root['SCRIPTS']['COGENTPBS'])
# Put the parm file location in an environment variable in the batch environment:
parm_file_server_path = server_dir + os.sep + os.path.basename (parm_file_path)
arguments += ' -v COGENT_PARM_FILE=' + parm_file_server_path
# And the working dir: (used by cd in COGENTPBS script)
# No space is allowed after the comma by qsub:
arguments += ',COGENT_WORK_DIR=' + server_dir 


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

# TODO: copy the resulting files from the server_dir to the plot files dir 
# AFTER COGENT comppletes, in another script.
# move_from_other_working(root['FILES']['plot_files_dir'], idl_work_dir)

print ('DONE running runCOGENT.py')
