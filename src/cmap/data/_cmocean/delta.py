__license__ = "MIT"


# Used to reconstruct the colormap in pycam02ucs.cm.viscm
# parameters = {'xp': [-3.4830597643097576, 0.6289831887553419, -17.483059764309758, -36.149726430976415, -10.119506350699233, -1.5386153198653005],
#        'yp': [-16.277777777777771, -46.80680359435172, -12.0, -2.6666666666666572, -4.590430134624931, 5.8888888888888857],
#        'min_Jp': 15.1681957187,
#        'max_Jp': 98.6544342508}

delta_blue = [
    [0.06597739, 0.12386005, 0.24948116],
    [0.06865758, 0.1266325, 0.25557624],
    [0.07132312, 0.12939515, 0.26166391],
    [0.07396584, 0.13214058, 0.2677948],
    [0.07658629, 0.13486916, 0.27396904],
    [0.07919242, 0.13758843, 0.28014206],
    [0.08176925, 0.14028419, 0.28640499],
    [0.08433407, 0.14297318, 0.29265629],
    [0.08687299, 0.14564215, 0.29898019],
    [0.08939564, 0.14830082, 0.30531941],
    [0.09189721, 0.15094484, 0.311703],
    [0.09437767, 0.1535746, 0.31813071],
    [0.09684032, 0.15619402, 0.32458157],
    [0.09927797, 0.15879644, 0.33109756],
    [0.10169939, 0.16139154, 0.33762358],
    [0.10409298, 0.1639684, 0.34422672],
    [0.10647003, 0.16653949, 0.35083602],
    [0.10881765, 0.16909286, 0.35752405],
    [0.11114624, 0.1716403, 0.36422476],
    [0.11344526, 0.17417268, 0.37099405],
    [0.11572015, 0.17669703, 0.37779407],
    [0.11796711, 0.17921142, 0.38463932],
    [0.12018172, 0.18171361, 0.39154591],
    [0.12237222, 0.18421369, 0.39845983],
    [0.12451836, 0.18669519, 0.40547913],
    [0.12663654, 0.18917624, 0.41250469],
    [0.12871435, 0.19164859, 0.41958831],
    [0.13074695, 0.19411179, 0.42673806],
    [0.13274084, 0.19657524, 0.43390608],
    [0.13468282, 0.19903239, 0.44113668],
    [0.13656674, 0.2014837, 0.44843501],
    [0.13839602, 0.20393744, 0.4557622],
    [0.14016368, 0.20639447, 0.46312314],
    [0.14185409, 0.20885126, 0.47055044],
    [0.14345986, 0.21131167, 0.47803591],
    [0.14497642, 0.2137823, 0.485557],
    [0.146391, 0.21626634, 0.49311434],
    [0.14768864, 0.218768, 0.50070638],
    [0.14885173, 0.22129285, 0.50832846],
    [0.14985965, 0.22384818, 0.51597154],
    [0.1506884, 0.2264434, 0.52362079],
    [0.15131023, 0.22909058, 0.53125369],
    [0.15168425, 0.23180303, 0.53885457],
    [0.15175702, 0.23459819, 0.54640144],
    [0.15150762, 0.23750367, 0.55379602],
    [0.15085272, 0.24054407, 0.56100954],
    [0.149778, 0.24375297, 0.56790391],
    [0.1482413, 0.24715977, 0.57437788],
    [0.14626774, 0.25078506, 0.58029534],
    [0.14393556, 0.25462901, 0.58555075],
    [0.14135408, 0.25866955, 0.59010335],
    [0.13864079, 0.26286871, 0.59397852],
    [0.13589174, 0.26718438, 0.59724867],
    [0.13319563, 0.27157423, 0.60000635],
    [0.13058114, 0.2760103, 0.60234289],
    [0.12806719, 0.28047115, 0.60433583],
    [0.12569199, 0.28493491, 0.60605594],
    [0.12343537, 0.28939604, 0.60755039],
    [0.12131237, 0.29384382, 0.60886431],
    [0.1193314, 0.29827105, 0.61003449],
    [0.11747335, 0.3026784, 0.61108156],
    [0.11574105, 0.30706267, 0.61202824],
    [0.11415261, 0.31141804, 0.61290024],
    [0.11269166, 0.31574724, 0.61370617],
    [0.11135538, 0.32005035, 0.61445721],
    [0.11014377, 0.32432716, 0.6151638],
    [0.10905648, 0.32857778, 0.61583463],
    [0.10809281, 0.3328026, 0.61647697],
    [0.10725185, 0.33700217, 0.61709693],
    [0.10653241, 0.34117717, 0.61769964],
    [0.10593314, 0.34532836, 0.61828945],
    [0.1054525, 0.34945656, 0.61887003],
    [0.10508879, 0.35356261, 0.61944452],
    [0.10484013, 0.35764738, 0.62001559],
    [0.10470452, 0.36171173, 0.62058554],
    [0.10467981, 0.36575652, 0.62115635],
    [0.10476371, 0.36978259, 0.62172971],
    [0.10495382, 0.37379076, 0.62230709],
    [0.10524762, 0.37778184, 0.62288978],
    [0.10564252, 0.3817566, 0.62347886],
    [0.1061358, 0.38571579, 0.62407531],
    [0.10672471, 0.38966014, 0.62467996],
    [0.10740642, 0.39359035, 0.62529352],
    [0.10817806, 0.39750711, 0.62591662],
    [0.10903675, 0.40141105, 0.62654981],
    [0.10998202, 0.40530231, 0.62719516],
    [0.11100819, 0.40918206, 0.62785128],
    [0.11211222, 0.41305092, 0.62851837],
    [0.11329127, 0.41690943, 0.62919672],
    [0.11454253, 0.42075813, 0.62988653],
    [0.11586327, 0.42459754, 0.63058799],
    [0.11725083, 0.42842816, 0.63130122],
    [0.1187026, 0.43225046, 0.63202632],
    [0.12021702, 0.4360647, 0.63276403],
    [0.12179033, 0.43987161, 0.6335134],
    [0.1234202, 0.44367161, 0.63427436],
    [0.12510445, 0.4474651, 0.6350469],
    [0.12684102, 0.45125247, 0.63583095],
    [0.12862799, 0.45503408, 0.63662642],
    [0.13046351, 0.45881028, 0.6374332],
    [0.13234563, 0.46258148, 0.63825092],
    [0.13427263, 0.46634802, 0.63907929],
    [0.13624311, 0.4701102, 0.63991816],
    [0.13825578, 0.47386832, 0.64076733],
    [0.14030945, 0.47762263, 0.64162657],
    [0.14240307, 0.48137341, 0.64249562],
    [0.14453572, 0.48512091, 0.64337422],
    [0.14670608, 0.48886546, 0.64426159],
    [0.14891319, 0.49260737, 0.64515709],
    [0.15115711, 0.49634669, 0.64606096],
    [0.15343746, 0.50008362, 0.64697283],
    [0.15575396, 0.50381833, 0.64789234],
    [0.15810648, 0.50755096, 0.64881909],
    [0.160495, 0.51128167, 0.64975267],
    [0.16291965, 0.51501059, 0.65069263],
    [0.16538066, 0.51873781, 0.6516385],
    [0.16787709, 0.52246378, 0.65258827],
    [0.17041079, 0.52618823, 0.65354289],
    [0.17298246, 0.52991124, 0.65450185],
    [0.17559291, 0.53363281, 0.65546464],
    [0.1782431, 0.53735298, 0.65643069],
    [0.18093416, 0.54107173, 0.65739946],
    [0.18366735, 0.54478903, 0.65837034],
    [0.18644408, 0.54850484, 0.65934275],
    [0.18926596, 0.55221906, 0.66031605],
    [0.19213472, 0.5559316, 0.66128961],
    [0.19505228, 0.55964231, 0.66226278],
    [0.19802076, 0.56335105, 0.66323489],
    [0.20104242, 0.5670576, 0.66420528],
    [0.20411976, 0.57076173, 0.66517325],
    [0.20725543, 0.57446319, 0.66613812],
    [0.21045232, 0.57816165, 0.6670992],
    [0.2137135, 0.58185676, 0.66805579],
    [0.21704227, 0.58554813, 0.6690072],
    [0.22044214, 0.58923531, 0.66995277],
    [0.22391686, 0.59291779, 0.67089183],
    [0.22747037, 0.59659503, 0.67182375],
    [0.23110686, 0.6002664, 0.67274791],
    [0.23483073, 0.60393124, 0.67366376],
    [0.2386466, 0.60758879, 0.67457077],
    [0.24255928, 0.61123826, 0.67546847],
    [0.24657379, 0.61487875, 0.67635647],
    [0.25069532, 0.61850931, 0.67723446],
    [0.25492963, 0.62212933, 0.67809791],
    [0.25928228, 0.62573723, 0.67895065],
    [0.26375886, 0.62933183, 0.67979274],
    [0.26836502, 0.63291182, 0.68062438],
    [0.27310635, 0.63647586, 0.68144595],
    [0.27799067, 0.64002284, 0.68225204],
    [0.28302187, 0.64355084, 0.68304906],
    [0.28820489, 0.64705829, 0.68383831],
    [0.29354581, 0.65054365, 0.68461866],
    [0.29905039, 0.65400523, 0.68538993],
    [0.30471967, 0.65744127, 0.68615859],
    [0.31055832, 0.66085014, 0.68692427],
    [0.31656915, 0.66423017, 0.68768878],
    [0.32274951, 0.66757995, 0.68845924],
    [0.32910283, 0.67089793, 0.68923459],
    [0.33562308, 0.67418311, 0.69002275],
    [0.34230732, 0.67743451, 0.69082687],
    [0.34914976, 0.68065146, 0.69165158],
    [0.35614127, 0.68383379, 0.69250293],
    [0.36327369, 0.68698145, 0.69338491],
    [0.37053484, 0.69009497, 0.6943034],
    [0.37791226, 0.69317522, 0.69526327],
    [0.38539385, 0.69622324, 0.69626827],
    [0.39296332, 0.69924082, 0.697324],
    [0.4006094, 0.70222938, 0.69843223],
    [0.40831594, 0.70519122, 0.69959724],
    [0.41607015, 0.7081284, 0.7008209],
    [0.42386201, 0.71104276, 0.70210342],
    [0.43167256, 0.71393771, 0.70344961],
    [0.43949947, 0.71681422, 0.70485557],
    [0.44732849, 0.71967527, 0.70632366],
    [0.45514951, 0.72252334, 0.70785413],
    [0.46296115, 0.72535947, 0.70944335],
    [0.47075349, 0.72818626, 0.71109189],
    [0.47851694, 0.73100635, 0.71280025],
    [0.48625412, 0.73382019, 0.71456376],
    [0.49396102, 0.73662941, 0.716381],
    [0.50163106, 0.73943622, 0.71825179],
    [0.50925965, 0.74224248, 0.72017521],
    [0.51685029, 0.74504841, 0.72214731],
    [0.52440134, 0.74785523, 0.72416643],
    [0.53191155, 0.75066408, 0.72623094],
    [0.53938005, 0.753476, 0.72833923],
    [0.54680444, 0.75629239, 0.73049037],
    [0.55418394, 0.75911426, 0.73268299],
    [0.5615215, 0.76194178, 0.73491438],
    [0.56881727, 0.7647757, 0.73718308],
    [0.57607152, 0.76761672, 0.73948764],
    [0.58328469, 0.7704655, 0.74182668],
    [0.5904573, 0.77332263, 0.74419886],
    [0.59758995, 0.77618869, 0.74660289],
    [0.60468333, 0.77906419, 0.7490375],
    [0.61173817, 0.78194964, 0.75150151],
    [0.61875522, 0.7848455, 0.75399375],
    [0.62573528, 0.7877522, 0.7565131],
    [0.63267915, 0.79067016, 0.75905849],
    [0.63958763, 0.79359978, 0.76162887],
    [0.64646151, 0.79654145, 0.76422323],
    [0.6533016, 0.79949552, 0.76684059],
    [0.66010867, 0.80246236, 0.76948001],
    [0.66688348, 0.80544232, 0.77214056],
    [0.67362676, 0.80843573, 0.77482134],
    [0.68033922, 0.81144292, 0.77752145],
    [0.68702155, 0.81446423, 0.78024002],
    [0.69367439, 0.81749998, 0.7829762],
    [0.7002975, 0.82055075, 0.78572944],
    [0.70689165, 0.82361681, 0.78849881],
    [0.71345823, 0.82669826, 0.79128316],
    [0.7199978, 0.82979542, 0.79408159],
    [0.72651088, 0.83290861, 0.7968932],
    [0.73299796, 0.83603816, 0.79971707],
    [0.73945951, 0.8391844, 0.80255223],
    [0.74589598, 0.84234767, 0.8053977],
    [0.7523078, 0.84552831, 0.80825242],
    [0.75869517, 0.84872673, 0.81111536],
    [0.76505775, 0.85194348, 0.81398568],
    [0.77139709, 0.85517859, 0.81686163],
    [0.77771359, 0.85843239, 0.81974187],
    [0.78400765, 0.86170526, 0.82262493],
    [0.79027967, 0.86499755, 0.82550921],
    [0.79653012, 0.8683096, 0.82839299],
    [0.8027595, 0.87164177, 0.83127437],
    [0.80896806, 0.87499448, 0.83415141],
    [0.8151567, 0.87836796, 0.83702171],
    [0.82132643, 0.88176244, 0.83988264],
    [0.82747812, 0.88517819, 0.84273144],
    [0.83361281, 0.88861542, 0.8455651],
    [0.83973174, 0.89207431, 0.84838033],
    [0.84583638, 0.89555495, 0.85117353],
    [0.85192854, 0.89905734, 0.85394079],
    [0.85801043, 0.90258135, 0.85667786],
    [0.86408444, 0.90612679, 0.85938032],
    [0.87015339, 0.9096933, 0.86204351],
    [0.87622047, 0.9132804, 0.8646626],
    [0.88228934, 0.9168874, 0.86723268],
    [0.88836402, 0.92051348, 0.86974885],
    [0.89444909, 0.92415756, 0.87220619],
    [0.90054949, 0.92781839, 0.87459995],
    [0.90666975, 0.93149475, 0.87692634],
    [0.91281478, 0.93518523, 0.87918186],
    [0.91898934, 0.93888836, 0.88136368],
    [0.92519787, 0.94260271, 0.88346979],
    [0.93144429, 0.94632694, 0.88549899],
    [0.93773184, 0.95005986, 0.88745092],
    [0.94406341, 0.95380038, 0.88932539],
    [0.95044015, 0.95754793, 0.89112376],
    [0.95686223, 0.96130226, 0.89284794],
    [0.963329, 0.96506343, 0.8944999],
    [0.96983887, 0.96883187, 0.89608183],
    [0.97638938, 0.97260834, 0.89759591],
    [0.98297732, 0.97639393, 0.89904421],
    [0.98959887, 0.98019003, 0.90042859],
    [0.99624974, 0.98399826, 0.90175064],
]


