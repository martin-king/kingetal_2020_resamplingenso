Figure caption: Top row: SLP composites for El Nin ̃o or La Nin ̃a events in the months shown during 1870–2014. CI is 1 hPa for JF and 0.5 hPa for ND. Gray shading indicates 5 percent confidence level for two-tailed t test. Second row: Corresponding Taylor diagrams analyzed for North Atlantic with 2000 bootstrap SLP composites.

1. Run `cdo_sel_elninoorlanina.py` to produce `elninomerge_jf.nc` and `elninovarmerge_jf_elnino.nc`.
2. Modify `cdo_sel_elninoorlanina.py` for La Nina.
3. Repeat 1. and 2. for ND.
4. Run `write_fortaylor.gs` to produce `elninomerge_atm_jf_fortaylor.txt`, etc.
5. Use `plotcomp.gs` and `plottaylor.m` for plotting. 

## Input data

prmsl.mon.mean_janfebmean.nc

prmsl.mon.mean_janfebmean_noelninos_mean_mulc0_841.nc

prmsl.mon.mean_janfebmean_nolaninas_mean_mulc0_865.nc

prmsl.mon.mean_novdecmean.nc

prmsl.mon.mean_novdecmean_noelninos_mean_mulc0_847.nc

prmsl.mon.mean_novdecmean_nolaninas_mean_mulc0_859.nc

## Output data

elninomerge_jf.nc

elninovarmerge_jf_elnino.nc

laninamerge_jf.nc

laninavarmerge_jf_lanina.nc

elninomerge_nd.nc

elninovarmerge_nd_elnino.nc

laninamerge_nd.nc

laninavarmerge_jf_lanina.nc

elninomerge_atm_jf_fortaylor.txt

laninamerge_atm_jf_fortaylor.txt

elninomerge_atm_nd_fortaylor.txt

laninamerge_atm_nd_fortaylor.txt

## Scripts and other files

cdo_sel_elninoorlanina.py

write_fortaylor.gs

plottaylor.m

startup.m

plotcomp.gs
