import ru_local as ru
dist_miles = 16637000000
dist_km = dist_miles * 1609
dist_astro = dist_miles * 1076 * 0.00000001
Speedperday = 38241 * 24
signalSpeed = 299792458 * 2.237
n = int(input(ru.DAYS))
res_miles = dist_miles + n * Speedperday
res_km = dist_km + n * Speedperday
res_astro = dist_astro + n * Speedperday
print(ru.DIST_MILES, res_miles)
print(ru.DIST_KM, res_km)
print(ru.DIST_ASTRO, res_astro)
print(ru.DELAYSPEED, res_miles/signalSpeed)