import numpy as np

np.random.seed(None)

trialtot=range(1,2002)

# >= 1 SD
#NDJ/DJ. years here are for jan/feb 26 events long 
elninoyears=np.array([1878,1889,1897,1900,1903,1906,1912,1919,1926,1931,1941,1942,1958, \
                      1964,1966,1973,1978,1983,1987,1988,1992,1995,1998,2003,2007,2010])
#NDJ/DJ. years here are for jan/feb 22 events long elninoyears=np.array([1887,1890,1893,1894,1910,1917,1925,1934,1943,1950,1951,1956,1971, \
#                      1974,1976,1985,1989,1999,2000,2008,2011,2012])        
#ON. years here are for nov/dec 25 events long elninoyears=np.array([1877,1885,1888,1896,1899,1902,1905,1918,1923,1925,1930,1941,1957,1963,1965,1972, \
#                      1977,1982,1986,1987,1991,1994,1997,2002,2009])
#ON. years here are for nov/dec 23 events long elninoyears=np.array([1874,1886,1889,1892,1893,1909,1916,1933,1942,1949,1950,1955,1964,1973,1975,1983, \
#                      1984,1988,1998,1999,2007,2010,2011])

for trial in trialtot:
   if trial !=1:
    el = np.random.choice(elninoyears, size=elninoyears.shape, replace=True)
    el = sorted(el)
#    elyears=','.join(str(ee) for ee in el)
   else:
    el = elninoyears

#el then contain the bootstrapped years  
   count=1
   print "rm -f rub*.nc"
   for year in el:
    print "cdo -s -O selyear,"+str(year)+" prmsl.mon.mean_novdecmean.nc rub"+str(count)+".nc" ##
    count+=1
   print "cdo -s -O ensmean rub*.nc rubsum.nc"
# SLP_anom = SLP_EL - SUM(SLP_n/EL)/n - SUM(SLP_EL)/n, n=164
# jf elnino 26/164=0.158536
   print "cdo -O mulc,0.158536 rubsum.nc rubsummulc.nc" ##
# jf lanina 22/164=0.134146 print "cdo -s -O mulc,0.134146 rubsum.nc rubsummulc.nc" ##
# nd elnino 25/164=0.152439 print "cdo -O mulc,0.152439 rubsum.nc rubsummulc.nc" ##
# nd lanina 23/164=0.140244 print "cdo -O mulc,0.140244 rubsum.nc rubsummulc.nc" ##

   count=1
   for year in el:
#138/164=0.84146, 142/164=0.86585, 139/164=0.84756, 141/164=0.85976.      
    print "cdo -s -O sub rub"+str(count)+".nc prmsl.mon.mean_janfebmean_noelninos_mean_mulc0_841.nc rubtmp.nc" ##
    print "cdo -s -O sub rubtmp.nc rubsummulc.nc rubrub"+str(count)+".nc"   
    count+=1

   print "cdo -s -O ensmean rubrub*.nc elnino.nc" ##
   print "cdo -s -O ensvar rubrub*.nc elninovar.nc" ##
   
#then I want to put all those anomalies together
   if trial==1:
    print "mv elnino.nc elninomerge_jf.nc" ##
    print "mv elninovar.nc elninovarmerge_jf_elnino.nc" ##
   else:
    print "cdo -O merge elnino.nc elninomerge_jf.nc elninomergenew.nc" ##
    print "mv elninomergenew.nc elninomerge_jf.nc" ##
##
    print "cdo -O merge elninovar.nc elninovarmerge_jf_elnino.nc elninovarmergenew.nc" ##
    print "mv elninovarmergenew.nc elninovarmerge_jf_elnino.nc" ##
##   
