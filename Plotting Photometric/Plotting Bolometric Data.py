import numpy as np
import matplotlib.pyplot as plt

read = open("PS1_PS1MD_PSc420122_snana_dat.txt", 'r')




flux_errs = {}
ts_to_plot = {}
fluxes_to_plot = {}
mag_to_plot = {}

all_filts = []

mag = [] #i'm calculating this out for each flux
i = 0
for line in read:
    if i > 0:
        d = line.split()
        
        
        time = float(d[1])
        flux = float(d[4])
        flux_err = float(d[5])
        filt = d[2]
        
        if all_filts.count(filt) == 0:
            all_filts.append(filt)
            
            flux_errs[filt] = []
            fluxes_to_plot[filt] = []
            ts_to_plot[filt] = []
            mag_to_plot[filt] = []
        


        
        if flux > 3*flux_err:
            flux_errs[filt].append(flux_err)
            fluxes_to_plot[filt].append(flux)
            ts_to_plot[filt].append(time)
            mag_to_plot[filt].append(-2.5*np.log10(flux) + 27.5)
        
        
    else:
        i+=1

    pass

plt.gca().invert_yaxis()
for k in all_filts:
    plt.scatter(ts_to_plot[k], mag_to_plot[k], label="Filter: "+str(k))

plt.legend()
plt.xlabel("Time (MJD)")
plt.ylabel("Apparent Magnitude")
plt.show()
    