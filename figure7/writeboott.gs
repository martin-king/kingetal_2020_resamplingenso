function writeboott

*bootT
*open elninomerge_atm_jf.ctl	
*open elninovarmerge_atm_jf_elnino.ctl

'set z 1'
'set x 1 180'
'set y 1 91'

'bootmean=ave(prmsl.1,z=1,z=2000)'
'set z 1 2000'
****
't=(prmsl.1-bootmean)*sqrt(23)/sqrt(prmsl.2)'

'set sdfwrite laninaBootTmerge_atm_nd.nc'

'sdfwrite t'

return


