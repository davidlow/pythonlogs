# IPython log file

# Tue, 06 Jun 2017 21:39:24
get_ipython().magic('matplotlib tk')
# Tue, 06 Jun 2017 21:39:30
get_ipython().magic('run qtconsole/2017/06/setups/setup_20170606.py')
# Tue, 06 Jun 2017 21:39:55
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-05-29_daqapproach\2017-06-06\2017-06-06_025437_Planefit.json", instruments=instruments)
# Tue, 06 Jun 2017 21:40:14
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170606.py')
# Tue, 06 Jun 2017 21:40:43
# %load qtconsole/2017/06/setups/quickscan_20170606.py
plt.close('all')
#pz.z.sweep(pz.z.V, -pz.z.Vmax)
#atto.x.step(50)
#pz.zero()
pf.update_c()
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=60)
sc.notes = '''
[dhl88]  Quick scan for testing scanning in qtconsole
prep for spectra at points
'''
sc.run()

# Tue, 06 Jun 2017 21:44:20
get_ipython().magic('pylab')
# Tue, 06 Jun 2017 21:44:42
# %load qtconsole/2017/06/setups/quickscan_20170606.py
plt.close('all')
#pz.z.sweep(pz.z.V, -pz.z.Vmax)
#atto.x.step(50)
#pz.zero()
pf.update_c()
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=60)
sc.notes = '''
[dhl88]  Quick scan for testing scanning in qtconsole
prep for spectra at points
'''
sc.run()

# Tue, 06 Jun 2017 22:09:06
get_ipython().magic('pinfo Sweep')
# Tue, 06 Jun 2017 22:09:12
get_ipython().magic('pinfo Piezos.sweep')
# Tue, 06 Jun 2017 22:10:53
_ = pz.sweep(pz.V, {'x':-165, 'y':-184, 'z':0})
# Tue, 06 Jun 2017 22:10:56
pz.V
#[Out]# {'x': -165.06471485444249,
#[Out]#  'y': -184.02991781401403,
#[Out]#  'z': -0.021217553453355895}
# Tue, 06 Jun 2017 22:16:03
spectrum = DaqSpectrum(instruments, measure_time=0.5)
# Tue, 06 Jun 2017 22:16:09
spectrum.run()
# Tue, 06 Jun 2017 22:17:15
spectrum = DaqSpectrum(instruments, measure_time=1)
# Tue, 06 Jun 2017 22:17:26
spectrum.run()
# Tue, 06 Jun 2017 22:19:39
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:19:41
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:19:45
pa = SR5113(port="COM2")
# Tue, 06 Jun 2017 22:19:50
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:19:52
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:19:54
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:20:48
pa = SR5113(port="COM3")
# Tue, 06 Jun 2017 22:20:54
spectrum.run()
# Tue, 06 Jun 2017 22:22:36
spectrum.run()
# Tue, 06 Jun 2017 22:29:57
# %load qtconsole/2017/06/setups/quickscan_20170606.py
plt.close('all')
#pz.z.sweep(pz.z.V, -pz.z.Vmax)
#atto.x.step(50)
#pz.zero()
#pf.update_c()
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=60)
sc.notes = '''
[dhl88]  Quick scan for testing scanning in qtconsole
prep for spectra at points
'''
sc.run()

# Tue, 06 Jun 2017 22:44:30
_ = pz.sweep(pz.V, {'x':210, 'y':0, 'z':0})
# Tue, 06 Jun 2017 22:44:51
spectrum = DaqSpectrum(instruments, measure_time=1)
# Tue, 06 Jun 2017 22:44:57
spectrum.run()
# Tue, 06 Jun 2017 22:53:41
plane.c
# Tue, 06 Jun 2017 22:53:49
pf.c
#[Out]# 169.98856461174591
# Tue, 06 Jun 2017 22:54:27
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':50})
# Tue, 06 Jun 2017 22:54:32
spectrum = DaqSpectrum(instruments, measure_time=1)
# Tue, 06 Jun 2017 22:54:50
spectrum.run()
# Tue, 06 Jun 2017 22:56:59
spectrum = DaqSpectrum(instruments, measure_time=10)
# Tue, 06 Jun 2017 22:57:03
spectrum.run()
# Tue, 06 Jun 2017 23:08:07
spectrum = DaqSpectrum(instruments, measure_time=10)
# Tue, 06 Jun 2017 23:08:27
spectrum.notes = "[dhl88] 3 Khz cutoff freq, long"
# Tue, 06 Jun 2017 23:08:33
spectrum.run()
# Tue, 06 Jun 2017 23:43:39
spectrum = DaqSpectrum(instruments, measure_time=10)
# Tue, 06 Jun 2017 23:43:43
spectrum.notes = "[dhl88] 3 Khz cutoff freq, long"
# Tue, 06 Jun 2017 23:43:46
spectrum.run()
# Tue, 06 Jun 2017 23:51:55
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':70});
# Tue, 06 Jun 2017 23:53:08
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=70 V"
spectrum.run()

# Tue, 06 Jun 2017 23:58:59
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':90});
# Tue, 06 Jun 2017 23:59:10
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=90 V"
spectrum.run()

# Wed, 07 Jun 2017 00:08:31
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':110});
# Wed, 07 Jun 2017 00:08:42
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=110 V"
spectrum.run()

# Wed, 07 Jun 2017 00:34:35
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':130});
# Wed, 07 Jun 2017 00:35:00
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=130 V"
spectrum.run()

# Wed, 07 Jun 2017 00:40:38
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':170});
# Wed, 07 Jun 2017 00:40:48
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=170 V"
spectrum.run()

# Wed, 07 Jun 2017 00:57:44
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':180});
# Wed, 07 Jun 2017 00:58:04
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=180 V definitely in contact"
spectrum.run()

# Wed, 07 Jun 2017 01:07:07
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':50});
# Wed, 07 Jun 2017 01:07:23
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=50 V definitely out of contact"
spectrum.run()

# Wed, 07 Jun 2017 02:02:55
_ = pz.sweep(pz.V, {'x':234, 'y':0, 'z':170});
# Wed, 07 Jun 2017 02:05:00
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] z=170 V definitely out of contact"
spectrum.run()

# Wed, 07 Jun 2017 02:44:11
spectrum.ax['loglog'].annotate('x={0},y={1}'.format(234,170), xy=(0.02, .9), xycoords='axes fraction', fontsize=10, ha='left', va='top', family='monospace')
#[Out]# <matplotlib.text.Annotation at 0x1ac92d68>
# Wed, 07 Jun 2017 02:45:02
spectrum.ax['loglog'].annotate(spectrum.notes, xy=(0.02, .9), xycoords='axes fraction', fontsize=10, ha='left', va='top', family='monospace')
#[Out]# <matplotlib.text.Annotation at 0x1cccfe48>
# Wed, 07 Jun 2017 02:46:14
_ = pz.sweep(pz.V, {'x':230, 'y':0, 'z':170});
# Wed, 07 Jun 2017 02:48:33
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] In contact, moving\nx=230, z=170"
spectrum.run()
spectrum.ax['loglog'].annotate(spectrum.notes,
                                xy=(0.02, .9),
                                xycoords='axes fraction',
                                fontsize=8, ha='left', va='top',
                                family='monospace'
)

