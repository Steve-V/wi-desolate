from math import radians, cos, sin, asin, sqrt

import itertools
import numpy as np

def haversine(a,b):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    
    #extract lat/lon from input points
    lat1 = a[1]
    lon1 = a[0]
    lat2 = b[1]
    lon2 = b[0]
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # 6367 = Radius of earth in kilometers. Use 3956 for miles, 3438.1451 for nautical
    dist = 3438.1451 * c
    return dist


def allWisconsinAirportsList():
    return [
    (-89.0501022338867,44.3042984008789),
    (-90.3891983032226,44.0099983215332),
    (-92.6557998657226,45.0318984985351),
    (-88.8808975219726,44.0275001525878),
    (-88.0167007446,42.523399353),
    (-88.7459030151367,42.6511001586914),
    (-92.4502029418945,45.6627006530761),
    (-88.391502380371,42.9653015136718),
    (-90.3551025390625,43.0435981750488),
    (-91.3076019287109,44.0036010742187),
    (-87.9514999389648,42.988899230957),
    (-92.1418991089,45.5071983336999),
    (-88.333396911621,43.2014007568359),
    (-88.4968032836914,42.6617012023925),
    (-89.3526000976562,43.8293991088867),
    (-87.8906021118164,42.793399810791),
    (-88.1578979492,42.8736000061),
    (-88.4992980957,44.1335983276),
    (-88.472297668457,43.1389007568359),
    (-89.3386993408,42.9314002991),
    (-88.0486984252929,42.7997016906738),
    (-88.1894989013671,45.1157989501953),
    (-90.9337997436523,44.9632987976074),
    (-89.5711975097656,43.3541984558105),
    (-88.194933,44.061183),
    (-90.3563003540039,45.1358985900878),
    (-88.9996032714843,43.6963996887207),
    (-92.376667,45.136944),
    (-91.5585021972656,45.7779998779296),
    (-89.4181976318359,42.9275016784667),
    (-89.1210021972656,46.1216011047363),
    (-88.8932037353515,43.0360984802246),
    (-88.9253997802734,44.0880012512207),
    (-92.0570983886718,45.1952018737792),
    (-91.8026962280273,45.8354988098144),
    (-89.3112030029296,42.6425018310546),
    (-88.7045974731445,43.9328002929687),
    (-87.8870010375976,43.3652992248535),
    (-89.1167984008789,43.849998474121),
    (-87.7917022705078,42.7084007263183),
    (-88.9525985717773,43.5149993896484),
    (-88.0640029907226,42.8403015136718),
    (-89.0964965820312,44.0222015380859),
    (-87.4402008057,44.635799408),
    (-88.8667984008789,42.9138984680175),
    (-88.1953964233398,43.6679992675781),
    (-87.9972991943359,43.3292007446289),
    (-92.5360031127999,45.2118988037),
    (-89.3174972534179,46.1547012329101),
    (-89.0792999267578,44.0214004516601),
    (-92.7177963256835,44.9623985290527),
    (-88.1284027099609,44.8650016784667),
    (-90.219497680664,43.0685997009277),
    (-90.8545989990234,44.3040008544921),
    (-91.6285018920898,45.9110984802246),
    (-92.6737976074218,45.0955009460449),
    (-88.4274978637695,42.554100036621),
    (-91.5099029541015,44.7943992614746),
    (-92.120341,44.528718),
    (-91.3034973144531,45.6991004943847),
    (-92.7137985229492,44.8077011108398),
    (-92.0466003417968,44.6040992736816),
    (-90.0273971557999,44.3255004882999),
    (-91.1056976318359,45.1655006408691),
    (-86.9244995117187,45.3861999511718),
    (-88.290901184082,43.4664001464843),
    (-89.60009765625,44.8526992797851),
    (-89.2865982055664,42.9435997009277),
    (-90.2276000976562,42.556900024414),
    (-88.0231018066406,43.0415000915527),
    (-88.398696899414,42.6427993774414),
    (-90.1632003784179,46.0974006652832),
    (-89.1862030029296,42.9136009216308),
    (-89.6653976440429,42.9696998596191),
    (-87.7789993286132,43.5974998474121),
    (-89.6348037719726,43.7599983215332),
    (-89.6303024291992,43.6542015075683),
    (-88.7613983154296,44.3578987121582),
    (-88.7811965942382,44.3394012451171),
    (-90.0192031860351,44.0064010620117),
    (-90.4192962646484,44.5297012329101),
    (-88.6732025146484,43.9486999511718),
    (-88.714269,44.015228),
    (-92.293239,45.913686),
    (-88.093578,44.280428),
    (-87.8084030151367,44.9519004821777),
    (-87.3592987060546,45.1918983459472),
    (-88.6019973754882,43.0071983337402),
    (-88.9626007080078,43.991600036621),
    (-88.7008972167968,44.3163986206054),
    (-88.419733,45.099606),
    (-88.0659027099609,44.5321998596191),
    (-89.7654037475585,43.4178009033203),
    (-88.4375991821289,42.7456016540527),
    (-91.2995986938476,44.0321998596191),
    (-89.7535018920898,42.9911003112792),
    (-88.8526000976562,44.3885993957519),
    (-90.6199035644531,43.4846992492675),
    (-88.0731964111328,45.2141990661621),
    (-87.1858978271484,45.135398864746),
    (-87.4197998046875,44.6422004699707),
    (-88.0876007080078,42.6570014953613),
    (-88.9845962524414,43.1528015136718),
    (-89.4073028564453,44.7652015686035),
    (-89.4022979736328,44.923599243164),
    (-88.7265014648437,42.8125),
    (-88.8746032714843,42.5900993347167),
    (-88.4581985473632,43.0332984924316),
    (-89.1218032836914,44.0532989501953),
    (-91.3777542114257,44.9937591552734),
    (-90.8706970214843,46.6916007995605),
    (-88.0456008911132,42.5702018737792),
    (-88.7711029052734,44.306900024414),
    (-91.7118988037109,45.2389984130859),
    (-87.6177978515625,44.1500015258789),
    (-91.4307022094726,44.9356002807617),
    (-91.3668975830078,44.556900024414),
    (-89.1210021972656,45.7901992797851),
    (-91.4307022094726,44.0583000183105),
    (-88.5798034667968,42.7386016845703),
    (-91.1100997924804,45.4543991088867),
    (-91.7325,45.031533),
    (-90.385067,44.772217),
    (-92.2835006713867,45),
    (-92.5561981201171,45.1176986694335),
    (-88.8081970214843,42.8899993896484),
    (-89.7301025390625,45.7938003540039),
    (-88.1584014892578,42.5334014892578),
    (-90.0154037475585,43.3791999816894),
    (-90.2325973510742,43.6699981689453),
    (-90.0001983642578,45.88330078125),
    (-91.2723999023437,44.9333000183105),
    (-89.1834030151367,43.483299255371),
    (-89.021499633789,45.6060981750488),
    (-88.1372985839843,45.3251991271972),
    (-89.7480010986328,45.5741004943847),
    (-91.4598999023437,44.7235984802246),
    (-87.8973007202148,43.80419921875),
    (-91.3762969970703,44.0513000488281),
    (-92.1918029785156,45.0069007873535),
    (-89.9863967895507,44.4169998168945),
    (-88.5360031127929,45.3320999145507),
    (-91.2329025268554,45.2941017150878),
    (-92.378303527832,45.4570007324218),
    (-87.6182022094726,45.0727996826171),
    (-87.9943008422851,44.4711990356445),
    (-88.470747,43.005208),
    (-88.146389,42.5975),
    (-88.527099609375,44.113899230957),
    (-88.5572967529296,44.0628013610839),
    (-90.056883,45.159644),
    (-89.7867965698242,42.6981010437011),
    (-89.4237,42.7181),
    (-92.2751998901367,45.00830078125),
    (-89.9686965942382,44.318000793457),
    (-89.5936965942382,44.7733993530273),
    (-87.9677963256835,43.744400024414),
    (-89.075698852539,42.8727989196777),
    (-92.3664016723632,45.6450996398925),
    (-89.1925964355468,43.0339012145996),
    (-91.4981994628906,46.3488006591796),
    (-88.2052001953125,42.5140991210937),
    (-91.1337966918945,44.7027015686035),
    (-91.6771011352539,45.9019012451171),
    (-89.4953994750976,44.2224998474121),
    (-89.0170974731445,43.2078018188476),
    (-87.6792984008789,45.0814018249511),
    (-89.4917984008789,45.2750015258789),
    (-91.3957977294921,44.366901397705),
    (-89.0835037231445,44.3358001708984),
    (-88.0043029785156,45.0760993957519),
    (-88.1648025512695,45.1296997070312),
    (-89.4843978881835,43.2682991027832),
    (-89.401802063,45.0323982239),
    (-92.2584991455078,44.5943984985351),
    (-88.7598037719726,42.8535995483398),
    (-89.7017974853515,45.8932991027832),
    (-88.2856979370117,43.7083015441894),
    (-88.094497680664,42.8236007690429),
    (-91.735386,45.514592),
    (-89.7376022338867,42.6657981872558),
    (-88.3003997802734,42.5183982849121),
    (-88.7001037597656,44.0414009094238),
    (-87.8219985961914,43.6192016601562),
    (-89.938003540039,42.676399230957),
    (-88.6629028320312,43.0774993896484),
    (-89.9971008300781,43.9710998535156),
    (-89.0251007080078,44.505500793457),
    (-91.2404022216796,43.8039016723632),
    (-92.6876983642578,45.3199996948242),
    (-89.451301574707,43.1786994934082),
    (-91.9877014160156,45.1805000305175),
    (-89.91259765625,44.4952011108398),
    (-92.7557983398437,44.8438987731933),
    (-91.5625,45.6772003173828),
    (-90.4316024780273,46.5154991149902),
    (-88.020896911621,44.8891983032226),
    (-87.6279983520507,44.6839981079101),
    (-89.2761001586914,42.6104011535644),
    (-88.2427978515625,43.011001586914),
    (-89.2678985595703,43.7966003417968),
    (-92.1987991333007,44.4998016357421),
    (-89.0106964111328,43.3800010681152),
    (-92.3544006347656,45.0321998596191),
    (-87.9658966064453,43.2663993835449),
    (-87.9928970336914,44.046100616455),
    (-91.5087966918945,45.2405014038085),
    (-87.9634017944335,43.1810989379882),
    (-87.7843017578125,43.5889015197753),
    (-92.5891036987304,45.3125),
    (-88.2031021118164,42.5717010498046),
    (-91.211611,44.577514),
    (-88.5596008300781,44.1599998474121),
    (-91.332728,44.367614),
    (-88.4264984130859,45.0652999877929),
    (-91.1099014282226,43.3730010986328),
    (-90.8843002319335,46.1585998535156),
    (-89.1781997680664,43.443000793457),
    (-88.0114974975585,44.5013999938964),
    (-90.9878997802734,44.3004989624023),
    (-89.4007034301757,42.8824996948242),
    (-89.3590011596679,43.4705009460449),
    (-90.149299621582,45.1589012145996),
    (-87.6024017333984,44.7806015014648),
    (-88.3254013061523,43.8305015563964),
    (-89.1384963989257,44.0229988098144),
    (-90.1764984130859,45.0786018371582),
    (-87.8143997192382,44.1492004394531),
    (-90.3461990356445,44.9705009460449),
    (-88.0426025390625,42.7625007629394),
    (-91.2473983765,43.7929992675999),
    (-92.2928009033203,45.0443992614746),
    (-89.8701019287109,42.8252983093261),
    (-89.1854019165039,43.0194015502929),
    (-88.5973968505859,42.8835983276367),
    (-87.8607025146484,44.50830078125),
    (-90.0320968627929,42.9068984985351),
    (-89.8143005371093,43.7439002990722),
    (-88.7282028198242,44.7536010742187),
    (-89.5309982299804,44.2247009277343),
    (-89.5553970336914,44.420799255371),
    (-87.8765029907226,43.3964004516601),
    (-88.54164,44.515496),
    (-87.6529006958007,44.6096992492675),
    (-88.1820983886718,45.6511001586914),
    (-90.6482009887695,42.9766998291015),
    (-92.602798461914,44.8652992248535),
    (-87.0674972534179,45.2350997924804),
    (-88.708396911621,45.5750007629394),
    (-89.7557983398437,43.2979011535644),
    (-90.0320968627929,44.2938995361328),
    (-88.2152023315429,44.6412010192871),
    (-89.6410980224609,45.296100616455),
    (-88.2095031738281,43.2536010742187),
    (-89.2500991821289,43.4500007629394),
    (-88.4164962768554,42.9874992370605),
    (-89.1296997070312,42.9361000061035),
    (-88.2509002685546,42.75),
    (-88.4936981201171,43.9411010742187),
    (-90.8602981567382,44.9632987976074),
    (-88.6176986694335,44.7846984863281),
    (-89.2710037231445,42.9510993957519),
    (-87.3805999755859,44.6808013916015),
    (-87.97509765625,42.9625015258789),
    (-88.6235961914062,44.3293991088867),
    (-87.7958984375,44.287498474121),
    (-87.9868011474609,44.2854995727539),
    (-88.1348037719726,42.9785995483398),
    (-88.5745010375976,42.8283004760742),
    (-89.0167999267578,45.1040992736816),
    (-88.3793029785156,42.6939010620117),
    (-92.0819015502929,46.6208000183105),
    (-88.6839981079101,44.1068992614746),
    (-92.1460037231445,45.9665985107421),
    (-87.8889999389648,43.4213981628417),
    (-89.029800415039,45.083999633789),
    (-89.5210037231445,43.3333015441894),
    (-89.777603149414,43.6068992614746),
    (-89.5668029785156,44.060001373291),
    (-88.158678,44.367639),
    (-91.8342971801757,45.4075012207031),
    (-89.3750991821289,42.5917015075683),
    (-88.6010971069335,42.6341018676757),
    (-87.958999633789,42.7033004760742),
    (-89.652603149414,43.7571983337402),
    (-88.1781602778,43.0902222222),
    (-91.2463989257812,46.1941986083984),
    (-92.020401001,45.0439987182999),
    (-88.9675979614257,42.4977989196777),
    (-90.7586975097656,46.7887001037597),
    (-88.3725967407226,42.7971992492675),
    (-90.279296875,45.542999267578),
    (-90.2575988769531,43.7064018249511),
    (-88.8175964355468,42.9631996154785),
    (-89.7880020141601,43.9612007141113),
    (-90.6809997558593,42.7804985046386),
    (-88.6529998779296,42.5256996154785),
    (-90.1377029418945,43.8386993408203),
    (-89.1855011,43.10490036),
    (-88.1135025024,43.9441986084),
    (-90.2983016967773,43.2834014892578),
    (-92.3753967285,45.2811012268),
    (-89.1107025146484,45.1542015075683),
    (-89.73090363,45.92789841),
    (-90.91899872,46.54850006),
    (-88.5190963745,44.2580986022999),
    (-89.6266021729,44.9262008667),
    (-90.8553009033203,44.2507019042968),
    (-89.6460037231,46.1374015808),
    (-88.3046035766601,42.6907005310058),
    (-88.389603,42.614899),
    (-89.5315017700195,43.1142997741699),
    (-89.9832000732421,43.5259017944335),
    (-89.4829025268554,43.5602989196777),
    (-90.964599609375,42.7042007446289),
    (-88.731300354,44.6138000487999),
    (-90.7378997802734,43.9583015441894),
    (-89.6668014526,44.7775993347),
    (-89.8823013305664,46.1220016479492),
    (-90.0850982666015,44.0334014892578),
    (-89.77020264,43.52270126),
    (-91.4842987060546,44.8657989501953),
    (-89.5904006958007,42.6148986816406),
    (-89.2683029175,45.9323005675999),
    (-87.92780304,42.59569931),
    (-88.1278991699,43.4221992493),
    (-88.5589981079101,44.7869987487792),
    (-88.4884033203,43.7711982727),
    (-88.1296005249023,44.4850997924804),
    (-92.6643981934,45.7980995178),
    (-90.3282012939453,43.6566009521484),
    (-88.39109802,43.34930038),
    (-91.4442977905,46.0251998901),
    (-89.8389968872,44.3602981567),
    (-89.0416030884,42.620300293),
    (-89.21209717,46.15399933),
    (-90.181602478,43.2117004395),
    (-91.256699,43.879002),
    (-91.8678970336914,44.8922996520996),
    (-90.30329895,45.10100174),
    (-90.1893005371,44.6369018555),
    (-87.8965988159179,42.9472007751464),
    (-90.2361984252929,42.8867988586425),
    (-89.3375015258789,43.1399002075195),
    (-87.6806030273437,44.1287994384765),
    (-88.0344009399414,43.1104011535644),
    (-87.9095993,44.87419891),
    (-92.691902160645,45.310001373291),
    (-91.8163986206054,46.3148002624511),
    (-88.5569992065429,43.9844017028808),
    (-90.67549896,43.16019821),
    (-90.4024963378906,45.708999633789),
    (-89.01979828,44.33330154),
    (-91.12370300293,43.019298553467),
    (-90.42440032959,45.955001831055),
    (-90.44439697,42.68939972),
    (-87.8152008057,42.7606010437),
    (-91.000503540039,45.4967994689941),
    (-89.4674987792968,45.6311988830566),
    (-91.7221984863281,45.4785995483398),
    (-92.5381012,45.14830017),
    (-91.77349854,45.41899872),
    (-89.7128982544,45.1988983154),
    (-88.7231979370117,43.1696014404296),
    (-92.3724975585937,45.8227005004882),
    (-87.85140228,43.76959991),
    (-91.92070007,45.73139954),
    (-89.530296325684,44.5452003479),
    (-87.42150116,44.84370041),
    (-92.094703674316,46.689701080322),
    (-89.80570221,45.46910095),
    (-91.981101989746,45.5060005187988),
    (-88.237098693848,43.041000366211),
    (-88.70320129,43.42660141),
    (-90.5121994018554,44.5581016540527),
    (-90.253402709961,43.938999176025),
    (-91.63619995,45.30619812),
    (-89.3044967651367,44.0415992736816),
    (-90.913101196289,43.5793991088867),
    (-88.9334030151367,45.5166015625),
    (-90.48349762,43.97499847),
    (-88.1333333333,43.4219444444),
    (-91.798,46.369833),
    (-91.51820374,45.17969894),
    (-89.2670974731,43.5663986206),
    (-87.97789764,42.57220078),
    (-91.5127029419,44.6411018372),
    (-89.5167999267578,42.983299255371),
    (-89.217903137207,44.1977996826171),
    (-88.0223007202148,44.4989013671875),
    (-88.5617980957031,44.4547004699707),
    (-89.2306976318359,44.8739013671875),
    (-87.9360961914062,42.5705986022949),
    (-88.9148025512695,42.5069999694824),
    (-88.1333999633789,42.7980995178222),
    (-91.9169006347656,44.8916015625),
    (-91.6844024658203,44.8083000183105),
    (-87.6156005859375,44.1272010803222),
    (-88.7667999267578,43.622200012207),
    (-87.9256973266601,43.2565002441406),
    (-88.4757995605,42.9771995544),
    (-91.6168975830078,46.4499015808105),
    (-89.2406997680664,42.5914001464843),
    (-91.624900817871,45.7066001892089),
    (-89.8395,44.254833),
    (-92.3877029418945,44.9665985107421),
    (-91.5014038085937,45.1025009155273),
    (-90.1296997070312,42.853099822998),
    (-91.4502029418945,45.13330078125),
    (-89.4335021972656,43.7999992370605),
    (-88.0920028686523,44.882999420166),
    (-91.2417984008789,44.9096984863281),
    (-88.6007995605468,44.3231010437011),
    (-91.0835037231445,46.866600036621),
    (-89.752197265625,42.8810997009277),
    (-92.0140991210937,44.5388984680175),
    (-91.4654006958007,44.7050018310546),
    (-91.9748992919921,44.9202003479003),
    (-87.5576019287109,44.5861015319824),
    (-92.4834976196289,44.9054985046386),
    (-89.7295989990234,43.4813995361328),
    (-91.6510009765625,46.4143981933593),
    (-91.3303985596,44.9873008727999),
    (-91.9023971557617,46.1035995483398),
    (-91.8398971557617,45.3969001770019),
    (-92.5727005004882,45.2158012390136),
    (-89.6201019287109,45.8265991210937),
    (-91.0962982177734,45.8083000183105),
    (-89.0075988769531,42.5483016967773),
    (-88.7578964233398,44.6244010925292),
    (-89.3523025512695,42.9132995605468),
    (-89.0342025756835,43.3224983215332),
    (-89.5298995971679,45.6571998596191),
    (-89.8253021240234,42.9488983154296),
    (-90.1296005249023,42.9522018432617),
    (-89.1392974853515,45.1414985656738),
    (-88.5399017333984,43.8828010559082),
    (-89.1501007080078,44.4333000183105),
    (-88.8709030151367,44.0046997070312),
    (-91.2265014648437,44.2860984802246),
    (-89.6376,43.398),
    (-89.3209991455078,43.3213996887207),
    (-88.6668014526367,44.6178016662597),
    (-89.8990020751953,42.9453010559082),
    (-90.1495971679687,44.9994010925292),
    (-88.9834976196289,43.986099243164),
    (-90.8607025146484,42.8816986083984),
    (-91.9626998901367,44.6211013793945),
    (-88.0279006958007,42.5222015380859),
    (-92.6865997314453,45.7743988037109),
    (-88.4632034301757,44.8328018188476),
    (-87.9943008422851,43.3488998413085),
    (-87.9981002807617,43.2695007324218),
    (-90.345703125,43.6486015319824),
    (-89.1361999511718,44.5069007873535),
    (-89.4682006835937,43.2221984863281),
    (-88.658203125,42.5872001647949),
    (-88.9007034302,43.8765983582),
    (-88.6408996582031,43.3955001831054),
    (-88.3333969115999,42.7999992371),
    (-88.6376037597656,42.7070007324218),
    (-88.6019973754882,42.6875),
    (-90.5718002319335,42.7999992370605),
    (-88.833396911621,44),
    (-88.6676025390625,43.9249992370605),
    (-92.2031021118164,44.4989013671875),
    (-88.7759017944335,42.9486007690429),
    (-88.160400390625,43.2070007324218),
    (-87.9349975585937,44.4258003234863),
    (-90.5565032958984,44.8526992797851),
    (-88.2697982788085,44.2691993713378),
    (-90.5910034179687,42.5242004394531),
    (-87.8195037841796,42.5786018371582),
    (-87.5109024047851,44.4500007629394),
    (-88.8404006958007,42.6888999938964),
    (-89.0279006958007,42.6199989318847),
    (-88.1359024047851,42.6609001159667),
    (-89.5243988037,45.2033004761),
    (-88.4501037597656,42.625),
    (-88.3673019409179,42.5722007751464),
    (-90.043701171875,44.296100616455),
    (-88.6396026611328,44.2028007507324),
    (-88.3611984252929,42.6610984802246),
    (-89.4018020629882,43.0656013488769),
    (-89.3410034179687,43.1267013549804),
    (-88.0154037475585,42.5778007507324),
    (-87.6751022338867,44.0948982238769),
    (-89.0647964477539,43.2578010559082),
    (-89.1973037719726,42.858299255371),
    (-88.9971008300781,42.8135986328125),
    (-90.0757980346679,43.782299041748),
    (-87.725601196289,43.6786003112792),
    (-89.508102417,44.1643981934),
    (-88.0037002563476,45.5858001708984),
    (-91.925833,45.584444),
    (-91.9027023315429,44.882999420166),
    (-87.9757003784179,44.0792007446289),
    (-87.3095016479492,44.9827995300292),
    (-89.3200988769531,43.4818992614746),
    (-89.5690002441406,45.2393989562988),
    (-88.5086975097656,43.0675010681152),
    (-88.0039978027343,42.5367012023925),
    (-89.4512023925781,45.8512992858886),
    (-88.28150177,42.6735992431999),
    (-88.1867980957031,42.6488990783691),
    (-88.3722991943359,43.244701385498),
    (-89.3504028320312,43.2747001647949),
    (-92.621597290039,45.2639007568359),
    (-91.2918014526367,45.375),
    (-87.923599243164,42.5635986328125),
    (-91.5224990844726,45.6594009399414),
    (-91.8086013793945,44.6571998596191),
    (-89.0708999633789,42.7374992370605),
    (-89.7160034179687,43.7425003051757),
    (-87.8792037963867,43.0616989135742),
    (-89.8650970458984,44.0325012207031),
    (-90.6250991821289,45.4771995544433),
    (-90.1634979248046,45.9877014160156),
    (-89.7851028442382,43.6272010803222),
    (-88.3769989013671,44.4179992675781),
    (-89.524803161621,44.0133018493652),
    (-89.0158996582031,44.4080009460449),
    (-88.1333999633789,45.100299835205),
    (-89.3231964111328,43.2644004821777),
    (-91.5896987915039,45.3119010925292),
    (-89.3587036132812,44.4640998840332),
    (-89.2654037475585,43.4952011108398),
    (-89.8014984130859,44.8471984863281),
    (-88.576083,43.985045),
    (-87.7102966308593,43.7719001770019),
    (-90.820701599121,46.8935012817382),
    (-90.66259766,43.95299912),
    (-88.1395034790039,43.1638984680175),
    (-88.6894989013671,44.3946990966796),
    (-89.7472000122,45.2160987854),
    (-91.3104019165039,46.0069007873535),
    (-87.8453979492187,45.5816001892089),
    (-87.6070022583007,44.3591995239257),
    (-89.4328994750976,43.0758018493652),
    (-89.3898010253906,43.5536003112792),
    (-88.1434020996093,45.1203002929687),
    (-92.5483016967773,45.1890983581542),
    (-87.9445037841796,44.2778015136718),
    (-89.2947998046875,43.483600616455),
    (-89.4509963989257,42.9091987609863),
    (-88.8282012939453,42.9314002990722),
    (-88.45320129,44.18780136),
    (-89.4371032714843,44.2714004516601),
    (-89.07080078125,42.8400001525878),
    (-91.5127029418945,44.8119010925292),
    (-89.6623992919921,45.6994018554687),
    (-89.032600402832,42.6883010864257),
    (-92.5513000488281,45.0121994018554),
    (-90.60009765625,44.9500007629394),
    (-88.0584030151367,44.3554992675781),
    (-90.7049026489257,45.5365982055664),
    (-89.6745986938476,45.3415985107421),
    (-88.8887023925781,43.8310012817382),
    (-91.3610000610351,44.9496994018554),
    (-90.7079010009765,43.13330078125),
    (-88.8776016235351,42.9067001342773),
    (-88.5227966308593,44.0237007141113),
    (-90.6809997558593,43.352798461914),
    (-89.404800415039,43.0578002929687),
    (-87.8268966674804,42.730598449707),
    (-89.9923019409179,43.5503005981445),
    (-88.7453994750976,42.5175018310546),
    (-87.7490005493164,43.7613983154296),
    (-88.1704025268554,42.5424995422363),
    (-91.8956985473632,45.8258018493652),
    (-87.3531036376953,44.8321990966796),
    (-90.8310012817382,44.9338989257812),
    (-90.5154037475585,43.9846992492675),
    (-89.5810012817382,42.9636001586914),
    (-90.8904037475585,46.5677986145019),
    (-89.5328979492187,45.8880996704101),
    (-89.6676025390625,44.9668998718261),
    (-88.1925964355468,43.4178009033203),
    (-91.2085037231445,46.7999000549316),
    (-89.3078994750976,43.7816009521484),
    (-91.5470962524414,44.5750007629394),
    (-88.8266983032226,43.4488983154296),
    (-92.6155014038085,45.4305000305175),
    (-88.0120010375976,44.852798461914),
    (-88.5767974853515,42.5209007263183),
    (-88.8245010375976,43.163101196289),
    (-88.7457962036,43.631401062),
    (-88.8245010375976,44.4706993103027),
    (-92.6871032714843,45.6839981079101),
    (-89.4878005981445,45.5503005981445),
    (-91.926902770996,45.74169921875),
    (-92.1084976196289,45.9480018615722),
    (-88.4432983398437,45.1267013549804),
    (-90.6636962890625,43.2085990905761),
    (-89.7673034667968,42.6208000183105),
    (-90.179702758789,44.6772003173828),
    (-91.4585037231445,46.576301574707) ]

def findNearestAirport(point, allAirports):
    nearestAirportDist = 99999
    for eachAirport in allAirports:
        if haversine(point, eachAirport) < nearestAirportDist:
            nearestAirportDist = haversine(point, eachAirport)
    return nearestAirportDist

def main():
    
    allWisconsin = getWisconsin()
    furthestAirport = 0
    
    thePoint = ("butt","butt")
    
    for eachPoint in allWisconsin:
        nearestDist = findNearestAirport(eachPoint , airports)
        if nearestDist > furthestAirport:
            furthestAirport = nearestDist
            thePoint = eachPoint
    
    print(furthestAirport,thePoint)
        
# main()
