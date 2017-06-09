%load qtconsole/2017/06/analyze/daqspectrum_image.py
# %load qtconsole/2017/06/analyze/daqspectrum_image.py
import os
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
import re
import numpy as np

def import_daqspectra(directory, start, end):
    '''
    Imports daqspectra from directory knowing the first and last file

    Arguments:
    directory       the directory to navigate to that contains all 
                    of these spectra
    start           beginning of the spectra in question (inclusive)
    end             end of the spectra in question (inclusive)

    returns all daqspectra in a list
    '''
    os.chdir(directory);
    allfiles = os.listdir();
    i_start = 0;
    i_end   = len(allfiles);
    has_changed_start = False;

    # find correct range
    for i in range(len(allfiles)):
        # finds only the first start file
        if (start in allfiles[i] and has_changed_start is False):
            i_start = i;
            has_changed_start = True;
        if (end in allfiles[i]):
            i_end = i;

    files = allfiles[i_start,i_end+1];

    for i in range(len(files),0,-1):
        if('.json' not in file[i] or 'DaqSpectrum' not in file[i]):
            del files[i]

    allspectra = [];
    for f in files:
        spectrum = DaqSpectrum.load(f)
        allspectra.append(spectrum)

    return allspectra

def make_spectra_struct(allspectra):
    '''
    Makes a struct containing the position of each spectra and the spectra

    Arguments:
    allspectra      list containing all spectra.  In spectrum.notes must be
                    'x=200', 'z=100', 'y=100'.  Exactly.  Anything else and 
                    the x,y, or z value will be set to zero.
    Returns:
                    [ [ np.array([x,y,z]),DaqSpectrum], ... ]
    '''

    allstructs = [];

    for spectrum in allspectra:
        notes = spectrum.notes;
        matchx = re.search('x=(\d+)',notes);
        matchy = re.search('y=(\d+)',notes);
        matchz = re.search('z=(\d+)',notes);
        allstructs.append(
            [
                np.array([
                    int(matchx.group(1)),
                    int(matchy.group(1)),
                    int(matchz.group(1))
                ]),
                spectrum
            ]
        );
    return allstructs;

def dist(p1,p2,p=2):
    '''
    Distance function 

    Arguments:
    p1          numpy array, first position
    p2          numpy array, second position
    p           p val for distance calc

    Returns:
    p norm between p1 and p2, a float
    '''
    return np.sum( (p1-p2)**p)**(1.0/p);

def find_nearest_spectrum(allspectra_struct,pos):
    '''
    Find the index of the spectrum nearest to pos

    Arguments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    pos                 np.array([x,y,z]), position nearest

    Returns:
    index of allspectra_struct that has a spectrum with a position
    closest to pos
    '''
    mindist  = dist(allspectra_struct[0][0],pos);
    minindex = 0

    for i in range(len(allspectra_struct)):
        thismindist = dist(allspectra_struct[i],pos):
        if mindist > thismindist:
            minindex = i;
            mindist = thismindist;
    return minindex

def spectra_diff(allspectra_struct,p1,p2):
    '''
    Finds the difference between the two spectra at positions p1, p2.

    Arugments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    p1                  1st position, np.array([x,y,z])
    p2                  2nd position, np.array([x,y,z])

    Returns:
    [spectdiff, freqs, spectrum_p1, spectrum_p2]

    spectdiff           absolute difference of the two spectra
    freqs               frequencies of the psd weight of each index
    spectrum_p1         spectrum at point p1
    spectrum_p2         spectrum at point p2
    '''
    index_p1 = find_nearest_spectrum(allspectra_struct, p1);
    index_p2 = find_nearest_spectrum(allspectra_struct, p2);

    spectrum_p1 = allspectra_struct[index_p1][1];
    spectrum_p2 = allspectra_struct[index_p2][1];

    spectdiff = np.abs(spectrum_p1.psdAve - spectrum_p2.psdAve);

    if np.sum((spectrum_p1.f-spectrum_p2.f)**2) > 1e-16:
        raise ValueError('The two spectra have different frequency bins')

    return [spectdiff, spectrum_p1.f, spectrum_p1, spectrum_p2];
# %load qtconsole/2017/06/analyze/daqspectrum_image.py
import os
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
import re
import numpy as np

def import_daqspectra(directory, start, end):
    '''
    Imports daqspectra from directory knowing the first and last file

    Arguments:
    directory       the directory to navigate to that contains all 
                    of these spectra
    start           beginning of the spectra in question (inclusive)
    end             end of the spectra in question (inclusive)

    returns all daqspectra in a list
    '''
    os.chdir(directory);
    allfiles = os.listdir();
    i_start = 0;
    i_end   = len(allfiles);
    has_changed_start = False;

    # find correct range
    for i in range(len(allfiles)):
        # finds only the first start file
        if (start in allfiles[i] and has_changed_start is False):
            i_start = i;
            has_changed_start = True;
        if (end in allfiles[i]):
            i_end = i;

    files = allfiles[i_start,i_end+1];

    for i in range(len(files),0,-1):
        if('.json' not in file[i] or 'DaqSpectrum' not in file[i]):
            del files[i]

    allspectra = [];
    for f in files:
        spectrum = DaqSpectrum.load(f)
        allspectra.append(spectrum)

    return allspectra

