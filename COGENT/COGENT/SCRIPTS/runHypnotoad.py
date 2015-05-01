# Created by creyn at 2015/02/13 10:35

print ('running runHypnoToad.py (file:"%s")' % __file__)

# Copied to other script(s) - need to import somehow:
import os
import os.path
import shutil

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
# END Copied to other script(s) - need to import somehow.

idl_work_dir = root['SETTINGS']['HYPNOTOAD']['workDir']
copy_to_other_work_dir(root['FILES']['G-EQDSK'], idl_work_dir)

idl_statement = 'hypnotoad'
arguments=' -e ' + idl_statement,
# useful if all IDL licenses are taken.  Runs for 7 minutes:
# arguments='-demo ' + arguments,
idl_source_dir = root['SETTINGS']['HYPNOTOAD']['sourceDir']
OMFITx.execute(
    command_line='cd ' + idl_source_dir + ';' +  
                 'module add idl;' + 
                 'idl',
    interactive_input=None,
    ignoreReturnCode=False,
    std_out=None,
    std_err=None,
    quiet=False,
    arguments=arguments,
    script=None)

# Have to do each file separately because every working OMFIT file lives in 
# its own directory:
move_from_other_work_dir(root['FILES']['hypnotoad_state'], idl_work_dir)
move_from_other_work_dir(root['FILES']['COGENT_Coefficients'], idl_work_dir)
remove_from_other_work_dir(root['FILES']['G-EQDSK'], idl_work_dir)

print ('DONE running runHypnoToad.py')
