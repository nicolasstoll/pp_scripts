

#%%

if 0:                                 
    rotation_list = [
                    ['216_1', 0],
                    ['216_2', 0],
                    ['216_3', 0],
                    ['216_4', 0],
                    ['216_5', 0],
                    ['216_6', 0],
                    ['225_1', 0],
                    ['225_2', 0],
                    ['225_3', 0],
                    ['225_4', 0],
                    ['225_5', 0],
                    ['225_6', 0],
                    ['242_2', 0],
                    ['243_3', -30],
                    ['244_1', -30],
                    ['245_1', 0],
                    ['246_1', 0],
                    ['247_1', 0],
                    ['252_1', 0],
                    ['252_2', 0],
                    ['252_3', 0],
                    ['252_4', 0],
                    ['252_5', 0],
                    ['252_6', 0],
                    ['253_1', 0],
                    ['253_2', 0],
                    ['253_3', 0],
                    ['253_4', 0],
                    ['253_5', 0],
                    ['266_1', -25],
                    ['266_2', -25],
                    ['266_3', -25],
                    ['266_4', -25],
                    ['266_5', -30],
                    ['266_6', -25],
                    ['293_1', -45],
                    ['293_2', -45],
                    ['293_3', -45],
                    ['293_4', -55],
                    ['293_5', -45],
                    ['293_6', -65],
                    ['294_1', -60],
                    ['294_2', -60],
                    ['294_3', -60],
                    ['294_4', -60],
                    ['294_5', -50],
                    ['294_6', -60],
                    ['296_1', -10],
                    ['296_2', -10],
                    ['296_3', -10],
                    ['296_4', -10],
                    ['296_5', -10],
                    ['296_6', -10],
                    ['300_1', 40],
                    ['300_2', 40],
                    ['300_3', 40],
                    ['300_4', 40],
                    ['300_5', 40],
                    ['300_6', 40],
                    ['301_1', 45],
                    ['301_2', 45],
                    ['301_3', 45],
                    ['301_4', 45],
                    ['301_5', 45],
                    ['301_6', 45],
                    ['327_1', 30],
                    ['327_2', 30],
                    ['327_3', 30],
                    ['327_4', 30],
                    ['327_5', 30],
                    ['327_6', 30],
                    ['346_1', -2],
                    ['346_2', -2],
                    ['346_3', -2],
                    ['346_4', -2],
                    ['346_5', -2],
                    ['346_6', -2],
                    ['356_1', 15],
                    ['356_2', 15],
                    ['356_3', 15],
                    ['356_4', 15],
                    ['356_5', 15],
                    ['356_6', 15],
                    ['375_1', -65],
                    ['375_2', -65],
                    ['375_3', -65],
                    ['375_4', -125],
                    ['375_5', -65],
                    ['375_6', -65],
                    ['387_1', -5],
                    ['387_2', -5],
                    ['387_3', -5],
                    ['387_4', -5],
                    ['387_5', -5],
                    ['387_6', -5],
                    ['415_1', -25],
                    ['415_2', -25],
                    ['415_3', -25],
                    ['415_4', -25],
                    ['415_5', -25],
                    ['415_6', -25],
                    ['416_1', -10],
                    ['416_2', -10],
                    ['416_3', -10],
                    ['416_4', -10],
                    ['416_5', -10],
                    ['416_6', -10],
                    ['427_1', 5],
                    ['427_2', 5],
                    ['427_3', 5],
                    ['427_4', 5],
                    ['427_5', 5],
                    ['427_6', 5],
                    ['432_1', -75],
                    ['434_1', 55],
                    ['436_1', 50],
                    ['438_1', -45],
                    ['438_2', -45],
                    ['438_3', -45],
                    ['438_4', -45],
                    ['438_5', -45],
                    ['438_6', -45],
                    ['440_1', -50],
                    ['440_2', -50],
                    ['440_3', -50],
                    ['440_4', -50],
                    ['440_5', -50],
                    ['440_6', -50],
                    ['442_1', -50],
                    ['444_1', -5],
                    ['446_2', 50],
                    ['448_1', 50],
                    ['450_1', 55],
                    ['452_1', 90],
                    ['455_1', -60],
                    ['455_2', -60],
                    ['455_3', -60],
                    ['455_4', -60],
                    ['455_5', -60],
                    ['455_6', -60],
                    ['477_1', 40],
                    ['477_2', 40],
                    ['477_3', 40],
                    ['477_4', 40],
                    ['477_6', 40],
                    ['486_1', 0],
                    ['486_2', 0],
                    ['486_3', 0],
                    ['486_4', 0],
                    ['486_5', 0],
                    ['486_6', 0],
                    ['495_1', -60],
                    ['495_2', -60],
                    ['495_3', -60],
                    ['495_4', -60],
                    ['495_5', -60],
                    ['495_6', -60],
                    ['504_1', -5],
                    ['504_2', -5],
                    ['504_3', -5],
                    ['504_4', -5],
                    ['504_5', -5],
                    ['504_6', -5],
                    ['505_1', -5],
                    ['505_2', -5],
                    ['505_3', -5],
                    ['505_4', -5],
                    ['505_5', -5],
                    ['505_6', -5],
                    ['526_1', 25],
                    ['526_2', 25],
                    ['526_3', 25],
                    ['526_4', 25],
                    ['526_5', 25],
                    ['526_6', 25],
                    ['535_1', 90],
                    ['535_2', 90],
                    ['535_3', 90],
                    ['535_4', 90],
                    ['535_5', 90],
                    ['535_6', 90],
                    ['550_1', 30],
                    ['550_2', 30],
                    ['550_3', 30],
                    ['550_4', 30],
                    ['550_5', 30],
                    ['550_6', 30],
                    ['551_1', -15],
                    ['551_2', -15],
                    ['551_3', -15],
                    ['551_4', -15],
                    ['551_5', -15],
                    ['551_6', -15],
                    ['566_1', -20],
                    ['566_2', -20],
                    ['566_3', -20],
                    ['566_4', -20],
                    ['566_5', -20],
                    ['566_6', -20],
                    ['582_1', 65],
                    ['582_2', 65],
                    ['582_3', 65],
                    ['582_4', 65],
                    ['582_5', 65],
                    ['582_6', 65],
                    ['583_1', 70],
                    ['583_2', 70],
                    ['583_3', 70],
                    ['583_4', 70],
                    ['583_5', 70],
                    ['583_6', 70],
                    ['596_1', -45],
                    ['596_2', -45],
                    ['596_3', -45],
                    ['596_4', -45],
                    ['596_5', -45],
                    ['596_6', -45],
                    ['597_1', -45],
                    ['597_2', -45],
                    ['597_3', -45],
                    ['597_4', -45],
                    ['597_5', -45],
                    ['597_6', -45],
                    ['616_1', 0],
                    ['616_2', 0],
                    ['616_3', 0],
                    ['616_4', 0],
                    ['616_5', 0],
                    ['616_6', 0],
                    ['636_1', 75],
                    ['636_2', 75],
                    ['636_3', 75],
                    ['636_4', 75],
                    ['636_5', 75],
                    ['636_6', 75],
                    ['646_1', 15],
                    ['646_2', 15],
                    ['646_3', 15],
                    ['646_4', 15],
                    ['646_5', 15],
                    ['646_6', 15],
                    ['657_1', -25],
                    ['657_2', -25],
                    ['657_3', -25],
                    ['657_4', -25],
                    ['657_6', -25],
                    ['666_1', -70],
                    ['666_2', -70],
                    ['666_3', -70],
                    ['666_4', -70],
                    ['666_5', -70],
                    ['666_6', -70],
                    ['686_1', -45],
                    ['686_2', -45],
                    ['686_3', -45],
                    ['686_4', -45],
                    ['686_5', -45],
                    ['686_6', -45],
                    ['724_1', 75],
                    ['724_2', 75],
                    ['724_3', 75],
                    ['724_4', 75],
                    ['724_5', 75],
                    ['724_6', 75],
                    ['756_1', -5],
                    ['756_2', -5],
                    ['756_3', -5],
                    ['756_4', -5],
                    ['756_5', -5],
                    ['756_6', -5],
                    ['776_1', -65],
                    ['776_2', -65],
                    ['776_3', -65],
                    ['776_4', -65],
                    ['776_5', -65],
                    ['776_6', -65],
                    ['796_1', -65],
                    ['796_2', -10],
                    ['796_3', -10],
                    ['796_4', -10],
                    ['796_5', -10],
                    ['796_6', -10],
                    ['816_1', -25],
                    ['816_2', -25],
                    ['816_3', -25],
                    ['816_4', -25],
                    ['816_5', -25],
                    ['816_6', -25],
                    ['836_2', 50],
                    ['836_3', 50],
                    ['836_4', 50],
                    ['836_5', 50],
                    ['836_6', 50],
                    ['866_1', -40],
                    ['866_2', -40],
                    ['866_3', -40],
                    ['866_4', -40],
                    ['866_5', -40],
                    ['866_6', -40],
                    ['896_1', -60],
                    ['896_2', -60],
                    ['896_3', -60],
                    ['896_4', -60],
                    ['896_5', -60],
                    ['896_6', -60],
                    ['936_1', -30],
                    ['936_2', -30],
                    ['936_3', -30],
                    ['936_4', -30],
                    ['936_5', -30],
                    ['956_1', 5],
                    ['956_2', 5],
                    ['956_3', 5],
                    ['956_4', 5],
                    ['956_5', 5],
                    ['956_6', 5],
                    ['977_1', -55],
                    ['977_2', -55],
                    ['977_3', -55],
                    ['977_4', -55],
                    ['977_5', -55],
                    ['977_6', -55],
                    ['995_1', 70],
                    ['995_2', 70],
                    ['995_3', 70],
                    ['995_4', 70],
                    ['995_5', 70],
                    ['995_6', 70],
                    ['1016_1', 30],
                    ['1016_2', 30],
                    ['1016_3', 30],
                    ['1016_4', 30],
                    ['1016_5', 30],
                    ['1016_6', 30],
                    ['1057_1', -38],
                    ['1057_2', -38],
                    ['1057_3', -38],
                    ['1057_4', -38],
                    ['1057_5', -38],
                    ['1057_6', -38],
                    ['1096_1', 25],
                    ['1096_2', 25],
                    ['1096_3', 25],
                    ['1096_4', 25],
                    ['1096_5', 25],
                    ['1096_6', 25],
                    ['1116_1', -15],
                    ['1116_2', -15],
                    ['1116_3', -15],
                    ['1116_4', -15],
                    ['1116_5', -15],
                    ['1116_6', -15],
                    ['1146_1', 0],
                    ['1146_2', 0],
                    ['1146_3', 0],
                    ['1146_4', 0],
                    ['1146_5', 0],
                    ['1146_6', 0],
                    ['1185_1', -90],
                    ['1185_2', -90],
                    ['1185_3', -90],
                    ['1185_4', -90],
                    ['1185_5', -90],
                    ['1185_6', -90],
                    ['1214_1', 68],
                    ['1214_2', 68],
                    ['1214_3', 68],
                    ['1214_4', 68],
                    ['1214_5', 68],
                    ['1214_6', 68],
                    ['1247_1', -62],
                    ['1247_2', -62],
                    ['1247_3', -62],
                    ['1247_4', -62],
                    ['1247_5', -62],
                    ['1247_6', -62],
                    ['1276_1', -20],
                    ['1276_2', -20],
                    ['1276_3', -20],
                    ['1276_4', -20],
                    ['1276_5', -20],
                    ['1276_6', -20],
                    ['1315_1', 88],
                    ['1315_2', 88],
                    ['1315_3', 88],
                    ['1315_4', 88],
                    ['1315_5', 88],
                    ['1315_6', 88],
                    ['1346_1', 90],
                    ['1346_2', 90],
                    ['1346_3', 90],
                    ['1346_4', 90],
                    ['1346_5', 90],
                    ['1346_6', 90],
                    ['1377_1', -10],
                    ['1377_2', -10],
                    ['1377_3', -10],
                    ['1377_4', -10],
                    ['1377_5', -10],
                    ['1377_6', -10],
                    ['1406_1', -65],
                    ['1406_2', -65],
                    ['1406_3', -65],
                    ['1406_4', -65],
                    ['1406_5', -65],
                    ['1406_6', -65],
                    ['1444_3', -10],
                    ['1444_4', -10],
                    ['1444_5', -10],
                    ['1444_6', -10], 
    #
                  # 
                 #  
                    ['1475_1', -5],
                    ['1475_2', -5],
                    ['1475_3', -5],
                    ['1475_4', -5],
                    ['1475_5', -5],
                    ['1475_6', -5],
                    ['1507_1', 15],
                    ['1507_3', 15],
                    ['1507_4', 15],
                    ['1507_5', 15],
                    ['1507_6', 15],              
                    ['1546_1', 85],
                    ['1546_2', 85],
                    ['1546_3', 85],
                    ['1546_4', 85],
                    ['1546_5', 85],
                    ['1546_6', 85],
                    ['1558_1', -10],
                    ['1558_2', -10],
                    ['1558_3', -10],
                    ['1558_4', -10],
                    ['1558_5', -10],
                    ['1558_6', -10],
                    ['1588_1', 25],
                    #['1588_2', -35], # Problem, Dünnschnitt verdreht
                    ['1588_3', 25],
                    ['1588_4', 25],
                    ['1588_6', 25],                
                    ['1615_1', -90],
                    ['1615_2', -90],
                    ['1615_3', -90],
                    ['1615_4', -90],
                    ['1615_5', -90],
                    ['1615_6', -90],
                    ['1637_1', 10],
                    ['1637_2', 10],
                    ['1637_3', 10],
                    ['1637_4', 10],
                    ['1637_5', 10],
                    ['1637_6', 10],
                    #['1656_1', -40],
                    #['1656_2', -40], # Verschoben
                    ['1656_3', -40],
                    ['1656_4', -40],
                    ['1656_5', -40],
                    ['1656_6', -40],
                    ['1686_1', -85],
                    ['1686_2', -85],
                    ['1686_3', -85],
                    ['1686_4', -85],
                    ['1686_5', -85],
                    ['1686_6', -85],
                    ['1716_1', -75],
                    ['1716_2', -75],
                    ['1716_3', -75],
                    ['1716_4', -75],
                    ['1716_5', -75],
                    ['1716_6', -75],
                    ['1746_1', 10],
                    ['1746_2', 10],
                    ['1746_3', 10],
                    ['1746_4', 10],
                    ['1746_5', 10],
                    ['1746_6', 10],
                    ['1776_1', -80],
                    ['1776_2', -80],
                    ['1776_3', -80],
                    ['1776_4', -80],
                    ['1776_5', -80],
                    ['1776_6', -80],
                    ['1806_1', -50],
                    ['1806_2', -50],
                    ['1806_3', -50],
                    ['1806_4', -50],
                    ['1806_5', -50],
                    ['1806_6', -50],
                    ['1846_1', 25],
                    ['1846_2', 25],
                    ['1846_3', 25],
                    ['1846_4', 25],
                    ['1846_5', 25],
                    ['1846_6', 25],
                    ['1876_1', 50],
                    ['1876_2', 50],
                    ['1876_3', 50],
                    ['1876_4', 50],
                    ['1876_5', 50],
                    ['1876_6', 50],
                    ['1906_1', 55],
                    ['1906_2', 55],
                    ['1906_3', 55],
                    ['1906_4', 55],
                    ['1906_5', 55],
                    ['1906_6', 55],
                    ['1933_1', -80],
                    ['1933_2', -80],
                    ['1933_3', -80],
                    ['1933_4', -80],
                    ['1933_5', -80],
                    ['1933_6', -80],
                    ['1965_1', 55],
                    ['1965_2', 55],
                    ['1965_3', 55],
                    ['1965_4', 55],
                    ['1965_5', 55],
                    ['1965_6', 55],
                    ['1996_1', 55],
                    ['1996_2', 55],
                    ['1996_4', 55],
                    ['1996_5', 55],
                    ['1996_6', 55],
                    ['2026_1', -85],
                    ['2026_2', -85],
                    ['2026_3', -85],
                    ['2026_4', -85],
                    ['2026_5', -85],
                    ['2026_6', -85],
                    ['2056_1', 40],
                    ['2056_2', 40],
                    ['2056_3', 40],
                    ['2056_4', 40],
                    ['2056_5', 40],
                    ['2056_6', 40],
                    ['2075_1', 67],
                    ['2075_2', 67],
                    ['2075_3', 67],
                    ['2075_4', 67],
                    ['2075_5', 67],
                    ['2075_6', 67],
                    ['2106_1', -15],
                    ['2106_2', -15],
                    ['2106_3', -15],
                    ['2106_4', -15],
                    ['2106_5', -15],
                    ['2106_6', -15],
                    ['2136_1', 5],
                    ['2136_2', 5],
                    ['2136_3', 5],
                    ['2136_4', 5],
                    ['2136_5', 5],
                    ['2136_6', 5],
                    ['2156_1', -75],
                    ['2156_2', -75],
                    ['2156_3', -75],
                    ['2156_4', -75],
                    ['2156_5', -75],
                    ['2156_6', -75],
                    ['2176_1', -18],
                    ['2176_2', -18],
                    ['2176_3', -18],
                    ['2176_4', -18],
                    ['2176_5', -18],
                    ['2176_6', -18],
                    ['2206_1', 20],
                    ['2206_2', 20],
                    ['2206_3', 20],
                    ['2206_4', 20],
                    ['2206_5', 20],
                    ['2206_6', 20],
                    ['2236_1', -90],
                    ['2236_2', -90],
                    ['2236_3', -90],
                    ['2236_4', -90],
                    ['2236_5', -90],
                    ['2236_6', -90],
                    ['2256_1', -3],
                    ['2256_2', -3],
                    ['2256_3', -3],
                    ['2256_4', -3],
                    ['2256_5', -3],
                    ['2256_6', -3],
                    ['2286_1', 70],
                    ['2286_2', 70],
                    ['2286_3', 70],
                    ['2286_4', 70],
                    ['2286_5', 70],
                    ['2286_6', 70],
                    ['2316_1', -79],
                    ['2316_2', -79],
                    ['2316_3', -79],
                    ['2316_4', -79],
                    ['2316_5', -79],
                    ['2316_6', -79],
                    ['2356_1', 75],
                    ['2356_2', 75],
                    ['2356_3', 75],
                    ['2356_4', 75],
                    ['2356_5', 75],
                    ['2356_6', 75],
                    ['2386_1', -53],
                    ['2386_2', -53],
                    ['2386_3', -53],
                    ['2386_4', -53],
                    ['2386_5', -53],
                    ['2386_6', -53],
                    ['2416_1', 20],
                    ['2416_2', 20],
                    ['2416_3', 20],
                    ['2416_4', 20],
                    ['2416_5', 20],
                    ['2416_6', 20],
                    ['2436_1', -18],
                    ['2436_2', -18],
                    ['2436_3', -18],
                    ['2436_4', -18],
                    ['2436_5', -18],
                    ['2436_6', -18],
                    ['2446_1', 10],
                    ['2446_2', 10],
                    ['2446_3', 10],
                    ['2446_4', 10],
                    ['2446_5', 10],
                    ['2446_6', 10],
                    ['2475_1', 85],
                    ['2475_2', 85],
                    ['2475_3', 85],
                    ['2475_4', 85],
                    ['2475_5', 85],
                    ['2475_6', 85],
                    ['2486_1', -47],
                    ['2486_2', -47],
                    ['2486_3', -47],
                    ['2486_4', -47],
                    ['2486_5', -47],
                    ['2486_6', -47],
                    ['2498_1', -85],
                    ['2498_2', -85],
                    ['2498_3', -85],
                    ['2498_4', -85],
                    ['2498_5', -85],
                    ['2498_6', -85],
                    ['2506_1', -75],
                    ['2506_2', -75],
                    ['2506_3', -75],
                    ['2506_4', -75],
                    ['2506_5', -75],
                    ['2506_6', -75],
                    ['2532_2', -80],
                    ['2532_3', -80],
                    ['2532_4', -80],
                    ['2532_5', -80],
                    ['2532_6', -80],
                    ['2535_1', 15],
                    ['2535_2', 15],
                    ['2535_3', 15],
                    ['2535_4', 15],
                    ['2535_5', 15],
                    ['2535_6', 15],
                    ['2565_1', -63],
                    ['2565_2', -63],
                    ['2565_3', -63],
                    ['2565_4', -63],
                    ['2565_5', -63],
                    ['2565_6', -63],
                    ['2570_1', 85],
                    ['2570_2', 85],
                    ['2570_3', 85],
                    ['2570_4', 85],
                    ['2570_5', 85],
                    ['2570_6', 85],
                    ['2596_1', -58],
                    ['2596_2', -58],
                    ['2596_3', -58],
                    ['2596_4', -58],
                    ['2596_5', -58],
                    ['2596_6', -58],
                    #['2617_1', -65],
                    ['2617_2', -55],
                    ['2617_3', -55],
                    ['2617_4', -55],
                    ['2617_5', -55],
                    ['2617_6', -55],
                    ['2626_1', 60],
                    ['2626_2', 60],
                    ['2626_3', 60],
                    ['2626_4', 60],
                    ['2626_5', 60],
                    ['2626_6', 60],
                    ['2635_1', -45],
                    ['2635_2', -45],
                    ['2635_3', -45],
                    ['2635_4', -45],
                    ['2635_5', -45],
                    ['2635_6', -45],
                    ['2642_1', -30],
                    ['2642_2', -30],
                    ['2642_3', -30],
                    ['2642_4', -30],
                    ['2642_5', -30],
                    ['2642_6', -30],
                    ['2662_1', 65],
                    ['2662_2', 65],
                    ['2662_3', 65],
                    ['2662_4', 65],
                    ['2662_5', 65],
                    ['2662_6', 65],
                    ['2666_1', 55],
                    ['2666_2', 55],
                    ['2666_3', 55],
                    ['2666_4', 55],
                    ['2666_5', 55],
                    ['2666_6', 55],
                    ['2696_1', 50],
                    ['2696_2', 50],
                    ['2696_3', 50],
                    ['2696_4', 50],
                    ['2696_5', 50],
                    ['2696_6', 50],
                    ['2726_2', 90],
                    ['2726_3', 90],
                    ['2726_4', 90],
                    ['2726_5', 90],
                    ['2726_6', 90],
                    ['2756_1', 88],
                    ['2756_2', 88],
                    ['2756_3', 88],
                    ['2756_4', 88],
                    ['2756_5', 88],
                    ['2756_6', 88],
                    ['2786_1', -55],
                    ['2786_2', -55],
                    ['2786_3', -55],
                    ['2786_4', -55],
                    ['2786_5', -55],
                    ['2786_6', -55],
                    ['2817_1', -15],
                    ['2817_2', -15],
                    ['2817_3', -15],
                    ['2817_4', -15],
                    ['2817_5', -15],
                    ['2817_6', -15],
                    ['2846_1', -85],
                    ['2846_2', -85],
                    ['2846_3', -85],
                    ['2846_4', -85],
                    ['2846_5', -85],
                    ['2846_6', -85],
                    ['2876_1', -60],
                    ['2876_2', -60],
                    ['2876_3', -60],
                    ['2876_4', -60],
                    ['2876_5', -60],
                    ['2876_6', -60],
                    ['2906_1', -65],
                    ['2906_2', -65],
                    ['2906_3', -65],
                    ['2906_4', -65],
                    ['2906_5', -65],
                    ['2906_6', -65],
                    ['2936_1', 85],
                    ['2936_2', 85],
                    ['2936_3', 85],
                    ['2936_4', 85],
                    ['2936_5', 85],
                    ['2936_6', 85],
                    ['2966_1', 70],
                    ['2966_2', 70],
                    ['2966_3', 70],
                    ['2966_4', 70],
                    ['2966_5', 70],
                    ['2966_6', 70],
                    ['2997_1', -3],
                    ['2997_2', -3],
                    ['2997_3', -3],
                    ['2997_4', -3],
                    ['2997_5', -3],
                    ['2997_6', -3],     
                    ['3027_1', -75],
                    ['3027_2', -75],
                    ['3027_3', -75],
                    ['3027_4', -75],
                    ['3027_5', -75],
                    ['3027_6', -75],
                    ['3056_1', 10],
                    ['3056_2', 10],
                    ['3056_3', 10],
                    ['3056_4', 10],
                    ['3056_5', 10],
                    ['3056_6', 10],
                    ['3086_1', -33],
                    ['3086_2', -33],
                    ['3086_3', -33],
                    ['3086_4', -33],
                    ['3086_5', -33],
                    ['3086_6', -33],
                    ['3117_1', 30],
                    ['3117_2', 30],
                    ['3117_3', 30],
                    ['3117_4', 30],
                    ['3117_5', 30],
                    ['3117_6', 30],
                    ['3206_1', 40],
                    ['3206_2', 40],
                    ['3206_3', 40],
                    ['3206_4', 40],
                    ['3206_5', 40],
                    ['3206_6', 40],
                    ['3236_1', 15],
                    ['3236_2', 15],
                    ['3236_3', 15],
                    ['3236_4', 15],
                    ['3236_5', 15],
                    ['3236_6', 15],
                    ['3260_1', -45],
                    ['3260_2', -45],
                    ['3260_3', -45],
                    ['3260_4', -45],
                    ['3260_5', -45],
                    ['3260_6', -45],
                    ['3266_1', -65],
                    ['3266_2', -65],
                    ['3266_3', -65],
                    ['3266_4', -65],
                    ['3266_5', -65],
                    ['3266_6', -65],                
                    ['3273_1', -20],
                    ['3273_2', -20],
                    #['3273_3', -20], # Problem, Probe verkippt
                    ['3273_4', -20],
                    ['3273_5', -20],
                    ['3273_6', -20],               
                    ['3296_1', 85],
                    ['3296_2', 85],
                    ['3296_3', 85],
                    ['3296_4', 85],
                    ['3296_5', 85],
                    ['3296_6', 85],
                    #['3311_1', -60],# verkippt
                    #['3311_2', -60],# verkippt
                    ['3311_4', -63],
                    ['3311_5', -63],
                    ['3311_6', -63],
                    ['3326_1', -73],
                    ['3326_2', -73],
                    ['3326_3', -73],
                    ['3326_4', -73],
                    ['3326_5', -73],
                    ['3326_6', -73],
                    ['3328_5', -73],
                    ['3328_6', -72],
                    ['3356_1', -48],
                    ['3356_2', -48],
                    ['3356_3', -48],
                    ['3356_4', -48],
                    ['3356_5', -48],
                    ['3356_6', -48],
                    ['3386_1', 15],
                    ['3386_2', 15],
                    ['3386_3', 15],
                    ['3386_4', 15],
                    ['3386_5', 15],
                    ['3386_6', 15],
                    ['3417_1', 82],
                    ['3417_2', 82],
                    ['3417_3', 82],
                    ['3417_4', 82],
                    ['3417_5', 82],
                    ['3417_6', 82],
                    ['3446_1', 87],
                    ['3446_2', 87],
                    ['3446_3', 87],
                    ['3446_4', 87],
                    ['3446_5', 87],
                    ['3446_6', 87],
                    ['3476_1', 75],
                    ['3476_2', 75],
                    ['3476_3', 75],
                    ['3476_4', 75],
                    ['3476_5', 75],
                    ['3476_6', 75],
                    ['3516_1', -10],
                    ['3516_3', -10],
                    ['3516_4', -10],
                    ['3516_5', -10],
                    ['3516_6', -10],
                    ['3566_1', 86],
                    ['3566_2', 86],
                    ['3566_3', 86],
                    ['3566_4', 86],
                    ['3566_5', 86],
                    ['3566_6', 86],
                    ['3596_1', 75],
                    ['3596_2', 75],
                    ['3596_3', 75],
                    ['3596_4', 75],
                    ['3596_5', 75],
                    ['3596_6', 75],
                    ['3626_1', 67],
                    ['3626_2', 67],
                    ['3626_3', 67],
                    ['3626_4', 67],
                    ['3626_5', 67],
                    ['3626_6', 67],
                    ['3656_1', 48],
                    ['3656_2', 48],
                    ['3656_3', 48],
                    ['3656_4', 48],
                    ['3656_5', 48],
                    ['3656_6', 48],
                    ['3680_1', 58],
                    ['3680_2', 58],
                    ['3680_3', 58],
                    ['3680_4', 58],
                    ['3680_5', 58],
                    ['3681_1', 60],
                    ['3681_3', 60],
                    ['3681_4', 60],
                    ['3681_5', 60],
                    ['3681_6', 60],
                    ['3685_1', 45],
                    ['3685_2', 45],
                    ['3685_3', 45],
                    ['3685_4', 45],
                    ['3685_5', 45],
                    ['3685_6', 45],
                    ['3693_1', 74],
                    ['3693_2', 74],
                    ['3693_3', 74],
                    ['3693_4', 74],
                    ['3693_5', 74],
                    ['3693_6', 74],
                    ['3704_3', 57],
                    ['3704_4', 62],
                    ['3715_1', 75],
                    ['3715_2', 75],
                    ['3715_3', 75],
                    ['3715_4', 75],
                    ['3715_5', 75],
                    ['3715_6', 75],
                    ['3746_1', 90],
                    ['3746_2', 90],
                    ['3746_3', 90],
                    ['3746_4', 90],
                    ['3746_5', 90],
                    ['3746_6', 90],
                    ['3776_1', 33],
                    ['3776_2', 33],
                    ['3776_3', 33],
                    ['3776_4', 33],
                    ['3776_5', 33],
                    ['3776_6', 33],
                    ['3785_1', 45],
                    ['3785_2', 45],
                    ['3785_3', 45],
                    ['3785_4', 45],
                    ['3785_5', 45],
                    ['3785_6', 45],
                    ['3795_1', 40],
                    ['3795_2', 40],
                    ['3795_3', 40],
                    ['3795_4', 40],
                    ['3795_5', 40],
                    #['3795_6', 40], # zwei probem verdreht
                    ['3806_1', 85],
                    ['3806_2', 85],
                    ['3806_3', 85],
                    ['3806_4', 85],
                    ['3806_5', 85],
                    ['3806_6', 85],
                    ['3836_1', -65],
                    ['3836_2', -65],
                    ['3836_3', -65],
                    ['3836_4', -65],
                    ['3836_5', -65],
                    ['3836_6', -65],
                    ['3856_1', -60],
                    ['3856_2', -60],
                    ['3856_5', -60],
                    ['3856_6', -60]
                    ]

#%%



if 0:
    
    rotationlistpath = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/'
    
    bagsec      = []
    rotation    = []
    
    for i in range(0, len(rotation_list) - 1):
        bagsec_ = rotation_list[i][0]
        rotation_ = rotation_list[i][1]
        
        bagsec.append(bagsec_)
        rotation.append(rotation_)
    
    df_rotation_list = pd.DataFrame(columns=['bag_section', 'rotation'])
    
    df_rotation_list['bag_section']     = bagsec
    df_rotation_list['rotation']        = rotation

    df_rotation_list.to_csv(rotationlistpath + 'rotation_list.csv', sep='\t', index=False)
