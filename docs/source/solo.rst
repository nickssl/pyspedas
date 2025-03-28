Solar Orbiter (SOLO)
========================================================================
The routines in this module can be used to load data from the Solar Orbiter (SOLO) mission.


Magnetometer (MAG)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.solo.mag

Example
^^^^^^^^^

.. code-block:: python
   
   import pyspedas
   from pyspedas import tplot
   mag_vars = pyspedas.projects.solo.mag(trange=['2020-06-01', '2020-06-02'], datatype='rtn-normal')
   tplot('B_RTN')

.. image:: _static/solo_mag.png
   :align: center
   :class: imgborder




Solar Wind Plasma Analyser (SWA)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.solo.swa

Example
^^^^^^^^^

.. code-block:: python
   
   import pyspedas
   from pyspedas import tplot
   swa_vars = pyspedas.projects.solo.swa(trange=['2020-07-22', '2020-07-23'], datatype='pas-eflux')
   tplot('eflux')

.. image:: _static/solo_swa.png
   :align: center
   :class: imgborder




Energetic Particle Detector (EPD)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.solo.epd

Example
^^^^^^^^^

.. code-block:: python
   
   import pyspedas
   from pyspedas import tplot
   epd_vars = pyspedas.projects.solo.epd(trange=['2020-06-01', '2020-06-02'], datatype='step', mode='rates')
   tplot(['Magnet_Flux', 'Integral_Flux'])

.. image:: _static/solo_epd.png
   :align: center
   :class: imgborder




Radio and Plasma Waves (RPW)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.solo.rpw

Example
^^^^^^^^^

.. code-block:: python
   
   import pyspedas
   from pyspedas import tplot
   rpw_vars = pyspedas.projects.solo.rpw(trange=['2020-06-15', '2020-06-16'], datatype='hfr-surv')
   tplot(['AVERAGE_NR', 'TEMPERATURE', 'FLUX_DENSITY1', 'FLUX_DENSITY2'])

.. image:: _static/solo_rpw.png
   :align: center
   :class: imgborder



