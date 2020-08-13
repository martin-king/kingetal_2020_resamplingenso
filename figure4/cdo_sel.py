import numpy as np

np.random.seed(None)

trialtot=range(1,2002)

# >= 1 SD
#NDJ/DJ. years here are for DJF or JF 18 events 
#elninoyears=np.array([1926,1931,1941,1942,1958,1964,1966,1973,1978,1983,1987,1988,1992,1995,1998,2003,2007,2010])
#NDJ/DJ. years here are for DJF or JF 16 events 
#laninayears=np.array([1925,1934,1943,1950,1951,1956,1971,1974,1976,1985,1989,1999,2000,2008,2011,2012])

#NDJ/DJ. years here are for DJF or JF 26 events long elninoyears=np.array([1878,1889,1897,1900,1903,1906,1912,1919,1926,1931,1941,1942,1958, \
#                      1964,1966,1973,1978,1983,1987,1988,1992,1995,1998,2003,2007,2010])
#NDJ/DJ. years here are for DJF or JF 22 events long laninayears=np.array([1887,1890,1893,1894,1910,1917,1925,1934,1943,1950,1951,1956,1971, \
#                      1974,1976,1985,1989,1999,2000,2008,2011,2012])

#NDJ/DJ. years here are for DJF or JF 47 events neutral elninoyears=np.array([1872,1881,1882,1884,1888,1892,1898,1902,1907,1908,1913,1916,1920,1921,1923, \
#                                                   1927,1928,1929,1932,1933,1935,1937,1938,1944,1945,1947,1948,1949,1953,1954,1959,1960, \
#                                                   1961,1962,1963,1967,1979,1981,1982,1990,1991,1993,1994,2002,2004,2013,2014])                                                            
#NDJ/DJ. years here are for DJF or JF 47 events neutral laninayears=np.array([1872,1881,1882,1884,1888,1892,1898,1902,1907,1908,1913,1916,1920,1921,1923, \
#                      1927,1928,1929,1932,1933,1935,1937,1938,1944,1945,1947,1948,1949,1953,1954,1959,1960, \
#                      1961,1962,1963,1967,1979,1981,1982,1990,1991,1993,1994,2002,2004,2013,2014]) 
         

#ON. years here are for ND 18 events elninoyears=np.array([1923,1925,1930,1941,1957,1963,1965,1972,1977,1982,1986,1987,1991,1994,1997,2002,2006,2009])
#ON. years here are for ND 17 events laninayears=np.array([1933,1942,1949,1950,1954,1955,1964,1973,1975,1983,1984,1988,1998,1999,2007,2010,2011])

#ON. years here are for ND 25 events long 
elninoyears=np.array([1877,1885,1888,1896,1899,1902,1905,1918,1923,1925,1930,1941,1957,1963,1965,1972, \
                      1977,1982,1986,1987,1991,1994,1997,2002,2009])
#ON. years here are for ND 23 events long 
laninayears=np.array([1874,1886,1889,1892,1893,1909,1916,1933,1942,1949,1950,1955,1964,1973,1975,1983, \
                      1984,1988,1998,1999,2007,2010,2011])

#ON. years here are for ND 37 events neutral 
#laninayears=np.array([1920,1922,1926,1927,1928,1931,1932,1934,1935,1937,1939,1943,1944,1946,1947,1948, \
#                      1952,1953,1958,1959,1960,1961,1962,1966,1967,1978,1980,1981,1989,1990,1992,1993,1996,2001,2005,2012,2013])
#ON. years here are for ND 82 events neutral laninayears=np.array([1870,1871,1872,1873,1875,1876,1878,1880,1881,1882,1883,1884,1887,1891,1894,1895,1897,1898,1900,1901,1903,1906, \
#                      1907,1908,1910,1912,1914,1915,1917,1919,1920,1921,1922,1924,1926,1927,1928,1929,1931,1932,1934,1935,1936,1937, \
#                      1938,1939,1943,1944,1945,1945,1946,1947,1948,1952,1953,1958,1959,1960,1961,1962,1966,1967,1968,1978,1979,1980, \
#                      1981,1985,1989,1990,1992,1993,1996,2001,2003,2004,2005,2008,2012,2013,2014])    

concyears=np.concatenate((elninoyears,laninayears))

for trial in trialtot:
   if trial !=1:
#    el = np.random.choice(elninoyears, size=elninoyears.shape, replace=True)
#    el = np.random.choice(elninoyears, size=15, replace=True)
#    el = elninoyears
    co=np.random.choice(concyears, size=concyears.shape, replace=False)
    el=co[0:25]
    el = sorted(el)
#    elyears=','.join(str(ee) for ee in el)   
#    la = np.random.choice(laninayears, size=laninayears.shape, replace=True)
#    la = np.random.choice(laninayears, size=15, replace=True)
#    la = laninayears
    la=co[25:48]
    la = sorted(la)
#    layears=','.join(str(ll) for ll in la)
   else:
    el = elninoyears
    la = laninayears
#    el = elninoyears[6:13]
#    la = laninayears[8:14]
#    el = elninoyears[0:6]
#    la = laninayears[0:8]

#el and la then contain the bootstrapped years  
#   if (trial==1) or (trial==2): 
   count=1
   print "rm -f rub*.nc"
   for year in el:
#    print "cdo -O selyear,"+str(year)+" HadISST_sst_djfmean_setrtoc_setmisstoc_1920_2017.nc rub"+str(count)+".nc"
    print "cdo -s -O selyear,"+str(year)+" prmsl.mon.mean_novdecmean.nc rub"+str(count)+".nc"
    count+=1
   print "cdo -O ensmean rub*.nc elnino.nc"
   print "cdo -O ensvar rub*.nc elninovar.nc"
#   print "cdo -O merge rub*.nc elninos.nc"
   
#   if (trial==1) or (trial==2):
   count=1
   print "rm -f rub*.nc"
   for year in la:
#     print "cdo -O selyear,"+str(year)+" HadISST_sst_djfmean_setrtoc_setmisstoc_1920_2017.nc rub"+str(count)+".nc"
    print "cdo -s -O selyear,"+str(year)+" prmsl.mon.mean_novdecmean.nc rub"+str(count)+".nc"
    count+=1
   print "cdo -O ensmean rub*.nc lanina.nc"
   print "cdo -O ensvar rub*.nc laninavar.nc"
#   print "cdo -O merge rub*.nc laninas.nc"
    
#ensocomp.nc contains enso anomaly for one trial
   print "cdo -O sub elnino.nc lanina.nc ensocomp.nc"

#then I want to put all those anomalies together
   if trial==1:
    print "mv ensocomp.nc ensomerge_nd_perm_long.nc" ##
##
    print "mv elninovar.nc elninovarmerge_nd_perm_long.nc" ##
    print "mv laninavar.nc laninavarmerge_nd_perm_long.nc" ##
   else:
    print "cdo -O merge ensocomp.nc ensomerge_nd_perm_long.nc ensomergenew.nc" ##
    print "mv ensomergenew.nc ensomerge_nd_perm_long.nc" ##
##
    print "cdo -O merge elninovar.nc elninovarmerge_nd_perm_long.nc elninovarmergenew.nc" ##
    print "mv elninovarmergenew.nc elninovarmerge_nd_perm_long.nc" ##
##
    print "cdo -O merge laninavar.nc laninavarmerge_nd_perm_long.nc laninavarmergenew.nc" ##
    print "mv laninavarmergenew.nc laninavarmerge_nd_perm_long.nc" ##
   