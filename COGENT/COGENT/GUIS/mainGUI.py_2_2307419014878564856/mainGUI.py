"""This is the main OMFIT GUI
"""
button_bg_normal='cornflower blue'
path_fg_found='blue'
path_fg_not_found='dark gray'

def path_exists(location):
    rel_path=eval(location)
    print ("rel_path: " + rel_path)
    return True

def add_path_entry(location, lbl, help, isDir=False):
    """default='', updateGUI=True, Sets text color to blue if path is present.
    """
 #   if path_exists(location):
 #       fg_color = path_fg_found
 #   else:
 #       fg_color = path_fg_not_found

    OMFITx.FilePicker(
        location=location,
        lbl=lbl,
        updateGUI=True,
        help=help,
        localRemote=True, 
        transferRemoteFile=False,
        directory=isDir,
        action='open',
        tree=False
#,
#        fg=fg_color
)

#    OMFITx.Entry(
#        location=location,
#        default='',
#        lbl=lbl,
#        updateGUI=True,
#        help=help,
#        fg=fg_color)

# GEQ file
def add_geq_file_entry(inout):
    add_path_entry(
        location="root['FILES']['GEQ']",
        lbl='GEQ file ' + inout,
        help='Output from EFIT, input to Hypnotoad')

# Coefficient files
def add_coeff_file_entry(inout):
    add_path_entry(
        location="root['FILES']['COGENT_Coefficients']",
        lbl='Coefficient file ' + inout,
        help='Output from Hypnotoad, input to grid post-processing')
def add_nodal_coeff_file_entry(inout):
    add_path_entry(
        location="root['FILES']['nodal_COGENT_Coefficients']",
        lbl='Nodal coefficient file ' + inout,
        help='Output from grid post-processing, input to Fix_X, input to COGENT')

# Grid/mesh files
def add_grid_file_entry(inout):
    add_path_entry(
        location="root['FILES']['grid']",
        lbl='Grid file ' + inout,
        help='Output from Hypnotoad, input to grid post-processing')
def add_nodal_grid_file_entry(inout):
    add_path_entry(
        location="root['FILES']['nodal_grid']",
        lbl='Nodal Grid file ' + inout,
        help='Output from grid post-processing, input to Fix_X')
def add_fixed_nodal_grid_file_entry(inout):
    add_path_entry(
        location="root['FILES']['fixed_nodal_grid']",
        lbl='Fixed Nodal Grid file ' + inout,
        help='Output from Fix_X, input to COGENT')

#Plot files
def add_plot_files_directory_entry(inout):
    add_path_entry(
        location="root['FILES']['plot_files_dir']",
        lbl='Plot files ' + inout + ' directory',
        help='Output from COGENT, input to VISIT')

# Server picker
def add_server_picker():
    OMFITx.ComboBox(
        "root['SETTINGS']['REMOTE_SETUP']['serverPicker']",
        root['MACHINES'].keys(),
        lbl='Job Server',
        updateGUI=True)
# Weird.  This:
#        [location=]"root['SETTINGS']['REMOTE_SETUP']['serverPicker']",
#        values=machines,
# gets:
#  TypeError: ComboBox() takes at least 2 arguments (2 given)

def monitor():
    print('Opening monitor web page...')
    # Run the job status viewer for the server machine:
    root['MACHINES'][root['SETTINGS']['REMOTE_SETUP']['serverPicker']]\
    ['job_status'].run()                   

#GUI sections
def create_EFIT_section():
    OMFITx.CompoundGUI(
        pythonFile=eval(root['SETTINGS']['DEPENDENCIES']['EFIT_GUI']),
        title='EFIT subGUI')

def create_Hypnotoad_section():
    def run_Hypnotoad():
        print ('Running Hypnotoad')
        root['SCRIPTS']['runHypnotoad'].run()
        print ('Done running Hypnotoad')

    OMFITx.Separator()
    add_geq_file_entry("in")
    add_coeff_file_entry("out")
    add_grid_file_entry("out")
    OMFITx.Button('Run Hypnotoad', run_Hypnotoad, bg=button_bg_normal)
    OMFITx.Separator()    

def create_Grid_post_processing_section():
    def run_grid_post_processing():
        print ('Running grid post-processing')
        root['SCRIPTS']['run_grid_post_processing'].run()
        print ('Done running grid post-processing')

    OMFITx.Separator()
    add_grid_file_entry("in")
    add_coeff_file_entry("in")
    add_nodal_grid_file_entry("out")
    add_nodal_coeff_file_entry("out")
    OMFITx.Button('Run grid post-processing', run_grid_post_processing, bg=button_bg_normal)
    OMFITx.Separator()    

def create_Fix_X_section():
    def run_Fix_X():
        print ('Pretending to run Fix_X')

    OMFITx.Separator()
    add_nodal_coeff_file_entry("in")
    add_nodal_grid_file_entry("in")
    add_fixed_nodal_grid_file_entry("out")
    OMFITx.Button('Run Fix_X', run_Fix_X, bg=button_bg_normal)
    OMFITx.Separator()
    
def create_COGENT_section():
    def submit():
        print('Submitting job...')
        root['SCRIPTS']['runCOGENT'].run()
        print('Submitted job.')
        
    OMFITx.Separator()
    add_nodal_coeff_file_entry("in")
    add_fixed_nodal_grid_file_entry("in")
    add_plot_files_directory_entry("out")
    add_server_picker()
    OMFITx.Button('Submit COGENT Job', submit, bg=button_bg_normal)
    OMFITx.Button('Monitor Job', monitor, bg=button_bg_normal)
    OMFITx.Separator()

def create_VISIT_section():
    def run_visit():
        print ('Pretending to run VISIT')

    OMFITx.Separator()
    add_plot_files_directory_entry("in")
    OMFITx.Button('Run VISIT', run_visit, bg=button_bg_normal)
    OMFITx.Separator()
    
def create_GUI_Test_section():

    def submit_hello():
        print('Submitting hello...')
        root['SCRIPTS']['runHello'].run()
        print('Submitted hello.')
        
    OMFITx.Separator()
    OMFITx.Label('GUI Test Section')
    add_server_picker()
    OMFITx.Button('Submit Hello World Job', submit_hello, bg=button_bg_normal)
    OMFITx.Button('Monitor Job', monitor, bg=button_bg_normal)
    OMFITx.Separator()

def create_Footer_section():
    def open_help():
        OMFITx.Open(root['help'])

    OMFITx.Separator()
    OMFITx.Button('Help', open_help, bg='lime green')
    OMFITx.Separator()

create_EFIT_section()
create_Hypnotoad_section()
create_Grid_post_processing_section()
create_Fix_X_section()
create_COGENT_section()
create_VISIT_section()
create_GUI_Test_section()
create_Footer_section()

# Title goes last to override any titles set by sub-GUIs:
OMFITx.TitleGUI('COGENT Main GUI')
