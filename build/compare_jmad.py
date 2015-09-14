import os

from pyoptics import *

jmad="/home/rdemaria/work/acc-co/trunk/accmodel/jmad/models/accmodel-jmad-models-lhc/src/java/cern/accsoft/steering/jmad/modeldefs/defs/repdata/2015/V6.503/strength/"

fnames="""\
IR1/ir1_1000.madx
IR1/ir1_11000.madx
IR1/ir1_1200.madx
IR1/ir1_1500.madx
IR1/ir1_1600.madx
IR1/ir1_2000.madx
IR1/ir1_2500.madx
IR1/ir1_3000.madx
IR1/ir1_4000.madx
IR1/ir1_400.madx
IR1/ir1_450.madx
IR1/ir1_500.madx
IR1/ir1_520.madx
IR1/ir1_550.madx
IR1/ir1_600.madx
IR1/ir1_650.madx
IR1/ir1_7000.madx
IR1/ir1_700.madx
IR1/ir1_800.madx
IR1/ir1_9000.madx
IR1/ir1_900.madx
IR1/betahigh/ir1_12600.madx
IR1/betahigh/ir1_14500.madx
IR1/betahigh/ir1_16700.madx
IR1/betahigh/ir1_19200.madx
IR1/betahigh/ir1_22000.madx
IR1/betahigh/ir1_25000.madx
IR1/betahigh/ir1_30000.madx
IR1/betahigh/ir1_33000.madx
IR1/betahigh/ir1_36000.madx
IR1/betahigh/ir1_40000.madx
IR1/betahigh/ir1_43000.madx
IR1/betahigh/ir1_46000.madx
IR1/betahigh/ir1_51000.madx
IR1/betahigh/ir1_54000.madx
IR1/betahigh/ir1_60000.madx
IR1/betahigh/ir1_67000.madx
IR1/betahigh/ir1_75000.madx
IR1/betahigh/v2/ir1_90000.madx
IR5/betahigh/ir5_12600.madx
IR5/betahigh/ir5_14500.madx
IR5/betahigh/ir5_16700.madx
IR5/betahigh/ir5_19200.madx
IR5/betahigh/ir5_22000.madx
IR5/betahigh/ir5_25000.madx
IR5/betahigh/ir5_30000.madx
IR5/betahigh/ir5_33000.madx
IR5/betahigh/ir5_36000.madx
IR5/betahigh/ir5_40000.madx
IR5/betahigh/ir5_43000.madx
IR5/betahigh/ir5_46000.madx
IR5/betahigh/ir5_51000.madx
IR5/betahigh/ir5_54000.madx
IR5/betahigh/ir5_60000.madx
IR5/betahigh/ir5_67000.madx
IR5/betahigh/ir5_75000.madx
IR5/betahigh/v2/ir5_90000.madx
IR5/ir5_1000.madx
IR5/ir5_11000.madx
IR5/ir5_1200.madx
IR5/ir5_1500.madx
IR5/ir5_1600.madx
IR5/ir5_2000.madx
IR5/ir5_2500.madx
IR5/ir5_3000.madx
IR5/ir5_4000.madx
IR5/ir5_400.madx
IR5/ir5_450.madx
IR5/ir5_500.madx
IR5/ir5_520.madx
IR5/ir5_550.madx
IR5/ir5_600.madx
IR5/ir5_650.madx
IR5/ir5_7000.madx
IR5/ir5_700.madx
IR5/ir5_800.madx
IR5/ir5_9000.madx
IR5/ir5_900.madx
IR8/ir8_3000_875.madx
IR8/ir8_3250_876.madx
IR8/ir8_3500_877.madx
IR8/ir8_4000_880.madx
IR8/ir8_5000_886.madx
IR8/ir8_6000_895.madx
IR8/ir8_7000_906.madx
IR8/ir8_7500_912.madx
IR8/ir8_8000_919.madx
IR8/ir8_9000_934.madx
IR8/betamed/ir8_12500_934.madx
IR8/betamed/ir8_14500_921.madx
IR8/betamed/ir8_16500_907.madx
IR8/betamed/ir8_17000_904.madx
IR8/betamed/ir8_18000_897.madx
IR8/betamed/ir8_19000_890.madx
IR8/betamed/ir8_20000_883.madx
IR8/betamed/ir8_21000_877.madx
IR8/betamed/ir8_22000_870.madx
IR8/betamed/ir8_24000_856.madx
IR8/betamed/ir8_26000_843.madx
IR8/betamed/ir8_27000_836.madx
IR8/betamed/ir8_28000_829.madx
IR8/betamed/ir8_30000_816.madx"""

import sys

sys.path.append('/home/rdemaria/work/lhc_2015/2015/toolkit/')

from pyoptics import madlang
from compare_opt import compare_optics

def set_crossing(t):
    for irn in '1258':
        for kn in 'sep x o a':
            setattr(t,'on_%s%s'%(kn,irn),1)


for fn in fnames.split('\n'):
    bn=os.path.basename(fn)
    irn=bn[2]
    ofn="IR%s/%s"%(irn,bn)
    jfn="%s/%s"%(jmad,fn)
    print jfn
    print ofn
    t1=madlang.open(ofn)
    t2=madlang.open(jfn)
    compare_optics(t1,t2,1.00001,1e-12)







