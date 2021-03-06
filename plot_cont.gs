function plotcont

*just plotting dash and solid contours
*sdfopen elninomerge_atm_jf_timevaries_025pctl.nc
*sdfopen elninomerge_atm_jf_timevaries_975pctl.nc

'reset'
'set vpage 0 11 0 6.5'
'set xlopts 1 10 0.29'
'set ylopts 1 10 0.29'

'/Users/martin/mbp1rsync.dir/work_2016dec.dir/martinking_temporary.dir/Desktop/work_sep2016.dir/scripts/polst.gs 10 n'

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
'set clopts -1 -1 0.12'
'set clab off'

'set gxout shaded'
'set rgb 16 170 170 170'
'set rbcols 16'
*'set cmin 0'
*'d sign1*sign2'
'd maskout(prmslo.1*prmslo.2,prmslo.1*prmslo.2)'

'set gxout contour'
'set clskip 1'
'set cint 1.0'
'set cmax -0.2'
*'set ccolor 1'
'set ccolor 58'
'set cstyle 2'
'set cthick 6'
'd prmslo.1/100'
*
'set cint 1.0'
'set cmin 0.2'
*'set ccolor 1'
'set ccolor 28'
'set cstyle 1'
'set cthick 6'
'd prmslo.1/100'
*
'set clevs 0'
'set ccolor 1'
'set cstyle 1'
'set cthick 10'
'set clab on'
'set clopts -1 -1 0.16'
'd prmslo.1/100'

return