def make_spectra_struct(allspectra):
    '''
    Makes a struct containing the position of each spectra and the spectra

    Arguments:
    allspectra      list containing all spectra.  In spectrum.notes must be
                    'x=200', 'z=100', 'y=100'.  Exactly.  Anything else and 
                    the x,y, or z value will be set to zero.
    Returns:
                    [ [ np.array([x,y,z]),DaqSpectrum], ... ]
    '''

    allstructs = [];

    for spectrum in allspectra:
        notes = spectrum.notes;
        matchx = re.search('x=(\d+)',notes);
        matchy = re.search('y=(\d+)',notes);
        matchz = re.search('z=(\d+)',notes);
        allstructs.append(
            [
                np.array([
                    int(matchx.group(1)),
                    int(matchy.group(1)),
                    int(matchz.group(1))
                ]),
                spectrum
            ]
        );
    return allstructs;

def dist(p1,p2,p=2):
    '''
    Distance function 

    Arguments:
    p1          numpy array, first position
    p2          numpy array, second position
    p           p val for distance calc

    Returns:
    p norm between p1 and p2, a float
    '''
    return np.sum( (p1-p2)**p)**(1.0/p);

def find_nearest_spectrum(allspectra_struct,pos):
    '''
    Find the index of the spectrum nearest to pos

    Arguments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    pos                 np.array([x,y,z]), position nearest

    Returns:
    index of allspectra_struct that has a spectrum with a position
    closest to pos
    '''
    mindist  = dist(allspectra_struct[0][0],pos);
    minindex = 0

    for i in range(len(allspectra_struct)):
        thismindist = dist(allspectra_struct[i],pos):
        if mindist > thismindist:
            minindex = i;
            mindist = thismindist;
    return minindex

def spectra_diff(allspectra_struct,p1,p2):
    '''
    Finds the difference between the two spectra at positions p1, p2.

    Arugments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    p1                  1st position, np.array([x,y,z])
    p2                  2nd position, np.array([x,y,z])

    Returns:
    [spectdiff, freqs, spectrum_p1, spectrum_p2]

    spectdiff           absolute difference of the two spectra
    freqs               frequencies of the psd weight of each index
    spectrum_p1         spectrum at point p1
    spectrum_p2         spectrum at point p2
    '''
    index_p1 = find_nearest_spectrum(allspectra_struct, p1);
    index_p2 = find_nearest_spectrum(allspectra_struct, p2);

    spectrum_p1 = allspectra_struct[index_p1][1];
    spectrum_p2 = allspectra_struct[index_p2][1];

    spectdiff = np.abs(spectrum_p1.psdAve - spectrum_p2.psdAve);

    if np.sum((spectrum_p1.f-spectrum_p2.f)**2) > 1e-16:
        raise ValueError('The two spectra have different frequency bins')

    return [spectdiff, spectrum_p1.f, spectrum_p1, spectrum_p2];
%run -i qtconsole/2017/06/analyze/daqspectrum_image.py
%run -i qtconsole/2017/06/analyze/daqspectrum_image.py
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
a = [0, 1,2,3,4,5,6]
a[1,2]
a[1:2]
%run -i qtconsole/2017/06/analyze/daqspectrum_image.py
ls
%load ~/qtconsole/2017/06/analyze/daqspectrum_image.py
# %load ~/qtconsole/2017/06/analyze/daqspectrum_image.py
import os
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
import re
import numpy as np

def import_daqspectra(directory, start, end):
    '''
    Imports daqspectra from directory knowing the first and last file

    Arguments:
    directory       the directory to navigate to that contains all 
                    of these spectra
    start           beginning of the spectra in question (inclusive)
    end             end of the spectra in question (inclusive)

    returns all daqspectra in a list
    '''
    os.chdir(directory);
    allfiles = os.listdir();
    i_start = 0;
    i_end   = len(allfiles);
    has_changed_start = False;

    # find correct range
    for i in range(len(allfiles)):
        # finds only the first start file
        if (start in allfiles[i] and has_changed_start is False):
            i_start = i;
            has_changed_start = True;
        if (end in allfiles[i]):
            i_end = i;

    files = allfiles[i_start:i_end+1];

    for i in range(len(files),0,-1):
        if('.json' not in file[i] or 'DaqSpectrum' not in file[i]):
            del files[i]

    allspectra = [];
    for f in files:
        spectrum = DaqSpectrum.load(f)
        allspectra.append(spectrum)

    return allspectra

