Figure caption: Top row: SLP composites for El Nino minus La Nina events in the months shown during 1870–
2014. The ENSO events are selected for Nino3.4 amplitudes greater than 1 standard deviation. CI in (a) and
(b) is 2 hPa, and is 1 hPa in (c). Gray shading indicates 5% confidence level for two-tailed t test. Second row: 
Corresponding Taylor diagrams analyzed for North Atlantic with 2000 bootstrap SLP composites. The blue, green, and 
red semi-circles indicate respectively the 5th, median, and 95th percentiles of the amplitude ratios. 
Blue, green, and red straight lines indicate respectively the 5th, median, and 95th percentiles of the spatial
correlations with observation. See Sect. 3.a for more details.

1. The steps and scripts used here are similar to Figures 1 and 2. Rerun `cdo_sel.py` with the longer periods (more ENSO events). This produces `ensomerge_djf_long.nc` needed for input in step 4.
2. Use `plotcomp.gs` in GRADS to plot the observed composite.
3. Repeat 1. and 2. for JF and ND as well.
4. Use `write_fortaylor.gs` in GRADS to produce the txt files needed by `plottaylor.m` in Matlab to plot the Taylor diagrams.

## Input data (as in Fig. 1):

prmsl.mon.mean_djfmean.nc

prmsl.mon.mean_janfebmean.nc

prmsl.mon.mean_novdecmean.nc

## Output data (txt files provided also here as their sizes are small):

ensomerge_atm_djf_fortaylor_2ndrun_long.txt

ensomerge_atm_jf_fortaylor_2ndrun_long.txt

ensomerge_atm_nd_fortaylor_2ndrun_long.txt

elninovarmerge_djf_long.nc

ensomerge_djf_long.nc

laninavarmerge_djf_long.nc

elninovarmerge_jf_long.nc

ensomerge_jf_long.nc

laninavarmerge_jf_long.nc

elninovarmerge_nd_long.nc

ensomerge_nd_long.nc

laninavarmerge_nd_long.nc

## Scripts and other files (same as Figs. 1 and 2 together):

cdo_sel.py

plotcomp.gs

polst.gs

write_fortaylor.gs

plottaylor.m

startup.m

elninovarmerge_atm_djf_long.ctl

ensomerge_atm_djf_long.ctl

laninavarmerge_atm_djf_long.ctl

elninovarmerge_atm_jf_long.ctl

ensomerge_atm_jf_long.ctl

laninavarmerge_atm_jf_long.ctl

elninovarmerge_atm_nd_long.ctl

ensomerge_atm_nd_long.ctl

laninavarmerge_atm_nd_long.ctl

