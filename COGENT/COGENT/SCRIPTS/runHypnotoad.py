#-*-Python-*-
# Created by creyn at 2015/02/13 10:35

import os.path

print ('running runHypnoToad.py (file:"%s")' % __file__)

# Copied elswhere - need to import somehow:
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
# END Copied elswhere - need to import somehow.

copy_to_other_working(root['FILES']['G-EQDSK'], idl_work_dir)

idl_statement = 'hypnotoad'
arguments='-e ' + idl_statement,
# useful if all IDL licenses are taken.  Runs for 7 minutes:
# arguments='-demo ' + arguments,

# For now, the IDL source dir is also the working dir:
idl_source_dir = idl_work_dir

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

# Have to copy each file separately because every 
# working OMFIT file lives in its own directory:
move_from_other_working(root['FILES']['hypnotoad_state'], idl_work_dir)

print ('DONE running runHypnoToad.py')
