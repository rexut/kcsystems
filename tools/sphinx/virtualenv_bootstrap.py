import sys
import subprocess

VENV_VERSION = '12.0.4'
PYPI_VENV_BASE = 'https://pypi.python.org/packages/source/v/virtualenv'
PYTHON = 'python2.7'
INITIAL_ENV = '.py27venv'

if "check_output" not in dir( subprocess ): # duck punch it in!
    def f(*popenargs, **kwargs):
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be overridden.')
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise subprocess.CalledProcessError(retcode, cmd)
        return output
    subprocess.check_output = f

def shellcmd(cmd, echo=True):
    """ Run 'cmd' in the shell and return its standard out.
    """
    if echo: print '[cmd] {0}'.format(cmd)
    out = subprocess.check_output(cmd, stderr=sys.stderr, shell=True)
    if echo: print out
    return out

dirname = 'virtualenv-' + VENV_VERSION
tgz_file = dirname + '.tar.gz'

# Fetch virtualenv from PyPI
venv_url = PYPI_VENV_BASE + '/' + tgz_file
shellcmd('curl -L -J -O {0}'.format(venv_url))

# Untar
shellcmd('tar xzf {0}'.format(tgz_file))

# Create the initial env
shellcmd('{0} {1}/virtualenv.py {2}'.format(PYTHON, dirname, INITIAL_ENV))

# Install the virtualenv package itself into the initial env
shellcmd('{0}/bin/pip install {1}'.format(INITIAL_ENV, tgz_file))

# Cleanup
shellcmd('rm -rf {0} {1}'.format(dirname, tgz_file))
