Caption: Taylor diagrams analyzed for North Atlantic with 2000 bootstrap SLP composites for El Nino minus La Nin ̃a events in the months shown during 1920–2012. The blue, green, and red semi-circles indicate respectively the 5th, median, and 95th percentiles of the amplitude ratios. Blue, green, and red straight lines indicate respectively the 5th, median, and 95th percentiles of the spatial correlations with observation. Second and third rows: Corresponding 5th- and 95th-percentile bootstrap SLP composites based on both amplitudes and spatial correlations. See Sect. 3.a for more details. CI is 2 hPa. Gray shading indicates 5% confidence level for two-tailed t test.

1. To plot the Taylor diagram: Open the previously created file `ensomerge_djf.nc` in GRADS, use `write_fortaylor.gs` to produce `ensomerge_atm_djf_fortaylor_2ndrun.txt` for the North Atlantic sector.
2. Use plottaylor.m in Matlab to plot the Taylor diagram.
3. Repeat 1. and 2. to produce JF and ND Taylor diagrams.
4. The 5th and 95th percentiles panels are found with the help of the Taylor diagrams and the *.txt files from 1. to identify which samples are at these levels, then plotted using plotcomp.gs like for Figure 1.

## Input data:

ensomerge_djf.nc

ensomerge_jf.nc

ensomerge_nd.nc

## Output data:

ensomerge_atm_djf_fortaylor_2ndrun.txt

ensomerge_atm_jf_fortaylor_2ndrun.txt

ensomerge_atm_nd_fortaylor_2ndrun.txt

## Scripts and other files:

write_fortaylor.gs

plottaylor.m

startup.m
