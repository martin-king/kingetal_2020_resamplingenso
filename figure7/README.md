Note: Same Fig. 8 except for ND.

Figure caption: Lower and upper limits of confidence intervals (at 95%) for ND El Niño and La Niña SLP composites corresponding to Fig. 6a, b. 
The ordt, perc, and bootT intervals are described in Sect. 3.3. Contour interval is 0.5 hPa, with red (blue) contours indicating positive 
(negative) anomalies. Gray shading indicates locations where the SLP anomalies have the same sign within the entire interval.

1. Use `plotstandarderror.gs` to plot column 1, for ordt.
2. Use `plot_cont.gs` to plot column 2, for perc.
3. Use `writeboott.gs` to produce elninoBootTmerge_atm_nd.nc and laninaBootTmerge_atm_nd.nc. Then change them to 
elninoBootTmerge_atm_nd_timevaries.nc and laninaBootTmerge_atm_nd_timevaries.nc. Then use cdo to produce elninoBootTmerge_atm_nd_timevaries_025pctl.nc, 
elninoBootTmerge_atm_nd_timevaries_975pctl.nc, laninaBootTmerge_atm_nd_timevaries_025pctl.nc, laninaBootTmerge_atm_nd_timevaries_975pctl.nc.
4. Use `plotboott.gs`to plot coloum 3, for bootT.

## Input data:

elninovarmerge_nd_elnino.nc

elninomerge_nd.nc

laninavarmerge_nd_lanina.nc

laninamerge_nd.nc

elninomerge_atm_nd_timevaries_025pctl.nc

elninomerge_atm_nd_timevaries_975pctl.nc

laninamerge_atm_nd_timevaries_025pctl.nc

laninamerge_atm_nd_timevaries_975pctl.nc

elninomerge_atm_nd_timevaries.nc

laninamerge_atm_nd_timevaries.nc

## Output data:
elninoBootTmerge_atm_nd.nc

laninaBootTmerge_atm_nd.nc

elninoBootTmerge_atm_nd_timevaries.nc

laninaBootTmerge_atm_nd_timevaries.nc

elninoBootTmerge_atm_nd_timevaries_025pctl.nc

elninoBootTmerge_atm_nd_timevaries_975pctl.nc

laninaBootTmerge_atm_nd_timevaries_025pctl.nc

laninaBootTmerge_atm_nd_timevaries_975pctl.nc

## Scripts and other files:

plotstandarderrro.gs

elninovarmerge_atm_nd.ctl

elninomerge_atm_nd.ctl

laninavarmerge_atm_nd.ctl

laninamerge_atm_nd.ctl

elninovarmerge_atm_nd_elnino.ctl

laninavarmerge_atm_nd_lanina.ctl

elninomerge_atm_nd_sfctimeswitched.ctl

laninamerge_atm_nd_sfctimeswitched.ctl

plot_cont.gs

writeboott.gs

plotboott.gs

fig07.png
