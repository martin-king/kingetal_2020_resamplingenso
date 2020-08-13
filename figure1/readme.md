Figure caption: Sea level pressure (SLP) composites for El Nino minus La Nina events in the months shown on the panels during 1920–2012. The ENSO events are selected for Nino3.4 amplitudes greater than 1 standard deviation. Contour interval (CI) in (a) and (b) is 2 hPa, and is 1 hPa in (c). Gray shading indicates 5% confidence level for two-tailed t test. All analyses in this paper use data from HadSST and NOAA-CIRES 20CR V2c.

1. The Python script cdo_sel.py is used for calculating DJF bootstraps and produces these files: 
ensomerge_djf.nc, elninovarmerge_djf.nc, laninavarmerge_djf.nc
2. Use the GRADS control files ensomerge_atm_djf.ctl, elninovarmerge_atm_djf.ctl and laninavarmerge_atm_djf.ctl to open and 
plot the outputs from 1. in GRADS. A typical plotting script is plotcomp.gs. The original (ie non resampled) composite is stored 
in the last step (level 2001) in my case here.
3. Edit cdo_sel.py and repeat steps 1 and 2 to obtain and plot the JF and ND composites.

Input data:
prmsl.mon.mean_djfmean.nc
prmsl.mon.mean_janfebmean.nc
prmsl.mon.mean_novdecmean.nc

Output data:
ensomerge_djf.nc
elninovarmerge_djf.nc
laninavarmerge_djf.nc
-
ensomerge_jf.nc
elninovarmerge_djf.nc
laninavarmerge_jf.nc
-
ensomerge_nd.nc
elninovarmerge_nd.nc
laninavarmerge_nd.nc
