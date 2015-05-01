#-*-Python-*-
# Created by creyn at 2015/05/01 13:46

import shutil

print ('running run_fix_x.py (file:"%s")' % __file__)

print ('(Unimplemented.  Only copies nodal_grid to fixed_nodal_grid so runCOGENT will work.')
nodal_grid_path = str(root['FILES']['nodal_grid'])
fixed_nodal_grid_path = str(root['FILES']['fixed_nodal_grid'])
shutil.copy(nodal_grid_path, fixed_nodal_grid_path) 

print ('DONE running run_fix_x.py')
