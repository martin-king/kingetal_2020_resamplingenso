function writefortaylor

'reset'

zmax=2001
z=1
*this line is VERY IMPORTANT to define the area available
'set lon -180 180'
*north pac 'set lon 0 360'

'set z 'zmax

*'meancomp=ave(prmsl,z=1,z=100)'
*djf 'magmeancomp=sqrt(atot(pow(meancomp,2),lon=-60,lon=0,lat=30,lat=70))'
*jf 'magmeancomp=sqrt(atot(pow(meancomp,2),lon=-60,lon=0,lat=30,lat=70))'
*nd 'magmeancomp=sqrt(atot(pow(meancomp,2),lon=-50,lon=10,lat=20,lat=60))'
*north pac. 'magmeancomp=sqrt(atot(pow(meancomp,2),lon=150,lon=240,lat=30,lat=60))'

'obscomp=prmsl'
*djf 
'magobscomp=sqrt(atot(pow(prmsl,2),lon=-60,lon=0,lat=30,lat=70))'
*jf 'magobscomp=sqrt(atot(pow(prmsl,2),lon=-60,lon=0,lat=30,lat=70))'
*nd 'magobscomp=sqrt(atot(pow(prmsl,2),lon=-50,lon=10,lat=20,lat=60))'
*north pac. 'magobscomp=sqrt(atot(pow(prmsl,2),lon=150,lon=240,lat=30,lat=60))'
*arctic 'magobscomp=sqrt(atot(pow(prmsl,2),lon=-180,lon=180,lat=80,lat=90))'
*jf nonsym 'magobscomp=sqrt(atot(pow(prmsl,2),lon=-40,lon=20,lat=30,lat=75))'

while (z<=zmax)
   'set z 'z
*djf 
'cosalpha=scorr(prmsl,obscomp,lon=-60,lon=0,lat=30,lat=70)'
*jf 'cosalpha=scorr(prmsl,obscomp,lon=-60,lon=0,lat=30,lat=70)'
*nd 'cosalpha=scorr(prmsl,obscomp,lon=-50,lon=10,lat=20,lat=60)'
*north pac. 'cosalpha=scorr(prmsl,obscomp,lon=150,lon=240,lat=30,lat=60)'
*arctic 'cosalpha=scorr(prmsl,obscomp,lon=-180,lon=180,lat=80,lat=90)'
*jf nonsym 'cosalpha=scorr(prmsl,obscomp,lon=-40,lon=20,lat=30,lat=75)'

*djf 
'magcomp=sqrt(atot(pow(prmsl,2),lon=-60,lon=0,lat=30,lat=70))'
*jf 'magcomp=sqrt(atot(pow(prmsl,2),lon=-60,lon=0,lat=30,lat=70))'
*nd 'magcomp=sqrt(atot(pow(prmsl,2),lon=-50,lon=10,lat=20,lat=60))'
*north pac. 'magcomp=sqrt(atot(pow(prmsl,2),lon=150,lon=240,lat=30,lat=60))'
*arctic 'magcomp=sqrt(atot(pow(prmsl,2),lon=-180,lon=180,lat=80,lat=90))'
*jf nonsym 'magcomp=sqrt(atot(pow(prmsl,2),lon=-40,lon=20,lat=30,lat=75))'
   'a=magcomp/magobscomp'

   'd cosalpha'
   line=sublin(result,1)
   val2=subwrd(line,4)

   'd a'
   line=sublin(result,1)
   val1=subwrd(line,4)

   cad=val1'       'val2
   rc=write('ensomerge_atm_djf_fortaylor_2ndrun_long.txt',cad,append)

   z=z+1
endwhile

return
 
  
 
