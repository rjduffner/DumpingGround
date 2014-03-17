from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

#
# TLE
# ISS
# Courtesy of http://celestrak.com
#
line1 = ('1 10674U 78018A   14074.06685253 -.00000059  00000-0 -12180-4 0  9995')
line2 = ('2 10674  69.3617 277.9244 0166662 289.9030 234.8639 13.43567065769518')


satellite = twoline2rv(line1, line2, wgs72)
print dir(satellite)

# 12:50:19 on 29 June 2000
# position, velocity = satellite.propagate(2000, 6, 29, 12, 50, 19)
#
position, velocity = satellite.propagate(2014, 3, 15, 21, 47, 30)
print satellite.propagate(2014, 3, 15, 21, 47, 30)

print position
#[5576.056952400586, -3999.371134576452, -1521.9571594376037]
print velocity
#[4.772627303379319, 5.119817120959591, 4.275553909172126]
