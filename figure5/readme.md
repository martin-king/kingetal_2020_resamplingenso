Figure caption: Each panel is the Taylor diagram for a permutation test corresponding to the analysis in the respective panel in Fig. 4. The gray thicker arc also corresponds to the one spanned by 5th to 95-th percentiles in each respective panel in Fig. 4. See last part of Sect. 3.a for more details.

1. Run `cdo_sel.py` to produce `ensomerge_djf_perm_long.nc`, etc.
2. Use `write_fortaylor.gs` with GRADS to produce `ensomerge_atm_djf_fortaylor_perm_long.txt`.
3. Redo steps 1. and 2. for JF and ND.
4. Use `plottaylor.m` to plot the Taylor diagrams

## Input data (as in Fig. 1):

prmsl.mon.mean_djfmean.nc

prmsl.mon.mean_janfebmean.nc

prmsl.mon.mean_novdecmean.nc

## Output data (the txt files are also provided here):

elninovarmerge_djf_perm_long.nc

elninovarmerge_jf_perm_long.nc

elninovarmerge_nd_perm_long.nc

ensomerge_djf_perm_long.nc

ensomerge_jf_perm_long.nc

ensomerge_nd_perm_long.nc

laninavarmerge_djf_perm_long.nc

laninavarmerge_jf_perm_long.nc

laninavarmerge_nd_perm_long.nc

ensomerge_atm_djf_fortaylor_perm_long.txt

ensomerge_atm_jf_fortaylor_perm_long.txt

ensomerge_atm_nd_fortaylor_perm_long.txt

## Scripts and other files:

cdo_sel.py

write_fortaylor.gs

plottaylor.m

startup.m

elninovarmerge_atm_djf_perm_long.ctl

elninovarmerge_atm_jf_perm_long.ctl

elninovarmerge_atm_nd_perm_long.ctl

ensomerge_atm_djf_perm_long.ctl

ensomerge_atm_jf_perm_long.ctl

ensomerge_atm_nd_perm_long.ctl

laninavarmerge_atm_djf_perm_long.ctl

laninavarmerge_atm_jf_perm_long.ctl

laninavarmerge_atm_nd_perm_long.ctl
