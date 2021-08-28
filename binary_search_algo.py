# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:08:42 2021

@author: bhavy
"""
def binary_search(list,item):
    low = 0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2 #I have used '//' indicates floor division in python 3.x. 
        #If we use '/' the resulting mid  is a float which is not allowed for list indicies
        guess = list[mid]
        if guess == item:
            return mid
        if guess>item:
            high = mid-1
        else:
            low = mid+1
    return None

my_list = [1,3,5,7,9,11]
list = [1,3,4,6,7,123,645,3532]
item = 123
item1= 645
item2= 0

list_with_1000_items = [7, 15, 18, 21, 32, 34, 37, 39, 45, 48, 55, 60, 65, 70, 86, 101, 112, 119, 120, 151, 152, 161, 170, 172, 200, 206, 223, 232, 233, 236, 270, 292, 300, 324, 333, 347, 354, 355, 363, 411, 419, 430, 443, 448, 457, 465, 497, 505, 508, 514, 526, 528, 534, 552, 555, 589, 597, 612, 627, 645, 654, 657, 663, 668, 670, 689, 692, 702, 703, 706, 726, 727, 732, 740, 743, 747, 756, 773, 777, 786, 787, 789, 794, 799, 801, 803, 842, 852, 856, 866, 901, 902, 904, 909, 912, 928, 929, 932, 939, 965, 984, 1006, 1019, 1045, 1050, 1078, 1080, 1094, 1103, 1105, 1119, 1121, 1132, 1137, 1145, 1166, 1169, 1174, 1183, 1188, 1194, 1199, 1202, 1223, 1227, 1237, 1241, 1255, 1265, 1279, 1290, 1291, 1310, 1315, 1317, 1324, 1326, 1342, 1350, 1362, 1363, 1366, 1371, 1376, 1392, 1393, 1395, 1399, 1406, 1415, 1429, 1446, 1448, 1453, 1466, 1469, 1471, 1480, 1500, 1518, 1520, 1521, 1529, 1548, 1558, 1560, 1561, 1565, 1569, 1573, 1593, 1597, 1599, 1616, 1618, 1645, 1646, 1693, 1694, 1713, 1714, 1717, 1734, 1740, 1742, 1763, 1780, 1806, 1814, 1823, 1828, 1844, 1849, 1853, 1860, 1867, 1869, 1870, 1882, 1889, 1895, 1904, 1908, 1934, 1951, 1980, 1991, 1993, 1996, 2005, 2021, 2028, 2033, 2038, 2044, 2047, 2053, 2054, 2061, 2067, 2087, 2091, 2096, 2101, 2119, 2128, 2132, 2133, 2136, 2160, 2175, 2186, 2201, 2202, 2207, 2209, 2211, 2219, 2222, 2240, 2278, 2288, 2322, 2327, 2339, 2342, 2360, 2367, 2386, 2392, 2394, 2405, 2409, 2416, 2436, 2443, 2476, 2478, 2491, 2493, 2494, 2496, 2524, 2525, 2541, 2557, 2562, 2584, 2618, 2623, 2625, 2627, 2637, 2661, 2674, 2678, 2692, 2703, 2704, 2711, 2715, 2716, 2722, 2730, 2766, 2781, 2786, 2802, 2835, 2836, 2857, 2859, 2873, 2878, 2880, 2923, 2948, 2975, 2980, 2994, 3003, 3009, 3013, 3019, 3020, 3043, 3050, 3056, 3073, 3074, 3078, 3083, 3084, 3093, 3100, 3102, 3112, 3121, 3145, 3153, 3159, 3187, 3202, 3247, 3250, 3264, 3283, 3284, 3288, 3290, 3292, 3299, 3301, 3326, 3333, 3338, 3341, 3361, 3377, 3389, 3393, 3401, 3435, 3454, 3456, 3467, 3474, 3482, 3485, 3490, 3491, 3498, 3504, 3530, 3534, 3545, 3552, 3564, 3574, 3586, 3606, 3615, 3619, 3622, 3636, 3647, 3655, 3688, 3711, 3725, 3739, 3760, 3765, 3774, 3780, 3791, 3822, 3826, 3828, 3830, 3841, 3849, 3854, 3857, 3863, 3885, 3888, 3889, 3903, 3911, 3916, 3961, 3981, 4045, 4080, 4082, 4089, 4122, 4134, 4145, 4151, 4152, 4176, 4193, 4200, 4205, 4211, 4213, 4215, 4227, 4237, 4238, 4249, 4257, 4275, 4281, 4294, 4297, 4299, 4310, 4316, 4326, 4328, 4338, 4341, 4357, 4359, 4363, 4364, 4396, 4414, 4435, 4437, 4442, 4470, 4471, 4484, 4486, 4489, 4493, 4512, 4515, 4524, 4527, 4543, 4550, 4553, 4555, 4560, 4568, 4571, 4587, 4600, 4613, 4627, 4633, 4668, 4673, 4676, 4686, 4691, 4710, 4719, 4731, 4767, 4775, 4780, 4803, 4815, 4831, 4834, 4879, 4882, 4914, 4918, 4922, 4925, 4941, 4954, 4967, 4981, 4982, 4985, 4993, 4999, 5013, 5026, 5033, 5038, 5044, 5052, 5055, 5066, 5086, 5089, 5098, 5103, 5118, 5146, 5147, 5148, 5164, 5177, 5180, 5190, 5196, 5201, 5217, 5221, 5263, 5271, 5278, 5280, 5286, 5295, 5316, 5319, 5320, 5344, 5371, 5376, 5380, 5384, 5391, 5406, 5415, 5436, 5439, 5446, 5451, 5465, 5474, 5485, 5504, 5507, 5511, 5519, 5522, 5544, 5548, 5567, 5572, 5591, 5595, 5618, 5619, 5621, 5627, 5635, 5659, 5678, 5682, 5690, 5703, 5714, 5716, 5719, 5721, 5742, 5760, 5771, 5774, 5786, 5827, 5843, 5845, 5853, 5871, 5874, 5877, 5878, 5887, 5900, 5904, 5923, 5925, 5945, 5967, 6004, 6005, 6006, 6009, 6027, 6038, 6047, 6053, 6057, 6061, 6067, 6075, 6079, 6080, 6088, 6089, 6106, 6113, 6145, 6151, 6155, 6165, 6171, 6179, 6182, 6192, 6198, 6207, 6220, 6232, 6234, 6240, 6243, 6252, 6258, 6270, 6274, 6286, 6300, 6301, 6314, 6316, 6322, 6325, 6326, 6339, 6349, 6354, 6365, 6371, 6384, 6387, 6402, 6412, 6430, 6436, 6447, 6452, 6463, 6464, 6467, 6480, 6487, 6539, 6559, 6565, 6566, 6567, 6572, 6581, 6588, 6592, 6604, 6614, 6623, 6640, 6642, 6648, 6649, 6653, 6682, 6694, 6710, 6733, 6748, 6761, 6769, 6774, 6779, 6780, 6781, 6793, 6846, 6861, 6880, 6898, 6922, 6930, 6938, 6949, 6964, 6977, 6983, 6993, 7001, 7009, 7010, 7015, 7019, 7023, 7025, 7028, 7033, 7049, 7051, 7060, 7076, 7080, 7114, 7118, 7119, 7129, 7131, 7134, 7137, 7168, 7169, 7183, 7219, 7242, 7257, 7258, 7299, 7301, 7304, 7306, 7310, 7317, 7318, 7322, 7326, 7337, 7346, 7358, 7382, 7388, 7389, 7390, 7392, 7398, 7400, 7415, 7423, 7425, 7427, 7429, 7444, 7450, 7475, 7486, 7490, 7491, 7499, 7526, 7532, 7536, 7549, 7562, 7570, 7578, 7579, 7583, 7597, 7600, 7605, 7626, 7628, 7630, 7636, 7639, 7645, 7648, 7661, 7680, 7681, 7694, 7706, 7717, 7723, 7732, 7734, 7738, 7740, 7762, 7773, 7802, 7829, 7846, 7847, 7878, 7903, 7915, 7922, 7926, 7932, 7938, 7960, 7967, 7975, 7985, 8002, 8013, 8031, 8039, 8040, 8046, 8071, 8073, 8075, 8082, 8098, 8099, 8105, 8139, 8148, 8159, 8165, 8171, 8187, 8188, 8197, 8204, 8220, 8222, 8226, 8247, 8248, 8263, 8267, 8274, 8283, 8299, 8301, 8315, 8361, 8370, 8372, 8373, 8395, 8396, 8400, 8406, 8421, 8427, 8437, 8447, 8456, 8458, 8467, 8470, 8474, 8506, 8513, 8514, 8522, 8525, 8542, 8543, 8544, 8562, 8570, 8577, 8580, 8586, 8590, 8602, 8607, 8614, 8624, 8630, 8634, 8650, 8666, 8667, 8671, 8677, 8688, 8699, 8713, 8723, 8724, 8733, 8734, 8736, 8742, 8744, 8746, 8749, 8764, 8774, 8786, 8803, 8807, 8849, 8853, 8861, 8865, 8869, 8875, 8882, 8900, 8904, 8905, 8916, 8919, 8947, 8965, 8969, 8981, 8988, 8997, 9004, 9019, 9028, 9037, 9044, 9071, 9074, 9076, 9079, 9152, 9163, 9164, 9166, 9182, 9199, 9227, 9230, 9238, 9247, 9258, 9269, 9290, 9307, 9314, 9351, 9361, 9362, 9367, 9376, 9382, 9395, 9412, 9426, 9430, 9434, 9439, 9453, 9465, 9474, 9481, 9491, 9494, 9502, 9504, 9524, 9539, 9542, 9550, 9573, 9579, 9596, 9600, 9632, 9633, 9641, 9663, 9674, 9684, 9693, 9697, 9700, 9706, 9708, 9710, 9713, 9716, 9747, 9751, 9753, 9767, 9772, 9773, 9775, 9776, 9783, 9788, 9789, 9805, 9808, 9819, 9822, 9827, 9833, 9838, 9840, 9847, 9852, 9857, 9866, 9874, 9881, 9887, 9901, 9917, 9931, 9945, 9949, 9952, 9991, 9997, 9999]

print(binary_search(list_with_1000_items, 21))
    