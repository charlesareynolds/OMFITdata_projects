"""This is the main OMFIT GUI
"""
def create_Setup_tab():
    OMFITx.Tab('Setup')
    OMFITx.CompoundGUI(
        pythonFile=root['GUIS']['HypnoToadGUI'],
        title='HypnoToad subGUI')

def create_Run_tab():
    
    def submit():
        print('Submitting job...')
        root['SCRIPTS']['runCOGENT'].run()
        print('Submitted job.')
        
    def submit_hello():
        print('Submitting hello...')
        root['SCRIPTS']['runHello'].run()
        print('Submitted hello.')
        
    def monitor():
        print('Monitoring job')
        OMFITx.Web("root['MACHINES']['edison']['job status']")
        
    def collect():
        print('Collecting results')
        
    OMFITx.Tab('Run')
    OMFITx.Label('Settings:')
    OMFITx.ComboBox(
        location="root['SETTINGS']['REMOTE_SETUP']['serverPicker']",
        values=root['MACHINES'].keys(),
        lbl='Run on server')

    OMFITx.Separator()
    OMFITx.Label('Command Section')
    OMFITx.Button('Submit Hello World', submit_hello, bg='lime green')
    OMFITx.Button('Submit Job', submit)
    OMFITx.Button('Monitor Job', monitor)
    OMFITx.Button('Collect Results', collect)

create_Run_tab()
create_Setup_tab()
# Title goes last to override any titles set by sub-GUIs:
OMFITx.TitleGUI('COGENT Main GUI')
