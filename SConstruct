from rsf.proj import *
import rsf.api as api

# Fetch Files from repository
modelFiles=['vp_marmousi-ii.segy','vs_marmousi-ii.segy',
             'density_marmousi-ii.segy']

outputFiles=['vp.rsf','vs.rsf','density.rsf']

for file in modelFiles:
    Fetch(file,"marm2")

# Convert model Files to RSF
for infile, outfile in zip(modelFiles, outputFiles):
    Flow(outfile, infile, ''' segyread tape=$SOURCE
    tfile=/dev/null hfile=/dev/null bfile=/dev/null | put
         d1=1.25 d2=1.25 o1=0 o2=0 label1=Depth label2=Distance
         unit1=m unit2=m |
         scale rscale=1000''')


# Convert stack data to rsf, extract a trace at 4000
Flow("seismic", "Kirchhoff_PreSTM_time.segy",
     ''' segyread tape=$SOURCE
tfile=/dev/null hfile=/dev/null bfile=/dev/null | put
d1=0.002 d2=6.25 o1=0 o2=0 label1=TWT label2=Distance
unit1=s unit2=m | window min2=4000 n2=1''')

# Convert vp, vs, rho into time and extract a well log
for f in outputFiles:
    logfile = 'log_' + f
    Flow(logfile, f,
         '''depth2time velocity=vp.rsf dt=0.002 |
    window min2=4000 n2=1''')

Flow(["rpp.npy", "seismic.npy"],
     ["log_vp.rsf", "log_vs.rsf", "log_density.rsf"],
     "python ref_and_convert.py ${SOURCES} ${TARGETS}" ,
     stdin=0, stdout=-1)







         

