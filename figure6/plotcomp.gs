function plotcomp

*example
*open ensomerge_atm_jf.ctl
*open elninovarmerge_atm_jf.ctl
*open laninavarmerge_atm_jf.ctl

'reset'
'set vpage 0 11 0 6.5'
'set xlopts 1 10 0.29'
'set ylopts 1 10 0.29'

zmax=2001
z=2001

while (z<=zmax)

'clear'
'set z 'z
'/Users/martin/mbp1rsync.dir/work_2016dec.dir/martinking_temporary.dir/Desktop/work_sep2016.dir/scripts/polst.gs 10 n'
*NA 'set lon -90 30'
*NA 'set lat 10 90'
*'set lon 120 240'   
*'set lat 10 90'

'set rgb 58  45  30 165'
'set rgb 28 192   0   0'

'set display color white'
'set grads off'
'set ylint 20'
'set xlint 30'
*'set grid on 5 1'
'set grid off'
'set mpdraw on'
'set rgb 17 80 80 80'
'set map 17 1 7'
'set clopts -1 -1 0.15'

'tstat2d=abs(prmsl.1)/sqrt(prmsl.2/26+prmsl.3/22)'
*'tstat2d=abs(prmsl.1)/sqrt(prmsl.2/23)'
'set gxout shaded'
'set rgb 16 200 200 200'
'set rbcols 16'
'set cmin 0'
'd tstat2d-2.1'

'set gxout contour'
'set clskip 2'
'set cint 0.5'
'set cmax -0.1'
*'set ccolor 1'
'set ccolor 58'
'set cstyle 2'
'set cthick 6'
'd prmsl.1/100'
*
'set cint 0.5'
'set cmin 0.1'
*'set ccolor 1'
'set ccolor 28'
'set cstyle 1'
'set cthick 6'
'd prmsl.1/100'
*
*'set clevs 0'
*'set ccolor 1'
*'set cstyle 1'
*'set cthick 10'
*'d prmsl.1/100'

*'gxprint ensocompboot_nd_'z'.png'

z=z+1

endwhile

return