#[Out]# <matplotlib.text.Annotation at 0x121c39b0>
# Wed, 07 Jun 2017 03:03:52
from importlib import reload
# Wed, 07 Jun 2017 03:03:57
reload(DaqSpectrum)
# Wed, 07 Jun 2017 03:04:46
reload(Nowack_Lab.Procedures.DaqSpectrum)
# Wed, 07 Jun 2017 03:08:10
import sys
# Wed, 07 Jun 2017 03:08:19
sys.modules
#[Out]# {'scipy.sparse.linalg.dsolve._superlu': <module 'scipy.sparse.linalg.dsolve._superlu' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\dsolve\\_superlu.cp35-win_amd64.pyd'>,
#[Out]#  'zmq.backend.cython._version': <module 'zmq.backend.cython._version' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_version.cp35-win_amd64.pyd'>,
#[Out]#  'Nowack_Lab.Procedures.heightsweep': <module 'Nowack_Lab.Procedures.heightsweep' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\heightsweep.py'>,
#[Out]#  'win32com': <module 'win32com' from 'C:\\Anaconda3\\lib\\site-packages\\win32com\\__init__.py'>,
#[Out]#  'numpy.lib.stride_tricks': <module 'numpy.lib.stride_tricks' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\stride_tricks.py'>,
#[Out]#  '_imp': <module '_imp' (built-in)>,
#[Out]#  'pkgutil': <module 'pkgutil' from 'C:\\Anaconda3\\lib\\pkgutil.py'>,
#[Out]#  'h5py.tests': <module 'h5py.tests' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\__init__.py'>,
#[Out]#  'email._encoded_words': <module 'email._encoded_words' from 'C:\\Anaconda3\\lib\\email\\_encoded_words.py'>,
#[Out]#  'numpy._globals': <module 'numpy._globals' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\_globals.py'>,
#[Out]#  'ctypes.wintypes': <module 'ctypes.wintypes' from 'C:\\Anaconda3\\lib\\ctypes\\wintypes.py'>,
#[Out]#  'scipy._lib._numpy_compat': <module 'scipy._lib._numpy_compat' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\_numpy_compat.py'>,
#[Out]#  'scipy.ndimage.io': <module 'scipy.ndimage.io' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\io.py'>,
#[Out]#  'Nowack_Lab.Procedures.touchdown': <module 'Nowack_Lab.Procedures.touchdown' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\touchdown.py'>,
#[Out]#  'numpy.lib.ufunclike': <module 'numpy.lib.ufunclike' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\ufunclike.py'>,
#[Out]#  'scipy.stats.contingency': <module 'scipy.stats.contingency' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\contingency.py'>,
#[Out]#  'h5py.utils': <module 'h5py.utils' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\utils.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.compat': <module 'matplotlib.compat' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\compat\\__init__.py'>,
#[Out]#  'cffi.model': <module 'cffi.model' from 'C:\\Anaconda3\\lib\\site-packages\\cffi\\model.py'>,
#[Out]#  'json.encoder': <module 'json.encoder' from 'C:\\Anaconda3\\lib\\json\\encoder.py'>,
#[Out]#  'zmq.sugar.attrsettr': <module 'zmq.sugar.attrsettr' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\attrsettr.py'>,
#[Out]#  'h5py.h5f': <module 'h5py.h5f' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5f.cp35-win_amd64.pyd'>,
#[Out]#  'instrumental.appdirs': <module 'instrumental.appdirs' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\appdirs.py'>,
#[Out]#  'h5py.tests.hl': <module 'h5py.tests.hl' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\hl\\__init__.py'>,
#[Out]#  'matplotlib.scale': <module 'matplotlib.scale' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\scale.py'>,
#[Out]#  'h5py.version': <module 'h5py.version' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\version.py'>,
#[Out]#  'scipy.sparse.linalg._norm': <module 'scipy.sparse.linalg._norm' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\_norm.py'>,
#[Out]#  'jupyter_client.manager': <module 'jupyter_client.manager' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\manager.py'>,
#[Out]#  'weakref': <module 'weakref' from 'C:\\Anaconda3\\lib\\weakref.py'>,
#[Out]#  'Nowack_Lab.Procedures.scanplane': <module 'Nowack_Lab.Procedures.scanplane' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\scanplane.py'>,
#[Out]#  'numpy.compat._inspect': <module 'numpy.compat._inspect' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\compat\\_inspect.py'>,
#[Out]#  'scipy.integrate.vode': <module 'scipy.integrate.vode' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\vode.cp35-win_amd64.pyd'>,
#[Out]#  'msvcrt': <module 'msvcrt' (built-in)>,
#[Out]#  'ipywidgets.widgets.widget_bool': <module 'ipywidgets.widgets.widget_bool' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_bool.py'>,
#[Out]#  'calendar': <module 'calendar' from 'C:\\Anaconda3\\lib\\calendar.py'>,
#[Out]#  'numpy.testing': <module 'numpy.testing' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\testing\\__init__.py'>,
#[Out]#  'IPython.core.inputsplitter': <module 'IPython.core.inputsplitter' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\inputsplitter.py'>,
#[Out]#  'IPython.utils.contexts': <module 'IPython.utils.contexts' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\contexts.py'>,
#[Out]#  'ipykernel.kernelapp': <module 'ipykernel.kernelapp' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\kernelapp.py'>,
#[Out]#  'distutils.version': <module 'distutils.version' from 'C:\\Anaconda3\\lib\\distutils\\version.py'>,
#[Out]#  'ipython_genutils._version': <module 'ipython_genutils._version' from 'C:\\Anaconda3\\lib\\site-packages\\ipython_genutils\\_version.py'>,
#[Out]#  'Nowack_Lab.Procedures.daqspectrum': <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>,
#[Out]#  'numpy.matlib': <module 'numpy.matlib' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\matlib.py'>,
#[Out]#  'IPython.core.magics.config': <module 'IPython.core.magics.config' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\config.py'>,
#[Out]#  'matplotlib.textpath': <module 'matplotlib.textpath' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\textpath.py'>,
#[Out]#  'IPython.core.macro': <module 'IPython.core.macro' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\macro.py'>,
#[Out]#  'configparser': <module 'configparser' from 'C:\\Anaconda3\\lib\\configparser.py'>,
#[Out]#  'traitlets._version': <module 'traitlets._version' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\_version.py'>,
#[Out]#  '_multiprocessing': <module '_multiprocessing' from 'C:\\Anaconda3\\DLLs\\_multiprocessing.pyd'>,
#[Out]#  'visa': <module 'visa' from 'C:\\Anaconda3\\lib\\site-packages\\visa.py'>,
#[Out]#  'matplotlib.tight_layout': <module 'matplotlib.tight_layout' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tight_layout.py'>,
#[Out]#  'scipy.signal._max_len_seq_inner': <module 'scipy.signal._max_len_seq_inner' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_max_len_seq_inner.cp35-win_amd64.pyd'>,
#[Out]#  'jupyter_client.session': <module 'jupyter_client.session' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\session.py'>,
#[Out]#  'pkg_resources.extern.six': <module 'pkg_resources._vendor.six' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\six.py'>,
#[Out]#  'pywintypes': <module 'pywintypes' (C:\Anaconda3\Library\bin\pywintypes35.dll)>,
#[Out]#  '_lzma': <module '_lzma' from 'C:\\Anaconda3\\DLLs\\_lzma.pyd'>,
#[Out]#  'mpl_toolkits': <module 'mpl_toolkits' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\__init__.py'>,
#[Out]#  'IPython.core.display_trap': <module 'IPython.core.display_trap' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\display_trap.py'>,
#[Out]#  'scipy.integrate.lsoda': <module 'scipy.integrate.lsoda' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\lsoda.cp35-win_amd64.pyd'>,
#[Out]#  'linecache': <module 'linecache' from 'C:\\Anaconda3\\lib\\linecache.py'>,
#[Out]#  'logging': <module 'logging' from 'C:\\Anaconda3\\lib\\logging\\__init__.py'>,
#[Out]#  'matplotlib._contour': <module 'matplotlib._contour' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_contour.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.polynomial.polynomial': <module 'numpy.polynomial.polynomial' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\polynomial.py'>,
#[Out]#  'cProfile': <module 'cProfile' from 'C:\\Anaconda3\\lib\\cProfile.py'>,
#[Out]#  'h5py.h5ds': <module 'h5py.h5ds' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5ds.cp35-win_amd64.pyd'>,
#[Out]#  'zmq.utils.sixcerpt': <module 'zmq.utils.sixcerpt' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\sixcerpt.py'>,
#[Out]#  'jsonpickle.tags': <module 'jsonpickle.tags' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\tags.py'>,
#[Out]#  'numpy.fft.fftpack_lite': <module 'numpy.fft.fftpack_lite' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\fft\\fftpack_lite.cp35-win_amd64.pyd'>,
#[Out]#  'os': <module 'os' from 'C:\\Anaconda3\\lib\\os.py'>,
#[Out]#  'difflib': <module 'difflib' from 'C:\\Anaconda3\\lib\\difflib.py'>,
#[Out]#  'matplotlib.mathtext': <module 'matplotlib.mathtext' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\mathtext.py'>,
#[Out]#  'ipykernel.displayhook': <module 'ipykernel.displayhook' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\displayhook.py'>,
#[Out]#  're': <module 're' from 'C:\\Anaconda3\\lib\\re.py'>,
#[Out]#  'jupyter_client.blocking.client': <module 'jupyter_client.blocking.client' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\blocking\\client.py'>,
#[Out]#  'scipy.ndimage.interpolation': <module 'scipy.ndimage.interpolation' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\interpolation.py'>,
#[Out]#  'random': <module 'random' from 'C:\\Anaconda3\\lib\\random.py'>,
#[Out]#  'encodings.aliases': <module 'encodings.aliases' from 'C:\\Anaconda3\\lib\\encodings\\aliases.py'>,
#[Out]#  '_decimal': <module '_decimal' from 'C:\\Anaconda3\\DLLs\\_decimal.pyd'>,
#[Out]#  'zlib': <module 'zlib' (built-in)>,
#[Out]#  'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>,
#[Out]#  'ipywidgets.widgets.widget_selection': <module 'ipywidgets.widgets.widget_selection' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_selection.py'>,
#[Out]#  'jupyter_client': <module 'jupyter_client' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\__init__.py'>,
#[Out]#  'sqlite3': <module 'sqlite3' from 'C:\\Anaconda3\\lib\\sqlite3\\__init__.py'>,
#[Out]#  'scipy.optimize._lsq.givens_elimination': <module 'scipy.optimize._lsq.givens_elimination' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\givens_elimination.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.utils.coloransi': <module 'IPython.utils.coloransi' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\coloransi.py'>,
#[Out]#  'email': <module 'email' from 'C:\\Anaconda3\\lib\\email\\__init__.py'>,
#[Out]#  'scipy.interpolate.interpolate': <module 'scipy.interpolate.interpolate' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\interpolate.py'>,
#[Out]#  'IPython.utils.process': <module 'IPython.utils.process' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\process.py'>,
#[Out]#  'matplotlib.artist': <module 'matplotlib.artist' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\artist.py'>,
#[Out]#  'unittest.main': <module 'unittest.main' from 'C:\\Anaconda3\\lib\\unittest\\main.py'>,
#[Out]#  'jsonpickle.backend': <module 'jsonpickle.backend' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\backend.py'>,
#[Out]#  'scipy._lib._version': <module 'scipy._lib._version' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\_version.py'>,
#[Out]#  'IPython.utils.terminal': <module 'IPython.utils.terminal' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\terminal.py'>,
#[Out]#  'pickle': <module 'pickle' from 'C:\\Anaconda3\\lib\\pickle.py'>,
#[Out]#  'concurrent.futures.thread': <module 'concurrent.futures.thread' from 'C:\\Anaconda3\\lib\\concurrent\\futures\\thread.py'>,
#[Out]#  'scipy.interpolate.fitpack2': <module 'scipy.interpolate.fitpack2' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\fitpack2.py'>,
#[Out]#  'importlib.abc': <module 'importlib.abc' from 'C:\\Anaconda3\\lib\\importlib\\abc.py'>,
#[Out]#  'tornado.platform.common': <module 'tornado.platform.common' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\platform\\common.py'>,
#[Out]#  'scipy.optimize._trustregion': <module 'scipy.optimize._trustregion' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_trustregion.py'>,
#[Out]#  'pkg_resources.extern.packaging': <module 'pkg_resources._vendor.packaging' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\packaging\\__init__.py'>,
#[Out]#  'scipy.signal._max_len_seq': <module 'scipy.signal._max_len_seq' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_max_len_seq.py'>,
#[Out]#  'zmq.eventloop.zmqstream': <module 'zmq.eventloop.zmqstream' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\eventloop\\zmqstream.py'>,
#[Out]#  'concurrent.futures': <module 'concurrent.futures' from 'C:\\Anaconda3\\lib\\concurrent\\futures\\__init__.py'>,
#[Out]#  'tornado.platform': <module 'tornado.platform' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\platform\\__init__.py'>,
#[Out]#  '__main__': <module '__main__'>,
#[Out]#  'IPython.core.splitinput': <module 'IPython.core.splitinput' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\splitinput.py'>,
#[Out]#  'pint.compat': <module 'pint.compat' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\compat\\__init__.py'>,
#[Out]#  'jupyter_client.jsonutil': <module 'jupyter_client.jsonutil' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\jsonutil.py'>,
#[Out]#  'matplotlib.projections.polar': <module 'matplotlib.projections.polar' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\projections\\polar.py'>,
#[Out]#  'numpy.core.info': <module 'numpy.core.info' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\info.py'>,
#[Out]#  'IPython.utils.warn': <module 'IPython.utils.warn' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\warn.py'>,
#[Out]#  'h5py.h5g': <module 'h5py.h5g' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5g.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.core.inputtransformer': <module 'IPython.core.inputtransformer' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\inputtransformer.py'>,
#[Out]#  'zmq.backend.cython.constants': <module 'zmq.backend.cython.constants' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\constants.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.misc.pilutil': <module 'scipy.misc.pilutil' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\misc\\pilutil.py'>,
#[Out]#  'jupyter_client.channelsabc': <module 'jupyter_client.channelsabc' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\channelsabc.py'>,
#[Out]#  'IPython.utils.path': <module 'IPython.utils.path' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\path.py'>,
#[Out]#  'matplotlib.backends': <module 'matplotlib.backends' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backends\\__init__.py'>,
#[Out]#  'scipy.signal._upfirdn_apply': <module 'scipy.signal._upfirdn_apply' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_upfirdn_apply.cp35-win_amd64.pyd'>,
#[Out]#  'jsonpickle.version': <module 'jsonpickle.version' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\version.py'>,
#[Out]#  'jsonpickle.ext.numpy': <module 'jsonpickle.ext.numpy' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\ext\\numpy.py'>,
#[Out]#  'h5py.tests.old.test_objects': <module 'h5py.tests.old.test_objects' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_objects.py'>,
#[Out]#  'matplotlib.image': <module 'matplotlib.image' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\image.py'>,
#[Out]#  '_warnings': <module '_warnings' (built-in)>,
#[Out]#  'fnmatch': <module 'fnmatch' from 'C:\\Anaconda3\\lib\\fnmatch.py'>,
#[Out]#  'scipy.sparse.linalg.isolve._iterative': <module 'scipy.sparse.linalg.isolve._iterative' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\_iterative.cp35-win_amd64.pyd'>,
#[Out]#  'Nowack_Lab.Utilities.utilities': <module 'Nowack_Lab.Utilities.utilities' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\utilities.py'>,
#[Out]#  'email.iterators': <module 'email.iterators' from 'C:\\Anaconda3\\lib\\email\\iterators.py'>,
#[Out]#  'zmq.backend.cython.message': <module 'zmq.backend.cython.message' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\message.cp35-win_amd64.pyd'>,
#[Out]#  'peakutils.prepare': <module 'peakutils.prepare' from 'C:\\Anaconda3\\lib\\site-packages\\peakutils\\prepare.py'>,
#[Out]#  'pyreadline.logger': <module 'pyreadline.logger' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\logger.py'>,
#[Out]#  'CryostationComm': <module 'CryostationComm'>,
#[Out]#  'scipy.special._comb': <module 'scipy.special._comb' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_comb.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.core.magic_arguments': <module 'IPython.core.magic_arguments' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magic_arguments.py'>,
#[Out]#  'pyreadline.clipboard.win32_clipboard': <module 'pyreadline.clipboard.win32_clipboard' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\clipboard\\win32_clipboard.py'>,
#[Out]#  'jsonpickle': <module 'jsonpickle' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\__init__.py'>,
#[Out]#  'scipy.optimize._lsq.trf': <module 'scipy.optimize._lsq.trf' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\trf.py'>,
#[Out]#  'pyexpat.errors': <module 'pyexpat.errors'>,
#[Out]#  'pyvisa.ctwrapper.functions': <module 'pyvisa.ctwrapper.functions' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\ctwrapper\\functions.py'>,
#[Out]#  '_bisect': <module '_bisect' (built-in)>,
#[Out]#  'IPython.utils.generics': <module 'IPython.utils.generics' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\generics.py'>,
#[Out]#  'scipy.signal.lti_conversion': <module 'scipy.signal.lti_conversion' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\lti_conversion.py'>,
#[Out]#  'scipy.optimize._differentialevolution': <module 'scipy.optimize._differentialevolution' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_differentialevolution.py'>,
#[Out]#  'pint.compat.chainmap': <module 'pint.compat.chainmap' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\compat\\chainmap.py'>,
#[Out]#  'h5py._hl.filters': <module 'h5py._hl.filters' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\filters.py'>,
#[Out]#  'tkinter.commondialog': <module 'tkinter.commondialog' from 'C:\\Anaconda3\\lib\\tkinter\\commondialog.py'>,
#[Out]#  'matplotlib.backends.tkagg': <module 'matplotlib.backends.tkagg' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backends\\tkagg.py'>,
#[Out]#  'scipy.special._ufuncs_cxx': <module 'scipy.special._ufuncs_cxx' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_ufuncs_cxx.cp35-win_amd64.pyd'>,
#[Out]#  'scipy._lib._util': <module 'scipy._lib._util' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\_util.py'>,
#[Out]#  'winreg': <module 'winreg' (built-in)>,
#[Out]#  '_random': <module '_random' (built-in)>,
#[Out]#  'traitlets': <module 'traitlets' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\__init__.py'>,
#[Out]#  'scipy.signal.signaltools': <module 'scipy.signal.signaltools' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\signaltools.py'>,
#[Out]#  'matplotlib._cm': <module 'matplotlib._cm' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_cm.py'>,
#[Out]#  'tornado.util': <module 'tornado.util' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\util.py'>,
#[Out]#  'matplotlib.tri.triangulation': <module 'matplotlib.tri.triangulation' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\triangulation.py'>,
#[Out]#  'IPython.lib.security': <module 'IPython.lib.security' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\security.py'>,
#[Out]#  'scipy.signal.sigtools': <module 'scipy.signal.sigtools' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\sigtools.cp35-win_amd64.pyd'>,
#[Out]#  'h5py.h5p': <module 'h5py.h5p' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5p.cp35-win_amd64.pyd'>,
#[Out]#  'pint.measurement': <module 'pint.measurement' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\measurement.py'>,
#[Out]#  'scipy.optimize._zeros': <module 'scipy.optimize._zeros' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_zeros.cp35-win_amd64.pyd'>,
#[Out]#  'pyreadline.modes': <module 'pyreadline.modes' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\modes\\__init__.py'>,
#[Out]#  'Nowack_Lab.Utilities.conversions': <module 'Nowack_Lab.Utilities.conversions' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\conversions.py'>,
#[Out]#  'array': <module 'array' (built-in)>,
#[Out]#  'numpy.core.numerictypes': <module 'numpy.core.numerictypes' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\numerictypes.py'>,
#[Out]#  'numpy.lib.npyio': <module 'numpy.lib.npyio' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\npyio.py'>,
#[Out]#  'scipy.special._ufuncs': <module 'scipy.special._ufuncs' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_ufuncs.cp35-win_amd64.pyd'>,
#[Out]#  'h5py._conv': <module 'h5py._conv' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_conv.cp35-win_amd64.pyd'>,
#[Out]#  'sre_constants': <module 'sre_constants' from 'C:\\Anaconda3\\lib\\sre_constants.py'>,
#[Out]#  'h5py.h5': <module 'h5py.h5' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.core.prompts': <module 'IPython.core.prompts' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\prompts.py'>,
#[Out]#  'matplotlib.offsetbox': <module 'matplotlib.offsetbox' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\offsetbox.py'>,
#[Out]#  'scipy.sparse.csgraph._validation': <module 'scipy.sparse.csgraph._validation' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_validation.py'>,
#[Out]#  'scipy.signal.wavelets': <module 'scipy.signal.wavelets' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\wavelets.py'>,
#[Out]#  'IPython.core.magics.execution': <module 'IPython.core.magics.execution' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\execution.py'>,
#[Out]#  'pkg_resources.extern.packaging.requirements': <module 'pkg_resources.extern.packaging.requirements' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\packaging\\requirements.py'>,
#[Out]#  'scipy.optimize._lsq.least_squares': <module 'scipy.optimize._lsq.least_squares' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\least_squares.py'>,
#[Out]#  'pyreadline.release': <module 'pyreadline.release' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\release.py'>,
#[Out]#  'scipy.signal.bsplines': <module 'scipy.signal.bsplines' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\bsplines.py'>,
#[Out]#  'h5py.h5ac': <module 'h5py.h5ac' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5ac.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.optimize._lsq': <module 'scipy.optimize._lsq' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\__init__.py'>,
#[Out]#  'traitlets.traitlets': <module 'traitlets.traitlets' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\traitlets.py'>,
#[Out]#  'IPython.core.debugger': <module 'IPython.core.debugger' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\debugger.py'>,
#[Out]#  '_stat': <module '_stat' (built-in)>,
#[Out]#  '_ast': <module '_ast' (built-in)>,
#[Out]#  'scipy.signal.spectral': <module 'scipy.signal.spectral' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\spectral.py'>,
#[Out]#  'IPython.terminal.embed': <module 'IPython.terminal.embed' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\terminal\\embed.py'>,
#[Out]#  'instrumental': <module 'instrumental' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\__init__.py'>,
#[Out]#  'uu': <module 'uu' from 'C:\\Anaconda3\\lib\\uu.py'>,
#[Out]#  'mpl_toolkits.axes_grid1.colorbar': <module 'mpl_toolkits.axes_grid1.colorbar' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\colorbar.py'>,
#[Out]#  'IPython.core.magics.logging': <module 'IPython.core.magics.logging' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\logging.py'>,
#[Out]#  'scipy.linalg.cython_lapack': <module 'scipy.linalg.cython_lapack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\cython_lapack.cp35-win_amd64.pyd'>,
#[Out]#  'http.client': <module 'http.client' from 'C:\\Anaconda3\\lib\\http\\client.py'>,
#[Out]#  'itertools': <module 'itertools' (built-in)>,
#[Out]#  'win32security': <module 'win32security' from 'C:\\Anaconda3\\lib\\site-packages\\win32\\win32security.pyd'>,
#[Out]#  'matplotlib.bezier': <module 'matplotlib.bezier' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\bezier.py'>,
#[Out]#  'selectors': <module 'selectors' from 'C:\\Anaconda3\\lib\\selectors.py'>,
#[Out]#  'instrumental.__about__': <module 'instrumental.__about__' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\__about__.py'>,
#[Out]#  'numpy': <module 'numpy' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\__init__.py'>,
#[Out]#  'IPython.utils.rlineimpl': <module 'IPython.utils.rlineimpl' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\rlineimpl.py'>,
#[Out]#  'scipy.sparse.linalg._onenormest': <module 'scipy.sparse.linalg._onenormest' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\_onenormest.py'>,
#[Out]#  'matplotlib.tri.triplot': <module 'matplotlib.tri.triplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\triplot.py'>,
#[Out]#  'h5py._hl.selections': <module 'h5py._hl.selections' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\selections.py'>,
#[Out]#  'zipfile': <module 'zipfile' from 'C:\\Anaconda3\\lib\\zipfile.py'>,
#[Out]#  'ipykernel.pylab.config': <module 'ipykernel.pylab.config' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\pylab\\config.py'>,
#[Out]#  'PIL.ImageMode': <module 'PIL.ImageMode' from 'C:\\Anaconda3\\lib\\site-packages\\PIL\\ImageMode.py'>,
#[Out]#  'IPython.lib.inputhook': <module 'IPython.lib.inputhook' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\inputhook.py'>,
#[Out]#  'matplotlib.legend_handler': <module 'matplotlib.legend_handler' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\legend_handler.py'>,
#[Out]#  'scipy.linalg._decomp_qz': <module 'scipy.linalg._decomp_qz' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_decomp_qz.py'>,
#[Out]#  'numpy.core._methods': <module 'numpy.core._methods' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\_methods.py'>,
#[Out]#  'pint.converters': <module 'pint.converters' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\converters.py'>,
#[Out]#  'Instrumental.instrumental': <module 'Instrumental.instrumental' from 'C:\\Users\\B82A\\Documents\\GitHub\\Instrumental\\instrumental\\__init__.py'>,
#[Out]#  'IPython.utils._tokenize_py3': <module 'IPython.utils._tokenize_py3' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\_tokenize_py3.py'>,
#[Out]#  'PyDAQmx.DAQmxFunctions': <module 'PyDAQmx.DAQmxFunctions' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\DAQmxFunctions.py'>,
#[Out]#  'pyvisa.constants': <module 'pyvisa.constants' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\constants.py'>,
#[Out]#  'multiprocessing.util': <module 'multiprocessing.util' from 'C:\\Anaconda3\\lib\\multiprocessing\\util.py'>,
#[Out]#  'path': <module 'path' from 'C:\\Anaconda3\\lib\\site-packages\\path.py'>,
#[Out]#  'instrumental.conf': <module 'instrumental.conf' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\conf.py'>,
#[Out]#  'scipy.optimize._trustregion_ncg': <module 'scipy.optimize._trustregion_ncg' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_trustregion_ncg.py'>,
#[Out]#  'sysconfig': <module 'sysconfig' from 'C:\\Anaconda3\\lib\\sysconfig.py'>,
#[Out]#  'Nowack_Lab.Procedures.scanline': <module 'Nowack_Lab.Procedures.scanline' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\scanline.py'>,
#[Out]#  'scipy.special': <module 'scipy.special' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\__init__.py'>,
#[Out]#  'scipy.signal._upfirdn': <module 'scipy.signal._upfirdn' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_upfirdn.py'>,
#[Out]#  'Instrumental.instrumental.__about__': <module 'Instrumental.instrumental.__about__' from 'C:\\Users\\B82A\\Documents\\GitHub\\Instrumental\\instrumental\\__about__.py'>,
#[Out]#  'IPython.core.excolors': <module 'IPython.core.excolors' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\excolors.py'>,
#[Out]#  'scipy.sparse.linalg.isolve.utils': <module 'scipy.sparse.linalg.isolve.utils' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\utils.py'>,
#[Out]#  'scipy.sparse.linalg.eigen.lobpcg': <module 'scipy.sparse.linalg.eigen.lobpcg' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\eigen\\lobpcg\\__init__.py'>,
#[Out]#  'operator': <module 'operator' from 'C:\\Anaconda3\\lib\\operator.py'>,
#[Out]#  'traitlets.config.application': <module 'traitlets.config.application' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\config\\application.py'>,
#[Out]#  'IPython.core.magics.history': <module 'IPython.core.magics.history' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\history.py'>,
#[Out]#  'numpy.linalg._umath_linalg': <module 'numpy.linalg._umath_linalg' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\linalg\\_umath_linalg.cp35-win_amd64.pyd'>,
#[Out]#  'encodings.latin_1': <module 'encodings.latin_1' from 'C:\\Anaconda3\\lib\\encodings\\latin_1.py'>,
#[Out]#  'zmq.sugar.frame': <module 'zmq.sugar.frame' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\frame.py'>,
#[Out]#  'ipywidgets.widgets.eventful': <module 'ipywidgets.widgets.eventful' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\eventful.py'>,
#[Out]#  'IPython.utils.py3compat': <module 'IPython.utils.py3compat' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\py3compat.py'>,
#[Out]#  '_ctypes': <module '_ctypes' from 'C:\\Anaconda3\\DLLs\\_ctypes.pyd'>,
#[Out]#  'scipy.sparse.linalg.isolve.lgmres': <module 'scipy.sparse.linalg.isolve.lgmres' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\lgmres.py'>,
#[Out]#  'h5py._hl.files': <module 'h5py._hl.files' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\files.py'>,
#[Out]#  'ipykernel.serialize': <module 'ipykernel.serialize' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\serialize.py'>,
#[Out]#  'scipy.stats.mstats': <module 'scipy.stats.mstats' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\mstats.py'>,
#[Out]#  'scipy.sparse.linalg.eigen.arpack': <module 'scipy.sparse.linalg.eigen.arpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\eigen\\arpack\\__init__.py'>,
#[Out]#  'matplotlib._qhull': <module 'matplotlib._qhull' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_qhull.cp35-win_amd64.pyd'>,
#[Out]#  'Nowack_Lab': <module 'Nowack_Lab' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\__init__.py'>,
#[Out]#  'scipy.stats': <module 'scipy.stats' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\__init__.py'>,
#[Out]#  'jupyter_client.blocking.channels': <module 'jupyter_client.blocking.channels' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\blocking\\channels.py'>,
#[Out]#  'IPython.core.alias': <module 'IPython.core.alias' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\alias.py'>,
#[Out]#  'scipy.sparse.lil': <module 'scipy.sparse.lil' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\lil.py'>,
#[Out]#  'pint.systems': <module 'pint.systems' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\systems.py'>,
#[Out]#  'scipy.sparse': <module 'scipy.sparse' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\__init__.py'>,
#[Out]#  'Nowack_Lab.Instruments.squidarray': <module 'Nowack_Lab.Instruments.squidarray' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\squidarray.py'>,
#[Out]#  'scipy.optimize.nonlin': <module 'scipy.optimize.nonlin' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\nonlin.py'>,
#[Out]#  'scipy.stats.stats': <module 'scipy.stats.stats' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\stats.py'>,
#[Out]#  'tornado.log': <module 'tornado.log' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\log.py'>,
#[Out]#  'numpy.polynomial.hermite': <module 'numpy.polynomial.hermite' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\hermite.py'>,
#[Out]#  'dateutil.rrule': <module 'dateutil.rrule' from 'C:\\Anaconda3\\lib\\site-packages\\dateutil\\rrule.py'>,
#[Out]#  'pkg_resources': <module 'pkg_resources' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\__init__.py'>,
#[Out]#  '_hashlib': <module '_hashlib' from 'C:\\Anaconda3\\DLLs\\_hashlib.pyd'>,
#[Out]#  'matplotlib._mathtext_data': <module 'matplotlib._mathtext_data' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_mathtext_data.py'>,
#[Out]#  'matplotlib.tri.trifinder': <module 'matplotlib.tri.trifinder' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\trifinder.py'>,
#[Out]#  'IPython.utils.wildcard': <module 'IPython.utils.wildcard' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\wildcard.py'>,
#[Out]#  'signal': <module 'signal' from 'C:\\Anaconda3\\lib\\signal.py'>,
#[Out]#  'numpy.add_newdocs': <module 'numpy.add_newdocs' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\add_newdocs.py'>,
#[Out]#  'scipy.optimize.minpack2': <module 'scipy.optimize.minpack2' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\minpack2.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.fft.fftpack': <module 'numpy.fft.fftpack' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\fft\\fftpack.py'>,
#[Out]#  '_csv': <module '_csv' (built-in)>,
#[Out]#  'datetime': <module 'datetime' from 'C:\\Anaconda3\\lib\\datetime.py'>,
#[Out]#  'numpy.testing.decorators': <module 'numpy.testing.decorators' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\testing\\decorators.py'>,
#[Out]#  '_bz2': <module '_bz2' from 'C:\\Anaconda3\\DLLs\\_bz2.pyd'>,
#[Out]#  'scipy.sparse.csc': <module 'scipy.sparse.csc' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csc.py'>,
#[Out]#  'mpl_toolkits.axes_grid1.axes_divider': <module 'mpl_toolkits.axes_grid1.axes_divider' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\axes_divider.py'>,
#[Out]#  'scipy.ndimage.morphology': <module 'scipy.ndimage.morphology' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\morphology.py'>,
#[Out]#  'scipy.linalg._expm_frechet': <module 'scipy.linalg._expm_frechet' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_expm_frechet.py'>,
#[Out]#  'sqlite3.dbapi2': <module 'sqlite3.dbapi2' from 'C:\\Anaconda3\\lib\\sqlite3\\dbapi2.py'>,
#[Out]#  'multiprocessing': <module 'multiprocessing' from 'C:\\Anaconda3\\lib\\multiprocessing\\__init__.py'>,
#[Out]#  'tornado.escape': <module 'tornado.escape' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\escape.py'>,
#[Out]#  'cmd': <module 'cmd' from 'C:\\Anaconda3\\lib\\cmd.py'>,
#[Out]#  'zmq.devices.monitoredqueuedevice': <module 'zmq.devices.monitoredqueuedevice' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\devices\\monitoredqueuedevice.py'>,
#[Out]#  'pkg_resources.extern.pyparsing': <module 'pkg_resources._vendor.pyparsing' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\pyparsing.py'>,
#[Out]#  'matplotlib.text': <module 'matplotlib.text' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\text.py'>,
#[Out]#  'numpy.lib._datasource': <module 'numpy.lib._datasource' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\_datasource.py'>,
#[Out]#  'scipy.signal._spectral': <module 'scipy.signal._spectral' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_spectral.cp35-win_amd64.pyd'>,
#[Out]#  'h5py.defs': <module 'h5py.defs' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\defs.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.core.latex_symbols': <module 'IPython.core.latex_symbols' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\latex_symbols.py'>,
#[Out]#  'pkg_resources._vendor': <module 'pkg_resources._vendor' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\__init__.py'>,
#[Out]#  'numpy.lib.arrayterator': <module 'numpy.lib.arrayterator' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\arrayterator.py'>,
#[Out]#  'IPython.utils.PyColorize': <module 'IPython.utils.PyColorize' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\PyColorize.py'>,
#[Out]#  'pyvisa.resources.resource': <module 'pyvisa.resources.resource' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\resource.py'>,
#[Out]#  'scipy.stats.mvn': <module 'scipy.stats.mvn' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\mvn.cp35-win_amd64.pyd'>,
#[Out]#  'simplegeneric': <module 'simplegeneric' from 'C:\\Anaconda3\\lib\\site-packages\\simplegeneric.py'>,
#[Out]#  'scipy.special._ellip_harm': <module 'scipy.special._ellip_harm' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_ellip_harm.py'>,
#[Out]#  'scipy.sparse.extract': <module 'scipy.sparse.extract' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\extract.py'>,
#[Out]#  'matplotlib.ttconv': <module 'matplotlib.ttconv' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\ttconv.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.ma.extras': <module 'numpy.ma.extras' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\ma\\extras.py'>,
#[Out]#  'stat': <module 'stat' from 'C:\\Anaconda3\\lib\\stat.py'>,
#[Out]#  'Nowack_Lab.Procedures.transport': <module 'Nowack_Lab.Procedures.transport' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\transport.py'>,
#[Out]#  'scipy.ndimage.filters': <module 'scipy.ndimage.filters' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\filters.py'>,
#[Out]#  '_locale': <module '_locale' (built-in)>,
#[Out]#  'readline': <module 'readline' from 'C:\\Anaconda3\\lib\\site-packages\\readline.py'>,
#[Out]#  'scipy.signal.ltisys': <module 'scipy.signal.ltisys' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\ltisys.py'>,
#[Out]#  'IPython.core.magics.code': <module 'IPython.core.magics.code' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\code.py'>,
#[Out]#  'zmq.sugar.constants': <module 'zmq.sugar.constants' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\constants.py'>,
#[Out]#  'runpy': <module 'runpy' from 'C:\\Anaconda3\\lib\\runpy.py'>,
#[Out]#  'matplotlib.tri.tritools': <module 'matplotlib.tri.tritools' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\tritools.py'>,
#[Out]#  'matplotlib._path': <module 'matplotlib._path' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_path.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.transforms': <module 'matplotlib.transforms' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\transforms.py'>,
#[Out]#  'Nowack_Lab.Instruments.attocube': <module 'Nowack_Lab.Instruments.attocube' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\attocube.py'>,
#[Out]#  'Nowack_Lab.Procedures.mod2D': <module 'Nowack_Lab.Procedures.mod2D' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\mod2D.py'>,
#[Out]#  'email.base64mime': <module 'email.base64mime' from 'C:\\Anaconda3\\lib\\email\\base64mime.py'>,
#[Out]#  'matplotlib._cm_listed': <module 'matplotlib._cm_listed' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_cm_listed.py'>,
#[Out]#  'scipy.optimize._trustregion_dogleg': <module 'scipy.optimize._trustregion_dogleg' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_trustregion_dogleg.py'>,
#[Out]#  'scipy.sparse.linalg.isolve.lsqr': <module 'scipy.sparse.linalg.isolve.lsqr' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\lsqr.py'>,
#[Out]#  'ipykernel.kernelbase': <module 'ipykernel.kernelbase' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py'>,
#[Out]#  'pyvisa.resources.registerbased': <module 'pyvisa.resources.registerbased' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\registerbased.py'>,
#[Out]#  'email.utils': <module 'email.utils' from 'C:\\Anaconda3\\lib\\email\\utils.py'>,
#[Out]#  'zmq.utils.strtypes': <module 'zmq.utils.strtypes' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\strtypes.py'>,
#[Out]#  'numpy.linalg.info': <module 'numpy.linalg.info' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\linalg\\info.py'>,
#[Out]#  'IPython.core.logger': <module 'IPython.core.logger' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\logger.py'>,
#[Out]#  'ipykernel.zmqshell': <module 'ipykernel.zmqshell' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\zmqshell.py'>,
#[Out]#  'scipy.signal.fir_filter_design': <module 'scipy.signal.fir_filter_design' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\fir_filter_design.py'>,
#[Out]#  'scipy.optimize.moduleTNC': <module 'scipy.optimize.moduleTNC' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\moduleTNC.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.polynomial.polyutils': <module 'numpy.polynomial.polyutils' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\polyutils.py'>,
#[Out]#  'jupyter_client.client': <module 'jupyter_client.client' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\client.py'>,
#[Out]#  'scipy.integrate.odepack': <module 'scipy.integrate.odepack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\odepack.py'>,
#[Out]#  'pyreadline.rlmain': <module 'pyreadline.rlmain' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\rlmain.py'>,
#[Out]#  'scipy.sparse.csgraph._laplacian': <module 'scipy.sparse.csgraph._laplacian' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_laplacian.py'>,
#[Out]#  'scipy.linalg._decomp_polar': <module 'scipy.linalg._decomp_polar' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_decomp_polar.py'>,
#[Out]#  'scipy.sparse.csgraph._components': <module 'scipy.sparse.csgraph._components' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_components.py'>,
#[Out]#  'encodings.mbcs': <module 'encodings.mbcs' from 'C:\\Anaconda3\\lib\\encodings\\mbcs.py'>,
#[Out]#  'ipykernel.comm.manager': <module 'ipykernel.comm.manager' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\comm\\manager.py'>,
#[Out]#  'mpl_toolkits.axes_grid1.parasite_axes': <module 'mpl_toolkits.axes_grid1.parasite_axes' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\parasite_axes.py'>,
#[Out]#  'code': <module 'code' from 'C:\\Anaconda3\\lib\\code.py'>,
#[Out]#  'IPython.extensions': <module 'IPython.extensions' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\extensions\\__init__.py'>,
#[Out]#  'h5py.tests.old.test_datatype': <module 'h5py.tests.old.test_datatype' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_datatype.py'>,
#[Out]#  'pint.context': <module 'pint.context' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\context.py'>,
#[Out]#  'IPython.core.magics.script': <module 'IPython.core.magics.script' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\script.py'>,
#[Out]#  'jsonpickle.handlers': <module 'jsonpickle.handlers' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\handlers.py'>,
#[Out]#  'pint.registry_helpers': <module 'pint.registry_helpers' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\registry_helpers.py'>,
#[Out]#  'scipy.linalg.decomp_cholesky': <module 'scipy.linalg.decomp_cholesky' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\decomp_cholesky.py'>,
#[Out]#  'IPython.utils.dir2': <module 'IPython.utils.dir2' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\dir2.py'>,
#[Out]#  'ipykernel.heartbeat': <module 'ipykernel.heartbeat' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\heartbeat.py'>,
#[Out]#  'IPython.terminal.interactiveshell': <module 'IPython.terminal.interactiveshell' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\terminal\\interactiveshell.py'>,
#[Out]#  '__mp_main__': <module 'ipykernel.__main__' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\__main__.py'>,
#[Out]#  'h5py.h5i': <module 'h5py.h5i' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5i.cp35-win_amd64.pyd'>,
#[Out]#  'imp': <module 'imp' from 'C:\\Anaconda3\\lib\\imp.py'>,
#[Out]#  'telnetlib': <module 'telnetlib' from 'C:\\Anaconda3\\lib\\telnetlib.py'>,
#[Out]#  'h5py.tests.hl.test_dataset_getitem': <module 'h5py.tests.hl.test_dataset_getitem' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\hl\\test_dataset_getitem.py'>,
#[Out]#  'pyreadline.console.ansi': <module 'pyreadline.console.ansi' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\console\\ansi.py'>,
#[Out]#  'scipy.stats._continuous_distns': <module 'scipy.stats._continuous_distns' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_continuous_distns.py'>,
#[Out]#  'pyvisa.resources': <module 'pyvisa.resources' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\__init__.py'>,
#[Out]#  '_functools': <module '_functools' (built-in)>,
#[Out]#  'matplotlib.rcsetup': <module 'matplotlib.rcsetup' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\rcsetup.py'>,
#[Out]#  'matplotlib.tight_bbox': <module 'matplotlib.tight_bbox' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tight_bbox.py'>,
#[Out]#  'IPython.core.magics': <module 'IPython.core.magics' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\__init__.py'>,
#[Out]#  'jupyter_client.managerabc': <module 'jupyter_client.managerabc' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\managerabc.py'>,
#[Out]#  'IPython.lib.clipboard': <module 'IPython.lib.clipboard' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\clipboard.py'>,
#[Out]#  'IPython.core.displaypub': <module 'IPython.core.displaypub' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\displaypub.py'>,
#[Out]#  'scipy.linalg._procrustes': <module 'scipy.linalg._procrustes' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_procrustes.py'>,
#[Out]#  'ipykernel.jsonutil': <module 'ipykernel.jsonutil' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\jsonutil.py'>,
#[Out]#  'scipy.linalg.misc': <module 'scipy.linalg.misc' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\misc.py'>,
#[Out]#  'Instrumental': <module 'Instrumental' from 'C:\\Users\\B82A\\Documents\\GitHub\\Instrumental\\__init__.py'>,
#[Out]#  'pyreadline.unicode_helper': <module 'pyreadline.unicode_helper' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\unicode_helper.py'>,
#[Out]#  'matplotlib.projections': <module 'matplotlib.projections' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\projections\\__init__.py'>,
#[Out]#  'tornado.stack_context': <module 'tornado.stack_context' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\stack_context.py'>,
#[Out]#  'urllib.parse': <module 'urllib.parse' from 'C:\\Anaconda3\\lib\\urllib\\parse.py'>,
#[Out]#  'h5py.tests.old.test_h5': <module 'h5py.tests.old.test_h5' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_h5.py'>,
#[Out]#  'scipy.interpolate.interpnd': <module 'scipy.interpolate.interpnd' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\interpnd.cp35-win_amd64.pyd'>,
#[Out]#  'pyreadline.lineeditor': <module 'pyreadline.lineeditor' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\lineeditor\\__init__.py'>,
#[Out]#  'matplotlib.backends.backend_tkagg': <module 'matplotlib.backends.backend_tkagg' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backends\\backend_tkagg.py'>,
#[Out]#  'h5py._hl.group': <module 'h5py._hl.group' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\group.py'>,
#[Out]#  'IPython.core.events': <module 'IPython.core.events' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\events.py'>,
#[Out]#  'scipy.sparse.csgraph': <module 'scipy.sparse.csgraph' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\__init__.py'>,
#[Out]#  'ipykernel.pickleutil': <module 'ipykernel.pickleutil' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\pickleutil.py'>,
#[Out]#  'zmq.sugar.version': <module 'zmq.sugar.version' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\version.py'>,
#[Out]#  'ipaddress': <module 'ipaddress' from 'C:\\Anaconda3\\lib\\ipaddress.py'>,
#[Out]#  'sre_parse': <module 'sre_parse' from 'C:\\Anaconda3\\lib\\sre_parse.py'>,
#[Out]#  'encodings': <module 'encodings' from 'C:\\Anaconda3\\lib\\encodings\\__init__.py'>,
#[Out]#  'matplotlib.axis': <module 'matplotlib.axis' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\axis.py'>,
#[Out]#  'scipy.sparse.base': <module 'scipy.sparse.base' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\base.py'>,
#[Out]#  'PyDAQmx': <module 'PyDAQmx' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\__init__.py'>,
#[Out]#  'matplotlib._pylab_helpers': <module 'matplotlib._pylab_helpers' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_pylab_helpers.py'>,
#[Out]#  'Nowack_Lab.Procedures.navigation': <module 'Nowack_Lab.Procedures.navigation' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\navigation.py'>,
#[Out]#  'Nowack_Lab.Utilities.plotting.plot_mpl': <module 'Nowack_Lab.Utilities.plotting.plot_mpl' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\plotting\\plot_mpl.py'>,
#[Out]#  'bdb': <module 'bdb' from 'C:\\Anaconda3\\lib\\bdb.py'>,
#[Out]#  'IPython.core.extensions': <module 'IPython.core.extensions' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\extensions.py'>,
#[Out]#  'h5py.tests.old.test_file': <module 'h5py.tests.old.test_file' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_file.py'>,
#[Out]#  'bz2': <module 'bz2' from 'C:\\Anaconda3\\lib\\bz2.py'>,
#[Out]#  'zmq.utils.constant_names': <module 'zmq.utils.constant_names' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\constant_names.py'>,
#[Out]#  'instrumental.drivers': <module 'instrumental.drivers' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\drivers\\__init__.py'>,
#[Out]#  'ipykernel.connect': <module 'ipykernel.connect' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\connect.py'>,
#[Out]#  '_ni_label': <module 'scipy.ndimage._ni_label' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\_ni_label.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.afm': <module 'matplotlib.afm' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\afm.py'>,
#[Out]#  'mpl_toolkits.axes_grid1': <module 'mpl_toolkits.axes_grid1' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\__init__.py'>,
#[Out]#  'numpy.core.records': <module 'numpy.core.records' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\records.py'>,
#[Out]#  'pyreadline.keysyms.keysyms': <module 'pyreadline.keysyms.keysyms' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\keysyms\\keysyms.py'>,
#[Out]#  'scipy.optimize.minpack': <module 'scipy.optimize.minpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\minpack.py'>,
#[Out]#  'IPython.utils.io': <module 'IPython.utils.io' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\io.py'>,
#[Out]#  'h5py.h5l': <module 'h5py.h5l' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5l.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.core.magics.osm': <module 'IPython.core.magics.osm' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\osm.py'>,
#[Out]#  'typing.re': typing.re,
#[Out]#  'traceback': <module 'traceback' from 'C:\\Anaconda3\\lib\\traceback.py'>,
#[Out]#  'IPython.utils.text': <module 'IPython.utils.text' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\text.py'>,
#[Out]#  'h5py.tests.old.test_attrs_data': <module 'h5py.tests.old.test_attrs_data' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_attrs_data.py'>,
#[Out]#  'scipy.spatial.qhull': <module 'scipy.spatial.qhull' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\qhull.cp35-win_amd64.pyd'>,
#[Out]#  'ipykernel.eventloops': <module 'ipykernel.eventloops' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\eventloops.py'>,
#[Out]#  'numpy.compat.py3k': <module 'numpy.compat.py3k' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\compat\\py3k.py'>,
#[Out]#  'scipy.optimize._group_columns': <module 'scipy.optimize._group_columns' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_group_columns.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.fftpack': <module 'scipy.fftpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\__init__.py'>,
#[Out]#  'ipywidgets.widgets.trait_types': <module 'ipywidgets.widgets.trait_types' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\trait_types.py'>,
#[Out]#  'pyreadline.console': <module 'pyreadline.console' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\console\\__init__.py'>,
#[Out]#  'collections': <module 'collections' from 'C:\\Anaconda3\\lib\\collections\\__init__.py'>,
#[Out]#  'concurrent.futures.process': <module 'concurrent.futures.process' from 'C:\\Anaconda3\\lib\\concurrent\\futures\\process.py'>,
#[Out]#  'scipy.ndimage.measurements': <module 'scipy.ndimage.measurements' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\measurements.py'>,
#[Out]#  'scipy.stats._multivariate': <module 'scipy.stats._multivariate' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_multivariate.py'>,
#[Out]#  'numpy.fft.info': <module 'numpy.fft.info' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\fft\\info.py'>,
#[Out]#  'scipy.sparse.linalg.eigen.arpack.arpack': <module 'scipy.sparse.linalg.eigen.arpack.arpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\eigen\\arpack\\arpack.py'>,
#[Out]#  'six.moves': <module 'six.moves' (<six._SixMetaPathImporter object at 0x0000000004661C88>)>,
#[Out]#  'six.moves.urllib.request': <module 'six.moves.urllib.request' (<six._SixMetaPathImporter object at 0x0000000004661C88>)>,
#[Out]#  'matplotlib.table': <module 'matplotlib.table' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\table.py'>,
#[Out]#  'base64': <module 'base64' from 'C:\\Anaconda3\\lib\\base64.py'>,
#[Out]#  'IPython.core.profiledir': <module 'IPython.core.profiledir' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\profiledir.py'>,
#[Out]#  'jupyter_client.launcher': <module 'jupyter_client.launcher' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\launcher.py'>,
#[Out]#  'gettext': <module 'gettext' from 'C:\\Anaconda3\\lib\\gettext.py'>,
#[Out]#  '_collections_abc': <module '_collections_abc' from 'C:\\Anaconda3\\lib\\_collections_abc.py'>,
#[Out]#  'Nowack_Lab.Instruments.keithley': <module 'Nowack_Lab.Instruments.keithley' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\keithley.py'>,
#[Out]#  'matplotlib.tri': <module 'matplotlib.tri' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\__init__.py'>,
#[Out]#  'pyreadline.modes.notemacs': <module 'pyreadline.modes.notemacs' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\modes\\notemacs.py'>,
#[Out]#  'matplotlib.tri.trirefine': <module 'matplotlib.tri.trirefine' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\trirefine.py'>,
#[Out]#  'string': <module 'string' from 'C:\\Anaconda3\\lib\\string.py'>,
#[Out]#  'scipy.signal.filter_design': <module 'scipy.signal.filter_design' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\filter_design.py'>,
#[Out]#  'IPython.lib': <module 'IPython.lib' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\__init__.py'>,
#[Out]#  'IPython.core.page': <module 'IPython.core.page' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\page.py'>,
#[Out]#  'multiprocessing.reduction': <module 'multiprocessing.reduction' from 'C:\\Anaconda3\\lib\\multiprocessing\\reduction.py'>,
#[Out]#  'scipy.spatial': <module 'scipy.spatial' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\__init__.py'>,
#[Out]#  'pydoc': <module 'pydoc' from 'C:\\Anaconda3\\lib\\pydoc.py'>,
#[Out]#  'Nowack_Lab.Instruments.piezos': <module 'Nowack_Lab.Instruments.piezos' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\piezos.py'>,
#[Out]#  'multiprocessing.context': <module 'multiprocessing.context' from 'C:\\Anaconda3\\lib\\multiprocessing\\context.py'>,
#[Out]#  'gc': <module 'gc' (built-in)>,
#[Out]#  'scipy.sparse.construct': <module 'scipy.sparse.construct' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\construct.py'>,
#[Out]#  'Nowack_Lab.Procedures.magnetotransport': <module 'Nowack_Lab.Procedures.magnetotransport' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\magnetotransport.py'>,
#[Out]#  'ipywidgets.widgets.widget_button': <module 'ipywidgets.widgets.widget_button' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_button.py'>,
#[Out]#  'scipy.sparse.compressed': <module 'scipy.sparse.compressed' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\compressed.py'>,
#[Out]#  'zmq.backend.cython._device': <module 'zmq.backend.cython._device' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_device.cp35-win_amd64.pyd'>,
#[Out]#  'ipython_genutils': <module 'ipython_genutils' from 'C:\\Anaconda3\\lib\\site-packages\\ipython_genutils\\__init__.py'>,
#[Out]#  'numpy.version': <module 'numpy.version' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\version.py'>,
#[Out]#  'decorator': <module 'decorator' from 'C:\\Anaconda3\\lib\\site-packages\\decorator.py'>,
#[Out]#  'Nowack_Lab.Procedures': <module 'Nowack_Lab.Procedures' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\__init__.py'>,
#[Out]#  'pkg_resources.extern.six.moves': <module 'pkg_resources._vendor.six.moves' (<pkg_resources._vendor.six._SixMetaPathImporter object at 0x0000000003190C88>)>,
#[Out]#  'lzma': <module 'lzma' from 'C:\\Anaconda3\\lib\\lzma.py'>,
#[Out]#  'tabulate': <module 'tabulate' from 'C:\\Anaconda3\\lib\\site-packages\\tabulate.py'>,
#[Out]#  'typing.io': typing.io,
#[Out]#  'numpy.testing.utils': <module 'numpy.testing.utils' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\testing\\utils.py'>,
#[Out]#  'json.scanner': <module 'json.scanner' from 'C:\\Anaconda3\\lib\\json\\scanner.py'>,
#[Out]#  'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Anaconda3\\lib\\encodings\\utf_8.py'>,
#[Out]#  'pkg_resources.extern.packaging._compat': <module 'pkg_resources.extern.packaging._compat' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\packaging\\_compat.py'>,
#[Out]#  'scipy.optimize._lsq.common': <module 'scipy.optimize._lsq.common' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\common.py'>,
#[Out]#  'tornado.speedups': <module 'tornado.speedups' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\speedups.cp35-win_amd64.pyd'>,
#[Out]#  'pyvisa.compat': <module 'pyvisa.compat' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\compat\\__init__.py'>,
#[Out]#  'instrumental.errors': <module 'instrumental.errors' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\errors.py'>,
#[Out]#  'pyvisa.resources.usb': <module 'pyvisa.resources.usb' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\usb.py'>,
#[Out]#  'scipy.sparse.linalg.isolve.iterative': <module 'scipy.sparse.linalg.isolve.iterative' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\iterative.py'>,
#[Out]#  'scipy.signal.spline': <module 'scipy.signal.spline' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\spline.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.linalg._solve_toeplitz': <module 'scipy.linalg._solve_toeplitz' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_solve_toeplitz.cp35-win_amd64.pyd'>,
#[Out]#  'PIL': <module 'PIL' from 'C:\\Anaconda3\\lib\\site-packages\\PIL\\__init__.py'>,
#[Out]#  'numpy.matrixlib': <module 'numpy.matrixlib' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\matrixlib\\__init__.py'>,
#[Out]#  'scipy.special.basic': <module 'scipy.special.basic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\basic.py'>,
#[Out]#  'csv': <module 'csv' from 'C:\\Anaconda3\\lib\\csv.py'>,
#[Out]#  'scipy.ndimage': <module 'scipy.ndimage' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\__init__.py'>,
#[Out]#  'zmq.devices.basedevice': <module 'zmq.devices.basedevice' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\devices\\basedevice.py'>,
#[Out]#  'ipykernel': <module 'ipykernel' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\__init__.py'>,
#[Out]#  'zmq.sugar.socket': <module 'zmq.sugar.socket' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\socket.py'>,
#[Out]#  'IPython.utils.ulinecache': <module 'IPython.utils.ulinecache' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\ulinecache.py'>,
#[Out]#  'numpy.core.function_base': <module 'numpy.core.function_base' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\function_base.py'>,
#[Out]#  'IPython.core.completer': <module 'IPython.core.completer' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\completer.py'>,
#[Out]#  'pint.formatting': <module 'pint.formatting' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\formatting.py'>,
#[Out]#  'profile': <module 'profile' from 'C:\\Anaconda3\\lib\\profile.py'>,
#[Out]#  'timeit': <module 'timeit' from 'C:\\Anaconda3\\lib\\timeit.py'>,
#[Out]#  'zmq.eventloop': <module 'zmq.eventloop' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\eventloop\\__init__.py'>,
#[Out]#  'h5py.h5fd': <module 'h5py.h5fd' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5fd.cp35-win_amd64.pyd'>,
#[Out]#  '_opcode': <module '_opcode' (built-in)>,
#[Out]#  'gzip': <module 'gzip' from 'C:\\Anaconda3\\lib\\gzip.py'>,
#[Out]#  'scipy.linalg': <module 'scipy.linalg' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\__init__.py'>,
#[Out]#  'numpy.compat': <module 'numpy.compat' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\compat\\__init__.py'>,
#[Out]#  'ipykernel.ipkernel': <module 'ipykernel.ipkernel' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\ipkernel.py'>,
#[Out]#  'scipy.integrate': <module 'scipy.integrate' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\__init__.py'>,
#[Out]#  'matplotlib.finance': <module 'matplotlib.finance' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\finance.py'>,
#[Out]#  'IPython.core.pylabtools': <module 'IPython.core.pylabtools' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\pylabtools.py'>,
#[Out]#  'scipy.stats.distributions': <module 'scipy.stats.distributions' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\distributions.py'>,
#[Out]#  'pint': <module 'pint' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\__init__.py'>,
#[Out]#  'mimetypes': <module 'mimetypes' from 'C:\\Anaconda3\\lib\\mimetypes.py'>,
#[Out]#  'traitlets.utils.sentinel': <module 'traitlets.utils.sentinel' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\utils\\sentinel.py'>,
#[Out]#  'hmac': <module 'hmac' from 'C:\\Anaconda3\\lib\\hmac.py'>,
#[Out]#  'numpy.core.memmap': <module 'numpy.core.memmap' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\memmap.py'>,
#[Out]#  'numpy.lib.info': <module 'numpy.lib.info' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\info.py'>,
#[Out]#  'tarfile': <module 'tarfile' from 'C:\\Anaconda3\\lib\\tarfile.py'>,
#[Out]#  'mpl_toolkits.axes_grid1.axes_size': <module 'mpl_toolkits.axes_grid1.axes_size' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\axes_size.py'>,
#[Out]#  'matplotlib.font_manager': <module 'matplotlib.font_manager' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\font_manager.py'>,
#[Out]#  'h5py.h5r': <module 'h5py.h5r' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5r.cp35-win_amd64.pyd'>,
#[Out]#  'PyDAQmx.DAQmxConstants': <module 'PyDAQmx.DAQmxConstants' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\DAQmxConstants.py'>,
#[Out]#  'pyreadline.lineeditor.lineobj': <module 'pyreadline.lineeditor.lineobj' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\lineeditor\\lineobj.py'>,
#[Out]#  'jupyter_core.version': <module 'jupyter_core.version' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_core\\version.py'>,
#[Out]#  'html': <module 'html' from 'C:\\Anaconda3\\lib\\html\\__init__.py'>,
#[Out]#  '_cython_0_23_4': <module '_cython_0_23_4'>,
#[Out]#  'scipy.linalg._matfuncs_sqrtm': <module 'scipy.linalg._matfuncs_sqrtm' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_matfuncs_sqrtm.py'>,
#[Out]#  'PyDAQmx.Task': <module 'PyDAQmx.Task' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\Task.py'>,
#[Out]#  'email.feedparser': <module 'email.feedparser' from 'C:\\Anaconda3\\lib\\email\\feedparser.py'>,
#[Out]#  'matplotlib.ticker': <module 'matplotlib.ticker' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\ticker.py'>,
#[Out]#  'scipy.optimize._lbfgsb': <module 'scipy.optimize._lbfgsb' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lbfgsb.cp35-win_amd64.pyd'>,
#[Out]#  'h5py.h5o': <module 'h5py.h5o' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5o.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.misc': <module 'scipy.misc' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\misc\\__init__.py'>,
#[Out]#  'scipy.special._spherical_bessel': <module 'scipy.special._spherical_bessel' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_spherical_bessel.py'>,
#[Out]#  'IPython.terminal.ipapp': <module 'IPython.terminal.ipapp' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\terminal\\ipapp.py'>,
#[Out]#  'matplotlib.projections.geo': <module 'matplotlib.projections.geo' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\projections\\geo.py'>,
#[Out]#  'matplotlib.pylab': <module 'matplotlib.pylab' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pylab.py'>,
#[Out]#  'pyreadline': <module 'pyreadline' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\__init__.py'>,
#[Out]#  'scipy.spatial._procrustes': <module 'scipy.spatial._procrustes' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\_procrustes.py'>,
#[Out]#  'numpy.ctypeslib': <module 'numpy.ctypeslib' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\ctypeslib.py'>,
#[Out]#  'zmq.backend.cython.socket': <module 'zmq.backend.cython.socket' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\socket.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.sparse.linalg.isolve.minres': <module 'scipy.sparse.linalg.isolve.minres' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\minres.py'>,
#[Out]#  'jsonpickle.pickler': <module 'jsonpickle.pickler' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\pickler.py'>,
#[Out]#  'ipywidgets.widgets': <module 'ipywidgets.widgets' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\__init__.py'>,
#[Out]#  '_collections': <module '_collections' (built-in)>,
#[Out]#  'zmq.utils.interop': <module 'zmq.utils.interop' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\interop.py'>,
#[Out]#  'pyreadline.clipboard': <module 'pyreadline.clipboard' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\clipboard\\__init__.py'>,
#[Out]#  'ipywidgets': <module 'ipywidgets' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\__init__.py'>,
#[Out]#  'h5py.tests.old.test_group': <module 'h5py.tests.old.test_group' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_group.py'>,
#[Out]#  'matplotlib.tri.tricontour': <module 'matplotlib.tri.tricontour' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\tricontour.py'>,
#[Out]#  'matplotlib.backend_tools': <module 'matplotlib.backend_tools' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backend_tools.py'>,
#[Out]#  'pyvisa.resources.messagebased': <module 'pyvisa.resources.messagebased' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\messagebased.py'>,
#[Out]#  'matplotlib.docstring': <module 'matplotlib.docstring' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\docstring.py'>,
#[Out]#  'zmq.devices': <module 'zmq.devices' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\devices\\__init__.py'>,
#[Out]#  'scipy.linalg.special_matrices': <module 'scipy.linalg.special_matrices' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\special_matrices.py'>,
#[Out]#  'zmq.backend': <module 'zmq.backend' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\__init__.py'>,
#[Out]#  'scipy.integrate._dop': <module 'scipy.integrate._dop' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\_dop.cp35-win_amd64.pyd'>,
#[Out]#  'reprlib': <module 'reprlib' from 'C:\\Anaconda3\\lib\\reprlib.py'>,
#[Out]#  'scipy.interpolate.rbf': <module 'scipy.interpolate.rbf' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\rbf.py'>,
#[Out]#  'contextlib': <module 'contextlib' from 'C:\\Anaconda3\\lib\\contextlib.py'>,
#[Out]#  'pyreadline.keysyms.winconstants': <module 'pyreadline.keysyms.winconstants' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\keysyms\\winconstants.py'>,
#[Out]#  '_codecs': <module '_codecs' (built-in)>,
#[Out]#  'scipy.linalg._solvers': <module 'scipy.linalg._solvers' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_solvers.py'>,
#[Out]#  'binascii': <module 'binascii' (built-in)>,
#[Out]#  'pyanc350v4.PyANC350v4': <module 'pyanc350v4.PyANC350v4' from 'C:\\Anaconda3\\lib\\site-packages\\pyanc350v4\\PyANC350v4.py'>,
#[Out]#  'matplotlib._png': <module 'matplotlib._png' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_png.cp35-win_amd64.pyd'>,
#[Out]#  'Nowack_Lab.Instruments': <module 'Nowack_Lab.Instruments' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\__init__.py'>,
#[Out]#  'zmq.utils.garbage': <module 'zmq.utils.garbage' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\garbage.py'>,
#[Out]#  'zmq.utils.jsonapi': <module 'zmq.utils.jsonapi' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\jsonapi.py'>,
#[Out]#  '_weakrefset': <module '_weakrefset' from 'C:\\Anaconda3\\lib\\_weakrefset.py'>,
#[Out]#  'Nowack_Lab.Utilities.save': <module 'Nowack_Lab.Utilities.save' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\save.py'>,
#[Out]#  'scipy.spatial.kdtree': <module 'scipy.spatial.kdtree' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\kdtree.py'>,
#[Out]#  'numpy.core.getlimits': <module 'numpy.core.getlimits' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\getlimits.py'>,
#[Out]#  '_io': <module 'io' (built-in)>,
#[Out]#  'h5py.tests.old.common': <module 'h5py.tests.old.common' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\common.py'>,
#[Out]#  'h5py.h5d': <module 'h5py.h5d' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5d.cp35-win_amd64.pyd'>,
#[Out]#  'posixpath': <module 'posixpath' from 'C:\\Anaconda3\\lib\\posixpath.py'>,
#[Out]#  'distutils': <module 'distutils' from 'C:\\Anaconda3\\lib\\distutils\\__init__.py'>,
#[Out]#  '_sitebuiltins': <module '_sitebuiltins' from 'C:\\Anaconda3\\lib\\_sitebuiltins.py'>,
#[Out]#  'urllib': <module 'urllib' from 'C:\\Anaconda3\\lib\\urllib\\__init__.py'>,
#[Out]#  'zmq.sugar.tracker': <module 'zmq.sugar.tracker' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\tracker.py'>,
#[Out]#  'matplotlib.fontconfig_pattern': <module 'matplotlib.fontconfig_pattern' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\fontconfig_pattern.py'>,
#[Out]#  'scipy.optimize.slsqp': <module 'scipy.optimize.slsqp' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\slsqp.py'>,
#[Out]#  'token': <module 'token' from 'C:\\Anaconda3\\lib\\token.py'>,
#[Out]#  'numpy.matrixlib.defmatrix': <module 'numpy.matrixlib.defmatrix' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\matrixlib\\defmatrix.py'>,
#[Out]#  'pyvisa.rname': <module 'pyvisa.rname' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\rname.py'>,
#[Out]#  'scipy.integrate._bvp': <module 'scipy.integrate._bvp' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\_bvp.py'>,
#[Out]#  'scipy.sparse.linalg.eigen.arpack._arpack': <module 'scipy.sparse.linalg.eigen.arpack._arpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\eigen\\arpack\\_arpack.cp35-win_amd64.pyd'>,
#[Out]#  'pkg_resources.extern.packaging.specifiers': <module 'pkg_resources.extern.packaging.specifiers' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\packaging\\specifiers.py'>,
#[Out]#  'plistlib': <module 'plistlib' from 'C:\\Anaconda3\\lib\\plistlib.py'>,
#[Out]#  'site': <module 'site' from 'C:\\Anaconda3\\lib\\site.py'>,
#[Out]#  'keyword': <module 'keyword' from 'C:\\Anaconda3\\lib\\keyword.py'>,
#[Out]#  'IPython.extensions.storemagic': <module 'IPython.extensions.storemagic' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\extensions\\storemagic.py'>,
#[Out]#  'matplotlib.container': <module 'matplotlib.container' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\container.py'>,
#[Out]#  'scipy.fftpack.helper': <module 'scipy.fftpack.helper' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\helper.py'>,
#[Out]#  'scipy.interpolate._fitpack': <module 'scipy.interpolate._fitpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\_fitpack.cp35-win_amd64.pyd'>,
#[Out]#  'zmq.utils': <module 'zmq.utils' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\utils\\__init__.py'>,
#[Out]#  'IPython.utils.data': <module 'IPython.utils.data' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\data.py'>,
#[Out]#  'scipy.optimize.optimize': <module 'scipy.optimize.optimize' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\optimize.py'>,
#[Out]#  '_compat_pickle': <module '_compat_pickle' from 'C:\\Anaconda3\\lib\\_compat_pickle.py'>,
#[Out]#  'scipy.stats.mstats_basic': <module 'scipy.stats.mstats_basic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\mstats_basic.py'>,
#[Out]#  'scipy.optimize.zeros': <module 'scipy.optimize.zeros' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\zeros.py'>,
#[Out]#  'scipy.spatial._plotutils': <module 'scipy.spatial._plotutils' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\_plotutils.py'>,
#[Out]#  'IPython.utils.strdispatch': <module 'IPython.utils.strdispatch' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\strdispatch.py'>,
#[Out]#  'matplotlib.stackplot': <module 'matplotlib.stackplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\stackplot.py'>,
#[Out]#  'IPython.lib.deepreload': <module 'IPython.lib.deepreload' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\deepreload.py'>,
#[Out]#  'uuid': <module 'uuid' from 'C:\\Anaconda3\\lib\\uuid.py'>,
#[Out]#  'matplotlib.axes._base': <module 'matplotlib.axes._base' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_base.py'>,
#[Out]#  'getpass': <module 'getpass' from 'C:\\Anaconda3\\lib\\getpass.py'>,
#[Out]#  'io': <module 'io' from 'C:\\Anaconda3\\lib\\io.py'>,
#[Out]#  'numpy.random.mtrand': <module 'numpy.random.mtrand' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\random\\mtrand.cp35-win_amd64.pyd'>,
#[Out]#  'numpy._import_tools': <module 'numpy._import_tools' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\_import_tools.py'>,
#[Out]#  'jupyter_client.clientabc': <module 'jupyter_client.clientabc' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\clientabc.py'>,
#[Out]#  'pdb': <module 'pdb' from 'C:\\Anaconda3\\lib\\pdb.py'>,
#[Out]#  'ipywidgets.widgets.widget_controller': <module 'ipywidgets.widgets.widget_controller' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_controller.py'>,
#[Out]#  'numpy.linalg': <module 'numpy.linalg' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\linalg\\__init__.py'>,
#[Out]#  'scipy._lib': <module 'scipy._lib' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\__init__.py'>,
#[Out]#  'tornado.platform.auto': <module 'tornado.platform.auto' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\platform\\auto.py'>,
#[Out]#  'scipy.fftpack.convolve': <module 'scipy.fftpack.convolve' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\convolve.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.interpolate': <module 'scipy.interpolate' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\__init__.py'>,
#[Out]#  'zmq.sugar.poll': <module 'zmq.sugar.poll' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\sugar\\poll.py'>,
#[Out]#  'typing': <module 'typing' from 'C:\\Anaconda3\\lib\\typing.py'>,
#[Out]#  'scipy.signal.windows': <module 'scipy.signal.windows' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\windows.py'>,
#[Out]#  'matplotlib._version': <module 'matplotlib._version' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_version.py'>,
#[Out]#  'zmq.backend.cython': <module 'zmq.backend.cython' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\__init__.py'>,
#[Out]#  'pyvisa.resources.tcpip': <module 'pyvisa.resources.tcpip' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\tcpip.py'>,
#[Out]#  'concurrent': <module 'concurrent' from 'C:\\Anaconda3\\lib\\concurrent\\__init__.py'>,
#[Out]#  'genericpath': <module 'genericpath' from 'C:\\Anaconda3\\lib\\genericpath.py'>,
#[Out]#  'scipy.linalg.decomp_lu': <module 'scipy.linalg.decomp_lu' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\decomp_lu.py'>,
#[Out]#  'matplotlib': <module 'matplotlib' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\__init__.py'>,
#[Out]#  'ipykernel.pylab.backend_inline': <module 'ipykernel.pylab.backend_inline' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\pylab\\backend_inline.py'>,
#[Out]#  'numpy.ma.core': <module 'numpy.ma.core' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\ma\\core.py'>,
#[Out]#  'IPython.utils.ipstruct': <module 'IPython.utils.ipstruct' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\ipstruct.py'>,
#[Out]#  'numpy.linalg.linalg': <module 'numpy.linalg.linalg' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\linalg\\linalg.py'>,
#[Out]#  'scipy.optimize.tnc': <module 'scipy.optimize.tnc' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\tnc.py'>,
#[Out]#  'jupyter_client._version': <module 'jupyter_client._version' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\_version.py'>,
#[Out]#  'scipy.interpolate.dfitpack': <module 'scipy.interpolate.dfitpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\dfitpack.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.stats._binned_statistic': <module 'scipy.stats._binned_statistic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_binned_statistic.py'>,
#[Out]#  'ipython_genutils.py3compat': <module 'ipython_genutils.py3compat' from 'C:\\Anaconda3\\lib\\site-packages\\ipython_genutils\\py3compat.py'>,
#[Out]#  'matplotlib.colorbar': <module 'matplotlib.colorbar' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\colorbar.py'>,
#[Out]#  'IPython.core.getipython': <module 'IPython.core.getipython' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\getipython.py'>,
#[Out]#  'pint.pint_eval': <module 'pint.pint_eval' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\pint_eval.py'>,
#[Out]#  'threading': <module 'threading' from 'C:\\Anaconda3\\lib\\threading.py'>,
#[Out]#  'scipy.fftpack.fftpack_version': <module 'scipy.fftpack.fftpack_version' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\fftpack_version.py'>,
#[Out]#  'multiprocessing.process': <module 'multiprocessing.process' from 'C:\\Anaconda3\\lib\\multiprocessing\\process.py'>,
#[Out]#  'builtins': <module 'builtins' (built-in)>,
#[Out]#  'pint.errors': <module 'pint.errors' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\errors.py'>,
#[Out]#  'pyvisa.resources.pxi': <module 'pyvisa.resources.pxi' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\pxi.py'>,
#[Out]#  'locale': <module 'locale' from 'C:\\Anaconda3\\lib\\locale.py'>,
#[Out]#  '_bootlocale': <module '_bootlocale' from 'C:\\Anaconda3\\lib\\_bootlocale.py'>,
#[Out]#  'jupyter_client.localinterfaces': <module 'jupyter_client.localinterfaces' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\localinterfaces.py'>,
#[Out]#  'matplotlib.backend_managers': <module 'matplotlib.backend_managers' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backend_managers.py'>,
#[Out]#  'matplotlib.compat.subprocess': <module 'matplotlib.compat.subprocess' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\compat\\subprocess.py'>,
#[Out]#  'ctypes': <module 'ctypes' from 'C:\\Anaconda3\\lib\\ctypes\\__init__.py'>,
#[Out]#  'IPython.testing': <module 'IPython.testing' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\testing\\__init__.py'>,
#[Out]#  'matplotlib.backends._backend_agg': <module 'matplotlib.backends._backend_agg' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backends\\_backend_agg.cp35-win_amd64.pyd'>,
#[Out]#  'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Anaconda3\\lib\\encodings\\cp1252.py'>,
#[Out]#  'pyvisa.errors': <module 'pyvisa.errors' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\errors.py'>,
#[Out]#  'scipy.linalg.cython_blas': <module 'scipy.linalg.cython_blas' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\cython_blas.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.lib.type_check': <module 'numpy.lib.type_check' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\type_check.py'>,
#[Out]#  'IPython.utils.tokenutil': <module 'IPython.utils.tokenutil' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\tokenutil.py'>,
#[Out]#  'pyreadline.modes.vi': <module 'pyreadline.modes.vi' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\modes\\vi.py'>,
#[Out]#  'pyparsing': <module 'pyparsing' from 'C:\\Anaconda3\\lib\\site-packages\\pyparsing.py'>,
#[Out]#  'Nowack_Lab.Procedures.mutual_inductance': <module 'Nowack_Lab.Procedures.mutual_inductance' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\mutual_inductance.py'>,
#[Out]#  'matplotlib.patches': <module 'matplotlib.patches' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\patches.py'>,
#[Out]#  'scipy.stats._constants': <module 'scipy.stats._constants' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_constants.py'>,
#[Out]#  'scipy.optimize._numdiff': <module 'scipy.optimize._numdiff' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_numdiff.py'>,
#[Out]#  'numpy.dual': <module 'numpy.dual' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\dual.py'>,
#[Out]#  'scipy.linalg.decomp_svd': <module 'scipy.linalg.decomp_svd' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\decomp_svd.py'>,
#[Out]#  'IPython.core.usage': <module 'IPython.core.usage' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\usage.py'>,
#[Out]#  'traitlets.log': <module 'traitlets.log' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\log.py'>,
#[Out]#  'ipywidgets.widgets.widget_float': <module 'ipywidgets.widgets.widget_float' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_float.py'>,
#[Out]#  'zmq': <module 'zmq' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\__init__.py'>,
#[Out]#  'scipy.sparse.linalg.isolve': <module 'scipy.sparse.linalg.isolve' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\__init__.py'>,
#[Out]#  'matplotlib.tri.tripcolor': <module 'matplotlib.tri.tripcolor' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\tripcolor.py'>,
#[Out]#  'ipython_genutils.path': <module 'ipython_genutils.path' from 'C:\\Anaconda3\\lib\\site-packages\\ipython_genutils\\path.py'>,
#[Out]#  'matplotlib.path': <module 'matplotlib.path' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\path.py'>,
#[Out]#  'pyvisa.resources.firewire': <module 'pyvisa.resources.firewire' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\firewire.py'>,
#[Out]#  'sys': <module 'sys' (built-in)>,
#[Out]#  'distutils.errors': <module 'distutils.errors' from 'C:\\Anaconda3\\lib\\distutils\\errors.py'>,
#[Out]#  'os.path': <module 'ntpath' from 'C:\\Anaconda3\\lib\\ntpath.py'>,
#[Out]#  'matplotlib._image': <module 'matplotlib._image' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_image.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.core._internal': <module 'numpy.core._internal' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\_internal.py'>,
#[Out]#  'h5py._hl.base': <module 'h5py._hl.base' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\base.py'>,
#[Out]#  'numpy.lib.twodim_base': <module 'numpy.lib.twodim_base' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\twodim_base.py'>,
#[Out]#  'ipykernel._version': <module 'ipykernel._version' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\_version.py'>,
#[Out]#  'jupyter_client.multikernelmanager': <module 'jupyter_client.multikernelmanager' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\multikernelmanager.py'>,
#[Out]#  'scipy.ndimage._nd_image': <module 'scipy.ndimage._nd_image' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\_nd_image.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.optimize.cobyla': <module 'scipy.optimize.cobyla' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\cobyla.py'>,
#[Out]#  '_socket': <module '_socket' from 'C:\\Anaconda3\\DLLs\\_socket.pyd'>,
#[Out]#  'matplotlib.contour': <module 'matplotlib.contour' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\contour.py'>,
#[Out]#  'IPython.utils.frame': <module 'IPython.utils.frame' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\frame.py'>,
#[Out]#  'distutils.dir_util': <module 'distutils.dir_util' from 'C:\\Anaconda3\\lib\\distutils\\dir_util.py'>,
#[Out]#  'xml.parsers.expat': <module 'xml.parsers.expat' from 'C:\\Anaconda3\\lib\\xml\\parsers\\expat.py'>,
#[Out]#  'email.header': <module 'email.header' from 'C:\\Anaconda3\\lib\\email\\header.py'>,
#[Out]#  'scipy.sparse.coo': <module 'scipy.sparse.coo' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\coo.py'>,
#[Out]#  'importlib': <module 'importlib' from 'C:\\Anaconda3\\lib\\importlib\\__init__.py'>,
#[Out]#  'unittest': <module 'unittest' from 'C:\\Anaconda3\\lib\\unittest\\__init__.py'>,
#[Out]#  'scipy.spatial.ckdtree': <module 'scipy.spatial.ckdtree' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\ckdtree.cp35-win_amd64.pyd'>,
#[Out]#  'IPython.utils.timing': <module 'IPython.utils.timing' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\timing.py'>,
#[Out]#  'numpy.core': <module 'numpy.core' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\__init__.py'>,
#[Out]#  'pyvisa.attributes': <module 'pyvisa.attributes' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\attributes.py'>,
#[Out]#  'scipy.sparse.bsr': <module 'scipy.sparse.bsr' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\bsr.py'>,
#[Out]#  'scipy.special.spfun_stats': <module 'scipy.special.spfun_stats' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\spfun_stats.py'>,
#[Out]#  'cffi.lock': <module 'cffi.lock' from 'C:\\Anaconda3\\lib\\site-packages\\cffi\\lock.py'>,
#[Out]#  'scipy.sparse.csgraph._reordering': <module 'scipy.sparse.csgraph._reordering' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_reordering.cp35-win_amd64.pyd'>,
#[Out]#  'ipywidgets.widgets.widget_image': <module 'ipywidgets.widgets.widget_image' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_image.py'>,
#[Out]#  'urllib.error': <module 'urllib.error' from 'C:\\Anaconda3\\lib\\urllib\\error.py'>,
#[Out]#  'scipy.optimize._nnls': <module 'scipy.optimize._nnls' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_nnls.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.widgets': <module 'matplotlib.widgets' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\widgets.py'>,
#[Out]#  'traitlets.utils.importstring': <module 'traitlets.utils.importstring' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\utils\\importstring.py'>,
#[Out]#  'unicodedata': <module 'unicodedata' from 'C:\\Anaconda3\\DLLs\\unicodedata.pyd'>,
#[Out]#  'tkinter.filedialog': <module 'tkinter.filedialog' from 'C:\\Anaconda3\\lib\\tkinter\\filedialog.py'>,
#[Out]#  'traitlets.config.loader': <module 'traitlets.config.loader' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\config\\loader.py'>,
#[Out]#  'matplotlib.style.core': <module 'matplotlib.style.core' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\style\\core.py'>,
#[Out]#  'h5py.tests.old.test_dataset': <module 'h5py.tests.old.test_dataset' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_dataset.py'>,
#[Out]#  'scipy.linalg.decomp_qr': <module 'scipy.linalg.decomp_qr' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\decomp_qr.py'>,
#[Out]#  '_ssl': <module '_ssl' from 'C:\\Anaconda3\\DLLs\\_ssl.pyd'>,
#[Out]#  'encodings.cp437': <module 'encodings.cp437' from 'C:\\Anaconda3\\lib\\encodings\\cp437.py'>,
#[Out]#  'numpy.linalg.lapack_lite': <module 'numpy.linalg.lapack_lite' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\linalg\\lapack_lite.cp35-win_amd64.pyd'>,
#[Out]#  'h5py.tests.common': <module 'h5py.tests.common' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\common.py'>,
#[Out]#  'scipy.interpolate._cubic': <module 'scipy.interpolate._cubic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\_cubic.py'>,
#[Out]#  'Nowack_Lab.Instruments.instrument': <module 'Nowack_Lab.Instruments.instrument' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\instrument.py'>,
#[Out]#  'platform': <module 'platform' from 'C:\\Anaconda3\\lib\\platform.py'>,
#[Out]#  'PIL._util': <module 'PIL._util' from 'C:\\Anaconda3\\lib\\site-packages\\PIL\\_util.py'>,
#[Out]#  'jupyter_client.connect': <module 'jupyter_client.connect' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\connect.py'>,
#[Out]#  'h5py.tests.old.test_base': <module 'h5py.tests.old.test_base' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_base.py'>,
#[Out]#  'numpy.__config__': <module 'numpy.__config__' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\__config__.py'>,
#[Out]#  'win32com.shell.shell': <module 'win32com.shell.shell' from 'C:\\Anaconda3\\lib\\site-packages\\win32comext\\shell\\shell.pyd'>,
#[Out]#  '_operator': <module '_operator' (built-in)>,
#[Out]#  'scipy.sparse._sparsetools': <module 'scipy.sparse._sparsetools' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\_sparsetools.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.stats.morestats': <module 'scipy.stats.morestats' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\morestats.py'>,
#[Out]#  'functools': <module 'functools' from 'C:\\Anaconda3\\lib\\functools.py'>,
#[Out]#  'IPython.lib.display': <module 'IPython.lib.display' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\display.py'>,
#[Out]#  'scipy.misc.common': <module 'scipy.misc.common' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\misc\\common.py'>,
#[Out]#  'ipykernel.datapub': <module 'ipykernel.datapub' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\datapub.py'>,
#[Out]#  'scipy.signal._savitzky_golay': <module 'scipy.signal._savitzky_golay' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_savitzky_golay.py'>,
#[Out]#  'ipywidgets.widgets.widget_string': <module 'ipywidgets.widgets.widget_string' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_string.py'>,
#[Out]#  'pyvisa.ctwrapper.types': <module 'pyvisa.ctwrapper.types' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\ctwrapper\\types.py'>,
#[Out]#  'collections.abc': <module 'collections.abc' from 'C:\\Anaconda3\\lib\\collections\\abc.py'>,
#[Out]#  'numpy.testing.nosetester': <module 'numpy.testing.nosetester' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\testing\\nosetester.py'>,
#[Out]#  'numpy.random.info': <module 'numpy.random.info' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\random\\info.py'>,
#[Out]#  '_datetime': <module '_datetime' (built-in)>,
#[Out]#  'ipykernel.comm.comm': <module 'ipykernel.comm.comm' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\comm\\comm.py'>,
#[Out]#  'scipy.optimize._minimize': <module 'scipy.optimize._minimize' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_minimize.py'>,
#[Out]#  'jupyter_client.adapter': <module 'jupyter_client.adapter' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\adapter.py'>,
#[Out]#  'dateutil.tzwin': <module 'dateutil.tzwin' from 'C:\\Anaconda3\\lib\\site-packages\\dateutil\\tzwin.py'>,
#[Out]#  'Nowack_Lab.Utilities.plotting': <module 'Nowack_Lab.Utilities.plotting' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\plotting\\__init__.py'>,
#[Out]#  'tokenize': <module 'tokenize' from 'C:\\Anaconda3\\lib\\tokenize.py'>,
#[Out]#  'IPython.utils.module_paths': <module 'IPython.utils.module_paths' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\module_paths.py'>,
#[Out]#  'scipy.signal.waveforms': <module 'scipy.signal.waveforms' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\waveforms.py'>,
#[Out]#  'scipy.sparse._csparsetools': <module 'scipy.sparse._csparsetools' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\_csparsetools.cp35-win_amd64.pyd'>,
#[Out]#  'pyexpat': <module 'pyexpat' from 'C:\\Anaconda3\\DLLs\\pyexpat.pyd'>,
#[Out]#  'pyvisa.util': <module 'pyvisa.util' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\util.py'>,
#[Out]#  'email.quoprimime': <module 'email.quoprimime' from 'C:\\Anaconda3\\lib\\email\\quoprimime.py'>,
#[Out]#  'html.entities': <module 'html.entities' from 'C:\\Anaconda3\\lib\\html\\entities.py'>,
#[Out]#  'matplotlib.backend_bases': <module 'matplotlib.backend_bases' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\backend_bases.py'>,
#[Out]#  'tornado.platform.windows': <module 'tornado.platform.windows' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\platform\\windows.py'>,
#[Out]#  'numpy.lib.function_base': <module 'numpy.lib.function_base' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\function_base.py'>,
#[Out]#  '_signal': <module '_signal' (built-in)>,
#[Out]#  'scipy.stats._discrete_distns': <module 'scipy.stats._discrete_distns' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_discrete_distns.py'>,
#[Out]#  'scipy.linalg._fblas': <module 'scipy.linalg._fblas' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_fblas.cp35-win_amd64.pyd'>,
#[Out]#  'xml.parsers.expat.model': <module 'pyexpat.model'>,
#[Out]#  'ipykernel.parentpoller': <module 'ipykernel.parentpoller' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\parentpoller.py'>,
#[Out]#  'IPython.utils.capture': <module 'IPython.utils.capture' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\capture.py'>,
#[Out]#  '__future__': <module '__future__' from 'C:\\Anaconda3\\lib\\__future__.py'>,
#[Out]#  'matplotlib.dviread': <module 'matplotlib.dviread' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\dviread.py'>,
#[Out]#  'pyreadline.modes.emacs': <module 'pyreadline.modes.emacs' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\modes\\emacs.py'>,
#[Out]#  'logging.handlers': <module 'logging.handlers' from 'C:\\Anaconda3\\lib\\logging\\handlers.py'>,
#[Out]#  'urllib.response': <module 'urllib.response' from 'C:\\Anaconda3\\lib\\urllib\\response.py'>,
#[Out]#  'Nowack_Lab.Utilities': <module 'Nowack_Lab.Utilities' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\__init__.py'>,
#[Out]#  'zmq.eventloop.ioloop': <module 'zmq.eventloop.ioloop' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\eventloop\\ioloop.py'>,
#[Out]#  'zmq.devices.monitoredqueue': <module 'zmq.devices.monitoredqueue' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\devices\\monitoredqueue.cp35-win_amd64.pyd'>,
#[Out]#  'errno': <module 'errno' (built-in)>,
#[Out]#  'Nowack_Lab.Instruments.preamp': <module 'Nowack_Lab.Instruments.preamp' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\preamp.py'>,
#[Out]#  'pyvisa.ctwrapper.highlevel': <module 'pyvisa.ctwrapper.highlevel' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\ctwrapper\\highlevel.py'>,
#[Out]#  'matplotlib._cntr': <module 'matplotlib._cntr' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\_cntr.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.fftpack._fftpack': <module 'scipy.fftpack._fftpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\_fftpack.cp35-win_amd64.pyd'>,
#[Out]#  'jsonpickle.ext': <module 'jsonpickle.ext' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\ext\\__init__.py'>,
#[Out]#  'IPython.core.application': <module 'IPython.core.application' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\application.py'>,
#[Out]#  '_pickle': <module '_pickle' (built-in)>,
#[Out]#  'matplotlib.units': <module 'matplotlib.units' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\units.py'>,
#[Out]#  'queue': <module 'queue' from 'C:\\Anaconda3\\lib\\queue.py'>,
#[Out]#  'pyreadline.console.console': <module 'pyreadline.console.console' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\console\\console.py'>,
#[Out]#  'pythoncom': <module 'pythoncom' (C:\Anaconda3\Library\bin\pythoncom35.dll)>,
#[Out]#  'concurrent.futures._base': <module 'concurrent.futures._base' from 'C:\\Anaconda3\\lib\\concurrent\\futures\\_base.py'>,
#[Out]#  'matplotlib.mlab': <module 'matplotlib.mlab' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\mlab.py'>,
#[Out]#  'numpy.fft.helper': <module 'numpy.fft.helper' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\fft\\helper.py'>,
#[Out]#  'IPython.utils.encoding': <module 'IPython.utils.encoding' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\encoding.py'>,
#[Out]#  'pyvisa.ctwrapper': <module 'pyvisa.ctwrapper' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\ctwrapper\\__init__.py'>,
#[Out]#  'numpy.polynomial': <module 'numpy.polynomial' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\__init__.py'>,
#[Out]#  'scipy.optimize._lsq.trf_linear': <module 'scipy.optimize._lsq.trf_linear' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\trf_linear.py'>,
#[Out]#  'matplotlib.lines': <module 'matplotlib.lines' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\lines.py'>,
#[Out]#  'scipy.misc.doccer': <module 'scipy.misc.doccer' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\misc\\doccer.py'>,
#[Out]#  'types': <module 'types' from 'C:\\Anaconda3\\lib\\types.py'>,
#[Out]#  'scipy.optimize.nnls': <module 'scipy.optimize.nnls' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\nnls.py'>,
#[Out]#  'jsonpickle.unpickler': <module 'jsonpickle.unpickler' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\unpickler.py'>,
#[Out]#  'scipy.version': <module 'scipy.version' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\version.py'>,
#[Out]#  '_sqlite3': <module '_sqlite3' from 'C:\\Anaconda3\\DLLs\\_sqlite3.pyd'>,
#[Out]#  'h5py._hl.attrs': <module 'h5py._hl.attrs' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\attrs.py'>,
#[Out]#  'zmq.backend.cython.context': <module 'zmq.backend.cython.context' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\context.cp35-win_amd64.pyd'>,
#[Out]#  'numpy.core.umath': <module 'numpy.core.umath' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\umath.cp35-win_amd64.pyd'>,
#[Out]#  'peakutils.baseline': <module 'peakutils.baseline' from 'C:\\Anaconda3\\lib\\site-packages\\peakutils\\baseline.py'>,
#[Out]#  'codecs': <module 'codecs' from 'C:\\Anaconda3\\lib\\codecs.py'>,
#[Out]#  'IPython.core.oinspect': <module 'IPython.core.oinspect' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\oinspect.py'>,
#[Out]#  'matplotlib.gridspec': <module 'matplotlib.gridspec' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\gridspec.py'>,
#[Out]#  'scipy.spatial.distance': <module 'scipy.spatial.distance' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\distance.py'>,
#[Out]#  'numpy.lib.financial': <module 'numpy.lib.financial' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\financial.py'>,
#[Out]#  'tornado': <module 'tornado' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\__init__.py'>,
#[Out]#  'scipy.ndimage._ni_label': <module 'scipy.ndimage._ni_label' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\_ni_label.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.cm': <module 'matplotlib.cm' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\cm.py'>,
#[Out]#  'scipy.integrate._quadpack': <module 'scipy.integrate._quadpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\_quadpack.cp35-win_amd64.pyd'>,
#[Out]#  'ast': <module 'ast' from 'C:\\Anaconda3\\lib\\ast.py'>,
#[Out]#  'instrumental.drivers.daq': <module 'instrumental.drivers.daq' from 'C:\\Anaconda3\\lib\\site-packages\\instrumental\\drivers\\daq\\__init__.py'>,
#[Out]#  'scipy.sparse.linalg.interface': <module 'scipy.sparse.linalg.interface' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\interface.py'>,
#[Out]#  'shutil': <module 'shutil' from 'C:\\Anaconda3\\lib\\shutil.py'>,
#[Out]#  'pyanc350v4.ANC350v4lib': <module 'pyanc350v4.ANC350v4lib' from 'C:\\Anaconda3\\lib\\site-packages\\pyanc350v4\\ANC350v4lib.py'>,
#[Out]#  'scipy.fftpack.basic': <module 'scipy.fftpack.basic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\basic.py'>,
#[Out]#  'ipykernel.pylab': <module 'ipykernel.pylab' from 'C:\\Anaconda3\\lib\\site-packages\\ipykernel\\pylab\\__init__.py'>,
#[Out]#  'numpy.lib.index_tricks': <module 'numpy.lib.index_tricks' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\index_tricks.py'>,
#[Out]#  'scipy.optimize._spectral': <module 'scipy.optimize._spectral' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_spectral.py'>,
#[Out]#  'IPython.utils.sentinel': <module 'IPython.utils.sentinel' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\sentinel.py'>,
#[Out]#  'scipy.optimize._minpack': <module 'scipy.optimize._minpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_minpack.cp35-win_amd64.pyd'>,
#[Out]#  'jsonpickle.compat': <module 'jsonpickle.compat' from 'C:\\Anaconda3\\lib\\site-packages\\jsonpickle\\compat.py'>,
#[Out]#  'scipy.interpolate._ppoly': <module 'scipy.interpolate._ppoly' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\_ppoly.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.optimize._slsqp': <module 'scipy.optimize._slsqp' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_slsqp.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.sparse.csgraph._traversal': <module 'scipy.sparse.csgraph._traversal' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_traversal.cp35-win_amd64.pyd'>,
#[Out]#  'jupyter_client.channels': <module 'jupyter_client.channels' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_client\\channels.py'>,
#[Out]#  'cffi.api': <module 'cffi.api' from 'C:\\Anaconda3\\lib\\site-packages\\cffi\\api.py'>,
#[Out]#  'IPython.utils.sysinfo': <module 'IPython.utils.sysinfo' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\sysinfo.py'>,
#[Out]#  'IPython.core.magics.extension': <module 'IPython.core.magics.extension' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\extension.py'>,
#[Out]#  'h5py.tests.old.test_dimension_scales': <module 'h5py.tests.old.test_dimension_scales' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_dimension_scales.py'>,
#[Out]#  'scipy.optimize._basinhopping': <module 'scipy.optimize._basinhopping' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_basinhopping.py'>,
#[Out]#  'pint.quantity': <module 'pint.quantity' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\quantity.py'>,
#[Out]#  'email._parseaddr': <module 'email._parseaddr' from 'C:\\Anaconda3\\lib\\email\\_parseaddr.py'>,
#[Out]#  'IPython.core.shadowns': <module 'IPython.core.shadowns' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\shadowns.py'>,
#[Out]#  'importlib.machinery': <module 'importlib.machinery' from 'C:\\Anaconda3\\lib\\importlib\\machinery.py'>,
#[Out]#  'matplotlib.axes._subplots': <module 'matplotlib.axes._subplots' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_subplots.py'>,
#[Out]#  'pyvisa.highlevel': <module 'pyvisa.highlevel' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\highlevel.py'>,
#[Out]#  'IPython.core.displayhook': <module 'IPython.core.displayhook' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\displayhook.py'>,
#[Out]#  'scipy.fftpack.pseudo_diffs': <module 'scipy.fftpack.pseudo_diffs' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\pseudo_diffs.py'>,
#[Out]#  'pyvisa': <module 'pyvisa' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\__init__.py'>,
#[Out]#  'peakutils': <module 'peakutils' from 'C:\\Anaconda3\\lib\\site-packages\\peakutils\\__init__.py'>,
#[Out]#  'decimal': <module 'decimal' from 'C:\\Anaconda3\\lib\\decimal.py'>,
#[Out]#  'pint.compat.tokenize': <module 'pint.compat.tokenize' from 'C:\\Anaconda3\\lib\\site-packages\\pint\\compat\\tokenize.py'>,
#[Out]#  'h5py.tests.old.test_selections': <module 'h5py.tests.old.test_selections' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_selections.py'>,
#[Out]#  'matplotlib.legend': <module 'matplotlib.legend' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\legend.py'>,
#[Out]#  'IPython.core.payload': <module 'IPython.core.payload' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\payload.py'>,
#[Out]#  'Nowack_Lab.Instruments.lockin': <module 'Nowack_Lab.Instruments.lockin' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\lockin.py'>,
#[Out]#  '_string': <module '_string' (built-in)>,
#[Out]#  'email.charset': <module 'email.charset' from 'C:\\Anaconda3\\lib\\email\\charset.py'>,
#[Out]#  '_compression': <module '_compression' from 'C:\\Anaconda3\\lib\\_compression.py'>,
#[Out]#  'pyreadline.error': <module 'pyreadline.error' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\error.py'>,
#[Out]#  'enum': <module 'enum' from 'C:\\Anaconda3\\lib\\enum.py'>,
#[Out]#  'h5py.tests.old.test_h5t': <module 'h5py.tests.old.test_h5t' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_h5t.py'>,
#[Out]#  'scipy.optimize._root': <module 'scipy.optimize._root' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_root.py'>,
#[Out]#  'matplotlib.colors': <module 'matplotlib.colors' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\colors.py'>,
#[Out]#  'matplotlib.animation': <module 'matplotlib.animation' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\animation.py'>,
#[Out]#  'IPython.utils.syspathcontext': <module 'IPython.utils.syspathcontext' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\syspathcontext.py'>,
#[Out]#  'IPython.display': <module 'IPython.display' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\display.py'>,
#[Out]#  'matplotlib.ft2font': <module 'matplotlib.ft2font' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\ft2font.cp35-win_amd64.pyd'>,
#[Out]#  'sre_compile': <module 'sre_compile' from 'C:\\Anaconda3\\lib\\sre_compile.py'>,
#[Out]#  'h5py.tests.old.test_slicing': <module 'h5py.tests.old.test_slicing' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_slicing.py'>,
#[Out]#  'email.message': <module 'email.message' from 'C:\\Anaconda3\\lib\\email\\message.py'>,
#[Out]#  'Nowack_Lab.Utilities.anim': <module 'Nowack_Lab.Utilities.anim' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\anim.py'>,
#[Out]#  'IPython.core.history': <module 'IPython.core.history' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\history.py'>,
#[Out]#  'IPython.lib.backgroundjobs': <module 'IPython.lib.backgroundjobs' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\lib\\backgroundjobs.py'>,
#[Out]#  'scipy.sparse.linalg.dsolve.linsolve': <module 'scipy.sparse.linalg.dsolve.linsolve' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\dsolve\\linsolve.py'>,
#[Out]#  'xml.parsers': <module 'xml.parsers' from 'C:\\Anaconda3\\lib\\xml\\parsers\\__init__.py'>,
#[Out]#  'matplotlib.blocking_input': <module 'matplotlib.blocking_input' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\blocking_input.py'>,
#[Out]#  'IPython.utils.openpy': <module 'IPython.utils.openpy' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\openpy.py'>,
#[Out]#  'zmq.backend.select': <module 'zmq.backend.select' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\select.py'>,
#[Out]#  'IPython.core.magics.deprecated': <module 'IPython.core.magics.deprecated' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\deprecated.py'>,
#[Out]#  'scipy.linalg.blas': <module 'scipy.linalg.blas' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\blas.py'>,
#[Out]#  'storemagic': <module 'storemagic' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\extensions\\storemagic.py'>,
#[Out]#  'pyreadline.py3k_compat': <module 'pyreadline.py3k_compat' from 'C:\\Anaconda3\\lib\\site-packages\\pyreadline\\py3k_compat.py'>,
#[Out]#  'h5py._objects': <module 'h5py._objects' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_objects.cp35-win_amd64.pyd'>,
#[Out]#  'jupyter_core': <module 'jupyter_core' from 'C:\\Anaconda3\\lib\\site-packages\\jupyter_core\\__init__.py'>,
#[Out]#  'numpy.polynomial._polybase': <module 'numpy.polynomial._polybase' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\_polybase.py'>,
#[Out]#  'Nowack_Lab.Utilities.dummy': <module 'Nowack_Lab.Utilities.dummy' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Utilities\\dummy.py'>,
#[Out]#  'scipy._lib.decorator': <module 'scipy._lib.decorator' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\decorator.py'>,
#[Out]#  'scipy.stats.kde': <module 'scipy.stats.kde' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\kde.py'>,
#[Out]#  'matplotlib.pyplot': <module 'matplotlib.pyplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py'>,
#[Out]#  'email.errors': <module 'email.errors' from 'C:\\Anaconda3\\lib\\email\\errors.py'>,
#[Out]#  'quopri': <module 'quopri' from 'C:\\Anaconda3\\lib\\quopri.py'>,
#[Out]#  'numpy.polynomial.legendre': <module 'numpy.polynomial.legendre' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\legendre.py'>,
#[Out]#  'matplotlib.spines': <module 'matplotlib.spines' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\spines.py'>,
#[Out]#  'zipimport': <module 'zipimport' (built-in)>,
#[Out]#  'abc': <module 'abc' from 'C:\\Anaconda3\\lib\\abc.py'>,
#[Out]#  'matplotlib.dates': <module 'matplotlib.dates' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\dates.py'>,
#[Out]#  'h5py._errors': <module 'h5py._errors' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_errors.cp35-win_amd64.pyd'>,
#[Out]#  'zmq.devices.proxydevice': <module 'zmq.devices.proxydevice' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\devices\\proxydevice.py'>,
#[Out]#  'pyvisa.resources.gpib': <module 'pyvisa.resources.gpib' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\resources\\gpib.py'>,
#[Out]#  'IPython.utils._process_win32': <module 'IPython.utils._process_win32' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\_process_win32.py'>,
#[Out]#  'matplotlib.figure': <module 'matplotlib.figure' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\figure.py'>,
#[Out]#  'dis': <module 'dis' from 'C:\\Anaconda3\\lib\\dis.py'>,
#[Out]#  'scipy.sparse.csgraph._shortest_path': <module 'scipy.sparse.csgraph._shortest_path' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_shortest_path.cp35-win_amd64.pyd'>,
#[Out]#  'h5py._hl.dataset': <module 'h5py._hl.dataset' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\dataset.py'>,
#[Out]#  'Nowack_Lab.Procedures.scanspectra': <module 'Nowack_Lab.Procedures.scanspectra' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\scanspectra.py'>,
#[Out]#  'traitlets.config': <module 'traitlets.config' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\config\\__init__.py'>,
#[Out]#  'bisect': <module 'bisect' from 'C:\\Anaconda3\\lib\\bisect.py'>,
#[Out]#  'scipy.special.specfun': <module 'scipy.special.specfun' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\specfun.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.fftpack.realtransforms': <module 'scipy.fftpack.realtransforms' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\fftpack\\realtransforms.py'>,
#[Out]#  'marshal': <module 'marshal' (built-in)>,
#[Out]#  'json.decoder': <module 'json.decoder' from 'C:\\Anaconda3\\lib\\json\\decoder.py'>,
#[Out]#  'PyDAQmx.DAQmxCallBack': <module 'PyDAQmx.DAQmxCallBack' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\DAQmxCallBack.py'>,
#[Out]#  'IPython.utils.signatures': <module 'IPython.utils.signatures' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\signatures.py'>,
#[Out]#  'multiprocessing.connection': <module 'multiprocessing.connection' from 'C:\\Anaconda3\\lib\\multiprocessing\\connection.py'>,
#[Out]#  'scipy.spatial._distance_wrap': <module 'scipy.spatial._distance_wrap' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\spatial\\_distance_wrap.cp35-win_amd64.pyd'>,
#[Out]#  'scipy.integrate.quadrature': <module 'scipy.integrate.quadrature' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\quadrature.py'>,
#[Out]#  'scipy.interpolate.fitpack': <module 'scipy.interpolate.fitpack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\fitpack.py'>,
#[Out]#  'matplotlib.axes._axes': <module 'matplotlib.axes._axes' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_axes.py'>,
#[Out]#  'matplotlib.markers': <module 'matplotlib.markers' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\markers.py'>,
#[Out]#  'matplotlib.tri.triinterpolate': <module 'matplotlib.tri.triinterpolate' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\tri\\triinterpolate.py'>,
#[Out]#  'IPython.utils._process_common': <module 'IPython.utils._process_common' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\_process_common.py'>,
#[Out]#  'matplotlib.style': <module 'matplotlib.style' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\style\\__init__.py'>,
#[Out]#  'mtrand': <module 'numpy.random.mtrand' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\random\\mtrand.cp35-win_amd64.pyd'>,
#[Out]#  'zmq.backend.cython.error': <module 'zmq.backend.cython.error' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\error.cp35-win_amd64.pyd'>,
#[Out]#  'h5py._hl.selections2': <module 'h5py._hl.selections2' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\_hl\\selections2.py'>,
#[Out]#  'matplotlib.collections': <module 'matplotlib.collections' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\collections.py'>,
#[Out]#  'pprint': <module 'pprint' from 'C:\\Anaconda3\\lib\\pprint.py'>,
#[Out]#  'Nowack_Lab.Instruments.nidaq': <module 'Nowack_Lab.Instruments.nidaq' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\nidaq.py'>,
#[Out]#  'email.parser': <module 'email.parser' from 'C:\\Anaconda3\\lib\\email\\parser.py'>,
#[Out]#  'scipy.sparse.dia': <module 'scipy.sparse.dia' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\dia.py'>,
#[Out]#  'scipy.sparse.linalg': <module 'scipy.sparse.linalg' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\__init__.py'>,
#[Out]#  'importlib.util': <module 'importlib.util' from 'C:\\Anaconda3\\lib\\importlib\\util.py'>,
#[Out]#  'scipy.optimize._cobyla': <module 'scipy.optimize._cobyla' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_cobyla.cp35-win_amd64.pyd'>,
#[Out]#  '_winapi': <module '_winapi' (built-in)>,
#[Out]#  '_strptime': <module '_strptime' from 'C:\\Anaconda3\\lib\\_strptime.py'>,
#[Out]#  'argparse': <module 'argparse' from 'C:\\Anaconda3\\lib\\argparse.py'>,
#[Out]#  'IPython.core.magic': <module 'IPython.core.magic' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magic.py'>,
#[Out]#  'dateutil.tz': <module 'dateutil.tz' from 'C:\\Anaconda3\\lib\\site-packages\\dateutil\\tz.py'>,
#[Out]#  'pkg_resources.extern.packaging.version': <module 'pkg_resources.extern.packaging.version' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\packaging\\version.py'>,
#[Out]#  'scipy.linalg.basic': <module 'scipy.linalg.basic' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\basic.py'>,
#[Out]#  'peakutils.peak': <module 'peakutils.peak' from 'C:\\Anaconda3\\lib\\site-packages\\peakutils\\peak.py'>,
#[Out]#  'IPython.core.compilerop': <module 'IPython.core.compilerop' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\compilerop.py'>,
#[Out]#  'struct': <module 'struct' from 'C:\\Anaconda3\\lib\\struct.py'>,
#[Out]#  'matplotlib.streamplot': <module 'matplotlib.streamplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\streamplot.py'>,
#[Out]#  'six.moves.urllib.parse': <module 'six.moves.urllib.parse' (<six._SixMetaPathImporter object at 0x0000000004661C88>)>,
#[Out]#  'zmq.backend.cython._poll': <module 'zmq.backend.cython._poll' from 'C:\\Anaconda3\\lib\\site-packages\\zmq\\backend\\cython\\_poll.cp35-win_amd64.pyd'>,
#[Out]#  'socket': <module 'socket' from 'C:\\Anaconda3\\lib\\socket.py'>,
#[Out]#  'ipywidgets.widgets.widget': <module 'ipywidgets.widgets.widget' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget.py'>,
#[Out]#  'select': <module 'select' from 'C:\\Anaconda3\\DLLs\\select.pyd'>,
#[Out]#  'scipy.linalg._flapack': <module 'scipy.linalg._flapack' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\_flapack.cp35-win_amd64.pyd'>,
#[Out]#  'tornado.concurrent': <module 'tornado.concurrent' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\concurrent.py'>,
#[Out]#  'scipy.ndimage.fourier': <module 'scipy.ndimage.fourier' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\ndimage\\fourier.py'>,
#[Out]#  'scipy.optimize._hungarian': <module 'scipy.optimize._hungarian' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_hungarian.py'>,
#[Out]#  'distutils.log': <module 'distutils.log' from 'C:\\Anaconda3\\lib\\distutils\\log.py'>,
#[Out]#  'copyreg': <module 'copyreg' from 'C:\\Anaconda3\\lib\\copyreg.py'>,
#[Out]#  'email._policybase': <module 'email._policybase' from 'C:\\Anaconda3\\lib\\email\\_policybase.py'>,
#[Out]#  'numpy.lib.arraypad': <module 'numpy.lib.arraypad' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\arraypad.py'>,
#[Out]#  'inspect': <module 'inspect' from 'C:\\Anaconda3\\lib\\inspect.py'>,
#[Out]#  'scipy.sparse.csgraph._min_spanning_tree': <module 'scipy.sparse.csgraph._min_spanning_tree' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\csgraph\\_min_spanning_tree.cp35-win_amd64.pyd'>,
#[Out]#  'CLR': <module 'clr' from 'C:\\Anaconda3\\lib\\site-packages\\clr.pyd'>,
#[Out]#  'IPython.core.formatters': <module 'IPython.core.formatters' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\formatters.py'>,
#[Out]#  'pkg_resources.extern': <module 'pkg_resources.extern' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\extern\\__init__.py'>,
#[Out]#  'IPython.core.prefilter': <module 'IPython.core.prefilter' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\prefilter.py'>,
#[Out]#  'IPython.utils._sysinfo': <module 'IPython.utils._sysinfo' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\_sysinfo.py'>,
#[Out]#  'textwrap': <module 'textwrap' from 'C:\\Anaconda3\\lib\\textwrap.py'>,
#[Out]#  'scipy.optimize._lsq.lsq_linear': <module 'scipy.optimize._lsq.lsq_linear' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_lsq\\lsq_linear.py'>,
#[Out]#  'scipy.sparse.linalg.isolve.lsmr': <module 'scipy.sparse.linalg.isolve.lsmr' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\lsmr.py'>,
#[Out]#  'traitlets.utils': <module 'traitlets.utils' from 'C:\\Anaconda3\\lib\\site-packages\\traitlets\\utils\\__init__.py'>,
#[Out]#  'Nowack_Lab.Procedures.squidIV': <module 'Nowack_Lab.Procedures.squidIV' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\squidIV.py'>,
#[Out]#  'tornado.platform.interface': <module 'tornado.platform.interface' from 'C:\\Anaconda3\\lib\\site-packages\\tornado\\platform\\interface.py'>,
#[Out]#  'encodings.mac_roman': <module 'encodings.mac_roman' from 'C:\\Anaconda3\\lib\\encodings\\mac_roman.py'>,
#[Out]#  'ipywidgets.widgets.widget_link': <module 'ipywidgets.widgets.widget_link' from 'C:\\Anaconda3\\lib\\site-packages\\ipywidgets\\widgets\\widget_link.py'>,
#[Out]#  'scipy.interpolate.polyint': <module 'scipy.interpolate.polyint' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\interpolate\\polyint.py'>,
#[Out]#  'scipy.stats.mstats_extras': <module 'scipy.stats.mstats_extras' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\stats\\mstats_extras.py'>,
#[Out]#  'glob': <module 'glob' from 'C:\\Anaconda3\\lib\\glob.py'>,
#[Out]#  'cffi.error': <module 'cffi.error' from 'C:\\Anaconda3\\lib\\site-packages\\cffi\\error.py'>,
#[Out]#  'scipy._lib.six': <module 'scipy._lib.six' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\_lib\\six.py'>,
#[Out]#  'IPython.core.ultratb': <module 'IPython.core.ultratb' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\ultratb.py'>,
#[Out]#  'cycler': <module 'cycler' from 'C:\\Anaconda3\\lib\\site-packages\\cycler.py'>,
#[Out]#  'h5py.tests.hl.test_file': <module 'h5py.tests.hl.test_file' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\hl\\test_file.py'>,
#[Out]#  'scipy.sparse.linalg.dsolve': <module 'scipy.sparse.linalg.dsolve' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\sparse\\linalg\\dsolve\\__init__.py'>,
#[Out]#  'numpy.lib.nanfunctions': <module 'numpy.lib.nanfunctions' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\nanfunctions.py'>,
#[Out]#  'codeop': <module 'codeop' from 'C:\\Anaconda3\\lib\\codeop.py'>,
#[Out]#  'ipython_genutils.encoding': <module 'ipython_genutils.encoding' from 'C:\\Anaconda3\\lib\\site-packages\\ipython_genutils\\encoding.py'>,
#[Out]#  'numpy.lib.scimath': <module 'numpy.lib.scimath' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\scimath.py'>,
#[Out]#  'pkg_resources._vendor.six': <module 'pkg_resources._vendor.six' from 'C:\\Anaconda3\\lib\\site-packages\\pkg_resources\\_vendor\\six.py'>,
#[Out]#  'IPython.core.magics.pylab': <module 'IPython.core.magics.pylab' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\magics\\pylab.py'>,
#[Out]#  'scipy.signal._arraytools': <module 'scipy.signal._arraytools' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\_arraytools.py'>,
#[Out]#  'h5py.h5a': <module 'h5py.h5a' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\h5a.cp35-win_amd64.pyd'>,
#[Out]#  'matplotlib.type1font': <module 'matplotlib.type1font' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\type1font.py'>,
#[Out]#  'scipy.optimize._linprog': <module 'scipy.optimize._linprog' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\_linprog.py'>,
#[Out]#  'win32com.gen_py': <module 'win32com.gen_py'>,
#[Out]#  'IPython.core.shellapp': <module 'IPython.core.shellapp' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\shellapp.py'>,
#[Out]#  'IPython': <module 'IPython' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\__init__.py'>,
#[Out]#  'PyDAQmx.DAQmxTypes': <module 'PyDAQmx.DAQmxTypes' from 'C:\\Anaconda3\\lib\\site-packages\\PyDAQmx\\DAQmxTypes.py'>,
#[Out]#  'unittest.util': <module 'unittest.util' from 'C:\\Anaconda3\\lib\\unittest\\util.py'>,
#[Out]#  'scipy.linalg.matfuncs': <module 'scipy.linalg.matfuncs' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\matfuncs.py'>,
#[Out]#  'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>,
#[Out]#  'numpy.polynomial.hermite_e': <module 'numpy.polynomial.hermite_e' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\polynomial\\hermite_e.py'>,
#[Out]#  'mpl_toolkits.axes_grid1.axes_grid': <module 'mpl_toolkits.axes_grid1.axes_grid' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\axes_grid.py'>,
#[Out]#  'warnings': <module 'warnings' from 'C:\\Anaconda3\\lib\\warnings.py'>,
#[Out]#  'IPython.core.payloadpage': <module 'IPython.core.payloadpage' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\payloadpage.py'>,
#[Out]#  'scipy.special._ellip_harm_2': <module 'scipy.special._ellip_harm_2' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\special\\_ellip_harm_2.cp35-win_amd64.pyd'>,
#[Out]#  'h5py.highlevel': <module 'h5py.highlevel' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\highlevel.py'>,
#[Out]#  'ujson': <module 'ujson' from 'C:\\Anaconda3\\lib\\site-packages\\ujson.cp35-win_amd64.pyd'>,
#[Out]#  'mpl_toolkits.axes_grid1.mpl_axes': <module 'mpl_toolkits.axes_grid1.mpl_axes' from 'C:\\Anaconda3\\lib\\site-packages\\mpl_toolkits\\axes_grid1\\mpl_axes.py'>,
#[Out]#  'clr._extras': <module 'clr._extras'>,
#[Out]#  'PIL._binary': <module 'PIL._binary' from 'C:\\Anaconda3\\lib\\site-packages\\PIL\\_binary.py'>,
#[Out]#  'pkg_resources.extern.six.moves.urllib': <module 'pkg_resources._vendor.six.moves.urllib' (<pkg_resources._vendor.six._SixMetaPathImporter object at 0x0000000003190C88>)>,
#[Out]#  'email.encoders': <module 'email.encoders' from 'C:\\Anaconda3\\lib\\email\\encoders.py'>,
#[Out]#  'cffi': <module 'cffi' from 'C:\\Anaconda3\\lib\\site-packages\\cffi\\__init__.py'>,
#[Out]#  'scipy.signal': <module 'scipy.signal' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\signal\\__init__.py'>,
#[Out]#  'h5py.tests.hl.test_dataset_swmr': <module 'h5py.tests.hl.test_dataset_swmr' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\hl\\test_dataset_swmr.py'>,
#[Out]#  'Nowack_Lab.Instruments.ppms': <module 'Nowack_Lab.Instruments.ppms' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Instruments\\ppms.py'>,
#[Out]#  '_weakref': <module '_weakref' (built-in)>,
#[Out]#  '_win32sysloader': <module '_win32sysloader' from 'C:\\Anaconda3\\lib\\site-packages\\win32\\_win32sysloader.pyd'>,
#[Out]#  'numpy.core.defchararray': <module 'numpy.core.defchararray' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\core\\defchararray.py'>,
#[Out]#  'PIL.Image': <module 'PIL.Image' from 'C:\\Anaconda3\\lib\\site-packages\\PIL\\Image.py'>,
#[Out]#  'numpy.lib.polynomial': <module 'numpy.lib.polynomial' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\lib\\polynomial.py'>,
#[Out]#  '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>,
#[Out]#  'unittest.result': <module 'unittest.result' from 'C:\\Anaconda3\\lib\\unittest\\result.py'>,
#[Out]#  'pyvisa.ctwrapper.cthelper': <module 'pyvisa.ctwrapper.cthelper' from 'C:\\Anaconda3\\lib\\site-packages\\pyvisa\\ctwrapper\\cthelper.py'>,
#[Out]#  'scipy.linalg.decomp_schur': <module 'scipy.linalg.decomp_schur' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\linalg\\decomp_schur.py'>,
#[Out]#  'h5py.tests.old.test_h5f': <module 'h5py.tests.old.test_h5f' from 'C:\\Anaconda3\\lib\\site-packages\\h5py\\tests\\old\\test_h5f.py'>,
#[Out]#  'tempfile': <module 'tempfile' from 'C:\\Anaconda3\\lib\\tempfile.py'>,
#[Out]#  '_json': <module '_json' (built-in)>,
#[Out]#  'scipy.optimize.lbfgsb': <module 'scipy.optimize.lbfgsb' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\lbfgsb.py'>,
#[Out]#  'scipy.integrate._ode': <module 'scipy.integrate._ode' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\integrate\\_ode.py'>,
#[Out]#  'IPython.utils.importstring': <module 'IPython.utils.importstring' from 'C:\\Anaconda3\\lib\\site-packages\\IPython\\utils\\importstring.py'>,
#[Out]#  'scipy.optimize': <module 'scipy.optimize' from 'C:\\Anaconda3\\lib\\site-packages\\scipy\\optimize\\__init__.py'>,
#[Out]#  ...}
# Wed, 07 Jun 2017 03:09:15
sys.modules[DaqSpectrum.__module__]
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 07 Jun 2017 03:09:29
reload(Nowack_Lab.Procedures.daqspectrum)
# Wed, 07 Jun 2017 03:11:11
import Nowack_lab.Procedures.daqspectrum.DaqSpectrum as DaqSpectrum
# Wed, 07 Jun 2017 03:13:34
import Nowack_Lab.Procedures.daqspectrum
# Wed, 07 Jun 2017 03:13:50
reload(Nowack_Lab.Procedures.daqspectrum
)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 07 Jun 2017 03:14:09
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
# Wed, 07 Jun 2017 03:14:23
_ = pz.sweep(pz.V, {'x':227, 'y':0, 'z':170});
# Wed, 07 Jun 2017 03:14:49
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] In contact, moving\nx=227, z=170"
spectrum.run()
#spectrum.ax['loglog'].annotate(spectrum.notes,
#                                xy=(0.02, .9),
#                                xycoords='axes fraction',
#                                fontsize=8, ha='left', va='top',
#                                family='monospace'
#)

