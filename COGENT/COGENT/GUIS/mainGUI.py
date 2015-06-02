"""This is the main OMFIT GUI
"""
import os.path

# Only needed in PyCharm, to prevent semantic errors in editor:
import sys
if "OMFITx" not in sys.modules:
    import OMFITx
    root={}
# END Only needed in PyCharm


button_color = 'seagreen1'
help_button_color = 'cornflower blue'
in_out_colors = {'in' : 'turquoise', 'out' : 'light blue'}

def show_path(
    r_f_location,
    description,
    in_out,
    usage,
    isDir=False):
    """Show file name, description, and in/out direction
    location: OMFIT tree location, relative to root['FILES']
    description: 
    in_out: file usage
    usage: unused?
    isDir: unused
    """
    location = "root['FILES']" + r_f_location
    path=str(eval(location))
    basename = os.path.basename(path)
    OMFITx.Label(
        text=in_out.upper() + ": " + basename + " - " + description + ", at " +r_f_location,
#        text=in_out.upper() + ": " + basename + " - " + r_f_location,
#        text=in_out.upper() + ": " + basename + " - " + description,
        align='left'
        ,
        bg=in_out_colors[in_out]
    )

# GEQ file
def add_geq_file_entry(in_out):
    show_path(
        r_f_location="['G-EQDSK']",
        description='GEQ file', 
        in_out=in_out,
        usage='Output from EFIT, input to Hypnotoad')

# Coefficient files
def add_coeff_file_entry(in_out):
    show_path(
        r_f_location="['COGENT_Coefficients']",
        description='Coefficient file', 
        in_out=in_out,
        usage='Output from Hypnotoad, input to grid post-processing')
def add_nodal_coeff_file_entry(in_out):
    show_path(
        r_f_location="['nodal_COGENT_Coefficients']",
        description='Nodal coefficient file', 
        in_out=in_out,
        usage='Output from grid post-processing, input to Fix_X, input to COGENT')

# Grid/mesh files
def add_IDL_state_file_entry(in_out):
    show_path(
        r_f_location="['hypnotoad_state']",
        description='hypnotoad state file', 
        in_out=in_out,
        usage='Output from Hypnotoad, input to grid post-processing')
def add_nodal_grid_file_entry(in_out):
    show_path(
        r_f_location="['nodal_grid']",
        description='Nodal Grid file', 
        in_out=in_out,
        usage='Output from grid post-processing, input to Fix_X')
def add_fixed_nodal_grid_file_entry(in_out):
    show_path(
        r_f_location="['fixed_nodal_grid']",
        description='Fixed Nodal Grid file', 
        in_out=in_out,
        usage='Output from Fix_X, input to COGENT')

#Plot files
def add_plot_files_directory_entry(in_out):
    show_path(
        r_f_location="['plot_files_dir']",
        description='Plot files directory', 
        in_out=in_out,
        usage='Output from COGENT, input to VISIT')

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
def create_Help_section():
    def open_help():
        OMFITx.Open(root['help'])

    OMFITx.Separator()
    OMFITx.Button('Help', open_help, bg=help_button_color)
    OMFITx.Separator()

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
    OMFITx.Button('Run Hypnotoad', run_Hypnotoad, bg=button_color)
    add_coeff_file_entry("out")
    add_grid_file_entry("out")
    OMFITx.Separator()    

def create_Grid_post_processing_section():
    def run_grid_post_processing():
        print ('Running grid post-processing')
        root['SCRIPTS']['run_cogent_grid'].run()
        print ('Done running grid post-processing')

    OMFITx.Separator()
    add_coeff_file_entry("in")
    add_grid_file_entry("in")
    OMFITx.Button('Run grid post-processing', run_grid_post_processing, bg=button_color)
    add_nodal_coeff_file_entry("out")
    add_nodal_grid_file_entry("out")
    OMFITx.Separator()    

def create_Fix_X_section():
    def run_Fix_X():
        print ('Pretending to run Fix_X')

    OMFITx.Separator()
    add_nodal_coeff_file_entry("in")
    add_nodal_grid_file_entry("in")
    OMFITx.Button('Run Fix_X', run_Fix_X, bg=button_color)
    add_fixed_nodal_grid_file_entry("out")
    OMFITx.Separator()
    
def create_COGENT_section():
    def submit():
        print('Submitting job...')
        root['SCRIPTS']['runCOGENT'].run()
        print('Submitted job.')
        
    OMFITx.Separator()
    add_nodal_coeff_file_entry("in")
    add_fixed_nodal_grid_file_entry("in")
    add_server_picker()
    OMFITx.Button('Submit COGENT Job', submit, bg=button_color)
    OMFITx.Button('Monitor Job', monitor, bg=button_color)
    add_plot_files_directory_entry("out")
    OMFITx.Separator()

def create_VISIT_section():
    def run_visit():
        print ('Pretending to run VISIT')

    OMFITx.Separator()
    add_plot_files_directory_entry("in")
    OMFITx.Button('Run VISIT', run_visit, bg=button_color)
    OMFITx.Separator()

    
def create_GUI_Test_section():

    def submit_hello():
        print('Submitting hello...')
        root['SCRIPTS']['runHello'].run()
        print('Submitted hello.')
        
    OMFITx.Separator()
    OMFITx.Label('GUI Test Section')
    add_server_picker()
    OMFITx.Button('Submit Hello World Job', submit_hello, bg=button_color)
    OMFITx.Button('Monitor Job', monitor, bg=button_color)
    OMFITx.Separator()

create_Help_section()
create_EFIT_section()
create_Hypnotoad_section()
create_Grid_post_processing_section()
create_Fix_X_section()
create_COGENT_section()
create_VISIT_section()

create_GUI_Test_section()

# Title goes last to override any titles set by sub-GUIs:
OMFITx.TitleGUI('COGENT Main GUI')
