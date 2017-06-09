import os
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
import re
import numpy as np
import matplotlib.pyplot as plt

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

    for i in range(len(files)-1,-1,-1):
        if('.json' not in files[i] or 'DaqSpectrum' not in files[i]):
            del files[i];

    allspectra = [];
    for f in files:
        spectrum = DaqSpectrum.load(f)
        allspectra.append(spectrum)

    return allspectra

def _get_matches_pos(match):
    try:
        pos = int(match.group(1));
    except:
        pos = 0
    return pos;

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
                    _get_matches_pos(matchx),
                    _get_matches_pos(matchy),
                    _get_matches_pos(matchz)
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
    [ index, position]
    index       index of of allspectra_struct that has a spectrum with 
                a position closest to pos
    position    closest position
    '''
    mindist  = dist(allspectra_struct[0][0],pos);
    minindex = 0

    for i in range(len(allspectra_struct)):
        thismindist = dist(allspectra_struct[i][0],pos);
        if mindist > thismindist:
            minindex = i;
            mindist = thismindist;
    return [minindex, allspectra_struct[minindex][0]]

def spectra_diff(allspectra_struct,p1,p2):
    '''
    Finds the difference between the two spectra at positions p1, p2.

    Arugments:
    allspectra_struct   [ [np.array([x,y,z]),DaqSpectrum], ... ]
    p1                  1st position, np.array([x,y,z])
    p2                  2nd position, np.array([x,y,z])

    Returns:
    [spectdiff, freqs, spectrum_p1, spectrum_p2, p1_r, p2_r]

    spectdiff           absolute difference of the two spectra
    freqs               frequencies of the psd weight of each index
    spectrum_p1         spectrum at point p1
    spectrum_p2         spectrum at point p2
    p1_r                position of spectrum_p1
    p2_r                position of spectrum_p2
    '''
    [index_p1, p1_r] = find_nearest_spectrum(allspectra_struct, p1);
    [index_p2, p2_r] = find_nearest_spectrum(allspectra_struct, p2);

    spectrum_p1 = allspectra_struct[index_p1][1];
    spectrum_p2 = allspectra_struct[index_p2][1];

    spectdiff = np.abs(spectrum_p1.psdAve - spectrum_p2.psdAve);

    if np.sum((spectrum_p1.f-spectrum_p2.f)**2) > 1e-16:
        raise ValueError('The two spectra have different frequency bins')

    return [spectdiff, spectrum_p1.f, spectrum_p1, spectrum_p2, p1_r, p2_r];

def plot(spectdiff, f, p1, p2):
    fig,ax = plt.subplots();
    ax.semilogy(f,spectdiff);
    ax.set_xlabel('Frequency (Hz)');
    ax.set_ylabel(
    r'Power Spectral Density ($\mathrm{V/\sqrt{Hz}}$)');
    note = '[x y z] = ' + '| ' + str(p1) + '-' + str(p2) + ' |';
    ax.annotate(note, xy=(0.02,.1), xycoords='axes fraction',
                fontsize=8, ha='left', va = 'top', family='monospace'
    )
    ax.set_xlim([0,1000])