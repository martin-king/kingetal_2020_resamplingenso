Note: Same Fig. 7 except for JF.

Figure caption: Lower and upper limits of confidence intervals (at 95%) for JF El Niño and La Niña SLP composites corresponding to Fig. 6c, d. The ordt, perc, and bootT intervals are described in Sect. 3.3. Contour interval is 1 hPa, with red (blue) contours indicating positive (negative) anomalies. Gray shading indicates locations where the SLP anomalies have the same sign within the entire interval.

1. Use `plotstandarderror.gs` to plot column 1, for ordt.
2. Use `plot_cont.gs` to plot column 2, for perc.
3. Use `writeboott.gs` to produce elninoBootTmerge_atm_jf.nc and laninaBootTmerge_atm_jf.nc. Then change them to 
elninoBootTmerge_atm_jf_timevaries.nc and laninaBootTmerge_atm_jf_timevaries.nc. Then use cdo to produce elninoBootTmerge_atm_jf_timevaries_025pctl.nc, 
elninoBootTmerge_atm_jf_timevaries_975pctl.nc, laninaBootTmerge_atm_jf_timevaries_025pctl.nc, laninaBootTmerge_atm_jf_timevaries_975pctl.nc.
4. Use `plotboott.gs`to plot coloum 3, for bootT.

## Input data:

elninovarmerge_jf_elnino.nc

elninomerge_jf.nc

laninavarmerge_jf_lanina.nc

laninamerge_jf.nc

elninomerge_atm_jf_timevaries_025pctl.nc

elninomerge_atm_jf_timevaries_975pctl.nc

laninamerge_atm_jf_timevaries_025pctl.nc

laninamerge_atm_jf_timevaries_975pctl.nc

elninomerge_atm_jf_timevaries.nc

laninamerge_atm_jf_timevaries.nc

## Output data:

elninoBootTmerge_atm_jf.nc

laninaBootTmerge_atm_jf.nc

elninoBootTmerge_atm_jf_timevaries.nc

laninaBootTmerge_atm_jf_timevaries.nc

elninoBootTmerge_atm_jf_timevaries_025pctl.nc

elninoBootTmerge_atm_jf_timevaries_975pctl.nc

laninaBootTmerge_atm_jf_timevaries_025pctl.nc

laninaBootTmerge_atm_jf_timevaries_975pctl.nc

## Scripts and other files:

plotstandarderrror.gs

elninovarmerge_atm_jf.ctl

elninomerge_atm_jf.ctl

laninavarmerge_atm_jf.ctl

laninamerge_atm_jf.ctl

elninovarmerge_atm_jf_elnino.ctl

laninavarmerge_atm_jf_lanina.ctl

elninomerge_atm_jf_sfctimeswitched.ctl

laninamerge_atm_jf_sfctimeswitched.ctl

plot_cont.gs

writeboott.gs

plotboott.gs

fig08.png