# Wed, 07 Jun 2017 03:15:40
spectrum = DaqSpectrum(instruments, measure_time=10,
                       annotate_notes=True)
spectrum.notes = "[dhl88] In contact, moving\nx=227, z=170"
spectrum.run()
#spectrum.ax['loglog'].annotate(spectrum.notes,
#                                xy=(0.02, .9),
#                                xycoords='axes fraction',
#                                fontsize=8, ha='left', va='top',
#                                family='monospace'
#)

# Wed, 07 Jun 2017 03:31:12
_ = pz.sweep(pz.V, {'x':150, 'y':0, 'z':170});
# Wed, 07 Jun 2017 03:33:55
spectrum = DaqSpectrum(instruments, measure_time=10)
spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V)
)
spectrum.run()

# Wed, 07 Jun 2017 03:46:26
_ = pz.sweep(pz.V, {'x':250, 'y':0, 'z':170});
# Wed, 07 Jun 2017 03:46:51
spectrum = DaqSpectrum(instruments, measure_time=10, annotate_notes=True)
spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V)
)
spectrum.run()

# Wed, 07 Jun 2017 04:12:04
spectrum.V
#[Out]# array([-0.04310438, -0.03247511, -0.03956129, ..., -0.02925412,
#[Out]#        -0.0356961 , -0.03247511])
# Wed, 07 Jun 2017 04:12:19
size(spectrum.V)
#[Out]# 2560000
# Wed, 07 Jun 2017 04:26:30
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:27:17
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,2);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
	for z in range(len(zs)):
		pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
		spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
										  annotate_notes=True);
		spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x](np.mean(spectrum.V))