def make_spectra_struct(allspectra):
    '''
    Makes a struct containing the position of each spectra and the spectra

    Arguments:
    allspectra      list containing all spectra.  In spectrum.notes must be
                    'x=200', 'z=100', 'y=100'.  Exactly.  Anything else and 
                    the x,y, or z value will be set to zero.
    Returns:
                    [ [ np.array([x,y,z]),DaqSpectrum], ... ]
    '''

    allstructs = [];

    for spectrum in allspectra:
        notes = spectrum.notes;
        matchx = re.search('x=(\d+)',notes);
        matchy = re.search('y=(\d+)',notes);
        matchz = re.search('z=(\d+)',notes);
        allstructs.append(
            [
                np.array([
                    int(matchx.group(1)),
                    int(matchy.group(1)),
                    int(matchz.group(1))
                ]),
                spectrum
            ]
        );
    return allstructs;

def dist(p1,p2,p=2):
    '''
    Distance function 

    Arguments:
    p1          numpy array, first position
    p2          numpy array, second position
    p           p val for distance calc

    Returns:
    p norm between p1 and p2, a float
    '''
    return np.sum( (p1-p2)**p)**(1.0/p);

def find_nearest_spectrum(allspectra_struct,pos):
    '''
    Find the index of the spectrum nearest to pos

    Arguments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    pos                 np.array([x,y,z]), position nearest

    Returns:
    index of allspectra_struct that has a spectrum with a position
    closest to pos
    '''
    mindist  = dist(allspectra_struct[0][0],pos);
    minindex = 0

    for i in range(len(allspectra_struct)):
        thismindist = dist(allspectra_struct[i][0],pos);
        if mindist > thismindist:
            minindex = i;
            mindist = thismindist;
    return minindex

def spectra_diff(allspectra_struct,p1,p2):
    '''
    Finds the difference between the two spectra at positions p1, p2.

    Arugments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    p1                  1st position, np.array([x,y,z])
    p2                  2nd position, np.array([x,y,z])

    Returns:
    [spectdiff, freqs, spectrum_p1, spectrum_p2]

    spectdiff           absolute difference of the two spectra
    freqs               frequencies of the psd weight of each index
    spectrum_p1         spectrum at point p1
    spectrum_p2         spectrum at point p2
    '''
    index_p1 = find_nearest_spectrum(allspectra_struct, p1);
    index_p2 = find_nearest_spectrum(allspectra_struct, p2);

    spectrum_p1 = allspectra_struct[index_p1][1];
    spectrum_p2 = allspectra_struct[index_p2][1];

    spectdiff = np.abs(spectrum_p1.psdAve - spectrum_p2.psdAve);

    if np.sum((spectrum_p1.f-spectrum_p2.f)**2) > 1e-16:
        raise ValueError('The two spectra have different frequency bins')

    return [spectdiff, spectrum_p1.f, spectrum_p1, spectrum_p2];
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
%run -i qtconsole/2017/06/analyze/daqspectrum_image.py
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
%load ~/qtconsole/2017/06/analyze/daqspectrum_image.py
# %load ~/qtconsole/2017/06/analyze/daqspectrum_image.py
import os
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
import re
import numpy as np

def import_daqspectra(directory, start, end):
    '''
    Imports daqspectra from directory knowing the first and last file

    Arguments:
    directory       the directory to navigate to that contains all 
                    of these spectra
    start           beginning of the spectra in question (inclusive)
    end             end of the spectra in question (inclusive)

    returns all daqspectra in a list
    '''
    os.chdir(directory);
    allfiles = os.listdir();
    i_start = 0;
    i_end   = len(allfiles);
    has_changed_start = False;

    # find correct range
    for i in range(len(allfiles)):
        # finds only the first start file
        if (start in allfiles[i] and has_changed_start is False):
            i_start = i;
            has_changed_start = True;
        if (end in allfiles[i]):
            i_end = i;

    files = allfiles[i_start:i_end+1];

    for i in range(len(files),0,-1):
        print(i);
        if('.json' not in files[i] or 'DaqSpectrum' not in files[i]):
            print('Deleting {0}'.format(i));
            del files[i];

    allspectra = [];
    for f in files:
        spectrum = DaqSpectrum.load(f)
        allspectra.append(spectrum)

    return allspectra

