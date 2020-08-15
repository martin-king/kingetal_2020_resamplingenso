import numpy as np

np.random.seed(None)

trialtot=range(1,2002)

# >= 1 SD
#NDJ/DJ. years here are for jan 26 events long elninoyears=np.array([1878,1889,1897,1900,1903,1906,1912,1919,1926,1931,1941,1942,1958, \
#                      1964,1966,1973,1978,1983,1987,1988,1992,1995,1998,2003,2007,2010])
#NDJ/DJ. years here are for jan 22 events long elninoyears=np.array([1887,1890,1893,1894,1910,1917,1925,1934,1943,1950,1951,1956,1971, \
#                      1974,1976,1985,1989,1999,2000,2008,2011,2012])        
#ON. years here are for oct 25 events long elninoyears=np.array([1877,1885,1888,1896,1899,1902,1905,1918,1923,1925,1930,1941,1957,1963,1965,1972, \
#                      1977,1982,1986,1987,1991,1994,1997,2002,2009])
#ON. years here are for oct 23 events long 
elninoyears=np.array([1874,1886,1889,1892,1893,1909,1916,1933,1942,1949,1950,1955,1964,1973,1975,1983, \
                      1984,1988,1998,1999,2007,2010,2011])
#
#DJ. years here are for jan EP El Nino elninoyears=np.array([1952,1953,1964,1966,1970,1973,1977,1998])  
#DJ. years here are for jan EP La Nina elninoyears=np.array([1955,1956,1965,1968,1972,1985,1996,2006])
#DJ. years here are for jan CP El Nino elninoyears=np.array([1954,1958,1969,1978,1980,1987,2003,2005,2010])  
#DJ. years here are for jan CP La Nina elninoyears=np.array([1974,1975,1976,1989,1999,2001,2011,2012]) 
#ND. years here are for oct EP El Nino elninoyears=np.array([1951,1952,1963,1965,1969,1972,1976,1997]) 
#ND. years here are for oct EP La Nina elninoyears=np.array([1954,1955,1964,1967,1971,1984,1995,2005])
#ND. years here are for oct CP El Nino elninoyears=np.array([1953,1957,1968,1977,1979,1986,2002,2004,2009]) 
#ND. years here are for oct CP La Nina elninoyears=np.array([1973,1974,1975,1988,1998,2000,2010,2011])

#elninoyears=np.concatenate((elninoyearso,laninayearso))

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
# jf elnino  print "cdo -O mulc,0.158536 rubsum.nc rubsummulc.nc" ##
# jf lanina  print "cdo -s -O mulc,0.134146 rubsum.nc rubsummulc.nc" ##
# nd elnino  print "cdo -O mulc,0.152439 rubsum.nc rubsummulc.nc" ##
# nd lanina  
   print "cdo -O mulc,0.140244 rubsum.nc rubsummulc.nc" ##
# jf/nd ep el nino, ep la nina, cp lanina print "cdo -O mulc,0.04878 rubsum.nc rubsummulc.nc" ##
# jf/nd cp el nino print "cdo -O mulc,0.05488 rubsum.nc rubsummulc.nc"
   count=1
   for year in el:
    print "cdo -s -O sub rub"+str(count)+".nc prmsl.mon.mean_novdecmean_nolaninas_mean_mulc0_859.nc rubtmp.nc" ##
    print "cdo -s -O sub rubtmp.nc rubsummulc.nc rubrub"+str(count)+".nc"   
    count+=1

   print "cdo -s -O ensmean rubrub*.nc lanina.nc" ##
   print "cdo -s -O ensvar rubrub*.nc laninavar.nc" ##
#   print "cdo -O merge rubrub*.nc laninas.nc"
#   print "grads -pbc forzscorr.gs"
   
#then I want to put all those anomalies together
   if trial==1:
    print "mv lanina.nc laninamerge_nd.nc" ##
    print "mv laninavar.nc laninavarmerge_nd_lanina.nc" ##
   else:
    print "cdo -O merge lanina.nc laninamerge_nd.nc laninamergenew.nc" ##
    print "mv laninamergenew.nc laninamerge_nd.nc" ##
##
    print "cdo -O merge laninavar.nc laninavarmerge_nd_lanina.nc laninavarmergenew.nc" ##
    print "mv laninavarmergenew.nc laninavarmerge_nd_lanina.nc" ##
##   