class Longscan_daqspectrumheight(Measurement):
	def __init__(self, instruments):
		super().__init__(instruments=instruments);
	def do(self, xs, zs, vs):
		self.xs = xs;
		self.zs = zs;
		self.vs = vs;
		self.plot();
		return;
	def plot(self):
		super().plot();
		image = ax.imshow(vs, cmap='viridis', origin='lower')
		cbar = plt.colorbar(image)
		ax.set_xlabel('x');
		ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);

# Wed, 07 Jun 2017 04:29:31
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:29:35
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x](np.mean(spectrum.V))

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs, zs, vs):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);


# Wed, 07 Jun 2017 04:30:10
pz.zero()
# Wed, 07 Jun 2017 04:30:33
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,3);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x](np.mean(spectrum.V))

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs, zs, vs):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);

# Wed, 07 Jun 2017 04:36:41
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:36:56
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,3);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs, zs, vs):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);


# Wed, 07 Jun 2017 04:45:35
ls_dsh.do(xs,zs,vs)
# Wed, 07 Jun 2017 04:47:21
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

#zs = np.linspace(50,170,3);
#xs = np.linspace(150,250,3);

#vs = np.outer(zs,xs);


#for x in range(len(xs)):
#    for z in range(len(zs)):
#        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
#        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
#                                          annotate_notes=True);
#        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
 #                   int(pz.x.V), int(pz.z.V));
 #       spectrum.run()
 #       vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);

    def do(self, xs, zs, vs):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;

    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);