def make_spectra_struct(allspectra):
    '''
    Makes a struct containing the position of each spectra and the spectra

    Arguments:
    allspectra      list containing all spectra.  In spectrum.notes must be
                    'x=200', 'z=100', 'y=100'.  Exactly.  Anything else and 
                    the x,y, or z value will be set to zero.
    Returns:
                    [ [ np.array([x,y,z]),DaqSpectrum], ... ]
    '''

    allstructs = [];

    for spectrum in allspectra:
        notes = spectrum.notes;
        matchx = re.search('x=(\d+)',notes);
        matchy = re.search('y=(\d+)',notes);
        matchz = re.search('z=(\d+)',notes);
        allstructs.append(
            [
                np.array([
                    int(matchx.group(1)),
                    int(matchy.group(1)),
                    int(matchz.group(1))
                ]),
                spectrum
            ]
        );
    return allstructs;

def dist(p1,p2,p=2):
    '''
    Distance function 

    Arguments:
    p1          numpy array, first position
    p2          numpy array, second position
    p           p val for distance calc

    Returns:
    p norm between p1 and p2, a float
    '''
    return np.sum( (p1-p2)**p)**(1.0/p);

def find_nearest_spectrum(allspectra_struct,pos):
    '''
    Find the index of the spectrum nearest to pos

    Arguments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    pos                 np.array([x,y,z]), position nearest

    Returns:
    index of allspectra_struct that has a spectrum with a position
    closest to pos
    '''
    mindist  = dist(allspectra_struct[0][0],pos);
    minindex = 0

    for i in range(len(allspectra_struct)):
        thismindist = dist(allspectra_struct[i][0],pos);
        if mindist > thismindist:
            minindex = i;
            mindist = thismindist;
    return minindex

def spectra_diff(allspectra_struct,p1,p2):
    '''
    Finds the difference between the two spectra at positions p1, p2.

    Arugments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    p1                  1st position, np.array([x,y,z])
    p2                  2nd position, np.array([x,y,z])

    Returns:
    [spectdiff, freqs, spectrum_p1, spectrum_p2]

    spectdiff           absolute difference of the two spectra
    freqs               frequencies of the psd weight of each index
    spectrum_p1         spectrum at point p1
    spectrum_p2         spectrum at point p2
    '''
    index_p1 = find_nearest_spectrum(allspectra_struct, p1);
    index_p2 = find_nearest_spectrum(allspectra_struct, p2);

    spectrum_p1 = allspectra_struct[index_p1][1];
    spectrum_p2 = allspectra_struct[index_p2][1];

    spectdiff = np.abs(spectrum_p1.psdAve - spectrum_p2.psdAve);

    if np.sum((spectrum_p1.f-spectrum_p2.f)**2) > 1e-16:
        raise ValueError('The two spectra have different frequency bins')

    return [spectdiff, spectrum_p1.f, spectrum_p1, spectrum_p2];
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
list(range(10,0))
list(range(10,0,-1))
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
allspectra = import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
spectrastruct = make_spectra_struct(allspectra)
import_daqspectra(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-08", "024432", "095430")
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
spectrastruct = make_spectra_struct(allspectra)
spectrastruct[0]
spectrastruct[1]
np
[spectdiff, f, s_p1, s_p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([250,0,50]))
s_p1
s_p1.notes
s_p2.notes
plt.semilogy(spectdiff,f)
plt.show()
plt.semilogy(f,spectdiff)
plt.show()
plt.semilogy(f,spectdiff); plt.xlim([0,1000])
plt.show()
[spectdiff, f, s_p1, s_p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([150,0,200]))
print(s_p1.notes,s_p2.notes)
plt.semilogy(f,spectdiff); plt.xlim([0,1000]); plt.show()
[spectdiff, f, s_p1, s_p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([250,0,50])); print(s_p1.notes,s_p2.notes);
plt.semilogy(f,spectdiff); plt.xlim([0,1000]); plt.show()
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([250,0,50])); print(s_p1.notes,s_p2.notes);
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([250,0,50]));
plot(spectdiff, f, p1,p2)
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
plot(spectdiff, f, p1,p2)
plt.show()
plot(spectdiff, f, p1,p2)
plt.show()
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
plot(spectdiff, f, p1,p2); plt.show()
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
plot(spectdiff, f, p1,p2); plt.show()
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([150,0,200]));
plot(spectdiff, f, p1,p2); plt.show()
%run -i ~/qtconsole/2017/06/analyze/daqspectrum_image.py
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,50]), np.array([250,0,50]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,200]), np.array([250,0,200]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([202,0,200]), np.array([202,0,50]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([202,0,200]), np.array([202,0,180]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([181,0,200]), np.array([181,0,180]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([181,0,200]), np.array([181,0,50]));
plot(spectdiff, f, p1,p2); plt.show()
[spectdiff, f, s_p1, s_p2,p1,p2] = spectra_diff(spectrastruct, np.array([150,0,200]), np.array([150,0,180]));
plot(spectdiff, f, p1,p2); plt.show()
%history
%history -f ~/qtconsole/2017/06/analyze/daqspectrum_image.log.py
pwd
%history -f ../../../../../qtconsole/2017/06/analyze/daqspectrum_image.log.py
