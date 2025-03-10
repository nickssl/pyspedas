import logging
import os
import matplotlib.pyplot as plt
from pytplot import get_data
from . import mms_load_mec


def mms_orbit_plot(trange=['2015-10-16', '2015-10-17'],
                   probes=[1, 2, 3, 4],
                   data_rate='srvy',
                   xr=None,
                   yr=None,
                   plane='xy',
                   coord='gse',
                   xsize=5,
                   ysize=5,
                   marker='x',
                   markevery=10,
                   markersize=5,
                   earth=True,
                   dpi=300,
                   save_png='',
                   save_pdf='',
                   save_eps='',
                   save_jpeg='',
                   save_svg='',
                   return_plot_objects=False,
                   display=True
                   ):
    """
    This function creates MMS orbit plots
    
    Parameters
    -----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        probes: list of str
            probe #, e.g., '4' for MMS4

        data_rate: str
            instrument data rate, e.g., 'srvy' or 'brst'

        plane: str
            coordinate plane to plot (options: 'xy', 'yz', 'xz')

        xr: list of float
            two element list specifying x-axis range

        yr: list of float
            two element list specifying y-axis range

        coord: str
            coordinate system

        xsize: float
            size of the figure in the x-direction, in inches (default: 5)

        ysize: float
            size of the figure in the y-direction, in inches (default: 5)

        marker: str
            marker style for the data points (default: 'x')

        markevery: int or sequence of int
            plot a marker at every n-th data point (default: 10)

        markersize: float
            size of the marker in points (default: 5)

        earth: bool
            plot a reference image of the Earth (default: True)

        dpi: int
            dots per inch for the plot (default: 300)

        save_png: str
            file path to save the plot as a PNG file (default: None)

        save_pdf: str
            file path to save the plot as a PDF file (default: None)

        save_eps: str
            file path to save the plot as an EPS file (default: None)

        save_jpeg: str
            file path to save the plot as a JPEG file (default: None)

        save_svg: str
            file path to save the plot as an SVG file (default: None)

        return_plot_objects: bool
            whether to return the plot objects as a tuple (default: False)

        display: bool
            whether to display the plot using matplotlib's `show()` function (default: True)

    """
    spacecraft_colors = [(0, 0, 0), (213/255, 94/255, 0), (0, 158/255, 115/255), (86/255, 180/255, 233/255)]

    mec_vars = mms_load_mec(trange=trange, data_rate=data_rate, probe=probes, varformat='*_r_' + coord, time_clip=True)

    if len(mec_vars) == 0:
        logging.error('Problem loading MEC data')
        return

    plane = plane.lower()
    coord = coord.lower()

    if plane not in ['xy', 'yz', 'xz']:
        logging.error('Error, invalid plane specified; valid options are: xy, yz, xz')
        return

    if coord not in ['eci', 'gsm', 'geo', 'sm', 'gse', 'gse2000']:
        logging.error('Error, invalid coordinate system specified; valid options are: eci, gsm, geo, sm, gse, gse2000')
        return

    km_in_re = 6371.2

    fig, axis = plt.subplots(sharey=True, sharex=True, figsize=(xsize, ysize))

    if earth:
        im = plt.imread(os.path.dirname(os.path.realpath(__file__)) + '/mec_tools/earth_polar1.png')
        plt.imshow(im, extent=(-1, 1, -1, 1))

    plot_count = 0

    for probe in probes:
        position_data = get_data('mms' + str(probe) + '_mec_r_' + coord)
        if position_data is None:
            logging.error('No ' + data_rate + ' MEC data found for ' + 'MMS' + str(probe))
            continue
        else:
            t, d = position_data
            plot_count += 1

        if plane == 'xy':
            axis.plot(d[:, 0]/km_in_re, d[:, 1]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1], marker=marker, markevery=markevery, markersize=markersize)
            axis.set_xlabel('X Position, Re')
            axis.set_ylabel('Y Position, Re')
        if plane == 'yz':
            axis.plot(d[:, 1]/km_in_re, d[:, 2]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1], marker=marker, markevery=markevery, markersize=markersize)
            axis.set_xlabel('Y Position, Re')
            axis.set_ylabel('Z Position, Re')
        if plane == 'xz':
            axis.plot(d[:, 0]/km_in_re, d[:, 2]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1], marker=marker, markevery=markevery, markersize=markersize)
            axis.set_xlabel('X Position, Re')
            axis.set_ylabel('Z Position, Re')

        axis.set_aspect('equal')

    if plot_count > 0:  # at least one plot created
        axis.legend()
        axis.set_title(trange[0] + ' to ' + trange[1])
        axis.annotate(coord.upper() + ' coordinates', xy=(0.6, 0.05), xycoords='axes fraction')
        if xr is not None:
            axis.set_xlim(xr)
        if yr is not None:
            axis.set_ylim(yr)

        if return_plot_objects:
            return fig, axis

        if save_png is not None and save_png != '':
            if not save_png.endswith('.png'):
                save_png += '.png'
            plt.savefig(save_png, dpi=dpi)

        if save_eps is not None and save_eps != '':
            if not save_eps.endswith('.eps'):
                save_eps += '.eps'
            plt.savefig(save_eps, dpi=dpi)

        if save_svg is not None and save_svg != '':
            if not save_svg.endswith('.svg'):
                save_svg += '.svg'
            plt.savefig(save_svg, dpi=dpi)

        if save_pdf is not None and save_pdf != '':
            if not save_pdf.endswith('.pdf'):
                save_pdf += '.pdf'
            plt.savefig(save_pdf, dpi=dpi)

        if save_jpeg is not None and save_jpeg != '':
            if not save_jpeg.endswith('.jpeg'):
                save_jpeg += '.jpeg'
            plt.savefig(save_jpeg, dpi=dpi)

        if display:
            plt.show()
