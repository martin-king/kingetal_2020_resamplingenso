function plotstanderr

*ordt
*example
*open elninovarmerge_atm_jf_elnino.ctl
*open elninomerge_atm_jf.ctl

'reset'
'set vpage 0 11 0 6.5'
'set xlopts 1 10 0.29'
'set ylopts 1 10 0.29'

z=2001
'clear'

'set z 'z
'/Users/martin/mbp1rsync.dir/work_2016dec.dir/martinking_temporary.dir/Desktop/work_sep2016.dir/scripts/polst.gs 10 n'

'set display color white'
'set grads off'
'set ylint 20'
'set xlint 30'
*'set grid on 5 1'
'set grid off'
'set mpdraw on'
'set rgb 17 140 140 140'
'set map 17 1 7'
'set clopts -1 -1 0.12'


****
'standerror2d=sqrt(prmsl.1/22)/100'
'sign1=prmsl.2(z=2001)/100+2.07*standerror2d'
'sign2=prmsl.2(z=2001)/100-2.07*standerror2d'



*'set gxout contour'
*'set cint 1'
*'set ccolor 1'
*'set cstyle 1'
*'set cthick 6'
*'d standerror2d'

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
*'set clopts -1 -1 0.12'
'set clab off'

'set gxout shaded'
'set rgb 16 170 170 170'
'set rbcols 16'
*'set cmin 0'
*'d sign1*sign2'
'd maskout(sign1*sign2,sign1*sign2)'

'set gxout contour'
'set clskip 1'
'set cint 1.0'
'set cmax -0.2'
*'set ccolor 1'
'set ccolor 58'
'set cstyle 2'
'set cthick 6'
'd prmsl.2(z=2001)/100-2.07*standerror2d'
*
'set cint 1.0'
'set cmin 0.2'
*'set ccolor 1'
'set ccolor 28'
'set cstyle 1'
'set cthick 6'
'd prmsl.2(z=2001)/100-2.07*standerror2d'
*
'set clevs 0'
'set ccolor 1'
'set cstyle 1'
'set cthick 10'
'set clab on'
'set clopts -1 -1 0.16'
'd prmsl.2(z=2001)/100-2.07*standerror2d'


return
