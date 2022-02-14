#!/usr/bin/env python3
"""
[ Cartesian x Spherical ] conversion matrices
"""

import numpy as np

def cart_sphe(n):
  if n == 0:
       return np.array([[1.0]])

  if n == 1:
       result = np.zeros( (3,3) )
       result [ 2, 0] = 1.0
       result [ 0, 1] = 1.0
       result [ 1, 2] = 1.0
       return result

  if n == 2:
       result = np.zeros( (6,5) )
       result[ 0, 0] = -0.5
       result[ 3, 0] = -0.5
       result[ 5, 0] = 1.0
       result[ 2, 1] = 1.0
       result[ 4, 2] = 1.0
       result[ 0, 3] = 0.86602540378443864676
       result[ 3, 3] = -0.86602540378443864676
       result[ 1, 4] = 1.0
       return result

  if n == 3:
       result = np.zeros( (10,7) )
       result[ 2, 0] = -0.67082039324993690892
       result[ 7, 0] = -0.67082039324993690892
       result[ 9, 0] = 1.0
       result[ 0, 1] = -0.61237243569579452455
       result[ 3, 1] = -0.27386127875258305673
       result[ 5, 1] = 1.0954451150103322269
       result[ 1, 2] = -0.27386127875258305673
       result[ 6, 2] = -0.61237243569579452455
       result[ 8, 2] = 1.0954451150103322269
       result[ 2, 3] = 0.86602540378443864676
       result[ 7, 3] = -0.86602540378443864676
       result[ 4, 4] = 1.0
       result[ 0, 5] = 0.790569415042094833
       result[ 3, 5] = -1.0606601717798212866
       result[ 1, 6] = 1.0606601717798212866
       result[ 6, 6] = -0.790569415042094833
       return result

  if n == 4:
       result = np.zeros( (15,9) )
       result[ 0, 0] = 0.375
       result[ 3, 0] = 0.21957751641341996535
       result[ 5, 0] = -0.87831006565367986142
       result[10, 0] = 0.375
       result[12, 0] = -0.87831006565367986142
       result[14, 0] = 1.0
       result[ 2, 1] = -0.89642145700079522998
       result[ 7, 1] = -0.40089186286863657703
       result[9, 1] = 1.19522860933439364
       result[ 4, 2] = -0.40089186286863657703
       result[11, 2] = -0.89642145700079522998
       result[13, 2] = 1.19522860933439364
       result[ 0, 3] = -0.5590169943749474241
       result[ 5, 3] = 0.9819805060619657157
       result[10, 3] = 0.5590169943749474241
       result[12, 3] = -0.9819805060619657157
       result[ 1, 4] = -0.42257712736425828875
       result[ 6, 4] = -0.42257712736425828875
       result[ 8, 4] = 1.1338934190276816816
       result[ 2, 5] = 0.790569415042094833
       result[ 7, 5] = -1.0606601717798212866
       result[ 4, 6] = 1.0606601717798212866
       result[11, 6] = -0.790569415042094833
       result[ 0, 7] = 0.73950997288745200532
       result[ 3, 7] = -1.2990381056766579701
       result[10, 7] = 0.73950997288745200532
       result[ 1, 8] = 1.1180339887498948482
       result[ 6, 8] = -1.1180339887498948482
       return result

  if n == 5:
       result = np.zeros( (21,11) )
       result[ 2, 0] = 0.625
       result[ 7, 0] = 0.36596252735569994226
       result[ 9, 0] = -1.0910894511799619063
       result[16, 0] = 0.625
       result[18, 0] = -1.0910894511799619063
       result[20, 0] = 1.0
       result[ 0, 1] = 0.48412291827592711065
       result[ 3, 1] = 0.21128856368212914438
       result[ 5, 1] = -1.2677313820927748663
       result[10, 1] = 0.16137430609197570355
       result[12, 1] = -0.56694670951384084082
       result[14, 1] = 1.2909944487358056284
       result[ 1, 2] = 0.16137430609197570355
       result[ 6, 2] = 0.21128856368212914438
       result[ 8, 2] = -0.56694670951384084082
       result[15, 2] = 0.48412291827592711065
       result[17, 2] = -1.2677313820927748663
       result[19, 2] = 1.2909944487358056284
       result[ 2, 3] = -0.85391256382996653194
       result[ 9, 3] = 1.1180339887498948482
       result[16, 3] = 0.85391256382996653194
       result[18, 3] = -1.1180339887498948482
       result[ 4, 4] = -0.6454972243679028142
       result[11, 4] = -0.6454972243679028142
       result[13, 4] = 1.2909944487358056284
       result[ 0, 5] = -0.52291251658379721749
       result[ 3, 5] = 0.22821773229381921394
       result[ 5, 5] = 0.91287092917527685576
       result[10, 5] = 0.52291251658379721749
       result[12, 5] = -1.2247448713915890491
       result[ 1, 6] = -0.52291251658379721749
       result[ 6, 6] = -0.22821773229381921394
       result[ 8, 6] = 1.2247448713915890491
       result[15, 6] = 0.52291251658379721749
       result[17, 6] = -0.91287092917527685576
       result[ 2, 7] = 0.73950997288745200532
       result[ 7, 7] = -1.2990381056766579701
       result[16, 7] = 0.73950997288745200532
       result[ 4, 8] = 1.1180339887498948482
       result[11, 8] = -1.1180339887498948482
       result[ 0, 9] = 0.7015607600201140098
       result[ 3, 9] = -1.5309310892394863114
       result[10, 9] = 1.169267933366856683
       result[ 1,10] = 1.169267933366856683
       result[ 6,10] = -1.5309310892394863114
       result[15,10] = 0.7015607600201140098
       return result

  if n == 6:
       result = np.zeros( (28,13) )
       result[ 0, 0] = -0.3125
       result[ 3, 0] = -0.16319780245846672329
       result[ 5, 0] = 0.97918681475080033975
       result[10, 0] = -0.16319780245846672329
       result[12, 0] = 0.57335309036732873772
       result[14, 0] = -1.3055824196677337863
       result[21, 0] = -0.3125
       result[23, 0] = 0.97918681475080033975
       result[25, 0] = -1.3055824196677337863
       result[27, 0] = 1.0
       result[ 2, 1] = 0.86356159963469679725
       result[ 7, 1] = 0.37688918072220452831
       result[ 9, 1] = -1.6854996561581052156
       result[16, 1] = 0.28785386654489893242
       result[18, 1] = -0.75377836144440905662
       result[20, 1] = 1.3816985594155148756
       result[ 4, 2] = 0.28785386654489893242
       result[11, 2] = 0.37688918072220452831
       result[13, 2] = -0.75377836144440905662
       result[22, 2] = 0.86356159963469679725
       result[24, 2] = -1.6854996561581052156
       result[26, 2] = 1.3816985594155148756
       result[ 0, 3] = 0.45285552331841995543
       result[ 3, 3] = 0.078832027985861408788
       result[ 5, 3] = -1.2613124477737825406
       result[10, 3] = -0.078832027985861408788
       result[14, 3] = 1.2613124477737825406
       result[21, 3] = -0.45285552331841995543
       result[23, 3] = 1.2613124477737825406
       result[25, 3] = -1.2613124477737825406
       result[ 1, 4] = 0.27308215547040717681
       result[ 6, 4] = 0.26650089544451304287
       result[ 8, 4] = -0.95346258924559231545
       result[15, 4] = 0.27308215547040717681
       result[17, 4] = -0.95346258924559231545
       result[19, 4] = 1.4564381625088382763
       result[ 2, 5] = -0.81924646641122153043
       result[ 7, 5] = 0.35754847096709711829
       result[ 9, 5] = 1.0660035817780521715
       result[16, 5] = 0.81924646641122153043
       result[18, 5] = -1.4301938838683884732
       result[ 4, 6] = -0.81924646641122153043
       result[11, 6] = -0.35754847096709711829
       result[13, 6] = 1.4301938838683884732
       result[22, 6] = 0.81924646641122153043
       result[24, 6] = -1.0660035817780521715
       result[ 0, 7] = -0.49607837082461073572
       result[ 3, 7] = 0.43178079981734839863
       result[ 5, 7] = 0.86356159963469679725
       result[10, 7] = 0.43178079981734839863
       result[12, 7] = -1.5169496905422946941
       result[21, 7] = -0.49607837082461073572
       result[23, 7] = 0.86356159963469679725
       result[ 1, 8] = -0.59829302641309923139
       result[ 8, 8] = 1.3055824196677337863
       result[15, 8] = 0.59829302641309923139
       result[17, 8] = -1.3055824196677337863
       result[ 2, 9] = 0.7015607600201140098
       result[ 7, 9] = -1.5309310892394863114
       result[16, 9] = 1.169267933366856683
       result[ 4,10] = 1.169267933366856683
       result[11,10] = -1.5309310892394863114
       result[22,10] = 0.7015607600201140098
       result[ 0,11] = 0.67169328938139615748
       result[ 3,11] = -1.7539019000502850245
       result[10,11] = 1.7539019000502850245
       result[21,11] = -0.67169328938139615748
       result[ 1,12] = 1.2151388809514737933
       result[ 6,12] = -1.9764235376052370825
       result[15,12] = 1.2151388809514737933
       return result

       return result

  if n == 7:
       result = np.zeros( (36,15) )
       result[ 2, 0] = -0.60670333962134435221
       result[ 7, 0] = -0.31684048566533184861
       result[ 9, 0] = 1.4169537279434593918
       result[16, 0] = -0.31684048566533184861
       result[18, 0] = 0.82968314787883083417
       result[20, 0] = -1.5208343311935928733
       result[29, 0] = -0.60670333962134435221
       result[31, 0] = 1.4169537279434593918
       result[33, 0] = -1.5208343311935928733
       result[35, 0] = 1.0
       result[ 0, 1] = -0.41339864235384227977
       result[ 3, 1] = -0.17963167078872714852
       result[ 5, 1] = 1.4370533663098171882
       result[10, 1] = -0.1338895422651523892
       result[12, 1] = 0.62718150750531807803
       result[14, 1] = -2.1422326762424382273
       result[21, 1] = -0.1146561540164598136
       result[23, 1] = 0.47901778876993906273
       result[25, 1] = -0.95803557753987812546
       result[27, 1] = 1.4675987714106856141
       result[ 1, 2] = -0.1146561540164598136
       result[ 6, 2] = -0.1338895422651523892
       result[ 8, 2] = 0.47901778876993906273
       result[15, 2] = -0.17963167078872714852
       result[17, 2] = 0.62718150750531807803
       result[19, 2] = -0.95803557753987812546
       result[28, 2] = -0.41339864235384227977
       result[30, 2] = 1.4370533663098171882
       result[32, 2] = -2.1422326762424382273
       result[34, 2] = 1.4675987714106856141
       result[ 2, 3] = 0.84254721963085980365
       result[ 7, 3] = 0.14666864502533059662
       result[ 9, 3] = -1.7491256557036030854
       result[16, 3] = -0.14666864502533059662
       result[20, 3] = 1.4080189922431737275
       result[29, 3] = -0.84254721963085980365
       result[31, 3] = 1.7491256557036030854
       result[33, 3] = -1.4080189922431737275
       result[ 4, 4] = 0.50807509012231371428
       result[11, 4] = 0.49583051751369852316
       result[13, 4] = -1.3222147133698627284
       result[22, 4] = 0.50807509012231371428
       result[24, 4] = -1.3222147133698627284
       result[26, 4] = 1.6258402883914038857
       result[ 0, 5] = 0.42961647140211000062
       result[ 3, 5] = -0.062226236090912312563
       result[ 5, 5] = -1.2445247218182462513
       result[10, 5] = -0.23190348980538452414
       result[12, 5] = 0.54315511828342602619
       result[14, 5] = 1.2368186122953841287
       result[21, 5] = -0.35746251148251142922
       result[23, 5] = 1.2445247218182462513
       result[25, 5] = -1.6593662957576616683
       result[ 1, 6] = 0.35746251148251142922
       result[ 6, 6] = 0.23190348980538452414
       result[ 8, 6] = -1.2445247218182462513
       result[15, 6] = 0.062226236090912312563
       result[17, 6] = -0.54315511828342602619
       result[19, 6] = 1.6593662957576616683
       result[28, 6] = -0.42961647140211000062
       result[30, 6] = 1.2445247218182462513
       result[32, 6] = -1.2368186122953841287
       result[ 2, 7] = -0.79037935147039945351
       result[ 7, 7] = 0.6879369240987588816
       result[ 9, 7] = 1.025515817677958738
       result[16, 7] = 0.6879369240987588816
       result[18, 7] = -1.8014417303072302517
       result[29, 7] = -0.79037935147039945351
       result[31, 7] = 1.025515817677958738
       result[ 4, 8] = -0.95323336395336381126
       result[13, 8] = 1.5504341823651057024
       result[22, 8] = 0.95323336395336381126
       result[24, 8] = -1.5504341823651057024
       result[ 0, 9] = -0.47495887979908323849
       result[ 3, 9] = 0.61914323168888299344
       result[ 5, 9] = 0.82552430891851065792
       result[10, 9] = 0.25637895441948968451
       result[12, 9] = -1.8014417303072302517
       result[21, 9] = -0.65864945955866621126
       result[23, 9] = 1.3758738481975177632
       result[ 1,10] = -0.65864945955866621126
       result[ 6,10] = 0.25637895441948968451
       result[ 8,10] = 1.3758738481975177632
       result[15,10] = 0.61914323168888299344
       result[17,10] = -1.8014417303072302517
       result[28,10] = -0.47495887979908323849
       result[30,10] = 0.82552430891851065792
       result[ 2,11] = 0.67169328938139615748
       result[ 7,11] = -1.7539019000502850245
       result[16,11] = 1.7539019000502850245
       result[29,11] = -0.67169328938139615748
       result[ 4,12] = 1.2151388809514737933
       result[11,12] = -1.9764235376052370825
       result[22,12] = 1.2151388809514737933
       result[ 0,13] = 0.64725984928774934788
       result[ 3,13] = -1.96875
       result[10,13] = 2.4456993503903949804
       result[21,13] = -1.2566230789301937693
       result[ 1,14] = 1.2566230789301937693
       result[ 6,14] = -2.4456993503903949804
       result[15,14] = 1.96875
       result[28,14] = -0.64725984928774934788
       return result

  if n == 8:
       result = np.zeros( (45,17) )
       result[ 0, 0] = 0.2734375
       result[ 3, 0] = 0.13566299095694674896
       result[ 5, 0] = -1.0853039276555739917
       result[10, 0] = 0.12099545906566282998
       result[12, 0] = -0.56678149117738375672
       result[14, 0] = 1.9359273450506052797
       result[21, 0] = 0.13566299095694674896
       result[23, 0] = -0.56678149117738375672
       result[25, 0] = 1.1335629823547675134
       result[27, 0] = -1.7364862842489183867
       result[36, 0] = 0.2734375
       result[38, 0] = -1.0853039276555739917
       result[40, 0] = 1.9359273450506052797
       result[42, 0] = -1.7364862842489183867
       result[44, 0] = 1.0
       result[ 2, 1] = -0.84721510698287244363
       result[ 7, 1] = -0.36813537731583001376
       result[ 9, 1] = 2.1951352762686132731
       result[16, 1] = -0.27439190953357665914
       result[18, 1] = 0.95803557753987812546
       result[20, 1] = -2.6341623315223359277
       result[29, 1] = -0.23497519304418891392
       result[31, 1] = 0.73171175875620442437
       result[33, 1] = -1.178033207410656044
       result[35, 1] = 1.5491933384829667541
       result[ 4, 2] = -0.23497519304418891392
       result[11, 2] = -0.27439190953357665914
       result[13, 2] = 0.73171175875620442437
       result[22, 2] = -0.36813537731583001376
       result[24, 2] = 0.95803557753987812546
       result[26, 2] = -1.178033207410656044
       result[37, 2] = -0.84721510698287244363
       result[39, 2] = 2.1951352762686132731
       result[41, 2] = -2.6341623315223359277
       result[43, 2] = 1.5491933384829667541
       result[ 0, 3] = -0.39218438743784791311
       result[ 3, 3] = -0.0972889728117695298
       result[ 5, 3] = 1.459334592176542947
       result[12, 3] = 0.25403754506115685714
       result[14, 3] = -2.3138757483972597747
       result[21, 3] = 0.0972889728117695298
       result[23, 3] = -0.25403754506115685714
       result[27, 3] = 1.5566235649883124768
       result[36, 3] = 0.39218438743784791311
       result[38, 3] = -1.459334592176542947
       result[40, 3] = 2.3138757483972597747
       result[42, 3] = -1.5566235649883124768
       result[ 1, 4] = -0.20252314682524563222
       result[ 6, 4] = -0.1967766362666553471
       result[ 8, 4] = 0.8800118701519835797
       result[15, 4] = -0.1967766362666553471
       result[17, 4] = 0.85880364827689588344
       result[19, 4] = -1.7491256557036030854
       result[28, 4] = -0.20252314682524563222
       result[30, 4] = 0.8800118701519835797
       result[32, 4] = -1.7491256557036030854
       result[34, 4] = 1.7974340685458342478
       result[ 2, 5] = 0.82265291131801144316
       result[ 7, 5] = -0.11915417049417047641
       result[ 9, 5] = -1.7762455001837659611
       result[16, 5] = -0.44406137504594149028
       result[18, 5] = 0.77521709118255285119
       result[20, 5] = 1.4209964001470127689
       result[29, 5] = -0.68448859700003543819
       result[31, 5] = 1.7762455001837659611
       result[33, 5] = -1.9064667279067276225
       result[ 4, 6] = 0.68448859700003543819
       result[11, 6] = 0.44406137504594149028
       result[13, 6] = -1.7762455001837659611
       result[22, 6] = 0.11915417049417047641
       result[24, 6] = -0.77521709118255285119
       result[26, 6] = 1.9064667279067276225
       result[37, 6] = -0.82265291131801144316
       result[39, 6] = 1.7762455001837659611
       result[41, 6] = -1.4209964001470127689
       result[ 0, 7] = 0.41132645565900572158
       result[ 3, 7] = -0.20407507102873838124
       result[ 5, 7] = -1.2244504261724302874
       result[10, 7] = -0.3033516698106721761
       result[12, 7] = 1.0657473001102595767
       result[14, 7] = 1.2134066792426887044
       result[21, 7] = -0.20407507102873838124
       result[23, 7] = 1.0657473001102595767
       result[25, 7] = -2.1314946002205191534
       result[36, 7] = 0.41132645565900572158
       result[38, 7] = -1.2244504261724302874
       result[40, 7] = 1.2134066792426887044
       result[ 1, 8] = 0.42481613669916071115
       result[ 6, 8] = 0.13758738481975177632
       result[ 8, 8] = -1.4767427774562605828
       result[15, 8] = -0.13758738481975177632
       result[19, 8] = 1.8344984642633570176
       result[28, 8] = -0.42481613669916071115
       result[30, 8] = 1.4767427774562605828
       result[32, 8] = -1.8344984642633570176
       result[ 2, 9] = -0.76584818175667166625
       result[ 7, 9] = 0.99833846339806020718
       result[ 9, 9] = 0.99215674164922147144
       result[16, 9] = 0.41339864235384227977
       result[18, 9] = -2.1650635094610966169
       result[29, 9] = -1.0620403417479017779
       result[31, 9] = 1.6535945694153691191
       result[ 4,10] = -1.0620403417479017779
       result[11,10] = 0.41339864235384227977
       result[13,10] = 1.6535945694153691191
       result[22,10] = 0.99833846339806020718
       result[24,10] = -2.1650635094610966169
       result[37,10] = -0.76584818175667166625
       result[39,10] = 0.99215674164922147144
       result[ 0,11] = -0.45768182862115030664
       result[ 3,11] = 0.79475821795059156217
       result[ 5,11] = 0.79475821795059156217
       result[12,11] = -2.0752447144854989366
       result[21,11] = -0.79475821795059156217
       result[23,11] = 2.0752447144854989366
       result[36,11] = 0.45768182862115030664
       result[38,11] = -0.79475821795059156217
       result[ 1,12] = -0.70903764004458888811
       result[ 6,12] = 0.53582588123382020898
       result[ 8,12] = 1.4377717134510610478
       result[15,12] = 0.53582588123382020898
       result[17,12] = -2.338535866733713366
       result[28,12] = -0.70903764004458888811
       result[30,12] = 1.4377717134510610478
       result[ 2,13] = 0.64725984928774934788
       result[ 7,13] = -1.96875
       result[16,13] = 2.4456993503903949804
       result[29,13] = -1.2566230789301937693
       result[ 4,14] = 1.2566230789301937693
       result[11,14] = -2.4456993503903949804
       result[22,14] = 1.96875
       result[37,14] = -0.64725984928774934788
       result[ 0,15] = 0.626706654240043952
       result[ 3,15] = -2.176535018670731151
       result[10,15] = 3.2353561313826025233
       result[21,15] = -2.176535018670731151
       result[36,15] = 0.626706654240043952
       result[ 1,16] = 1.2945196985754986958
       result[ 6,16] = -2.9348392204684739765
       result[15,16] = 2.9348392204684739765
       result[28,16] = -1.2945196985754986958
       return result

  if n == 9:
       result = np.zeros( (55,19) )
       result[ 2, 0] = 0.59686501473785067702
       result[ 7, 0] = 0.29612797475437320937
       result[ 9, 0] = -1.7657660842403202261
       result[16, 0] = 0.26411138361943717788
       result[18, 0] = -0.92214126273187869253
       result[20, 0] = 2.5354692827465969076
       result[29, 0] = 0.29612797475437320937
       result[31, 0] = -0.92214126273187869253
       result[33, 0] = 1.4846187947947014119
       result[35, 0] = -1.952374120367905548
       result[46, 0] = 0.59686501473785067702
       result[48, 0] = -1.7657660842403202261
       result[50, 0] = 2.5354692827465969076
       result[52, 0] = -1.952374120367905548
       result[54, 0] = 1.0
       result[ 0, 1] = 0.36685490255855924707
       result[ 3, 1] = 0.15916400393009351387
       result[ 5, 1] = -1.5916400393009351387
       result[10, 1] = 0.11811420148091719529
       result[12, 1] = -0.6916059470489090194
       result[14, 1] = 3.1497120394911252077
       result[21, 1] = 0.098709324918124403125
       result[23, 1] = -0.51549263708149354579
       result[25, 1] = 1.3746470322173161221
       result[27, 1] = -3.1586983973799809
       result[36, 1] = 0.088975383089683195547
       result[38, 1] = -0.44144152106008005653
       result[40, 1] = 1.0499040131637084026
       result[42, 1] = -1.4126128673922561809
       result[44, 1] = 1.62697843363992129
       result[ 1, 2] = 0.088975383089683195547
       result[ 6, 2] = 0.098709324918124403125
       result[ 8, 2] = -0.44144152106008005653
       result[15, 2] = 0.11811420148091719529
       result[17, 2] = -0.51549263708149354579
       result[19, 2] = 1.0499040131637084026
       result[28, 2] = 0.15916400393009351387
       result[30, 2] = -0.6916059470489090194
       result[32, 2] = 1.3746470322173161221
       result[34, 2] = -1.4126128673922561809
       result[45, 2] = 0.36685490255855924707
       result[47, 2] = -1.5916400393009351387
       result[49, 2] = 3.1497120394911252077
       result[51, 2] = -3.1586983973799809
       result[53, 2] = 1.62697843363992129
       result[ 2, 3] = -0.83466307816035426155
       result[ 7, 3] = -0.2070544267420625878
       result[ 9, 3] = 2.3149388661875113029
       result[18, 3] = 0.40297913150666282783
       result[20, 3] = -2.9546917977869539993
       result[29, 3] = 0.2070544267420625878
       result[31, 3] = -0.40297913150666282783
       result[35, 3] = 1.7063893769835631924
       result[46, 3] = 0.83466307816035426155
       result[48, 3] = -2.3149388661875113029
       result[50, 3] = 2.9546917977869539993
       result[52, 3] = -1.7063893769835631924
       result[ 4, 4] = -0.43101816018790287844
       result[11, 4] = -0.4187881980957120927
       result[13, 4] = 1.395960660319040309
       result[22, 4] = -0.4187881980957120927
       result[24, 4] = 1.3623181102386339839
       result[26, 4] = -2.2335370565104644944
       result[37, 4] = -0.43101816018790287844
       result[39, 4] = 1.395960660319040309
       result[41, 4] = -2.2335370565104644944
       result[43, 4] = 1.9703687322875560157
       result[ 0, 5] = -0.37548796377180986812
       result[ 5, 5] = 1.4661859659554465543
       result[10, 5] = 0.12089373945199884835
       result[12, 5] = -0.21236437647040795145
       result[14, 5] = -2.417874789039976967
       result[21, 5] = 0.20206443016189559856
       result[23, 5] = -0.79143530297864839268
       result[25, 5] = 1.0552470706381978569
       result[27, 5] = 1.6165154412951647885
       result[36, 5] = 0.27320762396104757397
       result[38, 5] = -1.2199404645272449631
       result[40, 5] = 2.417874789039976967
       result[42, 5] = -2.16878304804843549
       result[ 1, 6] = -0.27320762396104757397
       result[ 6, 6] = -0.20206443016189559856
       result[ 8, 6] = 1.2199404645272449631
       result[15, 6] = -0.12089373945199884835
       result[17, 6] = 0.79143530297864839268
       result[19, 6] = -2.417874789039976967
       result[30, 6] = 0.21236437647040795145
       result[32, 6] = -1.0552470706381978569
       result[34, 6] = 2.16878304804843549
       result[45, 6] = 0.37548796377180986812
       result[47, 6] = -1.4661859659554465543
       result[49, 6] = 2.417874789039976967
       result[51, 6] = -1.6165154412951647885
       result[ 2, 7] = 0.80430146722719804411
       result[ 7, 7] = -0.39904527606894581113
       result[ 9, 7] = -1.7845847267806657796
       result[16, 7] = -0.59316922059788797031
       result[18, 7] = 1.5532816304615888184
       result[20, 7] = 1.4236061294349311288
       result[29, 7] = -0.39904527606894581113
       result[31, 7] = 1.5532816304615888184
       result[33, 7] = -2.5007351860179508607
       result[46, 7] = 0.80430146722719804411
       result[48, 7] = -1.7845847267806657796
       result[50, 7] = 1.4236061294349311288
       result[ 4, 8] = 0.83067898344030094085
       result[11, 8] = 0.26903627024228973454
       result[13, 8] = -2.1522901619383178764
       result[22, 8] = -0.26903627024228973454
       result[26, 8] = 2.1522901619383178764
       result[37, 8] = -0.83067898344030094085
       result[39, 8] = 2.1522901619383178764
       result[41, 8] = -2.1522901619383178764
       result[ 0, 9] = 0.39636409043643194293
       result[ 3, 9] = -0.34393377440500167929
       result[ 5, 9] = -1.2037682104175058775
       result[10, 9] = -0.29776858550677551679
       result[12, 9] = 1.5691988753163563388
       result[14, 9] = 1.1910743420271020672
       result[23, 9] = 0.64978432507844251538
       result[25, 9] = -2.5991373003137700615
       result[36, 9] = 0.48066206207978815025
       result[38, 9] = -1.6693261563207085231
       result[40, 9] = 1.9851239033785034453
       result[ 1,10] = 0.48066206207978815025
       result[ 8,10] = -1.6693261563207085231
       result[15,10] = -0.29776858550677551679
       result[17,10] = 0.64978432507844251538
       result[19,10] = 1.9851239033785034453
       result[28,10] = -0.34393377440500167929
       result[30,10] = 1.5691988753163563388
       result[32,10] = -2.5991373003137700615
       result[45,10] = 0.39636409043643194293
       result[47,10] = -1.2037682104175058775
       result[49,10] = 1.1910743420271020672
       result[ 2,11] = -0.74463846463549402274
       result[ 7,11] = 1.2930544805637086353
       result[ 9,11] = 0.96378590571704436469
       result[18,11] = -2.5166038696554342464
       result[29,11] = -1.2930544805637086353
       result[31,11] = 2.5166038696554342464
       result[46,11] = 0.74463846463549402274
       result[48,11] = -0.96378590571704436469
       result[ 4,12] = -1.1535889489914915606
       result[11,12] = 0.87177715295353129935
       result[13,12] = 1.7435543059070625987
       result[22,12] = 0.87177715295353129935
       result[24,12] = -2.8358912905407192076
       result[37,12] = -1.1535889489914915606
       result[39,12] = 1.7435543059070625987
       result[ 0,13] = -0.44314852502786805507
       result[ 3,13] = 0.96132412415957630049
       result[ 5,13] = 0.76905929932766104039
       result[10,13] = -0.33291539937855436029
       result[12,13] = -2.3392235702823930554
       result[21,13] = -0.83466307816035426155
       result[23,13] = 2.9059238431784376645
       result[36,13] = 0.75235513151094117345
       result[38,13] = -1.4930907048606177933
       result[ 1,14] = -0.75235513151094117345
       result[ 6,14] = 0.83466307816035426155
       result[ 8,14] = 1.4930907048606177933
       result[15,14] = 0.33291539937855436029
       result[17,14] = -2.9059238431784376645
       result[28,14] = -0.96132412415957630049
       result[30,14] = 2.3392235702823930554
       result[45,14] = 0.44314852502786805507
       result[47,14] = -0.76905929932766104039
       result[ 2,15] = 0.626706654240043952
       result[ 7,15] = -2.176535018670731151
       result[16,15] = 3.2353561313826025233
       result[29,15] = -2.176535018670731151
       result[46,15] = 0.626706654240043952
       result[ 4,16] = 1.2945196985754986958
       result[11,16] = -2.9348392204684739765
       result[22,16] = 2.9348392204684739765
       result[37,16] = -1.2945196985754986958
       result[ 0,17] = 0.60904939217552380708
       result[ 3,17] = -2.3781845426185916576
       result[10,17] = 4.1179360680974030877
       result[21,17] = -3.4414040330583097636
       result[36,17] = 1.3294455750836041652
       result[ 1,18] = 1.3294455750836041652
       result[ 6,18] = -3.4414040330583097636
       result[15,18] = 4.1179360680974030877
       result[28,18] = -2.3781845426185916576
       result[45,18] = 0.60904939217552380708
       return result

  raise TypeError("Angular momentum too large")

data = {}
for i in range(10):
   data[i] = cart_sphe(i)
