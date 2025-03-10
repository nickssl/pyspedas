Electron Losses and Fields Investigation (ELFIN)
==============================================================================
The routines in this module can be used to load data from the Electron Losses and Fields Investigation (ELFIN) mission.


Fluxgate magnetometer (FGM)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.elfin.fgm

Example
^^^^^^^^^

.. code-block:: python

   import pyspedas
   from pyspedas import tplot
   fgm_vars = pyspedas.projects.elfin.fgm(probe='a', trange=['2022-08-19', '2022-08-19'])
   tplot(['ela_fgs_fsp_res_ndw', 'ela_fgs_fsp_res_obw'])




Energetic Particle Detector (EPD)
----------------------------------------------------------
.. autofunction:: pyspedas.projects.elfin.epd

Example
^^^^^^^^^

.. code-block:: python

   import pyspedas
   from pyspedas import tplot
   elf_vars = pyspedas.projects.elfin.epd(probe='a', trange=['2019-08-19', '2022-08-19'], level='l2')
   tplot(['ela_pef_fs_Epat_nflux', 'ela_pef_hs_Epat_nflux'. 'ela_pef_pa', ela_pef_tspin'])




Magnetic Field sensor XYZ data collected by IDPU (MRMI)
-------------------------------------------------------------------------
.. autofunction:: pyspedas.projects.elfin.mrmi

Example
^^^^^^^^^

.. code-block:: python

   import pyspedas
   from pyspedas import tplot
   mrmi_vars = pyspedas.projects.elfin.mrmi(probe='b', trange=['2022-08-19', '2022-08-19']
   tplot('elb_mrmi')




Magnetic Field sensor XYZ data collected by Attitude Control Board (MRMA)
-------------------------------------------------------------------------
.. autofunction:: pyspedas.projects.elfin.mrma

Example
^^^^^^^^^

.. code-block:: python

   import pyspedas
   from pyspedas import tplot
   mrma_vars = pyspedas.projects.elfin.mrma(probe='a', trange=['2022-08-19', '2022-08-19'])
   tplot('ela_mrma')




State data
----------------------------------------------------------
.. autofunction:: pyspedas.projects.elfin.state

Example
^^^^^^^^^

.. code-block:: python

   import pyspedas
   from pyspedas import tplot
   state_vars = pyspedas.projects.elfin.state(probe='a', trange=['2022-08-19', '2022-08-19'])
   tplot(['ela_pos_gei', 'ela_att_gei', 'ela_att_spinper', 'ela_spin_sun_angle' ])





