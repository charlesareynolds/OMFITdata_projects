#-*-Python-*-
# Created by creyn at 2015/02/12 11:06

import os.path

print ('running runCOGENT.py (file:"%s")' % __file__)

# Add the .pbs script:
arguments=str(root['SCRIPTS']['COGENTPBS'])

# Copy the parm file to a batch-accessible directory and add its batch location:
parm_file_tmp_name = str(root['FILES']['COGENT_parms'])
parm_file_basename = os.path.basename (parm_file_tmp_name)
parm_file_server_dir = '/global/homes/c/creyn/code/test'
#parm_file_server_dir = root['SETTINGS']['REMOTE_SETUP']['workDir']
parm_file_server_name = parm_file_server_dir + os.sep + parm_file_basename
OMFITx.remote_upsync(
	server=root['SETTINGS']['REMOTE_SETUP']['serverPicker'],
        local=parm_file_tmp_name,
        remote=parm_file_server_name)

arguments += ' -v ' + parm_file_server_name
#arguments += ' -v COGENT_INFILE=/global/homes/c/creyn/code/test/gam_regression.in_my'
# Below is commented out for now because it is on local /tmp which is not 
# available to batch nodes.  /global is, and /scratch1 is on edison.
#arguments += ' -v COGENT_INFILE=' + str(root['FILES']['COGENT_parms'])

OMFITx.execute(
    command_line='qsub',
    interactive_input=None,
    ignoreReturnCode=False,
    std_out=None,
    std_err=None,
    quiet=False,
    arguments=arguments,
    script=None)

print ('DONE running runCOGENT.py')