# # Used to reconstruct the colormap in pycam02ucs.cm.viscm
# parameters = {'xp': [-6.5021965791219287, -21.571501186307515, -24.083051954171779, -33.292071436340748, 3.7300472899546975, 0.56735373042192094, -3.0604418231597919],
#        'yp': [6.410835628206474, 4.8294888484400857, 18.503487473478852, 30.131037324702294, 39.433077205681045, 22.596385021109501, 11.992059556793727],
#        'min_Jp': 15.0,
#        'max_Jp': 98.6544342508}

delta_green = [
    [0.09053276, 0.13733861, 0.07325761],
    [0.09149314, 0.14105046, 0.07638733],
    [0.09241015, 0.14475747, 0.07947497],
    [0.09328192, 0.14846061, 0.08252095],
    [0.09408911, 0.15216506, 0.08552629],
    [0.09484852, 0.15586693, 0.08848984],
    [0.0955584, 0.15956697, 0.09141177],
    [0.09620477, 0.16326879, 0.09429209],
    [0.09679537, 0.1669707, 0.09713043],
    [0.09733238, 0.17067237, 0.09992671],
    [0.09781114, 0.17437504, 0.10268064],
    [0.0982227, 0.17808082, 0.10539142],
    [0.09857703, 0.18178753, 0.10805922],
    [0.09887273, 0.18549555, 0.11068374],
    [0.09910575, 0.18920581, 0.11326433],
    [0.099269, 0.19291982, 0.11579981],
    [0.09937074, 0.19663577, 0.11829057],
    [0.09940988, 0.2003539, 0.12073611],
    [0.09938537, 0.20407438, 0.12313591],
    [0.09929071, 0.20779846, 0.12548854],
    [0.09912769, 0.21152567, 0.12779367],
    [0.09889926, 0.21525533, 0.13005125],
    [0.09860476, 0.21898749, 0.13226069],
    [0.09824359, 0.22272214, 0.13442135],
    [0.09781527, 0.22645927, 0.13653262],
    [0.09731337, 0.2301999, 0.13859263],
    [0.09674403, 0.23394277, 0.14060198],
    [0.09610733, 0.23768772, 0.14256015],
    [0.09540319, 0.24143464, 0.14446653],
    [0.09463164, 0.24518338, 0.14632057],
    [0.09379283, 0.24893377, 0.14812169],
    [0.09288704, 0.25268563, 0.14986937],
    [0.09191348, 0.25643894, 0.15156278],
    [0.09087165, 0.26019363, 0.15320113],
    [0.08976486, 0.26394904, 0.15478462],
    [0.08859393, 0.26770495, 0.1563128],
    [0.08735983, 0.27146109, 0.15778524],
    [0.08606372, 0.27521722, 0.15920155],
    [0.08470696, 0.27897306, 0.16056134],
    [0.0832911, 0.28272833, 0.16186426],
    [0.08181798, 0.28648275, 0.16310997],
    [0.08028966, 0.29023603, 0.16429815],
    [0.07870853, 0.29398786, 0.1654285],
    [0.07707731, 0.29773796, 0.16650073],
    [0.07539909, 0.30148601, 0.16751459],
    [0.0736774, 0.3052317, 0.16846982],
    [0.07191583, 0.30897477, 0.16936603],
    [0.07011887, 0.31271491, 0.17020297],
    [0.06829236, 0.31645172, 0.17098061],
    [0.06644218, 0.3201849, 0.17169874],
    [0.06457505, 0.32391411, 0.17235714],
    [0.06269859, 0.32763902, 0.1729556],
    [0.06082143, 0.33135932, 0.17349393],
    [0.05895335, 0.33507466, 0.17397193],
    [0.05710539, 0.33878471, 0.1743894],
    [0.05528998, 0.34248913, 0.17474614],
    [0.05352104, 0.34618758, 0.17504196],
    [0.05181408, 0.34987969, 0.17527666],
    [0.05018627, 0.35356513, 0.17545005],
    [0.04865644, 0.35724353, 0.17556193],
    [0.04724506, 0.36091453, 0.17561211],
    [0.04597406, 0.36457776, 0.1756004],
    [0.04486662, 0.36823283, 0.17552659],
    [0.04394675, 0.37187939, 0.17539051],
    [0.04323878, 0.37551702, 0.17519196],
    [0.04276673, 0.37914535, 0.17493074],
    [0.04255352, 0.38276397, 0.17460669],
    [0.04262018, 0.38637248, 0.17421963],
    [0.04298497, 0.38997047, 0.17376937],
    [0.04366274, 0.39355751, 0.17325577],
    [0.04466372, 0.39713324, 0.17267831],
    [0.04599481, 0.40069717, 0.1720371],
    [0.04765813, 0.40424888, 0.17133208],
    [0.04965139, 0.40778792, 0.17056314],
    [0.05196846, 0.41131384, 0.16973019],
    [0.05459993, 0.41482619, 0.16883316],
    [0.05753382, 0.41832454, 0.16787201],
    [0.06075626, 0.42180841, 0.16684671],
    [0.06425218, 0.42527736, 0.1657573],
    [0.06800589, 0.42873094, 0.16460379],
    [0.07200158, 0.43216868, 0.16338628],
    [0.07622371, 0.43559013, 0.16210488],
    [0.08065728, 0.43899485, 0.16075975],
    [0.08528802, 0.4423824, 0.15935107],
    [0.09010251, 0.44575233, 0.15787909],
    [0.09508832, 0.44910425, 0.15634337],
    [0.10023389, 0.4524377, 0.15474474],
    [0.10552844, 0.45575227, 0.15308384],
    [0.11096207, 0.45904759, 0.15136111],
    [0.11652565, 0.46232325, 0.14957707],
    [0.12221076, 0.46557892, 0.14773227],
    [0.12800964, 0.46881425, 0.14582732],
    [0.1339151, 0.47202893, 0.14386292],
    [0.13992049, 0.47522266, 0.14183978],
    [0.14601973, 0.47839518, 0.13975846],
    [0.15220721, 0.48154623, 0.13761954],
    [0.15847719, 0.48467561, 0.13542453],
    [0.16482456, 0.48778316, 0.13317442],
    [0.17124448, 0.49086871, 0.13087024],
    [0.1777324, 0.49393216, 0.12851305],
    [0.18428396, 0.49697343, 0.126104],
    [0.19089503, 0.49999248, 0.12364426],
    [0.19756167, 0.50298929, 0.12113505],
    [0.20428009, 0.50596389, 0.11857764],
    [0.21104652, 0.50891636, 0.11597358],
    [0.21785748, 0.51184679, 0.11332427],
    [0.22470961, 0.51475531, 0.11063114],
    [0.23159967, 0.5176421, 0.1078957],
    [0.23852458, 0.52050736, 0.10511948],
    [0.24548136, 0.52335131, 0.10230412],
    [0.25246703, 0.52617424, 0.09945144],
    [0.25947856, 0.52897647, 0.09656369],
    [0.26651361, 0.5317583, 0.09364228],
    [0.27356965, 0.53452006, 0.09068917],
    [0.2806443, 0.53726212, 0.08770643],
    [0.28773525, 0.53998488, 0.08469633],
    [0.29484032, 0.54268874, 0.08166129],
    [0.30195743, 0.54537413, 0.07860394],
    [0.3090846, 0.5480415, 0.07552722],
    [0.31621948, 0.55069139, 0.07243519],
    [0.32336047, 0.55332424, 0.06933118],
    [0.3305062, 0.55594049, 0.0662188],
    [0.33765509, 0.55854062, 0.06310264],
    [0.34480568, 0.56112513, 0.05998797],
    [0.35195658, 0.56369452, 0.05688086],
    [0.3591065, 0.56624928, 0.05378828],
    [0.36625424, 0.56878993, 0.05071836],
    [0.37339864, 0.57131697, 0.0476805],
    [0.38053866, 0.57383092, 0.04468567],
    [0.38767326, 0.57633228, 0.04174672],
    [0.39480098, 0.5788217, 0.0388712],
    [0.4019216, 0.58129953, 0.03616635],
    [0.40903431, 0.58376629, 0.03367283],
    [0.41613836, 0.58622247, 0.03139676],
    [0.42323306, 0.58866858, 0.02934437],
    [0.43031775, 0.5911051, 0.02752213],
    [0.43739183, 0.59353253, 0.0259367],
    [0.44445471, 0.59595137, 0.024595],
    [0.45150585, 0.5983621, 0.02350422],
    [0.45854471, 0.60076521, 0.02267188],
    [0.46557081, 0.60316118, 0.0221058],
    [0.47258366, 0.6055505, 0.02181419],
    [0.47958278, 0.60793365, 0.02180565],
    [0.48656773, 0.61031113, 0.02208919],
    [0.49353805, 0.61268341, 0.02267429],
    [0.50049318, 0.61505101, 0.02357107],
    [0.50743284, 0.61741438, 0.02478977],
    [0.51435656, 0.61977401, 0.02634145],
    [0.52126388, 0.62213041, 0.02823776],
    [0.52815431, 0.62448406, 0.03049096],
    [0.53502735, 0.6268355, 0.033114],
    [0.54188249, 0.62918522, 0.03612051],
    [0.54871918, 0.63153377, 0.03952488],
    [0.55553684, 0.63388168, 0.04323651],
    [0.56233489, 0.6362295, 0.04713774],
    [0.56911267, 0.6385778, 0.05121917],
    [0.5758695, 0.64092715, 0.05546448],
    [0.58260468, 0.64327815, 0.05985969],
    [0.58931743, 0.64563142, 0.06439288],
    [0.59600693, 0.64798759, 0.06905401],
    [0.60267232, 0.65034731, 0.0738347],
    [0.60931267, 0.65271125, 0.078728],
    [0.61592727, 0.65508003, 0.08372822],
    [0.62251497, 0.65745441, 0.08883077],
    [0.62907452, 0.65983518, 0.09403193],
    [0.63560473, 0.66222315, 0.09932877],
    [0.64210433, 0.66461911, 0.10471901],
    [0.64857199, 0.66702394, 0.11020095],
    [0.65500629, 0.66943851, 0.11577336],
    [0.66140573, 0.67186375, 0.1214354],
    [0.66776872, 0.67430062, 0.12718656],
    [0.67409362, 0.67675013, 0.13302663],
    [0.68037867, 0.67921331, 0.13895556],
    [0.68662205, 0.68169124, 0.14497353],
    [0.69282238, 0.68418481, 0.15108128],
    [0.69897728, 0.68669535, 0.15727889],
    [0.70508453, 0.68922412, 0.16356662],
    [0.71114201, 0.69177235, 0.16994487],
    [0.71714753, 0.6943413, 0.17641399],
    [0.72309885, 0.69693228, 0.18297431],
    [0.72899368, 0.6995466, 0.18962605],
    [0.73482974, 0.70218562, 0.1963693],
    [0.74060474, 0.70485066, 0.20320411],
    [0.7463166, 0.70754299, 0.2101307],
    [0.75196261, 0.71026417, 0.21714799],
    [0.75754052, 0.71301555, 0.22425532],
    [0.76304813, 0.7157985, 0.23145177],
    [0.76848332, 0.71861432, 0.2387362],
    [0.77384408, 0.72146431, 0.2461072],
    [0.77912853, 0.7243497, 0.25356307],
    [0.78433484, 0.72727172, 0.2611016],
    [0.7894614, 0.73023149, 0.26872033],
    [0.79450691, 0.73323004, 0.27641686],
    [0.79947022, 0.73626828, 0.2841884],
    [0.80435041, 0.73934706, 0.29203197],
    [0.80914682, 0.74246709, 0.29994435],
    [0.81385901, 0.74562899, 0.30792214],
    [0.81848682, 0.74883326, 0.31596178],
    [0.82303017, 0.75208041, 0.32405836],
    [0.8274895, 0.75537065, 0.33220817],
    [0.83186554, 0.75870402, 0.34040823],
    [0.83615916, 0.76208053, 0.34865469],
    [0.84037142, 0.76550008, 0.35694373],
    [0.84450364, 0.76896245, 0.36527157],
    [0.84855731, 0.77246735, 0.37363449],
    [0.8525341, 0.77601436, 0.38202889],
    [0.85643585, 0.77960299, 0.39045126],
    [0.86026452, 0.78323268, 0.39889826],
    [0.8640222, 0.7869028, 0.4073667],
    [0.86771108, 0.79061266, 0.41585355],
    [0.87133343, 0.79436152, 0.42435598],
    [0.87489155, 0.7981486, 0.43287135],
    [0.87838781, 0.8019731, 0.4413972],
    [0.88182459, 0.80583419, 0.44993127],
    [0.88520428, 0.80973103, 0.45847151],
    [0.88852927, 0.81366275, 0.46701603],
    [0.89180194, 0.81762851, 0.47556314],
    [0.89502462, 0.82162744, 0.4841113],
    [0.89819963, 0.82565871, 0.49265916],
    [0.90132924, 0.82972148, 0.50120551],
    [0.90441569, 0.83381493, 0.50974926],
    [0.90746117, 0.83793825, 0.51828947],
    [0.9104678, 0.84209066, 0.52682531],
    [0.91343769, 0.84627138, 0.53535605],
    [0.91637286, 0.85047967, 0.54388105],
    [0.9192753, 0.85471481, 0.55239974],
    [0.92214698, 0.85897609, 0.56091165],
    [0.9249901, 0.86326276, 0.56941517],
    [0.92780705, 0.86757406, 0.57790823],
    [0.93059881, 0.87190949, 0.5863936],
    [0.93336714, 0.87626844, 0.59487104],
    [0.93611377, 0.88065031, 0.60334038],
    [0.93884038, 0.88505451, 0.61180142],
    [0.94154864, 0.88948047, 0.620254],
    [0.94424022, 0.89392765, 0.62869796],
    [0.94691718, 0.89839541, 0.63713184],
    [0.94958118, 0.90288322, 0.6455555],
    [0.95223308, 0.90739072, 0.65397092],
    [0.95487445, 0.91191742, 0.66237802],
    [0.95750683, 0.91646282, 0.67077672],
    [0.96013179, 0.92102646, 0.67916692],
    [0.96275088, 0.92560786, 0.68754852],
    [0.96536576, 0.93020653, 0.69592114],
    [0.96797753, 0.93482212, 0.70428588],
    [0.97058766, 0.93945419, 0.71264291],
    [0.97319768, 0.9441023, 0.72099216],
    [0.97580917, 0.94876601, 0.72933356],
    [0.97842373, 0.95344486, 0.73766705],
    [0.98104259, 0.95813849, 0.74599345],
    [0.98366662, 0.9628466, 0.75431452],
    [0.98629803, 0.96756863, 0.76262887],
    [0.98893848, 0.97230412, 0.77093649],
    [0.99158968, 0.97705259, 0.77923744],
    [0.99425336, 0.98181358, 0.78753178],
    [0.9969313, 0.98658659, 0.79581965],
    [0.99962532, 0.99137112, 0.80410124],
]

delta = delta_blue[::1] + delta_green[-2::-1]