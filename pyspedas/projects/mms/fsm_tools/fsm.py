from pyspedas.projects.mms.mms_load_data import mms_load_data



def mms_load_fsm(trange=['2015-10-16/05:59', '2015-10-16/06;01'], probe='1', data_rate='brst',
    level='l3', datatype='8khz', get_support_data=False, time_clip=False, no_update=False, 
    available=False, varformat=None, varnames=[], notplot=False, suffix='', latest_version=False, 
    major_version=False, min_version=None, cdf_version=None, spdf=False, always_prompt=False):
    """
    This function loads MMS FSM (FGM + SCM) data into tplot variables
    
    Parameters
    ----------
        trange : list of str
            time range of interest [start time, end time] with the format
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2015-10-16/05:59', '2015-10-16/06:01']

        probe : str or list of str
            list of probes, valid values for MMS probes are ['1','2','3','4'].
            Default: '1'

        data_rate : str or list of str
            Valid values: 'brst'
            Default: 'brst'

        level : str
            indicates level of data processing.
            Default: 'l3'

        datatype : str or list of str
            Valid datatype for FSM is: 8khz
            Default: '8khz'

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".
            Default: False

        time_clip: bool
            Data will be clipped to the exact trange specified by the trange keyword.
            Default: False

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.
            Default: None (all variables are loaded)

        varnames: list of str
            List of variable names to load (if not specified,
            all data variables are loaded)
            Default: [] (all variables are loaded)

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.
            Default: None

        notplot: bool
            If True, then data are returned in a hash table instead of 
            being stored in tplot variables (useful for debugging, and
            access to multidimensional data products)
            Default: False

        available: bool
            If True, simply return the available data files (without downloading)
            for the requested parameters
            Default: False

        no_update: bool
            Set this flag to preserve the original data. if not set and newer 
            data is found the existing data will be overwritten
            Default: False

        cdf_version: str
            Specify a specific CDF version # to load (e.g., cdf_version='4.3.0')
            Default: None

        min_version: str
            Specify a minimum CDF version # to load
            Default: None

        latest_version: bool
            Only grab the latest CDF version in the requested time interval
            Default: False

        major_version: bool
            Only open the latest major CDF version (e.g., X in vX.Y.Z) in the requested time interval
            Default: False

        always_prompt: bool
            Set this keyword to always prompt for the user's username and password;
            useful if you accidentally save an incorrect password, or if your SDC password has changed
            Default: False
            
        spdf: bool
            If True, download the data from the SPDF instead of the SDC
            Default: False

    Returns
    -------
        list of str
            List of tplot variables created.

    Example
    -------

    >>> import pyspedas
    >>> from pyspedas import tplot
    >>> fsm_data = pyspedas.projects.mms.mms_load_fsm(trange=['2015-10-16/05:59', '2015-10-16/06:01'])
    >>> tplot(['mms1_fsm_b_mag_brst_l3','mms1_fsm_b_gse_brst_l3','mms1_fsm_r_gse_brst_l3'])

    """
    tvars = mms_load_data(trange=trange, notplot=notplot, varformat=varformat, probe=probe, data_rate=data_rate, 
        level=level, instrument='fsm', datatype=datatype, get_support_data=get_support_data, time_clip=time_clip,
        no_update=no_update, available=available, suffix=suffix, latest_version=latest_version, varnames=varnames,
        major_version=major_version, min_version=min_version, cdf_version=cdf_version, spdf=spdf, always_prompt=always_prompt)
    return tvars
