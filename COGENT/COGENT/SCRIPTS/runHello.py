#-*-Python-*-
# Created by creyn at 2015/02/19 12:47

OMFITx.execute(
    command_line='qsub',
    interactive_input=None,
    ignoreReturnCode=False,
    std_out=None,
    std_err=None,
    quiet=False,
    arguments=str(root['SCRIPTS']['HelloPBS']),
    script=None)