# Wed, 07 Jun 2017 04:47:41
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

#zs = np.linspace(50,170,3);
#xs = np.linspace(150,250,3);

#vs = np.outer(zs,xs);


#for x in range(len(xs)):
#    for z in range(len(zs)):
#        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
#        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
#                                          annotate_notes=True);
#        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
 #                   int(pz.x.V), int(pz.z.V));
 #       spectrum.run()
 #       vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);

    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;

    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs,zs,vs);

# Wed, 07 Jun 2017 04:48:16
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

#zs = np.linspace(50,170,3);
#xs = np.linspace(150,250,3);

#vs = np.outer(zs,xs);


#for x in range(len(xs)):
#    for z in range(len(zs)):
#        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
#        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
#                                          annotate_notes=True);
#        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
 #                   int(pz.x.V), int(pz.z.V));
 #       spectrum.run()
 #       vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);

    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;

    def plot(self):
        super().plot();
        image = ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 04:48:40
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

#zs = np.linspace(50,170,3);
#xs = np.linspace(150,250,3);

#vs = np.outer(zs,xs);


#for x in range(len(xs)):
#    for z in range(len(zs)):
#        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
#        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
#                                          annotate_notes=True);
#        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
 #                   int(pz.x.V), int(pz.z.V));
 #       spectrum.run()
 #       vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);

    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;

    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='lower')
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 04:50:44
xs
#[Out]# array([ 150.,  200.,  250.])
# Wed, 07 Jun 2017 04:50:49
zs
#[Out]# array([  50.,  110.,  170.])
# Wed, 07 Jun 2017 04:50:52
vs
#[Out]# array([[-0.07500425, -0.08103261, -0.07406323],
#[Out]#        [-0.06734665, -0.10509628, -0.06422912],
#[Out]#        [-0.04315034, -0.23495772, -0.03760052]])
# Wed, 07 Jun 2017 04:52:24
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

#zs = np.linspace(50,170,3);
#xs = np.linspace(150,250,3);

#vs = np.outer(zs,xs);


#for x in range(len(xs)):
#    for z in range(len(zs)):
#        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
#        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
#                                          annotate_notes=True);
#        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
 #                   int(pz.x.V), int(pz.z.V));
 #       spectrum.run()
 #       vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);

    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;

    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 04:52:52
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:54:28
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170606.py')
# Wed, 07 Jun 2017 04:54:43
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:54:48
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);


# Wed, 07 Jun 2017 04:56:01
plt.close('all')
# Wed, 07 Jun 2017 04:56:14
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:56:15
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);


# Wed, 07 Jun 2017 04:58:20
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 04:58:22
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        plt.close('all');

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);


# Wed, 07 Jun 2017 04:58:42
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        plt.close('all');

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 04:59:32
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,3);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        plt.close('all');

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 05:00:15
pa = SR5113(port='COM3')
# Wed, 07 Jun 2017 05:00:47
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,10);
xs = np.linspace(150,250,16);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Wed, 07 Jun 2017 05:01:25
pa=SR5113(port='COM2')
