"""Capacited Vehicles Routing Problem (CVRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = [
        [0,97.02712,21.90485,82.05967,122.1025,60.07478,90.52579,103.4613,33.16941,111.412,90.23111,124.7541,63.02401,36.77473,109.9125,96.48365,84.67543,40.11067,45.78483,105.5005,123.0871,118.8979,81.76785,50.60423,107.3807,24.29323,38.93087,81.62723,88.30458,86.87041,126.764,90.07877,51.10377,63.2271,89.80429,90.84604,103.7983,60.47843,67.38408,25.00595,120.1383,31.89615,44.87163,82.61001,69.77193,44.32212,89.64681,112.0695,71.72084,67.731,36.78691],

[97.02712,0,111.9029,178.8647,195.0776,125.287,147.0205,154.1319,64.15302,195.7593,105.6602,197.1508,153.0387,65.6878,98.32492,106.3613,178.4707,56.93823,126.1575,183.7746,207.5105,186.9888,155.8319,104.4418,75.81753,120.2578,101.887,25.04671,185.3208,145.7317,210.5897,177.4728,57.01545,160.0847,186.61,101.8617,154.7559,37.36293,69.3623,75.16679,198.3763,96.61155,141.851,178.528,163.7723,76.5557,182.0634,76.25698,168.4592,164.6596,127.5161],

[21.90485,111.9029,0,68.70206,100.2289,41.25805,105.5959,84.69234,50.95893,114.3241,111.3829,102.8901,42.55132,46.81468,105.1764,117.7887,81.21861,56.65401,24.33345,83.61352,125.4202,97.29045,60.09487,70.15448,129.0791,26.83359,58.38659,93.16337,76.28988,101.6,129.2942,69.13407,71.66595,54.56203,80.15304,112.2432,84.95741,77.3166,68.10396,45.66038,98.28336,52.26159,36.95828,75.83765,67.1124,45.20886,87.50037,133.7068,58.33508,58.3182,16.04237],


[82.05967,178.8647,68.70206,0,91.96328,84.4697,114.0238,112.7381,115.2282,80.28373,147.0722,94.52311,40.88304,115.1434,165.1339,154.0466,39.60429,122.0951,66.87091,73.57504,87.15092,97.8421,73.38864,104.9591,179.5995,60.84731,96.68147,161.565,9.129211,109.8063,90.88749,46.97326,130.8423,23.44097,18.60815,149.9248,112.5728,142.5381,134.8333,105.9601,81.54279,95.8601,38.36816,26.48888,38.48785,113.0699,46.84838,184.7153,10.43468,19.1322,55.497],


[122.1025,195.0776,100.2289,91.96328,0,70.22184,194.2255,52.06387,146.2546,172.1203,210.7849,2.791003,66.27528,133.5628,131.9569,217.385,131.0483,149.6473,76.67832,19.16367,179.0806,12.54308,41.04857,168.1048,228.3516,117.5663,156.6915,171.0454,99.14869,189.8916,182.7855,45.36572,169.2876,105.7371,109.833,211.9916,51.44142,168.2244,128.5763,144.4199,13.3955,151.5722,105.2609,118.1902,125.9798,118.8766,138.5291,232.767,91.03834,104.3125,87.06455],


[60.07478,125.287,41.25805,84.4697,70.22184,0,146.775,43.55941,77.702,148.6688,149.941,72.4642,44.07533,63.55704,81.68504,155.9884,110.7778,80.25673,20.73152,58.68936,158.8751,63.56698,30.66386,110.4729,160.9027,67.01409,98.70844,101.7846,93.53991,142.7409,162.8301,58.36288,101.246,81.03677,101.1574,150.2338,43.85869,98.18305,61.76258,78.12943,73.13448,91.94157,68.41493,101.7394,98.86882,48.79477,118.0551,165.0295,76.15748,83.01244,37.87449],


[90.52579,147.0205,105.5959,114.0238,194.2255,146.775,0,189.8987,100.1186,66.34549,53.74071,197.0147,127.9973,117.0062,197.2709,58.83312,81.23121,106.2111,127.9181,175.2282,75.37149,195.2398,159.6533,45.98837,100.0352,80.26751,54.61376,146.0104,112.6315,4.343731,76.87055,151.2753,92.06924,92.44674,105.0209,58.46975,190.1177,115.145,152.2248,88.74105,187.4677,62.54839,88.98056,92.04007,75.86182,131.6307,77.96366,104.7387,109.0479,95.6787,111.8997],


[103.4613,154.1319,84.69234,112.7381,52.06387,43.55941,189.8987,0,117.3514,185.974,192.8096,52.83469,73.52236,100.5237,80.3567,198.6856,145.925,118.4172,62.11361,53.78765,195.2686,40.10087,39.40951,153.9741,200.3056,109.7367,142.2227,129.1837,121.6608,185.8056,199.2079,71.40481,140.9114,116.4074,131.1328,192.8669,0.671863,133.6515,84.90688,119.7787,62.32874,135.3572,107.4574,135.0079,136.0376,82.56087,153.5367,204.082,107.0244,117.1597,78.83373],


[33.16941,64.15302,50.95893,115.2282,146.2546,77.702,100.1186,117.3514,0,136.3874,80.41464,148.7213,93.49404,19.30796,99.08659,85.17451,115.0395,7.575177,70.56217,131.5459,148.2475,140.9175,105.2152,54.19633,83.2995,56.11137,46.37369,51.39878,121.3834,97.45235,151.6456,119.7926,23.63642,95.95075,122.4611,79.25538,117.8328,27.31089,53.65772,12.53813,146.4483,38.97585,77.78398,114.4835,100.2034,37.86126,119.137,87.34856,104.8891,100.5451,66.99924],


[111.412,195.7593,114.3241,80.28373,172.1203,148.6688,66.34549,185.974,136.3874,0,118.5464,174.7152,113.0653,147.2448,219.158,124.3003,41.20936,143.8485,127.9732,153.4691,11.86054,177.2986,148.394,93.06911,163.3184,89.21205,93.89374,187.6281,74.0148,64.09487,15.36923,126.851,138.861,69.66546,63.43753,123.0403,185.9592,159.4299,178.6127,123.8865,161.8182,99.34804,80.30692,53.93013,50.04108,155.2692,33.62437,168.2964,81.66457,69.49033,111.0788],


[90.23111,105.6602,111.3829,147.0722,210.7849,149.941,53.74071,192.8096,80.41464,118.5464,0,213.5112,146.8787,99.72114,177.6921,6.980258,123.4319,83.30009,135.6964,193.1079,128.3975,208.5989,171.3927,43.4583,46.57909,94.4277,54.29082,112.1824,148.5848,54.9787,130.1787,173.4835,61.43747,123.6442,143.619,4.812744,193.1963,82.51006,132.933,74.06669,207.1506,59.26611,112.6324,131.1588,113.331,118.0887,122.5267,51.12867,139.2843,127.9875,123.7222],


[124.7541,197.1508,102.8901,94.52311,2.791003,72.4642,197.0147,52.83469,148.7213,174.7152,213.5112,0,69.06624,135.8825,132.9611,220.1048,133.6663,152.052,79.27676,21.92298,181.6158,12.81551,43.55124,170.8545,230.9094,120.3372,159.4323,173.0467,101.6389,192.6806,185.3116,48.01968,171.796,108.4606,112.3315,214.7042,52.20005,170.5433,130.4084,146.9882,14.98506,154.2903,108.0488,120.7863,128.687,121.0423,141.1345,235.3115,93.70653,107.0075,89.79488],


[63.02401,153.0387,42.55132,40.88304,66.27528,44.07533,127.9973,73.52236,93.49404,113.0653,146.8787,69.06624,0,87.35182,125.5594,153.6725,72.5313,98.99886,29.2482,47.437,121.9725,67.67573,35.33753,103.5679,169.9875,52.5009,92.61776,132.5576,50.012,123.6688,125.8953,27.19403,113.9111,43.44877,58.50595,148.5631,73.44197,119.5536,99.57261,87.77709,60.63785,88.52349,39.14608,61.49478,63.67399,80.17084,80.17825,174.78,33.76602,43.75892,26.54891],


[36.77473,65.6878,46.81468,115.1434,133.5628,63.55704,117.0062,100.5237,19.30796,147.2448,99.72114,135.8825,87.35182,0,80.65601,104.4378,121.3994,18.07721,60.89599,120.3522,159.0242,127.0912,92.95397,71.61551,99.92576,60.97938,62.45299,46.42586,122.3118,114.0423,162.6126,112.0293,41.29685,98.60246,125.0399,98.5229,101.0442,34.66178,35.29428,28.43663,135.1991,54.59169,80.14721,118.7782,106.5106,18.90481,126.4213,103.5986,104.7173,102.8689,62.04243],


[109.9125,98.32492,105.1764,165.1339,131.9569,81.68504,197.2709,80.3567,99.08659,219.158,177.6921,132.9611,125.5594,80.65601,0,181.5034,185.9232,94.80005,98.33935,129.5803,230.4277,120.352,105.318,152.2291,165.8488,130.0668,142.6691,75.79552,174.0375,194.1271,234.2699,138.0653,116.3412,157.6019,180.6622,175.7391,81.01362,97.58633,45.45097,109.0816,140.8629,134.7251,141.4681,179.0779,172.1648,66.02766,192.478,167.9617,156.0663,160.5436,112.188],


[96.48365,106.3613,117.7887,154.0466,217.385,155.9884,58.83312,198.6856,85.17451,124.3003,6.980258,220.1048,153.6725,104.4378,181.5034,0,130.1576,87.61281,142.0744,199.7866,133.9313,215.0563,177.8488,50.35391,42.88159,101.2545,61.0574,114.3767,155.5298,60.40233,135.5957,180.3276,65.17796,130.6201,150.5056,5.924905,199.0828,85.36573,137.0658,79.48417,213.8766,65.81573,119.5863,138.0139,120.1984,122.9903,129.1275,47.08697,146.2644,134.9589,130.338],


[84.67543,178.4707,81.21861,39.60429,131.0483,110.7778,81.23121,145.925,115.0395,41.20936,123.4319,133.6663,72.5313,121.3994,185.9232,130.1576,0,122.5764,90.46184,112.3146,49.46233,136.0901,107.7313,86.29335,162.5526,60.42004,81.85227,165.7956,34.58191,77.37994,53.37463,85.72176,124.1233,29.84327,24.97401,127.1109,145.871,141.1111,148.7975,103.379,121.0229,84.33435,44.4632,13.16179,14.91679,125.4482,7.674406,167.7392,40.4652,28.77813,74.43261],


[40.11067,56.93823,56.65401,122.0951,149.6473,80.25673,106.2111,118.4172,7.575177,143.8485,83.30009,152.052,98.99886,18.07721,94.80005,87.61281,122.5764,0,74.87418,135.5327,155.709,143.7767,108.7133,60.2234,81.91765,63.44405,53.09437,43.85678,128.4151,103.6954,159.0891,124.921,23.36278,103.163,129.7064,81.73797,118.9274,20.70935,49.68124,19.96367,150.4383,45.92358,84.91276,121.8896,107.7293,36.90239,126.7039,85.66644,111.72,107.7267,72.66156],


[45.78483,126.1575,24.33345,66.87091,76.67832,20.73152,127.9181,62.11361,70.56217,127.9732,135.6964,79.27676,29.2482,60.89599,98.33935,142.0744,90.46184,74.87418,0,61.06223,138.2487,73.11316,36.01074,94.37676,151.7394,47.66852,82.6314,104.6047,75.7178,123.7905,142.2013,51.33941,93.02721,60.89714,82.44973,136.501,62.30052,94.72099,70.32509,67.79546,75.94401,76.59427,47.69322,81.95341,78.25576,51.4596,97.64284,156.208,57.7336,63.20211,17.2031],


[105.5005,183.7746,83.61352,73.57504,19.16367,58.68936,175.2282,53.78765,131.5459,153.4691,193.1079,21.92298,47.437,120.3522,129.5803,199.7866,112.3146,135.5327,61.06223,0,160.7116,24.65365,28.02565,150.1391,212.5309,99.30813,138.8683,160.4634,81.13421,170.8907,164.4595,26.63631,154.0809,86.61815,91.74214,194.4887,53.29625,154.8427,119.741,128.6711,14.90804,134.0675,86.24762,99.57038,106.9016,107.2218,119.8482,217.0747,72.11453,85.27838,69.57524],


[123.0871,207.5105,125.4202,87.15092,179.0806,158.8751,75.37149,195.2686,148.2475,11.86054,128.3975,181.6158,121.9725,159.0242,230.4277,133.9313,49.46233,155.709,138.2487,160.7116,0,184.8524,157.1936,104.5157,173.6801,100.6488,105.6274,199.4872,80.11042,73.53003,3.957828,134.0862,150.5782,78.88729,69.40004,132.9751,195.2278,171.2452,190.2014,135.747,168.3042,111.1604,90.73955,61.4046,60.00645,166.8268,41.79976,178.6053,89.65105,78.21448,121.5231],


[118.8979,186.9888,97.29045,97.8421,12.54308,63.56698,195.2398,40.10087,140.9175,177.2986,208.5989,12.81551,67.67573,127.0912,120.352,215.0563,136.0901,143.7767,73.11316,24.65365,184.8524,0,37.20783,166.5542,223.7478,116.8709,154.9494,162.6172,105.6066,190.9339,188.6348,50.90475,164.2793,109.3499,116.1603,209.5304,39.45971,161.6675,119.4377,140.0925,25.10064,149.3545,106.7572,123.5362,129.7834,111.4449,143.6877,228.0184,95.66849,108.4408,85.46639],


[81.76785,155.8319,60.09487,73.38864,41.04857,30.66386,159.6533,39.40951,105.2152,148.394,171.3927,43.55124,35.33753,92.95397,105.318,177.8488,107.7313,108.7133,36.01074,28.02565,157.1936,37.20783,0,129.4552,187.3909,80.29098,117.8148,132.4429,82.27418,155.3919,161.1045,33.7843,128.2459,78.78495,91.85202,172.3272,39.21878,127.5746,91.93269,103.5017,42.54771,112.1542,72.60489,96.31413,98.95703,79.27901,115.3954,191.7746,68.09244,79.00378,48.57891],


[50.60423,104.4418,70.15448,104.9591,168.1048,110.4729,45.98837,153.9741,54.19633,93.06911,43.4583,170.8545,103.5679,71.61551,152.2291,50.35391,86.29335,60.2234,94.37676,150.1391,104.5157,166.5542,129.4552,0,76.40919,51.06886,11.78308,100.796,107.3418,43.53887,107.3025,130.0585,47.74865,81.5653,103.5826,45.59678,154.2965,70.29488,106.9094,43.1841,164.0083,18.91489,69.39114,91.82756,74.10191,87.36771,87.16662,81.59913,96.64323,86.09673,81.17431],


[107.3807,75.81753,129.0791,179.5995,228.3516,160.9027,100.0352,200.3056,83.2995,163.3184,46.57909,230.9094,169.9875,99.92576,165.8488,42.88159,162.5526,81.91765,151.7394,212.5309,173.6801,223.7478,187.3909,76.40919,0,120.6506,83.05251,91.48624,182.8587,100.905,175.7012,197.1712,59.67885,156.57,179.75,41.7715,200.8092,69.75492,125.5766,83.94483,227.2911,83.96027,142.103,168.1882,150.5024,118.4792,162.9601,5.190087,170.5093,161.2484,144.1171],


[24.29323,120.2578,26.83359,60.84731,117.5663,67.01409,80.26751,109.7367,56.11137,89.21205,94.4277,120.3372,52.5009,60.97938,130.0668,101.2545,60.42004,63.44405,47.66852,99.30813,100.6488,116.8709,80.29098,51.06886,120.6506,0,40.27033,105.8091,66.04817,76.12662,104.435,79.08183,70.01936,40.0252,66.41298,96.23595,109.9384,83.158,89.76219,45.67349,113.01,37.02729,22.49035,58.51854,45.53571,66.32188,65.57052,125.6544,50.95203,44.70444,31.8532],


[38.93087,101.887,58.38659,96.68147,156.6915,98.70844,54.61376,142.2227,46.37369,93.89374,54.29082,159.4323,92.61776,62.45299,142.6691,61.0574,81.85227,53.09437,82.6314,138.8683,105.6274,154.9494,117.8148,11.78308,83.05251,40.27033,0,95.5325,99.80833,51.58974,108.7059,119.3425,44.97381,73.53915,96.99244,55.97332,142.5417,66.01402,97.62353,34.42591,152.8649,7.957299,59.9015,85.88652,68.59392,77.19704,83.71484,88.20128,87.86402,78.20435,69.66811],


[81.62723,25.04671,93.16337,161.565,171.0454,101.7846,146.0104,129.1837,51.39878,187.6281,112.1824,173.0467,132.5576,46.42586,75.79552,114.3767,165.7956,43.85678,104.6047,160.4634,199.4872,162.6172,132.4429,100.796,91.48624,105.8091,95.5325,0,168.6693,144.0312,202.8335,155.848,54.1427,144.5612,171.0978,109.1399,129.8115,30.98609,44.33893,63.79907,174.8966,88.93791,126.0973,164.2372,150.8909,53.62196,170.2093,93.08312,151.1368,148.9301,108.0617],


[88.30458,185.3208,76.28988,9.129211,99.14869,93.53991,112.6315,121.6608,121.3834,74.0148,148.5848,101.6389,50.012,122.3118,174.0375,155.5298,34.58191,128.4151,75.7178,81.13421,80.11042,105.6066,82.27418,107.3418,182.8587,66.04817,99.80833,168.6693,0,108.5122,83.75066,54.72398,135.9594,26.52742,10.71169,151.6653,121.4846,148.6693,143.085,111.6147,88.1949,99.67135,43.7061,21.62038,36.84753,121.0473,41.2393,188.0095,18.27904,21.76865,63.74173],


[86.87041,145.7317,101.6,109.8063,189.8916,142.7409,4.343731,185.8056,97.45235,64.09487,54.9787,192.6806,123.6688,114.0423,194.1271,60.40233,77.37994,103.6954,123.7905,170.8907,73.53003,190.9339,155.3919,43.53887,100.905,76.12662,51.58974,144.0312,108.5122,0,75.22056,146.9323,90.28013,88.15266,101.01,59.62908,186.0197,113.2625,149.1959,85.89193,183.124,59.47997,84.64314,88.0233,71.71123,128.3667,74.30854,105.695,104.7582,91.4126,107.7066],


[126.764,210.5897,129.2942,90.88749,182.7855,162.8301,76.87055,199.2079,151.6456,15.36923,130.1787,185.3116,125.8953,162.6126,234.2699,135.5957,53.37463,159.0891,142.2013,164.4595,3.957828,188.6348,161.1045,107.3025,175.7012,104.435,108.7059,202.8335,83.75066,75.22056,0,137.8415,153.6198,82.83366,73.03909,134.7944,199.1658,174.4414,193.9299,139.1326,171.9426,114.3629,94.68217,65.23906,63.96184,170.5697,45.71784,180.594,93.51014,82.13643,125.4676],


[90.07877,177.4728,69.13407,46.97326,45.36572,58.36288,151.2753,71.40481,119.7926,126.851,173.4835,48.01968,27.19403,112.0293,138.0653,180.3276,85.72176,124.921,51.33941,26.63631,134.0862,50.90475,33.7843,130.0585,197.1712,79.08183,119.3425,155.848,54.72398,146.9323,137.8415,0,140.7632,60.77352,65.25657,175.3147,71.08463,145.2455,119.2505,114.6756,36.42894,115.5249,62.84109,72.94049,80.81661,102.419,93.23569,201.954,45.69416,59.07938,53.36283],


[51.10377,57.01545,71.66595,130.8423,169.2876,101.246,92.06924,140.9114,23.63642,138.861,61.43747,171.796,113.9111,41.29685,116.3412,65.17796,124.1233,23.36278,93.02721,154.0809,150.5782,164.2793,128.2459,47.74865,59.67885,70.01936,44.97381,54.1427,135.9594,90.28013,153.6198,140.7632,0,109.6326,135.4389,59.3987,141.3995,23.16014,72.00202,26.14561,168.9464,40.28273,92.50813,125.9041,109.8644,60.19289,126.9766,63.78917,120.8294,114.381,87.42742],


[63.2271,160.0847,54.56203,23.44097,105.7371,81.03677,92.44674,116.4074,95.95075,69.66546,123.6442,108.4606,43.44877,98.60246,157.6019,130.6201,29.84327,103.163,60.89714,86.61815,78.88729,109.3499,78.78495,81.5653,156.57,40.0252,73.53915,144.5612,26.52742,88.15266,82.83366,60.77352,109.6326,0,26.57838,126.4841,116.3764,123.1158,122.649,85.69735,97.14656,73.17277,18.46851,21.50508,20.45009,99.7293,37.30689,161.7067,16.61587,4.765931,45.46019],


[89.80429,186.61,80.15304,18.60815,109.833,101.1574,105.0209,131.1328,122.4611,63.43753,143.619,112.3315,58.50595,125.0399,180.6622,150.5056,24.97401,129.7064,82.44973,91.74214,69.40004,116.1603,91.85202,103.5826,179.75,66.41298,96.99244,171.0978,10.71169,101.01,73.03909,65.25657,135.4389,26.57838,0,146.9321,130.9823,149.5695,147.8856,112.0147,98.90634,97.69802,45.01036,12.98868,30.37154,125.3249,31.09676,184.9283,25.01663,22.17467,69.05719],


[90.84604,101.8617,112.2432,149.9248,211.9916,150.2338,58.46975,192.8669,79.25538,123.0403,4.812744,214.7042,148.5631,98.5229,175.7391,5.924905,127.1109,81.73797,136.501,194.4887,132.9751,209.5304,172.3272,45.59678,41.7715,96.23595,55.97332,109.1399,151.6653,59.62908,134.7944,175.3147,59.3987,126.4841,146.9321,0,193.2672,79.85746,131.2292,73.5871,208.6423,60.43619,114.975,134.5667,116.7152,117.0672,126.3884,46.3399,141.9503,130.885,124.9808],


[103.7983,154.7559,84.95741,112.5728,51.44142,43.85869,190.1177,0.671863,117.8328,185.9592,193.1963,52.20005,73.44197,101.0442,81.01362,199.0828,145.871,118.9274,62.30052,53.29625,195.2278,39.45971,39.21878,154.2965,200.8092,109.9384,142.5417,129.8115,121.4846,186.0197,199.1658,71.08463,141.3995,116.3764,130.9823,193.2672,0,134.207,85.54003,120.2091,61.75161,135.6933,107.5235,134.919,136.0369,83.10781,153.487,204.5934,106.9115,117.1017,78.98234],


[60.47843,37.36293,77.3166,142.5381,168.2244,98.18305,115.145,133.6515,27.31089,159.4299,82.51006,170.5433,119.5536,34.66178,97.58633,85.36573,141.1111,20.70935,94.72099,154.8427,171.2452,161.6675,127.5746,70.29488,69.75492,83.158,66.01402,30.98609,148.6693,113.2625,174.4414,145.2455,23.16014,123.1158,149.5695,79.85746,134.207,0,55.83322,37.8221,169.7167,60.08491,105.0323,141.2555,126.4096,51.14923,144.758,72.6588,132.1945,127.7393,93.29821],


[67.38408,69.3623,68.10396,134.8333,128.5763,61.76258,152.2248,84.90688,53.65772,178.6127,132.933,130.4084,99.57261,35.29428,45.45097,137.0658,148.7975,49.68124,70.32509,119.741,190.2014,119.4377,91.93269,106.9094,125.5766,89.76219,97.62353,44.33893,143.085,149.1959,193.9299,119.2505,72.00202,122.649,147.8856,131.2292,85.54003,55.83322,0,63.72746,133.6445,89.7162,104.9632,143.9375,134.291,23.45094,154.6725,128.3707,124.8206,126.3073,79.35834],


[25.00595,75.16679,45.66038,105.9601,144.4199,78.12943,88.74105,119.7787,12.53813,123.8865,74.06669,146.9882,87.77709,28.43663,109.0816,79.48417,103.379,19.96367,67.79546,128.6711,135.747,140.0925,103.5017,43.1841,83.94483,45.67349,34.42591,63.79907,111.6147,85.89193,139.1326,114.6756,26.14561,85.69735,112.0147,73.5871,120.2091,37.8221,63.72746,0,143.4783,26.78602,67.91349,103.4636,88.63092,45.03533,107.2244,88.42328,95.76895,90.37675,61.31924],


[120.1383,198.3763,98.28336,81.54279,13.3955,73.13448,187.4677,62.32874,146.4483,161.8182,207.1506,14.98506,60.63785,135.1991,140.8629,213.8766,121.0229,150.4383,75.94401,14.90804,168.3042,25.10064,42.54771,164.0083,227.2911,113.01,152.8649,174.8966,88.1949,183.124,171.9426,36.42894,168.9464,97.14656,98.90634,208.6423,61.75161,169.7167,133.6445,143.4783,0,148.2801,98.67137,107.9927,117.04,121.8258,128.37,231.8575,81.70752,95.27343,83.94739],


[31.89615,96.61155,52.26159,95.8601,151.5722,91.94157,62.54839,135.3572,38.97585,99.34804,59.26611,154.2903,88.52349,54.59169,134.7251,65.81573,84.33435,45.92358,76.59427,134.0675,111.1604,149.3545,112.1542,18.91489,83.96027,37.02729,7.957299,88.93791,99.67135,59.47997,114.3629,115.5249,40.28273,73.17277,97.69802,60.43619,135.6933,60.08491,89.7162,26.78602,148.2801,0,58.14318,87.21175,70.45562,69.24258,86.84749,89.02725,86.59543,77.91448,64.54473],


[44.87163,141.851,36.95828,38.36816,105.2609,68.41493,88.98056,107.4574,77.78398,80.30692,112.6324,108.0488,39.14608,80.14721,141.4681,119.5863,44.4632,84.91276,47.69322,86.24762,90.73955,106.7572,72.60489,69.39114,142.103,22.49035,59.9015,126.0973,43.7061,84.64314,94.68217,62.84109,92.50813,18.46851,45.01036,114.975,107.5235,105.0323,104.9632,67.91349,98.67137,58.14318,0,39.08552,30.98421,81.82888,51.07715,147.1693,28.60511,22.87333,30.79071],


[82.61001,178.528,75.83765,26.48888,118.1902,101.7394,92.04007,135.0079,114.4835,53.93013,131.1588,120.7863,61.49478,118.7782,179.0779,138.0139,13.16179,121.8896,81.95341,99.57038,61.4046,123.5362,96.31413,91.82756,168.1882,58.51854,85.88652,164.2372,21.62038,88.0233,65.23906,72.94049,125.9041,21.50508,12.98868,134.5667,134.919,141.2555,143.9375,103.4636,107.9927,87.21175,39.08552,0,17.86208,120.8853,20.37815,173.3754,28.33119,18.75529,66.90152],


[69.77193,163.7723,67.1124,38.48785,125.9798,98.86882,75.86182,136.0376,100.2034,50.04108,113.331,128.687,63.67399,106.5106,172.1648,120.1984,14.91679,107.7293,78.25576,106.9016,60.00645,129.7834,98.95703,74.10191,150.5024,45.53571,68.59392,150.8909,36.84753,71.71123,63.96184,80.81661,109.8644,20.45009,30.37154,116.7152,136.0369,126.4096,134.291,88.63092,117.04,70.45562,30.98421,17.86208,0,110.8927,20.41383,155.6916,35.41359,21.76684,61.64759],


[44.32212,76.5557,45.20886,113.0699,118.8766,48.79477,131.6307,82.56087,37.86126,155.2692,118.0887,121.0423,80.17084,18.90481,66.02766,122.9903,125.4482,36.90239,51.4596,107.2218,166.8268,111.4449,79.27901,87.36771,118.4792,66.32188,77.19704,53.62196,121.0473,128.3667,170.5697,102.419,60.19289,99.7293,125.3249,117.0672,83.10781,51.14923,23.45094,45.03533,121.8258,69.24258,81.82888,120.8853,110.8927,0,131.2602,122.0191,102.8721,103.5266,57.70433],


[89.64681,182.0634,87.50037,46.84838,138.5291,118.0551,77.96366,153.5367,119.137,33.62437,122.5267,141.1345,80.17825,126.4213,192.478,129.1275,7.674406,126.7039,97.64284,119.8482,41.79976,143.6877,115.3954,87.16662,162.9601,65.57052,83.71484,170.2093,41.2393,74.30854,45.71784,93.23569,126.9766,37.30689,31.09676,126.3884,153.487,144.758,154.6725,107.2244,128.37,86.84749,51.07715,20.37815,20.41383,131.2602,0,168.1321,48.10297,36.41947,81.40735],


[112.0695,76.25698,133.7068,184.7153,232.767,165.0295,104.7387,204.082,87.34856,168.2964,51.12867,235.3115,174.78,103.5986,167.9617,47.08697,167.7392,85.66644,156.208,217.0747,178.6053,228.0184,191.7746,81.59913,5.190087,125.6544,88.20128,93.08312,188.0095,105.695,180.594,201.954,63.78917,161.7067,184.9283,46.3399,204.5934,72.6588,128.3707,88.42328,231.8575,89.02725,147.1693,173.3754,155.6916,122.0191,168.1321,0,175.5978,166.3892,148.8338],


[71.72084,168.4592,58.33508,10.43468,91.03834,76.15748,109.0479,107.0244,104.8891,81.66457,139.2843,93.70653,33.76602,104.7173,156.0663,146.2644,40.4652,111.72,57.7336,72.11453,89.65105,95.66849,68.09244,96.64323,170.5093,50.95203,87.86402,151.1368,18.27904,104.7582,93.51014,45.69416,120.8294,16.61587,25.01663,141.9503,106.9115,132.1945,124.8206,95.76895,81.70752,86.59543,28.60511,28.33119,35.41359,102.8721,48.10297,175.5978,0,13.72204,45.46845],


[67.731,164.6596,58.3182,19.1322,104.3125,83.01244,95.6787,117.1597,100.5451,69.49033,127.9875,107.0075,43.75892,102.8689,160.5436,134.9589,28.77813,107.7267,63.20211,85.27838,78.21448,108.4408,79.00378,86.09673,161.2484,44.70444,78.20435,148.9301,21.76865,91.4126,82.13643,59.07938,114.381,4.765931,22.17467,130.885,117.1017,127.7393,126.3073,90.37675,95.27343,77.91448,22.87333,18.75529,21.76684,103.5266,36.41947,166.3892,13.72204,0,48.3679],


[36.78691,127.5161,16.04237,55.497,87.06455,37.87449,111.8997,78.83373,66.99924,111.0788,123.7222,89.79488,26.54891,62.04243,112.188,130.338,74.43261,72.66156,17.2031,69.57524,121.5231,85.46639,48.57891,81.17431,144.1171,31.8532,69.66811,108.0617,63.74173,107.7066,125.4676,53.36283,87.42742,45.46019,69.05719,124.9808,78.98234,93.29821,79.35834,61.31924,83.94739,64.54473,30.79071,66.90152,61.64759,57.70433,81.40735,148.8338,45.46845,48.3679,0]
,
    ]
    data['demands'] = [0, 10,13,22,50,6,13,3,43,8,8,10,13,25,18,39,30,16,41,43,28,40,19,26,27,45,30,10,15,44,13,33,48,13,5,6,8,23,35,35,42,27,41,33,26,38,14,28,16,30,14]
    data['vehicle_capacities'] = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
    data['num_vehicles'] = 16
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, assignment):
    """Prints assignment on console."""
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))


def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        print_solution(data, manager, routing, assignment)


if __name__ == '__main__':
    main()
