import numpy as np
import matplotlib.pyplot as plt

read = open("PS1_PS1MD_PSc420122_snana_dat.txt", 'r')


ts = []
fluxes = []
flux_errs = []
ts_to_plot = []
fluxes_to_plot = []
mag_to_plot = []

mag = [] #i'm calculating this out for each flux
i = 0
for line in read:
    if i > 0:
        d = line.split()
        

        time = float(d[1])
        flux = float(d[4])
        flux_err = float(d[5])

        ts.append(time)
        fluxes.append(flux)
        flux_errs.append(flux_err)
        
        if flux > 3*flux_err:
            ts_to_plot.append(time)
            fluxes_to_plot.append(flux)
            #m-M = 5log(d/10)
            # =
            mag_to_plot.append(-2.5*np.log10(flux) + 27.5)
        
        
        if flux > 0:
            mag.append(2.5*np.log10(flux) - 27.5)
    else:
        i+=1

    pass
plt.scatter(ts_to_plot, mag_to_plot)
plt.show()
    