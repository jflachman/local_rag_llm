---
model-index:
- name: stella_en_400M_v5
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 92.35820895522387
    - type: ap
      value: 70.81322736988783
    - type: ap_weighted
      value: 70.81322736988783
    - type: f1
      value: 88.9505466159595
    - type: f1_weighted
      value: 92.68630932872613
    - type: main_score
      value: 92.35820895522387
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 97.1945
    - type: ap
      value: 96.08192192244094
    - type: ap_weighted
      value: 96.08192192244094
    - type: f1
      value: 97.1936887167346
    - type: f1_weighted
      value: 97.1936887167346
    - type: main_score
      value: 97.1945
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 59.528000000000006
    - type: f1
      value: 59.21016819840188
    - type: f1_weighted
      value: 59.21016819840188
    - type: main_score
      value: 59.528000000000006
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 64.24
    - type: map_at_1
      value: 40.398
    - type: map_at_10
      value: 56.215
    - type: map_at_100
      value: 56.833999999999996
    - type: map_at_1000
      value: 56.835
    - type: map_at_20
      value: 56.747
    - type: map_at_3
      value: 52.181
    - type: map_at_5
      value: 54.628
    - type: mrr_at_1
      value: 41.25177809388336
    - type: mrr_at_10
      value: 56.570762491815216
    - type: mrr_at_100
      value: 57.17548614361504
    - type: mrr_at_1000
      value: 57.176650626377466
    - type: mrr_at_20
      value: 57.08916253512566
    - type: mrr_at_3
      value: 52.47747747747754
    - type: mrr_at_5
      value: 54.94547178757718
    - type: nauc_map_at_1000_diff1
      value: 22.408086887100158
    - type: nauc_map_at_1000_max
      value: -8.730419096847543
    - type: nauc_map_at_1000_std
      value: -17.789262741255737
    - type: nauc_map_at_100_diff1
      value: 22.407371684274025
    - type: nauc_map_at_100_max
      value: -8.732263549026266
    - type: nauc_map_at_100_std
      value: -17.79550515579994
    - type: nauc_map_at_10_diff1
      value: 21.925005073301246
    - type: nauc_map_at_10_max
      value: -8.990323944492134
    - type: nauc_map_at_10_std
      value: -18.199246301671458
    - type: nauc_map_at_1_diff1
      value: 26.23276644969203
    - type: nauc_map_at_1_max
      value: -12.376511389571245
    - type: nauc_map_at_1_std
      value: -18.11411715207284
    - type: nauc_map_at_20_diff1
      value: 22.32455790850922
    - type: nauc_map_at_20_max
      value: -8.664671547236034
    - type: nauc_map_at_20_std
      value: -17.8290016125137
    - type: nauc_map_at_3_diff1
      value: 22.395462147465064
    - type: nauc_map_at_3_max
      value: -8.206580750918844
    - type: nauc_map_at_3_std
      value: -17.604490446911484
    - type: nauc_map_at_5_diff1
      value: 21.95307379904799
    - type: nauc_map_at_5_max
      value: -8.03958102978443
    - type: nauc_map_at_5_std
      value: -17.36578866595004
    - type: nauc_mrr_at_1000_diff1
      value: 20.124236798365587
    - type: nauc_mrr_at_1000_max
      value: -9.587376069575898
    - type: nauc_mrr_at_1000_std
      value: -17.79191612151833
    - type: nauc_mrr_at_100_diff1
      value: 20.123612603474033
    - type: nauc_mrr_at_100_max
      value: -9.589187218607831
    - type: nauc_mrr_at_100_std
      value: -17.7981617777748
    - type: nauc_mrr_at_10_diff1
      value: 19.723683875738075
    - type: nauc_mrr_at_10_max
      value: -9.774151729178815
    - type: nauc_mrr_at_10_std
      value: -18.168668675495162
    - type: nauc_mrr_at_1_diff1
      value: 23.945332059908132
    - type: nauc_mrr_at_1_max
      value: -12.260461466152819
    - type: nauc_mrr_at_1_std
      value: -18.007194922921148
    - type: nauc_mrr_at_20_diff1
      value: 20.04819461810257
    - type: nauc_mrr_at_20_max
      value: -9.518368283588936
    - type: nauc_mrr_at_20_std
      value: -17.831608149836136
    - type: nauc_mrr_at_3_diff1
      value: 19.8571785245832
    - type: nauc_mrr_at_3_max
      value: -9.464375021240478
    - type: nauc_mrr_at_3_std
      value: -17.728533927330453
    - type: nauc_mrr_at_5_diff1
      value: 19.670313652167827
    - type: nauc_mrr_at_5_max
      value: -8.966372585728434
    - type: nauc_mrr_at_5_std
      value: -17.468955834324817
    - type: nauc_ndcg_at_1000_diff1
      value: 21.863049281767417
    - type: nauc_ndcg_at_1000_max
      value: -8.18698520924057
    - type: nauc_ndcg_at_1000_std
      value: -17.634483364794804
    - type: nauc_ndcg_at_100_diff1
      value: 21.849924385738586
    - type: nauc_ndcg_at_100_max
      value: -8.226437560889345
    - type: nauc_ndcg_at_100_std
      value: -17.774648478087002
    - type: nauc_ndcg_at_10_diff1
      value: 19.888395590413573
    - type: nauc_ndcg_at_10_max
      value: -8.968706085632382
    - type: nauc_ndcg_at_10_std
      value: -19.31386964628115
    - type: nauc_ndcg_at_1_diff1
      value: 26.23276644969203
    - type: nauc_ndcg_at_1_max
      value: -12.376511389571245
    - type: nauc_ndcg_at_1_std
      value: -18.11411715207284
    - type: nauc_ndcg_at_20_diff1
      value: 21.38413342416933
    - type: nauc_ndcg_at_20_max
      value: -7.636238194084164
    - type: nauc_ndcg_at_20_std
      value: -17.946390844693028
    - type: nauc_ndcg_at_3_diff1
      value: 21.29169165029195
    - type: nauc_ndcg_at_3_max
      value: -6.793840499730093
    - type: nauc_ndcg_at_3_std
      value: -17.52359001586737
    - type: nauc_ndcg_at_5_diff1
      value: 20.238297656671364
    - type: nauc_ndcg_at_5_max
      value: -6.424992706950072
    - type: nauc_ndcg_at_5_std
      value: -17.082391132291356
    - type: nauc_precision_at_1000_diff1
      value: -7.05195108528572
    - type: nauc_precision_at_1000_max
      value: 34.439879624882145
    - type: nauc_precision_at_1000_std
      value: 68.72436351659353
    - type: nauc_precision_at_100_diff1
      value: -2.769464113932605
    - type: nauc_precision_at_100_max
      value: 9.89562961226698
    - type: nauc_precision_at_100_std
      value: -0.5880967482224028
    - type: nauc_precision_at_10_diff1
      value: 2.1371544726832323
    - type: nauc_precision_at_10_max
      value: -11.93051325147756
    - type: nauc_precision_at_10_std
      value: -30.83144187392059
    - type: nauc_precision_at_1_diff1
      value: 26.23276644969203
    - type: nauc_precision_at_1_max
      value: -12.376511389571245
    - type: nauc_precision_at_1_std
      value: -18.11411715207284
    - type: nauc_precision_at_20_diff1
      value: 3.780146814257504
    - type: nauc_precision_at_20_max
      value: 17.06527540214615
    - type: nauc_precision_at_20_std
      value: -20.36832563035565
    - type: nauc_precision_at_3_diff1
      value: 17.63894384012077
    - type: nauc_precision_at_3_max
      value: -2.0220490624638887
    - type: nauc_precision_at_3_std
      value: -17.285601413493918
    - type: nauc_precision_at_5_diff1
      value: 12.557855071944601
    - type: nauc_precision_at_5_max
      value: 0.5840236463956658
    - type: nauc_precision_at_5_std
      value: -15.827224420217846
    - type: nauc_recall_at_1000_diff1
      value: -7.051951085286463
    - type: nauc_recall_at_1000_max
      value: 34.43987962487738
    - type: nauc_recall_at_1000_std
      value: 68.724363516591
    - type: nauc_recall_at_100_diff1
      value: -2.769464113930314
    - type: nauc_recall_at_100_max
      value: 9.895629612270017
    - type: nauc_recall_at_100_std
      value: -0.58809674821745
    - type: nauc_recall_at_10_diff1
      value: 2.1371544726834495
    - type: nauc_recall_at_10_max
      value: -11.930513251477253
    - type: nauc_recall_at_10_std
      value: -30.83144187392047
    - type: nauc_recall_at_1_diff1
      value: 26.23276644969203
    - type: nauc_recall_at_1_max
      value: -12.376511389571245
    - type: nauc_recall_at_1_std
      value: -18.11411715207284
    - type: nauc_recall_at_20_diff1
      value: 3.7801468142575922
    - type: nauc_recall_at_20_max
      value: 17.0652754021456
    - type: nauc_recall_at_20_std
      value: -20.36832563035559
    - type: nauc_recall_at_3_diff1
      value: 17.63894384012074
    - type: nauc_recall_at_3_max
      value: -2.02204906246383
    - type: nauc_recall_at_3_std
      value: -17.28560141349386
    - type: nauc_recall_at_5_diff1
      value: 12.55785507194463
    - type: nauc_recall_at_5_max
      value: 0.5840236463957296
    - type: nauc_recall_at_5_std
      value: -15.827224420217856
    - type: ndcg_at_1
      value: 40.398
    - type: ndcg_at_10
      value: 64.24
    - type: ndcg_at_100
      value: 66.631
    - type: ndcg_at_1000
      value: 66.65100000000001
    - type: ndcg_at_20
      value: 66.086
    - type: ndcg_at_3
      value: 55.938
    - type: ndcg_at_5
      value: 60.370000000000005
    - type: precision_at_1
      value: 40.398
    - type: precision_at_10
      value: 8.962
    - type: precision_at_100
      value: 0.9950000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.836
    - type: precision_at_3
      value: 22.262
    - type: precision_at_5
      value: 15.519
    - type: recall_at_1
      value: 40.398
    - type: recall_at_10
      value: 89.616
    - type: recall_at_100
      value: 99.502
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 96.72800000000001
    - type: recall_at_3
      value: 66.78500000000001
    - type: recall_at_5
      value: 77.596
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 55.1564333205451
    - type: v_measure
      value: 55.1564333205451
    - type: v_measure_std
      value: 14.696883012214512
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 49.823698316694795
    - type: v_measure
      value: 49.823698316694795
    - type: v_measure_std
      value: 14.951660654298186
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 66.15294503553424
    - type: map
      value: 66.15294503553424
    - type: mrr
      value: 78.53438420612935
    - type: nAUC_map_diff1
      value: 12.569697092717997
    - type: nAUC_map_max
      value: 21.50670312412572
    - type: nAUC_map_std
      value: 16.943786429229064
    - type: nAUC_mrr_diff1
      value: 15.590272897361238
    - type: nAUC_mrr_max
      value: 34.96072022474653
    - type: nAUC_mrr_std
      value: 21.649217605241045
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 85.7824546319275
    - type: cosine_spearman
      value: 83.29587385660628
    - type: euclidean_pearson
      value: 84.58764190565167
    - type: euclidean_spearman
      value: 83.30069324352772
    - type: main_score
      value: 83.29587385660628
    - type: manhattan_pearson
      value: 84.95996839947179
    - type: manhattan_spearman
      value: 83.87480271054358
    - type: pearson
      value: 85.7824546319275
    - type: spearman
      value: 83.29587385660628
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 89.30194805194806
    - type: f1
      value: 89.26182507266391
    - type: f1_weighted
      value: 89.26182507266391
    - type: main_score
      value: 89.30194805194806
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 50.67972171889736
    - type: v_measure
      value: 50.67972171889736
    - type: v_measure_std
      value: 0.7687409980036303
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 45.80539715556144
    - type: v_measure
      value: 45.80539715556144
    - type: v_measure_std
      value: 0.9601346216579142
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack
    metrics:
    - type: main_score
      value: 44.361250000000005
    - type: map_at_1
      value: 28.304499999999997
    - type: map_at_10
      value: 38.54841666666666
    - type: map_at_100
      value: 39.83141666666667
    - type: map_at_1000
      value: 39.944750000000006
    - type: map_at_20
      value: 39.25341666666667
    - type: map_at_3
      value: 35.406749999999995
    - type: map_at_5
      value: 37.15558333333333
    - type: mrr_at_1
      value: 34.09077232860122
    - type: mrr_at_10
      value: 43.15445393211421
    - type: mrr_at_100
      value: 43.98645286848257
    - type: mrr_at_1000
      value: 44.037631313469404
    - type: mrr_at_20
      value: 43.64045813249614
    - type: mrr_at_3
      value: 40.674138648480486
    - type: mrr_at_5
      value: 42.106251182620255
    - type: nauc_map_at_1000_diff1
      value: 46.250011739434996
    - type: nauc_map_at_1000_max
      value: 30.13664446260598
    - type: nauc_map_at_1000_std
      value: 5.422301791618935
    - type: nauc_map_at_100_diff1
      value: 46.253631351999395
    - type: nauc_map_at_100_max
      value: 30.12612918885181
    - type: nauc_map_at_100_std
      value: 5.367077019987172
    - type: nauc_map_at_10_diff1
      value: 46.328171341741346
    - type: nauc_map_at_10_max
      value: 29.80274612581464
    - type: nauc_map_at_10_std
      value: 4.62996685176396
    - type: nauc_map_at_1_diff1
      value: 51.56118117729493
    - type: nauc_map_at_1_max
      value: 27.94885243863768
    - type: nauc_map_at_1_std
      value: 1.700366508927356
    - type: nauc_map_at_20_diff1
      value: 46.286750260299094
    - type: nauc_map_at_20_max
      value: 29.979205290353278
    - type: nauc_map_at_20_std
      value: 5.010588412441873
    - type: nauc_map_at_3_diff1
      value: 47.10018183619064
    - type: nauc_map_at_3_max
      value: 29.062318206078753
    - type: nauc_map_at_3_std
      value: 3.2235696254694197
    - type: nauc_map_at_5_diff1
      value: 46.41971733050039
    - type: nauc_map_at_5_max
      value: 29.456798617695657
    - type: nauc_map_at_5_std
      value: 4.0921691023077145
    - type: nauc_mrr_at_1000_diff1
      value: 45.88888977975723
    - type: nauc_mrr_at_1000_max
      value: 32.162138978089544
    - type: nauc_mrr_at_1000_std
      value: 6.2811943424217915
    - type: nauc_mrr_at_100_diff1
      value: 45.87480433011124
    - type: nauc_mrr_at_100_max
      value: 32.16011334212834
    - type: nauc_mrr_at_100_std
      value: 6.2865717772421785
    - type: nauc_mrr_at_10_diff1
      value: 45.849652904658825
    - type: nauc_mrr_at_10_max
      value: 32.13847916232293
    - type: nauc_mrr_at_10_std
      value: 6.105718728141999
    - type: nauc_mrr_at_1_diff1
      value: 51.013730325062156
    - type: nauc_mrr_at_1_max
      value: 32.77457396492779
    - type: nauc_mrr_at_1_std
      value: 4.415684893471724
    - type: nauc_mrr_at_20_diff1
      value: 45.86663046255274
    - type: nauc_mrr_at_20_max
      value: 32.15219360697865
    - type: nauc_mrr_at_20_std
      value: 6.19603046412763
    - type: nauc_mrr_at_3_diff1
      value: 46.522376582423185
    - type: nauc_mrr_at_3_max
      value: 32.18259009733714
    - type: nauc_mrr_at_3_std
      value: 5.288000648220897
    - type: nauc_mrr_at_5_diff1
      value: 45.86611481369745
    - type: nauc_mrr_at_5_max
      value: 32.14261639054921
    - type: nauc_mrr_at_5_std
      value: 5.8811238177073735
    - type: nauc_ndcg_at_1000_diff1
      value: 44.5055097547565
    - type: nauc_ndcg_at_1000_max
      value: 31.149682057975458
    - type: nauc_ndcg_at_1000_std
      value: 8.157937194901333
    - type: nauc_ndcg_at_100_diff1
      value: 44.12398363638596
    - type: nauc_ndcg_at_100_max
      value: 30.878064321409994
    - type: nauc_ndcg_at_100_std
      value: 8.40493441452808
    - type: nauc_ndcg_at_10_diff1
      value: 44.200093505221474
    - type: nauc_ndcg_at_10_max
      value: 30.15267107733158
    - type: nauc_ndcg_at_10_std
      value: 6.407495361566107
    - type: nauc_ndcg_at_1_diff1
      value: 51.013730325062156
    - type: nauc_ndcg_at_1_max
      value: 32.77457396492779
    - type: nauc_ndcg_at_1_std
      value: 4.415684893471724
    - type: nauc_ndcg_at_20_diff1
      value: 44.16988321564116
    - type: nauc_ndcg_at_20_max
      value: 30.333532500651213
    - type: nauc_ndcg_at_20_std
      value: 7.10024701386895
    - type: nauc_ndcg_at_3_diff1
      value: 45.35982873879988
    - type: nauc_ndcg_at_3_max
      value: 30.288312457948702
    - type: nauc_ndcg_at_3_std
      value: 4.653900898293395
    - type: nauc_ndcg_at_5_diff1
      value: 44.324558115380185
    - type: nauc_ndcg_at_5_max
      value: 30.048149698941373
    - type: nauc_ndcg_at_5_std
      value: 5.6684459618413205
    - type: nauc_precision_at_1000_diff1
      value: -7.282175798304458
    - type: nauc_precision_at_1000_max
      value: 7.820142031765352
    - type: nauc_precision_at_1000_std
      value: 11.736131836431172
    - type: nauc_precision_at_100_diff1
      value: 1.0222940256506976
    - type: nauc_precision_at_100_max
      value: 16.12346497070298
    - type: nauc_precision_at_100_std
      value: 18.202607395247874
    - type: nauc_precision_at_10_diff1
      value: 18.289439185857837
    - type: nauc_precision_at_10_max
      value: 26.116517399154375
    - type: nauc_precision_at_10_std
      value: 13.921214069982302
    - type: nauc_precision_at_1_diff1
      value: 51.013730325062156
    - type: nauc_precision_at_1_max
      value: 32.77457396492779
    - type: nauc_precision_at_1_std
      value: 4.415684893471724
    - type: nauc_precision_at_20_diff1
      value: 12.365165405210886
    - type: nauc_precision_at_20_max
      value: 22.946297258937367
    - type: nauc_precision_at_20_std
      value: 16.13862870358933
    - type: nauc_precision_at_3_diff1
      value: 32.063423642849685
    - type: nauc_precision_at_3_max
      value: 30.140965811989407
    - type: nauc_precision_at_3_std
      value: 8.501746262550146
    - type: nauc_precision_at_5_diff1
      value: 24.777203357717948
    - type: nauc_precision_at_5_max
      value: 28.401579566848472
    - type: nauc_precision_at_5_std
      value: 11.643246774390914
    - type: nauc_recall_at_1000_diff1
      value: 30.04216463401409
    - type: nauc_recall_at_1000_max
      value: 34.98067760563842
    - type: nauc_recall_at_1000_std
      value: 48.01453905250591
    - type: nauc_recall_at_100_diff1
      value: 31.193415507513972
    - type: nauc_recall_at_100_max
      value: 28.69740149270981
    - type: nauc_recall_at_100_std
      value: 25.20960758920368
    - type: nauc_recall_at_10_diff1
      value: 36.18870823636506
    - type: nauc_recall_at_10_max
      value: 26.005625231341238
    - type: nauc_recall_at_10_std
      value: 8.891983977041376
    - type: nauc_recall_at_1_diff1
      value: 51.56118117729493
    - type: nauc_recall_at_1_max
      value: 27.94885243863768
    - type: nauc_recall_at_1_std
      value: 1.700366508927356
    - type: nauc_recall_at_20_diff1
      value: 34.93996118564803
    - type: nauc_recall_at_20_max
      value: 26.149961715956138
    - type: nauc_recall_at_20_std
      value: 12.0657502367633
    - type: nauc_recall_at_3_diff1
      value: 40.80743946709512
    - type: nauc_recall_at_3_max
      value: 26.443127773025783
    - type: nauc_recall_at_3_std
      value: 3.7011448604241477
    - type: nauc_recall_at_5_diff1
      value: 37.608535157055776
    - type: nauc_recall_at_5_max
      value: 26.168016189725822
    - type: nauc_recall_at_5_std
      value: 6.344191564595316
    - type: ndcg_at_1
      value: 34.09083333333333
    - type: ndcg_at_10
      value: 44.361250000000005
    - type: ndcg_at_100
      value: 49.586166666666664
    - type: ndcg_at_1000
      value: 51.623583333333336
    - type: ndcg_at_20
      value: 46.40158333333333
    - type: ndcg_at_3
      value: 39.27733333333333
    - type: ndcg_at_5
      value: 41.662333333333336
    - type: precision_at_1
      value: 34.09083333333333
    - type: precision_at_10
      value: 7.957000000000002
    - type: precision_at_100
      value: 1.2521666666666669
    - type: precision_at_1000
      value: 0.16125
    - type: precision_at_20
      value: 4.6755
    - type: precision_at_3
      value: 18.402083333333334
    - type: precision_at_5
      value: 13.104333333333335
    - type: recall_at_1
      value: 28.304499999999997
    - type: recall_at_10
      value: 56.80666666666667
    - type: recall_at_100
      value: 79.66208333333334
    - type: recall_at_1000
      value: 93.6455
    - type: recall_at_20
      value: 64.2495
    - type: recall_at_3
      value: 42.431333333333335
    - type: recall_at_5
      value: 48.665416666666665
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 43.525999999999996
    - type: map_at_1
      value: 19.291
    - type: map_at_10
      value: 33.471000000000004
    - type: map_at_100
      value: 35.388999999999996
    - type: map_at_1000
      value: 35.568
    - type: map_at_20
      value: 34.496
    - type: map_at_3
      value: 28.713
    - type: map_at_5
      value: 31.384
    - type: mrr_at_1
      value: 43.77850162866449
    - type: mrr_at_10
      value: 56.28576598934912
    - type: mrr_at_100
      value: 56.8588518168194
    - type: mrr_at_1000
      value: 56.878236725973544
    - type: mrr_at_20
      value: 56.6409328120183
    - type: mrr_at_3
      value: 53.56134636264935
    - type: mrr_at_5
      value: 55.27795874049956
    - type: nauc_map_at_1000_diff1
      value: 27.262513153363876
    - type: nauc_map_at_1000_max
      value: 40.099398684385584
    - type: nauc_map_at_1000_std
      value: 18.847812394005512
    - type: nauc_map_at_100_diff1
      value: 27.238993503030745
    - type: nauc_map_at_100_max
      value: 40.07730434492169
    - type: nauc_map_at_100_std
      value: 18.795349250833684
    - type: nauc_map_at_10_diff1
      value: 27.70929180366227
    - type: nauc_map_at_10_max
      value: 39.55987024970173
    - type: nauc_map_at_10_std
      value: 17.214881544648996
    - type: nauc_map_at_1_diff1
      value: 43.34155892182403
    - type: nauc_map_at_1_max
      value: 38.23324890148018
    - type: nauc_map_at_1_std
      value: 6.0781444393516075
    - type: nauc_map_at_20_diff1
      value: 27.311577477800103
    - type: nauc_map_at_20_max
      value: 39.624414083413456
    - type: nauc_map_at_20_std
      value: 18.149811054163287
    - type: nauc_map_at_3_diff1
      value: 30.475965062734367
    - type: nauc_map_at_3_max
      value: 38.49324825043695
    - type: nauc_map_at_3_std
      value: 13.357656038648487
    - type: nauc_map_at_5_diff1
      value: 28.425110095017747
    - type: nauc_map_at_5_max
      value: 39.017894870747796
    - type: nauc_map_at_5_std
      value: 15.543817194122564
    - type: nauc_mrr_at_1000_diff1
      value: 33.16689354701644
    - type: nauc_mrr_at_1000_max
      value: 41.70755363247148
    - type: nauc_mrr_at_1000_std
      value: 24.61667417463176
    - type: nauc_mrr_at_100_diff1
      value: 33.147229262917506
    - type: nauc_mrr_at_100_max
      value: 41.712455697170725
    - type: nauc_mrr_at_100_std
      value: 24.6418922043652
    - type: nauc_mrr_at_10_diff1
      value: 32.94185191112572
    - type: nauc_mrr_at_10_max
      value: 41.64272730141954
    - type: nauc_mrr_at_10_std
      value: 24.663391015702707
    - type: nauc_mrr_at_1_diff1
      value: 39.571969559016395
    - type: nauc_mrr_at_1_max
      value: 39.396249211263495
    - type: nauc_mrr_at_1_std
      value: 16.984149923258357
    - type: nauc_mrr_at_20_diff1
      value: 33.10040770334742
    - type: nauc_mrr_at_20_max
      value: 41.807565560083034
    - type: nauc_mrr_at_20_std
      value: 24.8064180365271
    - type: nauc_mrr_at_3_diff1
      value: 33.065406161485704
    - type: nauc_mrr_at_3_max
      value: 41.049510969934694
    - type: nauc_mrr_at_3_std
      value: 23.18371458928609
    - type: nauc_mrr_at_5_diff1
      value: 33.2389593543916
    - type: nauc_mrr_at_5_max
      value: 41.629486918949915
    - type: nauc_mrr_at_5_std
      value: 24.5777253036149
    - type: nauc_ndcg_at_1000_diff1
      value: 25.868840609197637
    - type: nauc_ndcg_at_1000_max
      value: 42.79564910784761
    - type: nauc_ndcg_at_1000_std
      value: 27.035091271680113
    - type: nauc_ndcg_at_100_diff1
      value: 25.019789319579942
    - type: nauc_ndcg_at_100_max
      value: 42.482345143533735
    - type: nauc_ndcg_at_100_std
      value: 26.76872010731345
    - type: nauc_ndcg_at_10_diff1
      value: 25.949464660653238
    - type: nauc_ndcg_at_10_max
      value: 40.79769544643906
    - type: nauc_ndcg_at_10_std
      value: 22.486116508973204
    - type: nauc_ndcg_at_1_diff1
      value: 39.571969559016395
    - type: nauc_ndcg_at_1_max
      value: 39.396249211263495
    - type: nauc_ndcg_at_1_std
      value: 16.984149923258357
    - type: nauc_ndcg_at_20_diff1
      value: 25.173455685962214
    - type: nauc_ndcg_at_20_max
      value: 40.88873540662413
    - type: nauc_ndcg_at_20_std
      value: 24.4451041955519
    - type: nauc_ndcg_at_3_diff1
      value: 28.185416070726333
    - type: nauc_ndcg_at_3_max
      value: 39.10600031163912
    - type: nauc_ndcg_at_3_std
      value: 18.42694044215541
    - type: nauc_ndcg_at_5_diff1
      value: 27.112647584005583
    - type: nauc_ndcg_at_5_max
      value: 40.154045682322526
    - type: nauc_ndcg_at_5_std
      value: 20.26822517176828
    - type: nauc_precision_at_1000_diff1
      value: -16.42087927044017
    - type: nauc_precision_at_1000_max
      value: 3.5326295053913
    - type: nauc_precision_at_1000_std
      value: 24.406810708493197
    - type: nauc_precision_at_100_diff1
      value: -12.17648135724982
    - type: nauc_precision_at_100_max
      value: 15.895489260126183
    - type: nauc_precision_at_100_std
      value: 32.48346122610907
    - type: nauc_precision_at_10_diff1
      value: -1.2493131347748072
    - type: nauc_precision_at_10_max
      value: 26.409459305604376
    - type: nauc_precision_at_10_std
      value: 31.115432019300016
    - type: nauc_precision_at_1_diff1
      value: 39.571969559016395
    - type: nauc_precision_at_1_max
      value: 39.396249211263495
    - type: nauc_precision_at_1_std
      value: 16.984149923258357
    - type: nauc_precision_at_20_diff1
      value: -6.597509397240593
    - type: nauc_precision_at_20_max
      value: 21.461984620659695
    - type: nauc_precision_at_20_std
      value: 32.9450259748889
    - type: nauc_precision_at_3_diff1
      value: 9.46378764865453
    - type: nauc_precision_at_3_max
      value: 32.03650819375425
    - type: nauc_precision_at_3_std
      value: 26.489382638510765
    - type: nauc_precision_at_5_diff1
      value: 3.5987036728169537
    - type: nauc_precision_at_5_max
      value: 30.633955978579703
    - type: nauc_precision_at_5_std
      value: 30.532430088014443
    - type: nauc_recall_at_1000_diff1
      value: 10.714633106872254
    - type: nauc_recall_at_1000_max
      value: 43.94958623961
    - type: nauc_recall_at_1000_std
      value: 51.78914468954123
    - type: nauc_recall_at_100_diff1
      value: 9.63781472255557
    - type: nauc_recall_at_100_max
      value: 38.50917465255336
    - type: nauc_recall_at_100_std
      value: 37.78623984642377
    - type: nauc_recall_at_10_diff1
      value: 16.480342820841688
    - type: nauc_recall_at_10_max
      value: 35.982566867357406
    - type: nauc_recall_at_10_std
      value: 23.30688188788895
    - type: nauc_recall_at_1_diff1
      value: 43.34155892182403
    - type: nauc_recall_at_1_max
      value: 38.23324890148018
    - type: nauc_recall_at_1_std
      value: 6.0781444393516075
    - type: nauc_recall_at_20_diff1
      value: 13.521048985146367
    - type: nauc_recall_at_20_max
      value: 34.62462209239834
    - type: nauc_recall_at_20_std
      value: 27.85924191501618
    - type: nauc_recall_at_3_diff1
      value: 23.57032748533523
    - type: nauc_recall_at_3_max
      value: 36.32703197635613
    - type: nauc_recall_at_3_std
      value: 15.730238734014337
    - type: nauc_recall_at_5_diff1
      value: 19.61387036368584
    - type: nauc_recall_at_5_max
      value: 36.22030835529556
    - type: nauc_recall_at_5_std
      value: 19.76310648649897
    - type: ndcg_at_1
      value: 43.779
    - type: ndcg_at_10
      value: 43.525999999999996
    - type: ndcg_at_100
      value: 50.138000000000005
    - type: ndcg_at_1000
      value: 52.991
    - type: ndcg_at_20
      value: 46.083
    - type: ndcg_at_3
      value: 38.002
    - type: ndcg_at_5
      value: 39.842
    - type: precision_at_1
      value: 43.779
    - type: precision_at_10
      value: 13.205
    - type: precision_at_100
      value: 2.051
    - type: precision_at_1000
      value: 0.259
    - type: precision_at_20
      value: 7.722999999999999
    - type: precision_at_3
      value: 28.903000000000002
    - type: precision_at_5
      value: 21.368000000000002
    - type: recall_at_1
      value: 19.291
    - type: recall_at_10
      value: 48.754
    - type: recall_at_100
      value: 70.97200000000001
    - type: recall_at_1000
      value: 86.611
    - type: recall_at_20
      value: 55.884
    - type: recall_at_3
      value: 34.101
    - type: recall_at_5
      value: 40.784
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 49.884
    - type: map_at_1
      value: 9.913
    - type: map_at_10
      value: 23.186999999999998
    - type: map_at_100
      value: 34.207
    - type: map_at_1000
      value: 36.318
    - type: map_at_20
      value: 27.419
    - type: map_at_3
      value: 15.656
    - type: map_at_5
      value: 18.945999999999998
    - type: mrr_at_1
      value: 75.75
    - type: mrr_at_10
      value: 82.16279761904761
    - type: mrr_at_100
      value: 82.48445635330299
    - type: mrr_at_1000
      value: 82.4870246719901
    - type: mrr_at_20
      value: 82.36203632968338
    - type: mrr_at_3
      value: 81.29166666666666
    - type: mrr_at_5
      value: 82.02916666666667
    - type: nauc_map_at_1000_diff1
      value: 17.0739966990996
    - type: nauc_map_at_1000_max
      value: 28.440065298437133
    - type: nauc_map_at_1000_std
      value: 20.83498154003865
    - type: nauc_map_at_100_diff1
      value: 17.75982086107111
    - type: nauc_map_at_100_max
      value: 26.87850835673573
    - type: nauc_map_at_100_std
      value: 18.350282298599275
    - type: nauc_map_at_10_diff1
      value: 17.15984258564116
    - type: nauc_map_at_10_max
      value: 10.846179132675553
    - type: nauc_map_at_10_std
      value: -6.263534464094614
    - type: nauc_map_at_1_diff1
      value: 24.014897777973694
    - type: nauc_map_at_1_max
      value: -4.556638938723358
    - type: nauc_map_at_1_std
      value: -22.7844467526989
    - type: nauc_map_at_20_diff1
      value: 16.3179372493187
    - type: nauc_map_at_20_max
      value: 17.176378915498915
    - type: nauc_map_at_20_std
      value: 1.9378637630340372
    - type: nauc_map_at_3_diff1
      value: 19.12786794046792
    - type: nauc_map_at_3_max
      value: 0.09063919305677291
    - type: nauc_map_at_3_std
      value: -16.713143158330492
    - type: nauc_map_at_5_diff1
      value: 18.76504725420023
    - type: nauc_map_at_5_max
      value: 5.040867712207419
    - type: nauc_map_at_5_std
      value: -12.382578318931165
    - type: nauc_mrr_at_1000_diff1
      value: 54.61266255011247
    - type: nauc_mrr_at_1000_max
      value: 60.83961280977112
    - type: nauc_mrr_at_1000_std
      value: 32.70429260443016
    - type: nauc_mrr_at_100_diff1
      value: 54.61346236538542
    - type: nauc_mrr_at_100_max
      value: 60.8407974416647
    - type: nauc_mrr_at_100_std
      value: 32.69272843993462
    - type: nauc_mrr_at_10_diff1
      value: 54.74633685810871
    - type: nauc_mrr_at_10_max
      value: 61.084525933097865
    - type: nauc_mrr_at_10_std
      value: 33.001220210025565
    - type: nauc_mrr_at_1_diff1
      value: 56.12708423835806
    - type: nauc_mrr_at_1_max
      value: 58.9314540998289
    - type: nauc_mrr_at_1_std
      value: 27.39422607651012
    - type: nauc_mrr_at_20_diff1
      value: 54.58896150245695
    - type: nauc_mrr_at_20_max
      value: 60.890929983464815
    - type: nauc_mrr_at_20_std
      value: 32.65559641276393
    - type: nauc_mrr_at_3_diff1
      value: 54.38229071443791
    - type: nauc_mrr_at_3_max
      value: 59.987849044098596
    - type: nauc_mrr_at_3_std
      value: 33.439813880719974
    - type: nauc_mrr_at_5_diff1
      value: 54.961790262449824
    - type: nauc_mrr_at_5_max
      value: 61.17705173908951
    - type: nauc_mrr_at_5_std
      value: 33.30939850734856
    - type: nauc_ndcg_at_1000_diff1
      value: 29.27465932507067
    - type: nauc_ndcg_at_1000_max
      value: 47.952543312315214
    - type: nauc_ndcg_at_1000_std
      value: 36.17132236391485
    - type: nauc_ndcg_at_100_diff1
      value: 28.63072328980134
    - type: nauc_ndcg_at_100_max
      value: 41.460833419186564
    - type: nauc_ndcg_at_100_std
      value: 27.157100358988135
    - type: nauc_ndcg_at_10_diff1
      value: 23.41488013023301
    - type: nauc_ndcg_at_10_max
      value: 39.27798133072349
    - type: nauc_ndcg_at_10_std
      value: 21.979241438928312
    - type: nauc_ndcg_at_1_diff1
      value: 46.12120543657642
    - type: nauc_ndcg_at_1_max
      value: 47.28452124039853
    - type: nauc_ndcg_at_1_std
      value: 19.799884708952543
    - type: nauc_ndcg_at_20_diff1
      value: 23.627669045115574
    - type: nauc_ndcg_at_20_max
      value: 35.88225062457673
    - type: nauc_ndcg_at_20_std
      value: 18.218628030529498
    - type: nauc_ndcg_at_3_diff1
      value: 25.37309228946118
    - type: nauc_ndcg_at_3_max
      value: 40.64426332992231
    - type: nauc_ndcg_at_3_std
      value: 24.608330645901482
    - type: nauc_ndcg_at_5_diff1
      value: 24.055798594999654
    - type: nauc_ndcg_at_5_max
      value: 41.16180524175431
    - type: nauc_ndcg_at_5_std
      value: 24.048305528761315
    - type: nauc_precision_at_1000_diff1
      value: -18.234943251015576
    - type: nauc_precision_at_1000_max
      value: 0.48708502364659184
    - type: nauc_precision_at_1000_std
      value: 2.4473601543134027
    - type: nauc_precision_at_100_diff1
      value: -3.0077810947381227
    - type: nauc_precision_at_100_max
      value: 25.27249321108913
    - type: nauc_precision_at_100_std
      value: 37.36575792126928
    - type: nauc_precision_at_10_diff1
      value: -0.2393778190297635
    - type: nauc_precision_at_10_max
      value: 36.40513293547299
    - type: nauc_precision_at_10_std
      value: 37.4827885766009
    - type: nauc_precision_at_1_diff1
      value: 56.12708423835806
    - type: nauc_precision_at_1_max
      value: 58.9314540998289
    - type: nauc_precision_at_1_std
      value: 27.39422607651012
    - type: nauc_precision_at_20_diff1
      value: -1.2010133229402933
    - type: nauc_precision_at_20_max
      value: 34.117541814385966
    - type: nauc_precision_at_20_std
      value: 39.13273254177449
    - type: nauc_precision_at_3_diff1
      value: 11.757378092198486
    - type: nauc_precision_at_3_max
      value: 42.637962482588875
    - type: nauc_precision_at_3_std
      value: 37.42465077352342
    - type: nauc_precision_at_5_diff1
      value: 7.233177203405101
    - type: nauc_precision_at_5_max
      value: 43.1663582897407
    - type: nauc_precision_at_5_std
      value: 38.848449220750055
    - type: nauc_recall_at_1000_diff1
      value: 27.33938551969145
    - type: nauc_recall_at_1000_max
      value: 45.5614254479334
    - type: nauc_recall_at_1000_std
      value: 50.58528916250458
    - type: nauc_recall_at_100_diff1
      value: 23.610383761920097
    - type: nauc_recall_at_100_max
      value: 31.422168485847184
    - type: nauc_recall_at_100_std
      value: 25.58649926458304
    - type: nauc_recall_at_10_diff1
      value: 14.62495111808408
    - type: nauc_recall_at_10_max
      value: 7.4295041277681095
    - type: nauc_recall_at_10_std
      value: -9.32297089600654
    - type: nauc_recall_at_1_diff1
      value: 24.014897777973694
    - type: nauc_recall_at_1_max
      value: -4.556638938723358
    - type: nauc_recall_at_1_std
      value: -22.7844467526989
    - type: nauc_recall_at_20_diff1
      value: 14.027862330014662
    - type: nauc_recall_at_20_max
      value: 12.437478731690844
    - type: nauc_recall_at_20_std
      value: -3.0740743798103676
    - type: nauc_recall_at_3_diff1
      value: 16.354018356566712
    - type: nauc_recall_at_3_max
      value: -2.9812231240997917
    - type: nauc_recall_at_3_std
      value: -18.27746460743442
    - type: nauc_recall_at_5_diff1
      value: 16.81486583473587
    - type: nauc_recall_at_5_max
      value: 2.420128513974744
    - type: nauc_recall_at_5_std
      value: -14.441820321214108
    - type: ndcg_at_1
      value: 63.87500000000001
    - type: ndcg_at_10
      value: 49.884
    - type: ndcg_at_100
      value: 54.738
    - type: ndcg_at_1000
      value: 61.635
    - type: ndcg_at_20
      value: 48.894999999999996
    - type: ndcg_at_3
      value: 54.287
    - type: ndcg_at_5
      value: 52.40899999999999
    - type: precision_at_1
      value: 75.75
    - type: precision_at_10
      value: 40.9
    - type: precision_at_100
      value: 13.139999999999999
    - type: precision_at_1000
      value: 2.533
    - type: precision_at_20
      value: 30.8
    - type: precision_at_3
      value: 57.667
    - type: precision_at_5
      value: 51.05
    - type: recall_at_1
      value: 9.913
    - type: recall_at_10
      value: 28.591
    - type: recall_at_100
      value: 61.017999999999994
    - type: recall_at_1000
      value: 83.383
    - type: recall_at_20
      value: 37.834
    - type: recall_at_3
      value: 17.049
    - type: recall_at_5
      value: 21.685
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 78.77499999999999
    - type: f1
      value: 73.74058240799386
    - type: f1_weighted
      value: 79.78804377638227
    - type: main_score
      value: 78.77499999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: main_score
      value: 90.986
    - type: map_at_1
      value: 81.601
    - type: map_at_10
      value: 88.242
    - type: map_at_100
      value: 88.46000000000001
    - type: map_at_1000
      value: 88.472
    - type: map_at_20
      value: 88.375
    - type: map_at_3
      value: 87.237
    - type: map_at_5
      value: 87.85300000000001
    - type: mrr_at_1
      value: 87.81878187818782
    - type: mrr_at_10
      value: 92.20301196786335
    - type: mrr_at_100
      value: 92.24884236673292
    - type: mrr_at_1000
      value: 92.2496338899362
    - type: mrr_at_20
      value: 92.23112073283473
    - type: mrr_at_3
      value: 91.77417741774165
    - type: mrr_at_5
      value: 92.03970397039689
    - type: nauc_map_at_1000_diff1
      value: 56.54670664910505
    - type: nauc_map_at_1000_max
      value: 33.08375749975477
    - type: nauc_map_at_1000_std
      value: 2.7491595418252865
    - type: nauc_map_at_100_diff1
      value: 56.50887688686924
    - type: nauc_map_at_100_max
      value: 33.075487189958494
    - type: nauc_map_at_100_std
      value: 2.7675869969253375
    - type: nauc_map_at_10_diff1
      value: 56.08080806610569
    - type: nauc_map_at_10_max
      value: 32.776972098819066
    - type: nauc_map_at_10_std
      value: 2.5904846711290097
    - type: nauc_map_at_1_diff1
      value: 60.645344065853145
    - type: nauc_map_at_1_max
      value: 31.232776777514797
    - type: nauc_map_at_1_std
      value: -1.1946138176109171
    - type: nauc_map_at_20_diff1
      value: 56.28378454162355
    - type: nauc_map_at_20_max
      value: 32.98207150385811
    - type: nauc_map_at_20_std
      value: 2.8469814040214025
    - type: nauc_map_at_3_diff1
      value: 55.81958007095375
    - type: nauc_map_at_3_max
      value: 31.602707711038313
    - type: nauc_map_at_3_std
      value: 0.8117019292273401
    - type: nauc_map_at_5_diff1
      value: 55.706025752316535
    - type: nauc_map_at_5_max
      value: 32.16032683604737
    - type: nauc_map_at_5_std
      value: 1.8853201503498669
    - type: nauc_mrr_at_1000_diff1
      value: 75.4997173366251
    - type: nauc_mrr_at_1000_max
      value: 41.49117135484116
    - type: nauc_mrr_at_1000_std
      value: -2.0636172883680852
    - type: nauc_mrr_at_100_diff1
      value: 75.50118860648519
    - type: nauc_mrr_at_100_max
      value: 41.49490161517194
    - type: nauc_mrr_at_100_std
      value: -2.057024385178682
    - type: nauc_mrr_at_10_diff1
      value: 75.47295153099428
    - type: nauc_mrr_at_10_max
      value: 41.55003304042536
    - type: nauc_mrr_at_10_std
      value: -2.0353663198929253
    - type: nauc_mrr_at_1_diff1
      value: 76.632058433229
    - type: nauc_mrr_at_1_max
      value: 39.754483718891656
    - type: nauc_mrr_at_1_std
      value: -2.962241058101701
    - type: nauc_mrr_at_20_diff1
      value: 75.47221882396194
    - type: nauc_mrr_at_20_max
      value: 41.50779280480839
    - type: nauc_mrr_at_20_std
      value: -1.9620212266426307
    - type: nauc_mrr_at_3_diff1
      value: 75.5682297897137
    - type: nauc_mrr_at_3_max
      value: 41.53543801506081
    - type: nauc_mrr_at_3_std
      value: -3.391681195945978
    - type: nauc_mrr_at_5_diff1
      value: 75.37562775183947
    - type: nauc_mrr_at_5_max
      value: 41.42028509006753
    - type: nauc_mrr_at_5_std
      value: -2.418698675622726
    - type: nauc_ndcg_at_1000_diff1
      value: 59.364557011624
    - type: nauc_ndcg_at_1000_max
      value: 35.4112238125149
    - type: nauc_ndcg_at_1000_std
      value: 3.717516193303376
    - type: nauc_ndcg_at_100_diff1
      value: 58.55706703023122
    - type: nauc_ndcg_at_100_max
      value: 35.352285999934594
    - type: nauc_ndcg_at_100_std
      value: 4.273437944266781
    - type: nauc_ndcg_at_10_diff1
      value: 56.77422701267037
    - type: nauc_ndcg_at_10_max
      value: 34.24909893882957
    - type: nauc_ndcg_at_10_std
      value: 4.178151434006727
    - type: nauc_ndcg_at_1_diff1
      value: 76.632058433229
    - type: nauc_ndcg_at_1_max
      value: 39.754483718891656
    - type: nauc_ndcg_at_1_std
      value: -2.962241058101701
    - type: nauc_ndcg_at_20_diff1
      value: 57.27343398231262
    - type: nauc_ndcg_at_20_max
      value: 34.7416626740278
    - type: nauc_ndcg_at_20_std
      value: 4.955858766014002
    - type: nauc_ndcg_at_3_diff1
      value: 57.69267803121093
    - type: nauc_ndcg_at_3_max
      value: 33.13744317023105
    - type: nauc_ndcg_at_3_std
      value: 0.40380284030057023
    - type: nauc_ndcg_at_5_diff1
      value: 56.57461019113917
    - type: nauc_ndcg_at_5_max
      value: 33.244657840804386
    - type: nauc_ndcg_at_5_std
      value: 2.5121440827702046
    - type: nauc_precision_at_1000_diff1
      value: -14.54492513449718
    - type: nauc_precision_at_1000_max
      value: -5.94552147573623
    - type: nauc_precision_at_1000_std
      value: 1.2446209816057374
    - type: nauc_precision_at_100_diff1
      value: -15.452676132568344
    - type: nauc_precision_at_100_max
      value: -3.760241749847617
    - type: nauc_precision_at_100_std
      value: 4.623534605290865
    - type: nauc_precision_at_10_diff1
      value: -12.712908026086176
    - type: nauc_precision_at_10_max
      value: 0.45241316994816805
    - type: nauc_precision_at_10_std
      value: 7.849478570138391
    - type: nauc_precision_at_1_diff1
      value: 76.632058433229
    - type: nauc_precision_at_1_max
      value: 39.754483718891656
    - type: nauc_precision_at_1_std
      value: -2.962241058101701
    - type: nauc_precision_at_20_diff1
      value: -14.514618673172041
    - type: nauc_precision_at_20_max
      value: -1.113635490621818
    - type: nauc_precision_at_20_std
      value: 8.599811730457576
    - type: nauc_precision_at_3_diff1
      value: 6.1367799850003815
    - type: nauc_precision_at_3_max
      value: 8.466271950897857
    - type: nauc_precision_at_3_std
      value: 1.7458051543195068
    - type: nauc_precision_at_5_diff1
      value: -5.804548945783379
    - type: nauc_precision_at_5_max
      value: 3.4060251839074818
    - type: nauc_precision_at_5_std
      value: 5.583410511782371
    - type: nauc_recall_at_1000_diff1
      value: 19.329432953574095
    - type: nauc_recall_at_1000_max
      value: 43.260442595158736
    - type: nauc_recall_at_1000_std
      value: 53.89644660661804
    - type: nauc_recall_at_100_diff1
      value: 21.265326296051235
    - type: nauc_recall_at_100_max
      value: 38.573000195373695
    - type: nauc_recall_at_100_std
      value: 42.169391082152785
    - type: nauc_recall_at_10_diff1
      value: 29.785129558987432
    - type: nauc_recall_at_10_max
      value: 28.379657867558034
    - type: nauc_recall_at_10_std
      value: 21.132574624091973
    - type: nauc_recall_at_1_diff1
      value: 60.645344065853145
    - type: nauc_recall_at_1_max
      value: 31.232776777514797
    - type: nauc_recall_at_1_std
      value: -1.1946138176109171
    - type: nauc_recall_at_20_diff1
      value: 25.88845612373954
    - type: nauc_recall_at_20_max
      value: 30.24785945821152
    - type: nauc_recall_at_20_std
      value: 31.73911437468067
    - type: nauc_recall_at_3_diff1
      value: 42.2968464797395
    - type: nauc_recall_at_3_max
      value: 26.494318009870018
    - type: nauc_recall_at_3_std
      value: 2.6045977160467544
    - type: nauc_recall_at_5_diff1
      value: 35.81340094401374
    - type: nauc_recall_at_5_max
      value: 25.91082947510634
    - type: nauc_recall_at_5_std
      value: 9.759404930864779
    - type: ndcg_at_1
      value: 87.819
    - type: ndcg_at_10
      value: 90.986
    - type: ndcg_at_100
      value: 91.69
    - type: ndcg_at_1000
      value: 91.863
    - type: ndcg_at_20
      value: 91.293
    - type: ndcg_at_3
      value: 89.621
    - type: ndcg_at_5
      value: 90.333
    - type: precision_at_1
      value: 87.819
    - type: precision_at_10
      value: 10.753
    - type: precision_at_100
      value: 1.138
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_20
      value: 5.4879999999999995
    - type: precision_at_3
      value: 33.703
    - type: precision_at_5
      value: 20.831
    - type: recall_at_1
      value: 81.601
    - type: recall_at_10
      value: 95.44200000000001
    - type: recall_at_100
      value: 98.14399999999999
    - type: recall_at_1000
      value: 99.157
    - type: recall_at_20
      value: 96.43
    - type: recall_at_3
      value: 91.729
    - type: recall_at_5
      value: 93.552
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 56.056
    - type: map_at_1
      value: 28.666000000000004
    - type: map_at_10
      value: 47.437000000000005
    - type: map_at_100
      value: 49.537
    - type: map_at_1000
      value: 49.665
    - type: map_at_20
      value: 48.618
    - type: map_at_3
      value: 41.355
    - type: map_at_5
      value: 44.525
    - type: mrr_at_1
      value: 55.55555555555556
    - type: mrr_at_10
      value: 63.705173427395614
    - type: mrr_at_100
      value: 64.25449940779741
    - type: mrr_at_1000
      value: 64.27635581092147
    - type: mrr_at_20
      value: 64.03796029079103
    - type: mrr_at_3
      value: 61.49691358024688
    - type: mrr_at_5
      value: 62.73148148148143
    - type: nauc_map_at_1000_diff1
      value: 43.24282910397747
    - type: nauc_map_at_1000_max
      value: 28.506093180265644
    - type: nauc_map_at_1000_std
      value: -13.040508386155054
    - type: nauc_map_at_100_diff1
      value: 43.23650442904607
    - type: nauc_map_at_100_max
      value: 28.470565635459156
    - type: nauc_map_at_100_std
      value: -12.988098780714935
    - type: nauc_map_at_10_diff1
      value: 43.393840733087686
    - type: nauc_map_at_10_max
      value: 26.637302062720153
    - type: nauc_map_at_10_std
      value: -14.47500292113762
    - type: nauc_map_at_1_diff1
      value: 47.705150227211725
    - type: nauc_map_at_1_max
      value: 15.354189686550129
    - type: nauc_map_at_1_std
      value: -14.559819859039067
    - type: nauc_map_at_20_diff1
      value: 43.14121075706104
    - type: nauc_map_at_20_max
      value: 27.811170590408395
    - type: nauc_map_at_20_std
      value: -13.459413585283583
    - type: nauc_map_at_3_diff1
      value: 44.33938667720801
    - type: nauc_map_at_3_max
      value: 21.785619884549398
    - type: nauc_map_at_3_std
      value: -15.569980103071593
    - type: nauc_map_at_5_diff1
      value: 43.39280905665027
    - type: nauc_map_at_5_max
      value: 25.021492190645017
    - type: nauc_map_at_5_std
      value: -14.48856622187443
    - type: nauc_mrr_at_1000_diff1
      value: 52.971563939946286
    - type: nauc_mrr_at_1000_max
      value: 38.88019486172324
    - type: nauc_mrr_at_1000_std
      value: -12.412991642381616
    - type: nauc_mrr_at_100_diff1
      value: 52.978468139876945
    - type: nauc_mrr_at_100_max
      value: 38.89751787948751
    - type: nauc_mrr_at_100_std
      value: -12.3677876252269
    - type: nauc_mrr_at_10_diff1
      value: 52.78507148048174
    - type: nauc_mrr_at_10_max
      value: 38.55079809310022
    - type: nauc_mrr_at_10_std
      value: -12.944127025078755
    - type: nauc_mrr_at_1_diff1
      value: 55.52626805861546
    - type: nauc_mrr_at_1_max
      value: 40.49306809164979
    - type: nauc_mrr_at_1_std
      value: -12.886607701317681
    - type: nauc_mrr_at_20_diff1
      value: 52.9592152665678
    - type: nauc_mrr_at_20_max
      value: 38.88514014589964
    - type: nauc_mrr_at_20_std
      value: -12.434464359819444
    - type: nauc_mrr_at_3_diff1
      value: 52.73696844091174
    - type: nauc_mrr_at_3_max
      value: 38.61018727252859
    - type: nauc_mrr_at_3_std
      value: -13.123989867364166
    - type: nauc_mrr_at_5_diff1
      value: 53.037110010188
    - type: nauc_mrr_at_5_max
      value: 38.44770729849151
    - type: nauc_mrr_at_5_std
      value: -13.49318771828972
    - type: nauc_ndcg_at_1000_diff1
      value: 44.73813840091289
    - type: nauc_ndcg_at_1000_max
      value: 33.70113904685389
    - type: nauc_ndcg_at_1000_std
      value: -10.328687058192742
    - type: nauc_ndcg_at_100_diff1
      value: 44.595174119928835
    - type: nauc_ndcg_at_100_max
      value: 33.4788285112467
    - type: nauc_ndcg_at_100_std
      value: -8.695355259716946
    - type: nauc_ndcg_at_10_diff1
      value: 44.39837225263
    - type: nauc_ndcg_at_10_max
      value: 29.188289725593393
    - type: nauc_ndcg_at_10_std
      value: -13.67608323673103
    - type: nauc_ndcg_at_1_diff1
      value: 55.52626805861546
    - type: nauc_ndcg_at_1_max
      value: 40.49306809164979
    - type: nauc_ndcg_at_1_std
      value: -12.886607701317681
    - type: nauc_ndcg_at_20_diff1
      value: 44.24661739902305
    - type: nauc_ndcg_at_20_max
      value: 31.667868318249965
    - type: nauc_ndcg_at_20_std
      value: -10.65470780066342
    - type: nauc_ndcg_at_3_diff1
      value: 43.39857166975522
    - type: nauc_ndcg_at_3_max
      value: 31.764668313577495
    - type: nauc_ndcg_at_3_std
      value: -14.494866954678152
    - type: nauc_ndcg_at_5_diff1
      value: 43.16976647347281
    - type: nauc_ndcg_at_5_max
      value: 29.878329062643143
    - type: nauc_ndcg_at_5_std
      value: -13.987689089179739
    - type: nauc_precision_at_1000_diff1
      value: -9.807973252625484
    - type: nauc_precision_at_1000_max
      value: 26.6279603849494
    - type: nauc_precision_at_1000_std
      value: 7.113187103520632
    - type: nauc_precision_at_100_diff1
      value: -4.777149603323976
    - type: nauc_precision_at_100_max
      value: 31.03410463692187
    - type: nauc_precision_at_100_std
      value: 10.463144150275435
    - type: nauc_precision_at_10_diff1
      value: 8.691528703215962
    - type: nauc_precision_at_10_max
      value: 33.329579434123374
    - type: nauc_precision_at_10_std
      value: -0.8002015226329403
    - type: nauc_precision_at_1_diff1
      value: 55.52626805861546
    - type: nauc_precision_at_1_max
      value: 40.49306809164979
    - type: nauc_precision_at_1_std
      value: -12.886607701317681
    - type: nauc_precision_at_20_diff1
      value: 3.4564653474184284
    - type: nauc_precision_at_20_max
      value: 34.401070158471136
    - type: nauc_precision_at_20_std
      value: 5.813431200164549
    - type: nauc_precision_at_3_diff1
      value: 22.463219705462187
    - type: nauc_precision_at_3_max
      value: 34.77413976546924
    - type: nauc_precision_at_3_std
      value: -7.083890789741479
    - type: nauc_precision_at_5_diff1
      value: 14.011006004883154
    - type: nauc_precision_at_5_max
      value: 35.73655466853702
    - type: nauc_precision_at_5_std
      value: -2.8395172077771598
    - type: nauc_recall_at_1000_diff1
      value: 16.478046357391555
    - type: nauc_recall_at_1000_max
      value: 43.231704288282344
    - type: nauc_recall_at_1000_std
      value: 38.430684937573645
    - type: nauc_recall_at_100_diff1
      value: 30.764718344602436
    - type: nauc_recall_at_100_max
      value: 31.769050487166655
    - type: nauc_recall_at_100_std
      value: 23.48468311677149
    - type: nauc_recall_at_10_diff1
      value: 34.47339565324045
    - type: nauc_recall_at_10_max
      value: 19.054212335800454
    - type: nauc_recall_at_10_std
      value: -11.039734015330437
    - type: nauc_recall_at_1_diff1
      value: 47.705150227211725
    - type: nauc_recall_at_1_max
      value: 15.354189686550129
    - type: nauc_recall_at_1_std
      value: -14.559819859039067
    - type: nauc_recall_at_20_diff1
      value: 32.1011474016873
    - type: nauc_recall_at_20_max
      value: 25.546372988304423
    - type: nauc_recall_at_20_std
      value: -0.007233471152482897
    - type: nauc_recall_at_3_diff1
      value: 37.5708138019065
    - type: nauc_recall_at_3_max
      value: 16.66410785756736
    - type: nauc_recall_at_3_std
      value: -15.404817020108966
    - type: nauc_recall_at_5_diff1
      value: 35.714519648479595
    - type: nauc_recall_at_5_max
      value: 19.02075233009296
    - type: nauc_recall_at_5_std
      value: -13.180963359760725
    - type: ndcg_at_1
      value: 55.556000000000004
    - type: ndcg_at_10
      value: 56.056
    - type: ndcg_at_100
      value: 62.44
    - type: ndcg_at_1000
      value: 64.263
    - type: ndcg_at_20
      value: 58.638999999999996
    - type: ndcg_at_3
      value: 51.722
    - type: ndcg_at_5
      value: 52.701
    - type: precision_at_1
      value: 55.556000000000004
    - type: precision_at_10
      value: 15.679000000000002
    - type: precision_at_100
      value: 2.252
    - type: precision_at_1000
      value: 0.257
    - type: precision_at_20
      value: 9.02
    - type: precision_at_3
      value: 34.619
    - type: precision_at_5
      value: 25.093
    - type: recall_at_1
      value: 28.666000000000004
    - type: recall_at_10
      value: 63.717999999999996
    - type: recall_at_100
      value: 86.938
    - type: recall_at_1000
      value: 97.603
    - type: recall_at_20
      value: 71.649
    - type: recall_at_3
      value: 46.663
    - type: recall_at_5
      value: 53.313
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 71.74199999999999
    - type: map_at_1
      value: 41.729
    - type: map_at_10
      value: 63.168
    - type: map_at_100
      value: 64.132
    - type: map_at_1000
      value: 64.199
    - type: map_at_20
      value: 63.736000000000004
    - type: map_at_3
      value: 59.826
    - type: map_at_5
      value: 61.882000000000005
    - type: mrr_at_1
      value: 83.45712356515868
    - type: mrr_at_10
      value: 87.850342432719
    - type: mrr_at_100
      value: 88.0016320691113
    - type: mrr_at_1000
      value: 88.00576596968136
    - type: mrr_at_20
      value: 87.94463253190389
    - type: mrr_at_3
      value: 87.13706954760278
    - type: mrr_at_5
      value: 87.59419311276136
    - type: nauc_map_at_1000_diff1
      value: 13.635446621095054
    - type: nauc_map_at_1000_max
      value: 18.670632529445633
    - type: nauc_map_at_1000_std
      value: 10.444842636150575
    - type: nauc_map_at_100_diff1
      value: 13.599262398010783
    - type: nauc_map_at_100_max
      value: 18.636389405484806
    - type: nauc_map_at_100_std
      value: 10.460027483576043
    - type: nauc_map_at_10_diff1
      value: 13.235053919323942
    - type: nauc_map_at_10_max
      value: 18.252140477080047
    - type: nauc_map_at_10_std
      value: 9.9075337042203
    - type: nauc_map_at_1_diff1
      value: 76.51940497836482
    - type: nauc_map_at_1_max
      value: 51.251419487235474
    - type: nauc_map_at_1_std
      value: 0.16714896857146574
    - type: nauc_map_at_20_diff1
      value: 13.4178245722222
    - type: nauc_map_at_20_max
      value: 18.40988771210718
    - type: nauc_map_at_20_std
      value: 10.216685163366282
    - type: nauc_map_at_3_diff1
      value: 13.38370761663418
    - type: nauc_map_at_3_max
      value: 17.760962555456537
    - type: nauc_map_at_3_std
      value: 7.15741965624388
    - type: nauc_map_at_5_diff1
      value: 13.138133309724855
    - type: nauc_map_at_5_max
      value: 17.871761295251044
    - type: nauc_map_at_5_std
      value: 8.475147426940074
    - type: nauc_mrr_at_1000_diff1
      value: 75.82650818891959
    - type: nauc_mrr_at_1000_max
      value: 53.6736100668434
    - type: nauc_mrr_at_1000_std
      value: 1.8025016349213916
    - type: nauc_mrr_at_100_diff1
      value: 75.82530574210111
    - type: nauc_mrr_at_100_max
      value: 53.68067545829002
    - type: nauc_mrr_at_100_std
      value: 1.8147470536495791
    - type: nauc_mrr_at_10_diff1
      value: 75.8330135686799
    - type: nauc_mrr_at_10_max
      value: 53.78626885349077
    - type: nauc_mrr_at_10_std
      value: 1.7975782717226636
    - type: nauc_mrr_at_1_diff1
      value: 76.51940497836482
    - type: nauc_mrr_at_1_max
      value: 51.251419487235474
    - type: nauc_mrr_at_1_std
      value: 0.16714896857146574
    - type: nauc_mrr_at_20_diff1
      value: 75.82783382464166
    - type: nauc_mrr_at_20_max
      value: 53.68364567043885
    - type: nauc_mrr_at_20_std
      value: 1.742037904463963
    - type: nauc_mrr_at_3_diff1
      value: 75.6944609768663
    - type: nauc_mrr_at_3_max
      value: 53.803941340341666
    - type: nauc_mrr_at_3_std
      value: 1.1849945458077804
    - type: nauc_mrr_at_5_diff1
      value: 75.73006960604903
    - type: nauc_mrr_at_5_max
      value: 53.62223096420106
    - type: nauc_mrr_at_5_std
      value: 1.6144067563410909
    - type: nauc_ndcg_at_1000_diff1
      value: 21.58025241642726
    - type: nauc_ndcg_at_1000_max
      value: 24.675747527001153
    - type: nauc_ndcg_at_1000_std
      value: 13.075943547492718
    - type: nauc_ndcg_at_100_diff1
      value: 20.30260137544846
    - type: nauc_ndcg_at_100_max
      value: 23.757528813872018
    - type: nauc_ndcg_at_100_std
      value: 13.648994687574062
    - type: nauc_ndcg_at_10_diff1
      value: 18.995052360997818
    - type: nauc_ndcg_at_10_max
      value: 22.254260808196037
    - type: nauc_ndcg_at_10_std
      value: 11.27212390633054
    - type: nauc_ndcg_at_1_diff1
      value: 76.51940497836482
    - type: nauc_ndcg_at_1_max
      value: 51.251419487235474
    - type: nauc_ndcg_at_1_std
      value: 0.16714896857146574
    - type: nauc_ndcg_at_20_diff1
      value: 19.333742380695757
    - type: nauc_ndcg_at_20_max
      value: 22.527779834633364
    - type: nauc_ndcg_at_20_std
      value: 12.161009000707917
    - type: nauc_ndcg_at_3_diff1
      value: 20.013329040965534
    - type: nauc_ndcg_at_3_max
      value: 21.99692460311921
    - type: nauc_ndcg_at_3_std
      value: 6.8076290638386165
    - type: nauc_ndcg_at_5_diff1
      value: 19.08226315942471
    - type: nauc_ndcg_at_5_max
      value: 21.71185964294168
    - type: nauc_ndcg_at_5_std
      value: 8.671911269518214
    - type: nauc_precision_at_1000_diff1
      value: 2.4462475489446764
    - type: nauc_precision_at_1000_max
      value: 29.145662064268578
    - type: nauc_precision_at_1000_std
      value: 49.20704909525856
    - type: nauc_precision_at_100_diff1
      value: 0.11271196725540299
    - type: nauc_precision_at_100_max
      value: 17.37584606388067
    - type: nauc_precision_at_100_std
      value: 34.66099346244071
    - type: nauc_precision_at_10_diff1
      value: 2.9923183951227825
    - type: nauc_precision_at_10_max
      value: 14.261884731124264
    - type: nauc_precision_at_10_std
      value: 18.084188795498378
    - type: nauc_precision_at_1_diff1
      value: 76.51940497836482
    - type: nauc_precision_at_1_max
      value: 51.251419487235474
    - type: nauc_precision_at_1_std
      value: 0.16714896857146574
    - type: nauc_precision_at_20_diff1
      value: 1.9180293008303761
    - type: nauc_precision_at_20_max
      value: 13.832269193468512
    - type: nauc_precision_at_20_std
      value: 21.65284406055607
    - type: nauc_precision_at_3_diff1
      value: 7.226609484731811
    - type: nauc_precision_at_3_max
      value: 15.162908526977272
    - type: nauc_precision_at_3_std
      value: 8.451859972962776
    - type: nauc_precision_at_5_diff1
      value: 4.705236845538159
    - type: nauc_precision_at_5_max
      value: 14.022910843582666
    - type: nauc_precision_at_5_std
      value: 11.777269322821605
    - type: nauc_recall_at_1000_diff1
      value: 2.446247548945172
    - type: nauc_recall_at_1000_max
      value: 29.14566206426889
    - type: nauc_recall_at_1000_std
      value: 49.20704909525879
    - type: nauc_recall_at_100_diff1
      value: 0.1127119672553316
    - type: nauc_recall_at_100_max
      value: 17.37584606388062
    - type: nauc_recall_at_100_std
      value: 34.660993462440686
    - type: nauc_recall_at_10_diff1
      value: 2.9923183951227927
    - type: nauc_recall_at_10_max
      value: 14.261884731124299
    - type: nauc_recall_at_10_std
      value: 18.08418879549837
    - type: nauc_recall_at_1_diff1
      value: 76.51940497836482
    - type: nauc_recall_at_1_max
      value: 51.251419487235474
    - type: nauc_recall_at_1_std
      value: 0.16714896857146574
    - type: nauc_recall_at_20_diff1
      value: 1.918029300830432
    - type: nauc_recall_at_20_max
      value: 13.832269193468566
    - type: nauc_recall_at_20_std
      value: 21.65284406055605
    - type: nauc_recall_at_3_diff1
      value: 7.226609484731802
    - type: nauc_recall_at_3_max
      value: 15.162908526977182
    - type: nauc_recall_at_3_std
      value: 8.451859972962634
    - type: nauc_recall_at_5_diff1
      value: 4.705236845538197
    - type: nauc_recall_at_5_max
      value: 14.02291084358265
    - type: nauc_recall_at_5_std
      value: 11.777269322821638
    - type: ndcg_at_1
      value: 83.45700000000001
    - type: ndcg_at_10
      value: 71.74199999999999
    - type: ndcg_at_100
      value: 75.008
    - type: ndcg_at_1000
      value: 76.242
    - type: ndcg_at_20
      value: 73.114
    - type: ndcg_at_3
      value: 67.128
    - type: ndcg_at_5
      value: 69.645
    - type: precision_at_1
      value: 83.45700000000001
    - type: precision_at_10
      value: 14.747
    - type: precision_at_100
      value: 1.73
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_20
      value: 7.8149999999999995
    - type: precision_at_3
      value: 42.323
    - type: precision_at_5
      value: 27.381
    - type: recall_at_1
      value: 41.729
    - type: recall_at_10
      value: 73.734
    - type: recall_at_100
      value: 86.502
    - type: recall_at_1000
      value: 94.60499999999999
    - type: recall_at_20
      value: 78.14999999999999
    - type: recall_at_3
      value: 63.483999999999995
    - type: recall_at_5
      value: 68.45400000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 96.4904
    - type: ap
      value: 94.85481918794709
    - type: ap_weighted
      value: 94.85481918794709
    - type: f1
      value: 96.4898592305707
    - type: f1_weighted
      value: 96.4898592305707
    - type: main_score
      value: 96.4904
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 43.692
    - type: map_at_1
      value: 23.751
    - type: map_at_10
      value: 36.553999999999995
    - type: map_at_100
      value: 37.721
    - type: map_at_1000
      value: 37.763999999999996
    - type: map_at_20
      value: 37.289
    - type: map_at_3
      value: 32.643
    - type: map_at_5
      value: 34.851
    - type: mrr_at_1
      value: 24.455587392550143
    - type: mrr_at_10
      value: 37.18388706963206
    - type: mrr_at_100
      value: 38.28330737932916
    - type: mrr_at_1000
      value: 38.32054399710817
    - type: mrr_at_20
      value: 37.8818001216278
    - type: mrr_at_3
      value: 33.35721107927405
    - type: mrr_at_5
      value: 35.52483285577843
    - type: nauc_map_at_1000_diff1
      value: 36.3576177260684
    - type: nauc_map_at_1000_max
      value: 7.854511605962703
    - type: nauc_map_at_1000_std
      value: -17.701121059746878
    - type: nauc_map_at_100_diff1
      value: 36.356075649230505
    - type: nauc_map_at_100_max
      value: 7.862168042999533
    - type: nauc_map_at_100_std
      value: -17.670102459097233
    - type: nauc_map_at_10_diff1
      value: 36.22122978875574
    - type: nauc_map_at_10_max
      value: 7.80848606967416
    - type: nauc_map_at_10_std
      value: -18.3265151386167
    - type: nauc_map_at_1_diff1
      value: 39.28605466408357
    - type: nauc_map_at_1_max
      value: 6.20202977590459
    - type: nauc_map_at_1_std
      value: -15.734334090045026
    - type: nauc_map_at_20_diff1
      value: 36.33637880909657
    - type: nauc_map_at_20_max
      value: 7.843437969476022
    - type: nauc_map_at_20_std
      value: -17.917533363025996
    - type: nauc_map_at_3_diff1
      value: 36.24864976076741
    - type: nauc_map_at_3_max
      value: 7.420345251835957
    - type: nauc_map_at_3_std
      value: -18.71678497722944
    - type: nauc_map_at_5_diff1
      value: 36.0789619291824
    - type: nauc_map_at_5_max
      value: 7.7314285669514495
    - type: nauc_map_at_5_std
      value: -18.748688764538706
    - type: nauc_mrr_at_1000_diff1
      value: 36.23912675623378
    - type: nauc_mrr_at_1000_max
      value: 7.690553436255147
    - type: nauc_mrr_at_1000_std
      value: -17.609526070212304
    - type: nauc_mrr_at_100_diff1
      value: 36.23782651189002
    - type: nauc_mrr_at_100_max
      value: 7.70075095171647
    - type: nauc_mrr_at_100_std
      value: -17.575714144960184
    - type: nauc_mrr_at_10_diff1
      value: 36.125229472534215
    - type: nauc_mrr_at_10_max
      value: 7.635472248755658
    - type: nauc_mrr_at_10_std
      value: -18.208166616511086
    - type: nauc_mrr_at_1_diff1
      value: 39.20986875554532
    - type: nauc_mrr_at_1_max
      value: 6.062668487561363
    - type: nauc_mrr_at_1_std
      value: -16.04130340817602
    - type: nauc_mrr_at_20_diff1
      value: 36.21207088739667
    - type: nauc_mrr_at_20_max
      value: 7.699610250145951
    - type: nauc_mrr_at_20_std
      value: -17.778245221724028
    - type: nauc_mrr_at_3_diff1
      value: 36.03957583885305
    - type: nauc_mrr_at_3_max
      value: 7.225515576504581
    - type: nauc_mrr_at_3_std
      value: -18.74478742943741
    - type: nauc_mrr_at_5_diff1
      value: 35.969152496648974
    - type: nauc_mrr_at_5_max
      value: 7.584059789018233
    - type: nauc_mrr_at_5_std
      value: -18.569374723129332
    - type: nauc_ndcg_at_1000_diff1
      value: 35.894655529841806
    - type: nauc_ndcg_at_1000_max
      value: 8.579327424366236
    - type: nauc_ndcg_at_1000_std
      value: -16.359677367747896
    - type: nauc_ndcg_at_100_diff1
      value: 35.89861902483983
    - type: nauc_ndcg_at_100_max
      value: 8.830873623962242
    - type: nauc_ndcg_at_100_std
      value: -15.173125564722978
    - type: nauc_ndcg_at_10_diff1
      value: 35.36499811105169
    - type: nauc_ndcg_at_10_max
      value: 8.449267180956992
    - type: nauc_ndcg_at_10_std
      value: -18.41978802362402
    - type: nauc_ndcg_at_1_diff1
      value: 39.15422481210622
    - type: nauc_ndcg_at_1_max
      value: 6.055515791928331
    - type: nauc_ndcg_at_1_std
      value: -16.042779610876252
    - type: nauc_ndcg_at_20_diff1
      value: 35.73402868264468
    - type: nauc_ndcg_at_20_max
      value: 8.695705518210847
    - type: nauc_ndcg_at_20_std
      value: -16.7735829470466
    - type: nauc_ndcg_at_3_diff1
      value: 35.31358242856231
    - type: nauc_ndcg_at_3_max
      value: 7.645692789058997
    - type: nauc_ndcg_at_3_std
      value: -19.460003734786874
    - type: nauc_ndcg_at_5_diff1
      value: 35.05216588927143
    - type: nauc_ndcg_at_5_max
      value: 8.216690520604715
    - type: nauc_ndcg_at_5_std
      value: -19.3982054492159
    - type: nauc_precision_at_1000_diff1
      value: -4.440002625111349
    - type: nauc_precision_at_1000_max
      value: 7.886988951901723
    - type: nauc_precision_at_1000_std
      value: 9.88111187048247
    - type: nauc_precision_at_100_diff1
      value: 15.728286119463325
    - type: nauc_precision_at_100_max
      value: 13.218650824470654
    - type: nauc_precision_at_100_std
      value: 16.113245895522553
    - type: nauc_precision_at_10_diff1
      value: 29.51218489610567
    - type: nauc_precision_at_10_max
      value: 10.197432401942912
    - type: nauc_precision_at_10_std
      value: -16.950603431359493
    - type: nauc_precision_at_1_diff1
      value: 39.15422481210622
    - type: nauc_precision_at_1_max
      value: 6.055515791928331
    - type: nauc_precision_at_1_std
      value: -16.042779610876252
    - type: nauc_precision_at_20_diff1
      value: 27.825993070397338
    - type: nauc_precision_at_20_max
      value: 11.437632287846007
    - type: nauc_precision_at_20_std
      value: -7.450353566405601
    - type: nauc_precision_at_3_diff1
      value: 32.14135556796588
    - type: nauc_precision_at_3_max
      value: 7.989252443574163
    - type: nauc_precision_at_3_std
      value: -21.566254595671055
    - type: nauc_precision_at_5_diff1
      value: 30.68778685307082
    - type: nauc_precision_at_5_max
      value: 9.332160758499892
    - type: nauc_precision_at_5_std
      value: -20.928554713448914
    - type: nauc_recall_at_1000_diff1
      value: 25.00810478716878
    - type: nauc_recall_at_1000_max
      value: 46.518165765201644
    - type: nauc_recall_at_1000_std
      value: 61.4734635576085
    - type: nauc_recall_at_100_diff1
      value: 33.895581318261726
    - type: nauc_recall_at_100_max
      value: 20.10706035872801
    - type: nauc_recall_at_100_std
      value: 24.204226584457047
    - type: nauc_recall_at_10_diff1
      value: 32.363127359576296
    - type: nauc_recall_at_10_max
      value: 10.729923804989545
    - type: nauc_recall_at_10_std
      value: -18.1335370184202
    - type: nauc_recall_at_1_diff1
      value: 39.28605466408357
    - type: nauc_recall_at_1_max
      value: 6.20202977590459
    - type: nauc_recall_at_1_std
      value: -15.734334090045026
    - type: nauc_recall_at_20_diff1
      value: 33.47804003169795
    - type: nauc_recall_at_20_max
      value: 12.781494765263382
    - type: nauc_recall_at_20_std
      value: -9.263970132202658
    - type: nauc_recall_at_3_diff1
      value: 32.71001429428999
    - type: nauc_recall_at_3_max
      value: 8.353439197382693
    - type: nauc_recall_at_3_std
      value: -21.235097744366954
    - type: nauc_recall_at_5_diff1
      value: 31.87451464963415
    - type: nauc_recall_at_5_max
      value: 9.635051450907305
    - type: nauc_recall_at_5_std
      value: -21.113235357132794
    - type: ndcg_at_1
      value: 24.47
    - type: ndcg_at_10
      value: 43.692
    - type: ndcg_at_100
      value: 49.211
    - type: ndcg_at_1000
      value: 50.244
    - type: ndcg_at_20
      value: 46.278000000000006
    - type: ndcg_at_3
      value: 35.719
    - type: ndcg_at_5
      value: 39.652
    - type: precision_at_1
      value: 24.47
    - type: precision_at_10
      value: 6.857
    - type: precision_at_100
      value: 0.9610000000000001
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_20
      value: 3.968
    - type: precision_at_3
      value: 15.181000000000001
    - type: precision_at_5
      value: 11.117
    - type: recall_at_1
      value: 23.751
    - type: recall_at_10
      value: 65.64
    - type: recall_at_100
      value: 90.967
    - type: recall_at_1000
      value: 98.738
    - type: recall_at_20
      value: 75.639
    - type: recall_at_3
      value: 43.927
    - type: recall_at_5
      value: 53.366
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 98.82580939352485
    - type: f1
      value: 98.75201754333801
    - type: f1_weighted
      value: 98.82795205108245
    - type: main_score
      value: 98.82580939352485
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 92.29822161422709
    - type: f1
      value: 77.75210224871594
    - type: f1_weighted
      value: 93.58661422540348
    - type: main_score
      value: 92.29822161422709
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 85.17484868863484
    - type: f1
      value: 81.94484244487094
    - type: f1_weighted
      value: 85.21022593423332
    - type: main_score
      value: 85.17484868863484
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 89.61667787491594
    - type: f1
      value: 89.02701927621264
    - type: f1_weighted
      value: 89.56306982022801
    - type: main_score
      value: 89.61667787491594
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 46.318282423948574
    - type: v_measure
      value: 46.318282423948574
    - type: v_measure_std
      value: 0.9729055662461538
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 44.29033625273981
    - type: v_measure
      value: 44.29033625273981
    - type: v_measure_std
      value: 1.0596383629128594
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 33.0526129239962
    - type: map
      value: 33.0526129239962
    - type: mrr
      value: 34.29260046890935
    - type: nAUC_map_diff1
      value: 12.579738077238032
    - type: nAUC_map_max
      value: -20.936629344962
    - type: nAUC_map_std
      value: -1.6096805784945216
    - type: nAUC_mrr_diff1
      value: 11.597584463580807
    - type: nAUC_mrr_max
      value: -15.723702838537504
    - type: nAUC_mrr_std
      value: 0.2719172965777737
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 41.486000000000004
    - type: map_at_1
      value: 6.866
    - type: map_at_10
      value: 15.895999999999999
    - type: map_at_100
      value: 21.093
    - type: map_at_1000
      value: 23.067
    - type: map_at_20
      value: 18.125
    - type: map_at_3
      value: 11.421000000000001
    - type: map_at_5
      value: 13.415
    - type: mrr_at_1
      value: 52.63157894736842
    - type: mrr_at_10
      value: 61.486805248415166
    - type: mrr_at_100
      value: 62.08211009182091
    - type: mrr_at_1000
      value: 62.10828701365016
    - type: mrr_at_20
      value: 61.904411187915784
    - type: mrr_at_3
      value: 59.90712074303407
    - type: mrr_at_5
      value: 60.91331269349847
    - type: nauc_map_at_1000_diff1
      value: 25.484625278529403
    - type: nauc_map_at_1000_max
      value: 31.206600396418853
    - type: nauc_map_at_1000_std
      value: 15.569448072357156
    - type: nauc_map_at_100_diff1
      value: 27.636750226316764
    - type: nauc_map_at_100_max
      value: 29.66992681250722
    - type: nauc_map_at_100_std
      value: 10.570600484002671
    - type: nauc_map_at_10_diff1
      value: 32.76642525548697
    - type: nauc_map_at_10_max
      value: 21.459225397237663
    - type: nauc_map_at_10_std
      value: -3.546494734209264
    - type: nauc_map_at_1_diff1
      value: 48.8002894871328
    - type: nauc_map_at_1_max
      value: 5.7236722609868815
    - type: nauc_map_at_1_std
      value: -13.283554044471352
    - type: nauc_map_at_20_diff1
      value: 30.57169701502308
    - type: nauc_map_at_20_max
      value: 25.79666139518404
    - type: nauc_map_at_20_std
      value: 1.781732492989651
    - type: nauc_map_at_3_diff1
      value: 40.076315947201095
    - type: nauc_map_at_3_max
      value: 12.862524429140054
    - type: nauc_map_at_3_std
      value: -9.188349777126817
    - type: nauc_map_at_5_diff1
      value: 36.9918718052938
    - type: nauc_map_at_5_max
      value: 16.74234374361876
    - type: nauc_map_at_5_std
      value: -7.818523349307494
    - type: nauc_mrr_at_1000_diff1
      value: 26.88183002609805
    - type: nauc_mrr_at_1000_max
      value: 47.10209348428658
    - type: nauc_mrr_at_1000_std
      value: 32.067825924992924
    - type: nauc_mrr_at_100_diff1
      value: 26.871482491566745
    - type: nauc_mrr_at_100_max
      value: 47.11303868498556
    - type: nauc_mrr_at_100_std
      value: 32.08961428818868
    - type: nauc_mrr_at_10_diff1
      value: 26.6356914977722
    - type: nauc_mrr_at_10_max
      value: 47.091624558810366
    - type: nauc_mrr_at_10_std
      value: 31.942424120660164
    - type: nauc_mrr_at_1_diff1
      value: 28.19774198483673
    - type: nauc_mrr_at_1_max
      value: 41.44380927834253
    - type: nauc_mrr_at_1_std
      value: 25.18222691885917
    - type: nauc_mrr_at_20_diff1
      value: 26.86487347109452
    - type: nauc_mrr_at_20_max
      value: 47.1987778214726
    - type: nauc_mrr_at_20_std
      value: 32.143517921610034
    - type: nauc_mrr_at_3_diff1
      value: 27.34340373236422
    - type: nauc_mrr_at_3_max
      value: 46.358726506276646
    - type: nauc_mrr_at_3_std
      value: 31.74924155572593
    - type: nauc_mrr_at_5_diff1
      value: 27.209667205060672
    - type: nauc_mrr_at_5_max
      value: 46.79883369072009
    - type: nauc_mrr_at_5_std
      value: 31.655605306670758
    - type: nauc_ndcg_at_1000_diff1
      value: 18.940195769769687
    - type: nauc_ndcg_at_1000_max
      value: 46.48551313937331
    - type: nauc_ndcg_at_1000_std
      value: 33.64819502089232
    - type: nauc_ndcg_at_100_diff1
      value: 19.50885253809146
    - type: nauc_ndcg_at_100_max
      value: 40.53174462354878
    - type: nauc_ndcg_at_100_std
      value: 28.516152877751118
    - type: nauc_ndcg_at_10_diff1
      value: 16.01699218096564
    - type: nauc_ndcg_at_10_max
      value: 41.17322878314514
    - type: nauc_ndcg_at_10_std
      value: 29.002233224832196
    - type: nauc_ndcg_at_1_diff1
      value: 27.443547710102205
    - type: nauc_ndcg_at_1_max
      value: 40.66529763309582
    - type: nauc_ndcg_at_1_std
      value: 24.15016766225869
    - type: nauc_ndcg_at_20_diff1
      value: 17.541197675685062
    - type: nauc_ndcg_at_20_max
      value: 40.53231266973844
    - type: nauc_ndcg_at_20_std
      value: 29.54096347876548
    - type: nauc_ndcg_at_3_diff1
      value: 18.649628357473716
    - type: nauc_ndcg_at_3_max
      value: 41.18603570171764
    - type: nauc_ndcg_at_3_std
      value: 27.125524188420396
    - type: nauc_ndcg_at_5_diff1
      value: 17.519593751448483
    - type: nauc_ndcg_at_5_max
      value: 42.715997890377345
    - type: nauc_ndcg_at_5_std
      value: 27.902627839899868
    - type: nauc_precision_at_1000_diff1
      value: -15.528797630565155
    - type: nauc_precision_at_1000_max
      value: 13.741640921778671
    - type: nauc_precision_at_1000_std
      value: 44.50896053788372
    - type: nauc_precision_at_100_diff1
      value: -14.491464489721887
    - type: nauc_precision_at_100_max
      value: 23.136434418999457
    - type: nauc_precision_at_100_std
      value: 49.73145147863128
    - type: nauc_precision_at_10_diff1
      value: -4.829188942994277
    - type: nauc_precision_at_10_max
      value: 40.327612559528866
    - type: nauc_precision_at_10_std
      value: 39.34919529635044
    - type: nauc_precision_at_1_diff1
      value: 28.19774198483673
    - type: nauc_precision_at_1_max
      value: 41.44380927834253
    - type: nauc_precision_at_1_std
      value: 25.18222691885917
    - type: nauc_precision_at_20_diff1
      value: -7.210726293112847
    - type: nauc_precision_at_20_max
      value: 37.195679576636984
    - type: nauc_precision_at_20_std
      value: 45.4597096418357
    - type: nauc_precision_at_3_diff1
      value: 7.578219537774854
    - type: nauc_precision_at_3_max
      value: 41.59775233475654
    - type: nauc_precision_at_3_std
      value: 30.764584790895118
    - type: nauc_precision_at_5_diff1
      value: 1.655451789039598
    - type: nauc_precision_at_5_max
      value: 43.435739407610455
    - type: nauc_precision_at_5_std
      value: 33.42552263325999
    - type: nauc_recall_at_1000_diff1
      value: 5.030705700690516
    - type: nauc_recall_at_1000_max
      value: 19.108072570815583
    - type: nauc_recall_at_1000_std
      value: 14.697734974217308
    - type: nauc_recall_at_100_diff1
      value: 14.746540318132407
    - type: nauc_recall_at_100_max
      value: 21.798705033854795
    - type: nauc_recall_at_100_std
      value: 11.416195108842587
    - type: nauc_recall_at_10_diff1
      value: 25.548642427860486
    - type: nauc_recall_at_10_max
      value: 18.711677681987474
    - type: nauc_recall_at_10_std
      value: -5.988904818971677
    - type: nauc_recall_at_1_diff1
      value: 48.8002894871328
    - type: nauc_recall_at_1_max
      value: 5.7236722609868815
    - type: nauc_recall_at_1_std
      value: -13.283554044471352
    - type: nauc_recall_at_20_diff1
      value: 23.39140739154809
    - type: nauc_recall_at_20_max
      value: 19.351150636155474
    - type: nauc_recall_at_20_std
      value: -2.757280266915132
    - type: nauc_recall_at_3_diff1
      value: 38.17453576012812
    - type: nauc_recall_at_3_max
      value: 13.47003839643972
    - type: nauc_recall_at_3_std
      value: -8.75780163862688
    - type: nauc_recall_at_5_diff1
      value: 33.02812855226899
    - type: nauc_recall_at_5_max
      value: 15.477626408978477
    - type: nauc_recall_at_5_std
      value: -9.072206441070708
    - type: ndcg_at_1
      value: 50.773999999999994
    - type: ndcg_at_10
      value: 41.486000000000004
    - type: ndcg_at_100
      value: 39.051
    - type: ndcg_at_1000
      value: 48.106
    - type: ndcg_at_20
      value: 39.432
    - type: ndcg_at_3
      value: 47.428
    - type: ndcg_at_5
      value: 45.227000000000004
    - type: precision_at_1
      value: 52.632
    - type: precision_at_10
      value: 31.146
    - type: precision_at_100
      value: 10.328
    - type: precision_at_1000
      value: 2.432
    - type: precision_at_20
      value: 23.793
    - type: precision_at_3
      value: 45.201
    - type: precision_at_5
      value: 39.876
    - type: recall_at_1
      value: 6.866
    - type: recall_at_10
      value: 20.447000000000003
    - type: recall_at_100
      value: 40.607
    - type: recall_at_1000
      value: 73.411
    - type: recall_at_20
      value: 26.082
    - type: recall_at_3
      value: 12.484
    - type: recall_at_5
      value: 15.847
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 69.072
    - type: map_at_1
      value: 45.483000000000004
    - type: map_at_10
      value: 62.050000000000004
    - type: map_at_100
      value: 62.693
    - type: map_at_1000
      value: 62.702999999999996
    - type: map_at_20
      value: 62.498
    - type: map_at_3
      value: 58.285
    - type: map_at_5
      value: 60.711000000000006
    - type: mrr_at_1
      value: 50.840092699884124
    - type: mrr_at_10
      value: 64.54635224116673
    - type: mrr_at_100
      value: 64.9526548702289
    - type: mrr_at_1000
      value: 64.95908460752281
    - type: mrr_at_20
      value: 64.82949565799959
    - type: mrr_at_3
      value: 61.89165701042856
    - type: mrr_at_5
      value: 63.632676709154026
    - type: nauc_map_at_1000_diff1
      value: 43.187285304185224
    - type: nauc_map_at_1000_max
      value: 32.39921659632756
    - type: nauc_map_at_1000_std
      value: -5.780901333066553
    - type: nauc_map_at_100_diff1
      value: 43.184487221204456
    - type: nauc_map_at_100_max
      value: 32.41176116347982
    - type: nauc_map_at_100_std
      value: -5.76422606662383
    - type: nauc_map_at_10_diff1
      value: 42.967066814031746
    - type: nauc_map_at_10_max
      value: 32.489617364418514
    - type: nauc_map_at_10_std
      value: -6.029045531102664
    - type: nauc_map_at_1_diff1
      value: 46.16376563218624
    - type: nauc_map_at_1_max
      value: 26.342624776802232
    - type: nauc_map_at_1_std
      value: -7.142171388751972
    - type: nauc_map_at_20_diff1
      value: 43.15894358608328
    - type: nauc_map_at_20_max
      value: 32.46492198956245
    - type: nauc_map_at_20_std
      value: -5.788373305449195
    - type: nauc_map_at_3_diff1
      value: 43.231752344608545
    - type: nauc_map_at_3_max
      value: 31.68003009949564
    - type: nauc_map_at_3_std
      value: -8.015235132765458
    - type: nauc_map_at_5_diff1
      value: 42.86197608819917
    - type: nauc_map_at_5_max
      value: 32.363857571094485
    - type: nauc_map_at_5_std
      value: -6.780487416387977
    - type: nauc_mrr_at_1000_diff1
      value: 43.40542912045782
    - type: nauc_mrr_at_1000_max
      value: 32.8461770324533
    - type: nauc_mrr_at_1000_std
      value: -3.6505425530008204
    - type: nauc_mrr_at_100_diff1
      value: 43.40233508014468
    - type: nauc_mrr_at_100_max
      value: 32.85598538385942
    - type: nauc_mrr_at_100_std
      value: -3.637477352635459
    - type: nauc_mrr_at_10_diff1
      value: 43.260179162806054
    - type: nauc_mrr_at_10_max
      value: 32.942643527040474
    - type: nauc_mrr_at_10_std
      value: -3.712052825320437
    - type: nauc_mrr_at_1_diff1
      value: 46.354919460881206
    - type: nauc_mrr_at_1_max
      value: 29.1760258591106
    - type: nauc_mrr_at_1_std
      value: -4.107225031227406
    - type: nauc_mrr_at_20_diff1
      value: 43.37092385434311
    - type: nauc_mrr_at_20_max
      value: 32.93390254712846
    - type: nauc_mrr_at_20_std
      value: -3.5719056112132006
    - type: nauc_mrr_at_3_diff1
      value: 43.1744474040527
    - type: nauc_mrr_at_3_max
      value: 32.741290559777994
    - type: nauc_mrr_at_3_std
      value: -4.72677925120697
    - type: nauc_mrr_at_5_diff1
      value: 43.108396819975674
    - type: nauc_mrr_at_5_max
      value: 32.970519514893084
    - type: nauc_mrr_at_5_std
      value: -4.090906158975974
    - type: nauc_ndcg_at_1000_diff1
      value: 42.786664193638714
    - type: nauc_ndcg_at_1000_max
      value: 33.65554095609296
    - type: nauc_ndcg_at_1000_std
      value: -4.024030130584482
    - type: nauc_ndcg_at_100_diff1
      value: 42.691246775210814
    - type: nauc_ndcg_at_100_max
      value: 34.063232335110875
    - type: nauc_ndcg_at_100_std
      value: -3.477813807415248
    - type: nauc_ndcg_at_10_diff1
      value: 41.90988990571757
    - type: nauc_ndcg_at_10_max
      value: 34.58934812881633
    - type: nauc_ndcg_at_10_std
      value: -4.3295110195497655
    - type: nauc_ndcg_at_1_diff1
      value: 46.354919460881206
    - type: nauc_ndcg_at_1_max
      value: 29.1760258591106
    - type: nauc_ndcg_at_1_std
      value: -4.107225031227406
    - type: nauc_ndcg_at_20_diff1
      value: 42.493206675867114
    - type: nauc_ndcg_at_20_max
      value: 34.562441307459544
    - type: nauc_ndcg_at_20_std
      value: -3.4456116866749107
    - type: nauc_ndcg_at_3_diff1
      value: 42.24180336502808
    - type: nauc_ndcg_at_3_max
      value: 33.064267018100594
    - type: nauc_ndcg_at_3_std
      value: -7.786248093572142
    - type: nauc_ndcg_at_5_diff1
      value: 41.692714787779565
    - type: nauc_ndcg_at_5_max
      value: 34.20502498949156
    - type: nauc_ndcg_at_5_std
      value: -5.979557859282785
    - type: nauc_precision_at_1000_diff1
      value: -13.779832506640702
    - type: nauc_precision_at_1000_max
      value: 1.243001688631421
    - type: nauc_precision_at_1000_std
      value: 17.351623398622323
    - type: nauc_precision_at_100_diff1
      value: -11.310526816290297
    - type: nauc_precision_at_100_max
      value: 5.771669506192959
    - type: nauc_precision_at_100_std
      value: 19.917795079540113
    - type: nauc_precision_at_10_diff1
      value: 2.163699384635286
    - type: nauc_precision_at_10_max
      value: 19.66440698458386
    - type: nauc_precision_at_10_std
      value: 13.689876348315726
    - type: nauc_precision_at_1_diff1
      value: 46.354919460881206
    - type: nauc_precision_at_1_max
      value: 29.1760258591106
    - type: nauc_precision_at_1_std
      value: -4.107225031227406
    - type: nauc_precision_at_20_diff1
      value: -3.038735879584471
    - type: nauc_precision_at_20_max
      value: 14.132968299701695
    - type: nauc_precision_at_20_std
      value: 17.78069734664346
    - type: nauc_precision_at_3_diff1
      value: 21.783760758070095
    - type: nauc_precision_at_3_max
      value: 30.244127986404497
    - type: nauc_precision_at_3_std
      value: -0.12411163467738723
    - type: nauc_precision_at_5_diff1
      value: 10.980635723302418
    - type: nauc_precision_at_5_max
      value: 25.302293738975575
    - type: nauc_precision_at_5_std
      value: 6.4740817488722024
    - type: nauc_recall_at_1000_diff1
      value: 34.10343772356593
    - type: nauc_recall_at_1000_max
      value: 80.72497340357538
    - type: nauc_recall_at_1000_std
      value: 69.54564103264093
    - type: nauc_recall_at_100_diff1
      value: 33.427719956774126
    - type: nauc_recall_at_100_max
      value: 71.54086768335449
    - type: nauc_recall_at_100_std
      value: 49.66157377654885
    - type: nauc_recall_at_10_diff1
      value: 33.70139560054039
    - type: nauc_recall_at_10_max
      value: 45.47878072860151
    - type: nauc_recall_at_10_std
      value: 1.4188516615716378
    - type: nauc_recall_at_1_diff1
      value: 46.16376563218624
    - type: nauc_recall_at_1_max
      value: 26.342624776802232
    - type: nauc_recall_at_1_std
      value: -7.142171388751972
    - type: nauc_recall_at_20_diff1
      value: 35.805379874970086
    - type: nauc_recall_at_20_max
      value: 51.80479822253392
    - type: nauc_recall_at_20_std
      value: 13.531467576460143
    - type: nauc_recall_at_3_diff1
      value: 37.288500141631616
    - type: nauc_recall_at_3_max
      value: 35.07078243516728
    - type: nauc_recall_at_3_std
      value: -10.452926441410405
    - type: nauc_recall_at_5_diff1
      value: 34.83186104526897
    - type: nauc_recall_at_5_max
      value: 39.58488976496973
    - type: nauc_recall_at_5_std
      value: -6.3049292065708835
    - type: ndcg_at_1
      value: 50.839999999999996
    - type: ndcg_at_10
      value: 69.072
    - type: ndcg_at_100
      value: 71.538
    - type: ndcg_at_1000
      value: 71.77799999999999
    - type: ndcg_at_20
      value: 70.41
    - type: ndcg_at_3
      value: 62.544999999999995
    - type: ndcg_at_5
      value: 66.33099999999999
    - type: precision_at_1
      value: 50.839999999999996
    - type: precision_at_10
      value: 10.495000000000001
    - type: precision_at_100
      value: 1.1900000000000002
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_20
      value: 5.5809999999999995
    - type: precision_at_3
      value: 27.636
    - type: precision_at_5
      value: 18.864
    - type: recall_at_1
      value: 45.483000000000004
    - type: recall_at_10
      value: 87.483
    - type: recall_at_100
      value: 97.844
    - type: recall_at_1000
      value: 99.66199999999999
    - type: recall_at_20
      value: 92.294
    - type: recall_at_3
      value: 71.2
    - type: recall_at_5
      value: 79.753
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: main_score
      value: 89.58
    - type: map_at_1
      value: 71.819
    - type: map_at_10
      value: 86.04899999999999
    - type: map_at_100
      value: 86.648
    - type: map_at_1000
      value: 86.66199999999999
    - type: map_at_20
      value: 86.441
    - type: map_at_3
      value: 83.114
    - type: map_at_5
      value: 84.981
    - type: mrr_at_1
      value: 82.62
    - type: mrr_at_10
      value: 88.62899999999979
    - type: mrr_at_100
      value: 88.70918591324215
    - type: mrr_at_1000
      value: 88.70973091492397
    - type: mrr_at_20
      value: 88.68914765317221
    - type: mrr_at_3
      value: 87.74999999999979
    - type: mrr_at_5
      value: 88.36799999999974
    - type: nauc_map_at_1000_diff1
      value: 77.89207709760448
    - type: nauc_map_at_1000_max
      value: 29.63371361495422
    - type: nauc_map_at_1000_std
      value: -48.628180385874344
    - type: nauc_map_at_100_diff1
      value: 77.89592179104915
    - type: nauc_map_at_100_max
      value: 29.617171506130756
    - type: nauc_map_at_100_std
      value: -48.66057170774648
    - type: nauc_map_at_10_diff1
      value: 78.0618161228185
    - type: nauc_map_at_10_max
      value: 29.178490609366737
    - type: nauc_map_at_10_std
      value: -50.74755004592002
    - type: nauc_map_at_1_diff1
      value: 81.64335579973574
    - type: nauc_map_at_1_max
      value: 21.813832226652174
    - type: nauc_map_at_1_std
      value: -42.57570978190876
    - type: nauc_map_at_20_diff1
      value: 77.9299081005938
    - type: nauc_map_at_20_max
      value: 29.458718470003888
    - type: nauc_map_at_20_std
      value: -49.63337236763102
    - type: nauc_map_at_3_diff1
      value: 78.72941448509229
    - type: nauc_map_at_3_max
      value: 26.600997896960056
    - type: nauc_map_at_3_std
      value: -51.889002227479885
    - type: nauc_map_at_5_diff1
      value: 78.31466610917171
    - type: nauc_map_at_5_max
      value: 28.09863984582896
    - type: nauc_map_at_5_std
      value: -52.14058096096497
    - type: nauc_mrr_at_1000_diff1
      value: 78.42667263739992
    - type: nauc_mrr_at_1000_max
      value: 31.98996235127974
    - type: nauc_mrr_at_1000_std
      value: -44.380439148429296
    - type: nauc_mrr_at_100_diff1
      value: 78.42661032698115
    - type: nauc_mrr_at_100_max
      value: 31.991652631740102
    - type: nauc_mrr_at_100_std
      value: -44.37854108460535
    - type: nauc_mrr_at_10_diff1
      value: 78.39126022544136
    - type: nauc_mrr_at_10_max
      value: 32.02023484451197
    - type: nauc_mrr_at_10_std
      value: -44.561252349176954
    - type: nauc_mrr_at_1_diff1
      value: 79.21630894647448
    - type: nauc_mrr_at_1_max
      value: 31.526303156060177
    - type: nauc_mrr_at_1_std
      value: -41.887504422443136
    - type: nauc_mrr_at_20_diff1
      value: 78.42548039170424
    - type: nauc_mrr_at_20_max
      value: 31.99588275070137
    - type: nauc_mrr_at_20_std
      value: -44.44957722627042
    - type: nauc_mrr_at_3_diff1
      value: 78.26165151833735
    - type: nauc_mrr_at_3_max
      value: 32.18028826126801
    - type: nauc_mrr_at_3_std
      value: -44.6998237213182
    - type: nauc_mrr_at_5_diff1
      value: 78.34786430903962
    - type: nauc_mrr_at_5_max
      value: 32.168476272879566
    - type: nauc_mrr_at_5_std
      value: -44.7915919956712
    - type: nauc_ndcg_at_1000_diff1
      value: 77.79198355957816
    - type: nauc_ndcg_at_1000_max
      value: 31.14363511518406
    - type: nauc_ndcg_at_1000_std
      value: -46.69335151274275
    - type: nauc_ndcg_at_100_diff1
      value: 77.79898090286419
    - type: nauc_ndcg_at_100_max
      value: 31.115103811629215
    - type: nauc_ndcg_at_100_std
      value: -46.73078913421965
    - type: nauc_ndcg_at_10_diff1
      value: 77.74856635461343
    - type: nauc_ndcg_at_10_max
      value: 30.279584686212747
    - type: nauc_ndcg_at_10_std
      value: -50.23514662356807
    - type: nauc_ndcg_at_1_diff1
      value: 79.17833000040999
    - type: nauc_ndcg_at_1_max
      value: 31.703788144510746
    - type: nauc_ndcg_at_1_std
      value: -41.854817402870715
    - type: nauc_ndcg_at_20_diff1
      value: 77.7380353804671
    - type: nauc_ndcg_at_20_max
      value: 30.622294129001553
    - type: nauc_ndcg_at_20_std
      value: -49.035794761065254
    - type: nauc_ndcg_at_3_diff1
      value: 77.41476880573593
    - type: nauc_ndcg_at_3_max
      value: 29.015949978243032
    - type: nauc_ndcg_at_3_std
      value: -49.78627087622648
    - type: nauc_ndcg_at_5_diff1
      value: 77.64439137502896
    - type: nauc_ndcg_at_5_max
      value: 29.444684897492206
    - type: nauc_ndcg_at_5_std
      value: -51.21908400252501
    - type: nauc_precision_at_1000_diff1
      value: -44.92396459446822
    - type: nauc_precision_at_1000_max
      value: -3.674153720989045
    - type: nauc_precision_at_1000_std
      value: 39.56552468277785
    - type: nauc_precision_at_100_diff1
      value: -44.75143023259094
    - type: nauc_precision_at_100_max
      value: -3.705280025140011
    - type: nauc_precision_at_100_std
      value: 39.433619999113326
    - type: nauc_precision_at_10_diff1
      value: -41.0651074726579
    - type: nauc_precision_at_10_max
      value: -0.21097985601783667
    - type: nauc_precision_at_10_std
      value: 26.24652824589493
    - type: nauc_precision_at_1_diff1
      value: 79.17833000040999
    - type: nauc_precision_at_1_max
      value: 31.703788144510746
    - type: nauc_precision_at_1_std
      value: -41.854817402870715
    - type: nauc_precision_at_20_diff1
      value: -43.368001340920294
    - type: nauc_precision_at_20_max
      value: -2.036990010399129
    - type: nauc_precision_at_20_std
      value: 32.37747041406297
    - type: nauc_precision_at_3_diff1
      value: -22.089307548346877
    - type: nauc_precision_at_3_max
      value: 6.2280973175296
    - type: nauc_precision_at_3_std
      value: 5.323992514036145
    - type: nauc_precision_at_5_diff1
      value: -34.07115055244003
    - type: nauc_precision_at_5_max
      value: 2.5955315789198834
    - type: nauc_precision_at_5_std
      value: 16.26096689407332
    - type: nauc_recall_at_1000_diff1
      value: 58.27703860947467
    - type: nauc_recall_at_1000_max
      value: 68.59835835315768
    - type: nauc_recall_at_1000_std
      value: 77.96687006056064
    - type: nauc_recall_at_100_diff1
      value: 73.24371223081737
    - type: nauc_recall_at_100_max
      value: 39.55925344664591
    - type: nauc_recall_at_100_std
      value: -32.25605030215798
    - type: nauc_recall_at_10_diff1
      value: 73.41261201339202
    - type: nauc_recall_at_10_max
      value: 26.822979434062926
    - type: nauc_recall_at_10_std
      value: -74.2909332592806
    - type: nauc_recall_at_1_diff1
      value: 81.64335579973574
    - type: nauc_recall_at_1_max
      value: 21.813832226652174
    - type: nauc_recall_at_1_std
      value: -42.57570978190876
    - type: nauc_recall_at_20_diff1
      value: 72.7621297920656
    - type: nauc_recall_at_20_max
      value: 26.02492304096079
    - type: nauc_recall_at_20_std
      value: -77.8724532438279
    - type: nauc_recall_at_3_diff1
      value: 75.25149312810714
    - type: nauc_recall_at_3_max
      value: 23.20545662481487
    - type: nauc_recall_at_3_std
      value: -59.69689982140521
    - type: nauc_recall_at_5_diff1
      value: 73.69807273001406
    - type: nauc_recall_at_5_max
      value: 24.073666798066057
    - type: nauc_recall_at_5_std
      value: -67.91121268130719
    - type: ndcg_at_1
      value: 82.64
    - type: ndcg_at_10
      value: 89.58
    - type: ndcg_at_100
      value: 90.606
    - type: ndcg_at_1000
      value: 90.676
    - type: ndcg_at_20
      value: 90.132
    - type: ndcg_at_3
      value: 86.88
    - type: ndcg_at_5
      value: 88.40299999999999
    - type: precision_at_1
      value: 82.64
    - type: precision_at_10
      value: 13.604
    - type: precision_at_100
      value: 1.539
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.188
    - type: precision_at_3
      value: 38.083
    - type: precision_at_5
      value: 25.018
    - type: recall_at_1
      value: 71.819
    - type: recall_at_10
      value: 96.34700000000001
    - type: recall_at_100
      value: 99.715
    - type: recall_at_1000
      value: 99.995
    - type: recall_at_20
      value: 98.073
    - type: recall_at_3
      value: 88.57300000000001
    - type: recall_at_5
      value: 92.908
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 71.18966762070158
    - type: v_measure
      value: 71.18966762070158
    - type: v_measure_std
      value: 2.7498969054457048
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 74.42014716862516
    - type: v_measure
      value: 74.42014716862516
    - type: v_measure_std
      value: 9.909739891410648
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 25.041999999999998
    - type: map_at_1
      value: 5.893000000000001
    - type: map_at_10
      value: 15.260000000000002
    - type: map_at_100
      value: 18.084
    - type: map_at_1000
      value: 18.467
    - type: map_at_20
      value: 16.675
    - type: map_at_3
      value: 10.526
    - type: map_at_5
      value: 12.775
    - type: mrr_at_1
      value: 28.999999999999996
    - type: mrr_at_10
      value: 41.03575396825395
    - type: mrr_at_100
      value: 42.136771862785835
    - type: mrr_at_1000
      value: 42.16698555415099
    - type: mrr_at_20
      value: 41.707493696104315
    - type: mrr_at_3
      value: 37.34999999999998
    - type: mrr_at_5
      value: 39.59999999999995
    - type: nauc_map_at_1000_diff1
      value: 12.080002654911883
    - type: nauc_map_at_1000_max
      value: 29.813563682286276
    - type: nauc_map_at_1000_std
      value: 20.36659817908673
    - type: nauc_map_at_100_diff1
      value: 12.108735517749706
    - type: nauc_map_at_100_max
      value: 29.76830671710955
    - type: nauc_map_at_100_std
      value: 20.3433621032846
    - type: nauc_map_at_10_diff1
      value: 12.91575031185637
    - type: nauc_map_at_10_max
      value: 29.427600958386318
    - type: nauc_map_at_10_std
      value: 16.89867275177153
    - type: nauc_map_at_1_diff1
      value: 19.353069488987916
    - type: nauc_map_at_1_max
      value: 17.093914951159693
    - type: nauc_map_at_1_std
      value: 8.19886078055046
    - type: nauc_map_at_20_diff1
      value: 11.977233457943113
    - type: nauc_map_at_20_max
      value: 29.171812822948805
    - type: nauc_map_at_20_std
      value: 18.780517506173965
    - type: nauc_map_at_3_diff1
      value: 14.453129464176092
    - type: nauc_map_at_3_max
      value: 25.801958649112077
    - type: nauc_map_at_3_std
      value: 11.572823684429643
    - type: nauc_map_at_5_diff1
      value: 13.167155808104997
    - type: nauc_map_at_5_max
      value: 27.355626948365792
    - type: nauc_map_at_5_std
      value: 14.414151839192183
    - type: nauc_mrr_at_1000_diff1
      value: 17.262104643988636
    - type: nauc_mrr_at_1000_max
      value: 23.991373837217058
    - type: nauc_mrr_at_1000_std
      value: 12.44755488671623
    - type: nauc_mrr_at_100_diff1
      value: 17.267280132318703
    - type: nauc_mrr_at_100_max
      value: 24.022189287889294
    - type: nauc_mrr_at_100_std
      value: 12.480695500214788
    - type: nauc_mrr_at_10_diff1
      value: 17.012383998246268
    - type: nauc_mrr_at_10_max
      value: 24.192637911171722
    - type: nauc_mrr_at_10_std
      value: 12.524608847408917
    - type: nauc_mrr_at_1_diff1
      value: 19.43518811038007
    - type: nauc_mrr_at_1_max
      value: 17.747482933395602
    - type: nauc_mrr_at_1_std
      value: 8.410779775558684
    - type: nauc_mrr_at_20_diff1
      value: 17.202663281407446
    - type: nauc_mrr_at_20_max
      value: 24.091991130543118
    - type: nauc_mrr_at_20_std
      value: 12.503814263019908
    - type: nauc_mrr_at_3_diff1
      value: 17.52733013432995
    - type: nauc_mrr_at_3_max
      value: 23.569459518780214
    - type: nauc_mrr_at_3_std
      value: 11.770846827520726
    - type: nauc_mrr_at_5_diff1
      value: 17.10817561975543
    - type: nauc_mrr_at_5_max
      value: 23.945141435234678
    - type: nauc_mrr_at_5_std
      value: 12.034468615317719
    - type: nauc_ndcg_at_1000_diff1
      value: 12.317811393346936
    - type: nauc_ndcg_at_1000_max
      value: 30.809991350156103
    - type: nauc_ndcg_at_1000_std
      value: 24.517501065205067
    - type: nauc_ndcg_at_100_diff1
      value: 12.824804203182936
    - type: nauc_ndcg_at_100_max
      value: 30.895499817010748
    - type: nauc_ndcg_at_100_std
      value: 25.424376279745402
    - type: nauc_ndcg_at_10_diff1
      value: 13.32724552457439
    - type: nauc_ndcg_at_10_max
      value: 30.409088666807456
    - type: nauc_ndcg_at_10_std
      value: 18.216330475714113
    - type: nauc_ndcg_at_1_diff1
      value: 19.43518811038007
    - type: nauc_ndcg_at_1_max
      value: 17.747482933395602
    - type: nauc_ndcg_at_1_std
      value: 8.410779775558684
    - type: nauc_ndcg_at_20_diff1
      value: 12.224399111852902
    - type: nauc_ndcg_at_20_max
      value: 29.86352330445272
    - type: nauc_ndcg_at_20_std
      value: 21.196937851331807
    - type: nauc_ndcg_at_3_diff1
      value: 15.367489533734027
    - type: nauc_ndcg_at_3_max
      value: 26.76486390741532
    - type: nauc_ndcg_at_3_std
      value: 12.606077508789923
    - type: nauc_ndcg_at_5_diff1
      value: 13.831157482390935
    - type: nauc_ndcg_at_5_max
      value: 28.070226983968904
    - type: nauc_ndcg_at_5_std
      value: 15.236787943125435
    - type: nauc_precision_at_1000_diff1
      value: 0.016122957101357048
    - type: nauc_precision_at_1000_max
      value: 24.380929903557334
    - type: nauc_precision_at_1000_std
      value: 34.54045112720052
    - type: nauc_precision_at_100_diff1
      value: 7.255224788507301
    - type: nauc_precision_at_100_max
      value: 27.98453788447542
    - type: nauc_precision_at_100_std
      value: 35.38999555441665
    - type: nauc_precision_at_10_diff1
      value: 9.69185099834181
    - type: nauc_precision_at_10_max
      value: 32.532315522580454
    - type: nauc_precision_at_10_std
      value: 21.48948348473612
    - type: nauc_precision_at_1_diff1
      value: 19.43518811038007
    - type: nauc_precision_at_1_max
      value: 17.747482933395602
    - type: nauc_precision_at_1_std
      value: 8.410779775558684
    - type: nauc_precision_at_20_diff1
      value: 6.964076536695672
    - type: nauc_precision_at_20_max
      value: 29.30087236410044
    - type: nauc_precision_at_20_std
      value: 26.413625895571986
    - type: nauc_precision_at_3_diff1
      value: 14.145134359925155
    - type: nauc_precision_at_3_max
      value: 29.915650960808303
    - type: nauc_precision_at_3_std
      value: 14.095370019867797
    - type: nauc_precision_at_5_diff1
      value: 11.043933558522692
    - type: nauc_precision_at_5_max
      value: 30.93016505807111
    - type: nauc_precision_at_5_std
      value: 17.749256196062603
    - type: nauc_recall_at_1000_diff1
      value: -0.7776817772090345
    - type: nauc_recall_at_1000_max
      value: 23.094717340324518
    - type: nauc_recall_at_1000_std
      value: 37.189908681396425
    - type: nauc_recall_at_100_diff1
      value: 6.887748742013364
    - type: nauc_recall_at_100_max
      value: 27.00798435230277
    - type: nauc_recall_at_100_std
      value: 35.908147807345344
    - type: nauc_recall_at_10_diff1
      value: 9.605632017480751
    - type: nauc_recall_at_10_max
      value: 31.845202901168655
    - type: nauc_recall_at_10_std
      value: 21.497414586634683
    - type: nauc_recall_at_1_diff1
      value: 19.353069488987916
    - type: nauc_recall_at_1_max
      value: 17.093914951159693
    - type: nauc_recall_at_1_std
      value: 8.19886078055046
    - type: nauc_recall_at_20_diff1
      value: 6.927503731844782
    - type: nauc_recall_at_20_max
      value: 28.611698183338202
    - type: nauc_recall_at_20_std
      value: 26.69018660149911
    - type: nauc_recall_at_3_diff1
      value: 14.043724087062268
    - type: nauc_recall_at_3_max
      value: 29.269835821380465
    - type: nauc_recall_at_3_std
      value: 14.104419605998094
    - type: nauc_recall_at_5_diff1
      value: 11.017319452873336
    - type: nauc_recall_at_5_max
      value: 30.295720628306228
    - type: nauc_recall_at_5_std
      value: 17.758048545573825
    - type: ndcg_at_1
      value: 28.999999999999996
    - type: ndcg_at_10
      value: 25.041999999999998
    - type: ndcg_at_100
      value: 35.045
    - type: ndcg_at_1000
      value: 40.803
    - type: ndcg_at_20
      value: 28.584
    - type: ndcg_at_3
      value: 23.249
    - type: ndcg_at_5
      value: 20.533
    - type: precision_at_1
      value: 28.999999999999996
    - type: precision_at_10
      value: 13.120000000000001
    - type: precision_at_100
      value: 2.7470000000000003
    - type: precision_at_1000
      value: 0.41200000000000003
    - type: precision_at_20
      value: 8.584999999999999
    - type: precision_at_3
      value: 21.633
    - type: precision_at_5
      value: 18.099999999999998
    - type: recall_at_1
      value: 5.893000000000001
    - type: recall_at_10
      value: 26.567
    - type: recall_at_100
      value: 55.800000000000004
    - type: recall_at_1000
      value: 83.608
    - type: recall_at_20
      value: 34.86
    - type: recall_at_3
      value: 13.153
    - type: recall_at_5
      value: 18.323
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 86.57284584320382
    - type: cosine_spearman
      value: 82.20531642680812
    - type: euclidean_pearson
      value: 83.94261758556554
    - type: euclidean_spearman
      value: 82.20721497738559
    - type: main_score
      value: 82.20531642680812
    - type: manhattan_pearson
      value: 84.15902154703083
    - type: manhattan_spearman
      value: 82.19506027155957
    - type: pearson
      value: 86.57284584320382
    - type: spearman
      value: 82.20531642680812
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 86.28047602146931
    - type: cosine_spearman
      value: 79.51504881448884
    - type: euclidean_pearson
      value: 83.10545189967856
    - type: euclidean_spearman
      value: 79.50586960492797
    - type: main_score
      value: 79.51504881448884
    - type: manhattan_pearson
      value: 83.44244457500889
    - type: manhattan_spearman
      value: 79.730303339846
    - type: pearson
      value: 86.28047602146931
    - type: spearman
      value: 79.51504881448884
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 88.74723553048702
    - type: cosine_spearman
      value: 89.18936052329725
    - type: euclidean_pearson
      value: 88.90400878928668
    - type: euclidean_spearman
      value: 89.19174821431281
    - type: main_score
      value: 89.18936052329725
    - type: manhattan_pearson
      value: 88.81504628424054
    - type: manhattan_spearman
      value: 89.18063294142597
    - type: pearson
      value: 88.74723553048702
    - type: spearman
      value: 89.18936052329725
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 86.45403437836023
    - type: cosine_spearman
      value: 85.14654611519086
    - type: euclidean_pearson
      value: 85.87509624462743
    - type: euclidean_spearman
      value: 85.1391108856681
    - type: main_score
      value: 85.14654611519086
    - type: manhattan_pearson
      value: 85.96635794953866
    - type: manhattan_spearman
      value: 85.3271371527667
    - type: pearson
      value: 86.45403437836023
    - type: spearman
      value: 85.14654611519086
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 87.84742260009705
    - type: cosine_spearman
      value: 89.10215217191254
    - type: euclidean_pearson
      value: 88.97393286325477
    - type: euclidean_spearman
      value: 89.1014105509662
    - type: main_score
      value: 89.10215217191254
    - type: manhattan_pearson
      value: 89.31698781090151
    - type: manhattan_spearman
      value: 89.53000001764433
    - type: pearson
      value: 87.84742260009705
    - type: spearman
      value: 89.10215217191254
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 85.22397535461835
    - type: cosine_spearman
      value: 87.14066355879785
    - type: euclidean_pearson
      value: 86.31393364087295
    - type: euclidean_spearman
      value: 87.14018892702765
    - type: main_score
      value: 87.14066355879785
    - type: manhattan_pearson
      value: 86.36366855248434
    - type: manhattan_spearman
      value: 87.20858630423012
    - type: pearson
      value: 85.22397535461835
    - type: spearman
      value: 87.14066355879785
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 90.66131612061355
    - type: cosine_spearman
      value: 90.97082650129164
    - type: euclidean_pearson
      value: 90.98181906744969
    - type: euclidean_spearman
      value: 90.99008476850047
    - type: main_score
      value: 90.97082650129164
    - type: manhattan_pearson
      value: 90.75245040709021
    - type: manhattan_spearman
      value: 90.6199877691265
    - type: pearson
      value: 90.66131612061355
    - type: spearman
      value: 90.97082650129164
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 67.270656447085
    - type: cosine_spearman
      value: 67.82870469746828
    - type: euclidean_pearson
      value: 69.03857775285664
    - type: euclidean_spearman
      value: 67.74455108773341
    - type: main_score
      value: 67.82870469746828
    - type: manhattan_pearson
      value: 69.25304172245812
    - type: manhattan_spearman
      value: 68.00987097916055
    - type: pearson
      value: 67.270656447085
    - type: spearman
      value: 67.82870469746828
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 87.17245205384889
    - type: cosine_spearman
      value: 87.7360146030987
    - type: euclidean_pearson
      value: 87.48919412794656
    - type: euclidean_spearman
      value: 87.7312047878383
    - type: main_score
      value: 87.7360146030987
    - type: manhattan_pearson
      value: 87.61476224354806
    - type: manhattan_spearman
      value: 87.95220889254693
    - type: pearson
      value: 87.17245205384889
    - type: spearman
      value: 87.7360146030987
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 88.43547871921146
    - type: map
      value: 88.43547871921146
    - type: mrr
      value: 96.5564473652709
    - type: nAUC_map_diff1
      value: -13.66029392579231
    - type: nAUC_map_max
      value: 50.325613574053506
    - type: nAUC_map_std
      value: 60.02986231275796
    - type: nAUC_mrr_diff1
      value: 23.83821476411125
    - type: nAUC_mrr_max
      value: 86.72643311769906
    - type: nAUC_mrr_std
      value: 72.12741063469213
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 78.233
    - type: map_at_1
      value: 61.49400000000001
    - type: map_at_10
      value: 73.30600000000001
    - type: map_at_100
      value: 73.719
    - type: map_at_1000
      value: 73.724
    - type: map_at_20
      value: 73.611
    - type: map_at_3
      value: 70.626
    - type: map_at_5
      value: 72.417
    - type: mrr_at_1
      value: 64.66666666666666
    - type: mrr_at_10
      value: 74.30357142857143
    - type: mrr_at_100
      value: 74.56950898079988
    - type: mrr_at_1000
      value: 74.57295833098681
    - type: mrr_at_20
      value: 74.46165223665226
    - type: mrr_at_3
      value: 72.3888888888889
    - type: mrr_at_5
      value: 73.60555555555557
    - type: nauc_map_at_1000_diff1
      value: 76.51524604780636
    - type: nauc_map_at_1000_max
      value: 53.48521938401881
    - type: nauc_map_at_1000_std
      value: -7.347799382158861
    - type: nauc_map_at_100_diff1
      value: 76.5122888096236
    - type: nauc_map_at_100_max
      value: 53.49221847471618
    - type: nauc_map_at_100_std
      value: -7.329683735681086
    - type: nauc_map_at_10_diff1
      value: 76.30928630674504
    - type: nauc_map_at_10_max
      value: 53.00102977185941
    - type: nauc_map_at_10_std
      value: -7.7467740085108705
    - type: nauc_map_at_1_diff1
      value: 79.54189281784247
    - type: nauc_map_at_1_max
      value: 46.630071622109526
    - type: nauc_map_at_1_std
      value: -14.395943134644112
    - type: nauc_map_at_20_diff1
      value: 76.41604361947962
    - type: nauc_map_at_20_max
      value: 53.578883876146875
    - type: nauc_map_at_20_std
      value: -7.403103451288041
    - type: nauc_map_at_3_diff1
      value: 76.25911617571941
    - type: nauc_map_at_3_max
      value: 49.140287380513605
    - type: nauc_map_at_3_std
      value: -11.35992449218983
    - type: nauc_map_at_5_diff1
      value: 76.35122077770336
    - type: nauc_map_at_5_max
      value: 52.1744367901208
    - type: nauc_map_at_5_std
      value: -7.85753955055384
    - type: nauc_mrr_at_1000_diff1
      value: 76.97223309515867
    - type: nauc_mrr_at_1000_max
      value: 57.263787498613326
    - type: nauc_mrr_at_1000_std
      value: -4.884090708840035
    - type: nauc_mrr_at_100_diff1
      value: 76.97312970894603
    - type: nauc_mrr_at_100_max
      value: 57.26850730446478
    - type: nauc_mrr_at_100_std
      value: -4.875200894216617
    - type: nauc_mrr_at_10_diff1
      value: 76.65927674223613
    - type: nauc_mrr_at_10_max
      value: 57.30979763941454
    - type: nauc_mrr_at_10_std
      value: -4.863331094022142
    - type: nauc_mrr_at_1_diff1
      value: 80.0454932568644
    - type: nauc_mrr_at_1_max
      value: 56.76038421319305
    - type: nauc_mrr_at_1_std
      value: -4.101939392632653
    - type: nauc_mrr_at_20_diff1
      value: 76.87237970440503
    - type: nauc_mrr_at_20_max
      value: 57.33843605225869
    - type: nauc_mrr_at_20_std
      value: -4.96248984417978
    - type: nauc_mrr_at_3_diff1
      value: 76.74130186666727
    - type: nauc_mrr_at_3_max
      value: 56.19313244846155
    - type: nauc_mrr_at_3_std
      value: -5.684365934009136
    - type: nauc_mrr_at_5_diff1
      value: 76.66406918799962
    - type: nauc_mrr_at_5_max
      value: 57.56110093228628
    - type: nauc_mrr_at_5_std
      value: -3.7464413085588073
    - type: nauc_ndcg_at_1000_diff1
      value: 76.19194173971773
    - type: nauc_ndcg_at_1000_max
      value: 55.57464600170693
    - type: nauc_ndcg_at_1000_std
      value: -6.0761689532372625
    - type: nauc_ndcg_at_100_diff1
      value: 76.14631273843654
    - type: nauc_ndcg_at_100_max
      value: 55.72246565373382
    - type: nauc_ndcg_at_100_std
      value: -5.595160698860595
    - type: nauc_ndcg_at_10_diff1
      value: 75.0108223611192
    - type: nauc_ndcg_at_10_max
      value: 55.27894212877493
    - type: nauc_ndcg_at_10_std
      value: -6.968331740214591
    - type: nauc_ndcg_at_1_diff1
      value: 80.0454932568644
    - type: nauc_ndcg_at_1_max
      value: 56.76038421319305
    - type: nauc_ndcg_at_1_std
      value: -4.101939392632653
    - type: nauc_ndcg_at_20_diff1
      value: 75.54887755702472
    - type: nauc_ndcg_at_20_max
      value: 56.406879417251496
    - type: nauc_ndcg_at_20_std
      value: -6.495231061329629
    - type: nauc_ndcg_at_3_diff1
      value: 75.03620356688509
    - type: nauc_ndcg_at_3_max
      value: 52.147381077773424
    - type: nauc_ndcg_at_3_std
      value: -8.448005688956199
    - type: nauc_ndcg_at_5_diff1
      value: 75.1195898074229
    - type: nauc_ndcg_at_5_max
      value: 54.2321033861173
    - type: nauc_ndcg_at_5_std
      value: -5.882690780895338
    - type: nauc_precision_at_1000_diff1
      value: -28.081979732100532
    - type: nauc_precision_at_1000_max
      value: 35.055348014832916
    - type: nauc_precision_at_1000_std
      value: 59.61280468927384
    - type: nauc_precision_at_100_diff1
      value: -25.112740730587458
    - type: nauc_precision_at_100_max
      value: 38.26331300116496
    - type: nauc_precision_at_100_std
      value: 62.46316222328831
    - type: nauc_precision_at_10_diff1
      value: -2.6766206473658833
    - type: nauc_precision_at_10_max
      value: 45.95321867204845
    - type: nauc_precision_at_10_std
      value: 45.07212468670564
    - type: nauc_precision_at_1_diff1
      value: 80.0454932568644
    - type: nauc_precision_at_1_max
      value: 56.76038421319305
    - type: nauc_precision_at_1_std
      value: -4.101939392632653
    - type: nauc_precision_at_20_diff1
      value: -10.698911116738385
    - type: nauc_precision_at_20_max
      value: 43.467275950182994
    - type: nauc_precision_at_20_std
      value: 48.00467321991766
    - type: nauc_precision_at_3_diff1
      value: 33.6344708541193
    - type: nauc_precision_at_3_max
      value: 49.309242331670504
    - type: nauc_precision_at_3_std
      value: 21.02940391379915
    - type: nauc_precision_at_5_diff1
      value: 13.560415600596318
    - type: nauc_precision_at_5_max
      value: 48.918726500100085
    - type: nauc_precision_at_5_std
      value: 39.940930429172184
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: 70.82166199813196
    - type: nauc_recall_at_100_max
      value: 76.6106442577042
    - type: nauc_recall_at_100_std
      value: 66.47992530345513
    - type: nauc_recall_at_10_diff1
      value: 62.68908885556092
    - type: nauc_recall_at_10_max
      value: 58.14262437741839
    - type: nauc_recall_at_10_std
      value: -12.946717875063369
    - type: nauc_recall_at_1_diff1
      value: 79.54189281784247
    - type: nauc_recall_at_1_max
      value: 46.630071622109526
    - type: nauc_recall_at_1_std
      value: -14.395943134644112
    - type: nauc_recall_at_20_diff1
      value: 65.79470497876567
    - type: nauc_recall_at_20_max
      value: 71.68308183488456
    - type: nauc_recall_at_20_std
      value: -12.556850697268453
    - type: nauc_recall_at_3_diff1
      value: 68.3240211318129
    - type: nauc_recall_at_3_max
      value: 45.05998217275036
    - type: nauc_recall_at_3_std
      value: -14.23179772593869
    - type: nauc_recall_at_5_diff1
      value: 67.53366869904056
    - type: nauc_recall_at_5_max
      value: 53.57935627081027
    - type: nauc_recall_at_5_std
      value: -3.3271112904853393
    - type: ndcg_at_1
      value: 64.667
    - type: ndcg_at_10
      value: 78.233
    - type: ndcg_at_100
      value: 79.806
    - type: ndcg_at_1000
      value: 79.92099999999999
    - type: ndcg_at_20
      value: 79.006
    - type: ndcg_at_3
      value: 74.018
    - type: ndcg_at_5
      value: 76.334
    - type: precision_at_1
      value: 64.667
    - type: precision_at_10
      value: 10.4
    - type: precision_at_100
      value: 1.1199999999999999
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.383
    - type: precision_at_3
      value: 29.444
    - type: precision_at_5
      value: 19.467000000000002
    - type: recall_at_1
      value: 61.49400000000001
    - type: recall_at_10
      value: 92.156
    - type: recall_at_100
      value: 99.167
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 94.833
    - type: recall_at_3
      value: 80.833
    - type: recall_at_5
      value: 86.6
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.8039603960396
    - type: cosine_accuracy_threshold
      value: 84.54211950302124
    - type: cosine_ap
      value: 95.59056372734358
    - type: cosine_f1
      value: 90.1394422310757
    - type: cosine_f1_threshold
      value: 84.54211950302124
    - type: cosine_precision
      value: 89.78174603174604
    - type: cosine_recall
      value: 90.5
    - type: dot_accuracy
      value: 99.80594059405941
    - type: dot_accuracy_threshold
      value: 85.57180166244507
    - type: dot_ap
      value: 95.53453431914399
    - type: dot_f1
      value: 90.10442565887618
    - type: dot_f1_threshold
      value: 84.59715843200684
    - type: dot_precision
      value: 89.61424332344214
    - type: dot_recall
      value: 90.60000000000001
    - type: euclidean_accuracy
      value: 99.8039603960396
    - type: euclidean_accuracy_threshold
      value: 53.253382444381714
    - type: euclidean_ap
      value: 95.5850992402159
    - type: euclidean_f1
      value: 90.09457441513192
    - type: euclidean_f1_threshold
      value: 55.725520849227905
    - type: euclidean_precision
      value: 89.69276511397423
    - type: euclidean_recall
      value: 90.5
    - type: main_score
      value: 95.7485189884476
    - type: manhattan_accuracy
      value: 99.81485148514851
    - type: manhattan_accuracy_threshold
      value: 3491.29638671875
    - type: manhattan_ap
      value: 95.7485189884476
    - type: manhattan_f1
      value: 90.464048954615
    - type: manhattan_f1_threshold
      value: 3491.29638671875
    - type: manhattan_precision
      value: 92.2996878251821
    - type: manhattan_recall
      value: 88.7
    - type: max_ap
      value: 95.7485189884476
    - type: max_f1
      value: 90.464048954615
    - type: max_precision
      value: 92.2996878251821
    - type: max_recall
      value: 90.60000000000001
    - type: similarity_accuracy
      value: 99.8039603960396
    - type: similarity_accuracy_threshold
      value: 84.54211950302124
    - type: similarity_ap
      value: 95.59056372734358
    - type: similarity_f1
      value: 90.1394422310757
    - type: similarity_f1_threshold
      value: 84.54211950302124
    - type: similarity_precision
      value: 89.78174603174604
    - type: similarity_recall
      value: 90.5
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 78.49205191950675
    - type: v_measure
      value: 78.49205191950675
    - type: v_measure_std
      value: 2.84869550699959
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 48.90421736513028
    - type: v_measure
      value: 48.90421736513028
    - type: v_measure_std
      value: 1.6875865714471023
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 52.9874730481696
    - type: map
      value: 52.9874730481696
    - type: mrr
      value: 53.85867604617604
    - type: nAUC_map_diff1
      value: 39.633429293407616
    - type: nAUC_map_max
      value: 10.236807988858546
    - type: nAUC_map_std
      value: 10.276522217929674
    - type: nAUC_mrr_diff1
      value: 40.0543079218377
    - type: nAUC_mrr_max
      value: 10.96209807382042
    - type: nAUC_mrr_std
      value: 10.524400196109918
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 30.727801109114232
    - type: cosine_spearman
      value: 31.66058223980157
    - type: dot_pearson
      value: 30.78818248622866
    - type: dot_spearman
      value: 31.525158776890265
    - type: main_score
      value: 31.66058223980157
    - type: pearson
      value: 30.727801109114232
    - type: spearman
      value: 31.66058223980157
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 85.206
    - type: map_at_1
      value: 0.246
    - type: map_at_10
      value: 2.1950000000000003
    - type: map_at_100
      value: 14.179
    - type: map_at_1000
      value: 35.037
    - type: map_at_20
      value: 4.143
    - type: map_at_3
      value: 0.7100000000000001
    - type: map_at_5
      value: 1.135
    - type: mrr_at_1
      value: 94.0
    - type: mrr_at_10
      value: 96.66666666666666
    - type: mrr_at_100
      value: 96.66666666666666
    - type: mrr_at_1000
      value: 96.66666666666666
    - type: mrr_at_20
      value: 96.66666666666666
    - type: mrr_at_3
      value: 96.66666666666666
    - type: mrr_at_5
      value: 96.66666666666666
    - type: nauc_map_at_1000_diff1
      value: -4.6264497624527525
    - type: nauc_map_at_1000_max
      value: 44.594457564749355
    - type: nauc_map_at_1000_std
      value: 73.17642341400133
    - type: nauc_map_at_100_diff1
      value: 23.451335157405726
    - type: nauc_map_at_100_max
      value: 25.426398857299525
    - type: nauc_map_at_100_std
      value: 64.07416694472633
    - type: nauc_map_at_10_diff1
      value: 46.57568738568346
    - type: nauc_map_at_10_max
      value: 9.693233249079238
    - type: nauc_map_at_10_std
      value: 28.549530265164357
    - type: nauc_map_at_1_diff1
      value: 53.48238396620123
    - type: nauc_map_at_1_max
      value: 0.33476619393733076
    - type: nauc_map_at_1_std
      value: 8.906362219128463
    - type: nauc_map_at_20_diff1
      value: 39.40719602207749
    - type: nauc_map_at_20_max
      value: 9.635915072074045
    - type: nauc_map_at_20_std
      value: 35.15634791346394
    - type: nauc_map_at_3_diff1
      value: 53.11784737840137
    - type: nauc_map_at_3_max
      value: 3.059682761072153
    - type: nauc_map_at_3_std
      value: 21.310633086556617
    - type: nauc_map_at_5_diff1
      value: 49.91570701185436
    - type: nauc_map_at_5_max
      value: 8.045082896244576
    - type: nauc_map_at_5_std
      value: 20.597686235051647
    - type: nauc_mrr_at_1000_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_1000_max
      value: 78.24463118580779
    - type: nauc_mrr_at_1000_std
      value: 0.30812324930028195
    - type: nauc_mrr_at_100_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_100_max
      value: 78.24463118580779
    - type: nauc_mrr_at_100_std
      value: 0.30812324930028195
    - type: nauc_mrr_at_10_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_10_max
      value: 78.24463118580779
    - type: nauc_mrr_at_10_std
      value: 0.30812324930028195
    - type: nauc_mrr_at_1_diff1
      value: 38.62433862433873
    - type: nauc_mrr_at_1_max
      value: 80.78120136943666
    - type: nauc_mrr_at_1_std
      value: -10.768751945222197
    - type: nauc_mrr_at_20_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_20_max
      value: 78.24463118580779
    - type: nauc_mrr_at_20_std
      value: 0.30812324930028195
    - type: nauc_mrr_at_3_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_3_max
      value: 78.24463118580779
    - type: nauc_mrr_at_3_std
      value: 0.30812324930028195
    - type: nauc_mrr_at_5_diff1
      value: 41.98412698412726
    - type: nauc_mrr_at_5_max
      value: 78.24463118580779
    - type: nauc_mrr_at_5_std
      value: 0.30812324930028195
    - type: nauc_ndcg_at_1000_diff1
      value: 0.5174948602880207
    - type: nauc_ndcg_at_1000_max
      value: 48.60686602077053
    - type: nauc_ndcg_at_1000_std
      value: 75.72456343175277
    - type: nauc_ndcg_at_100_diff1
      value: -20.747252137999254
    - type: nauc_ndcg_at_100_max
      value: 49.985132618254994
    - type: nauc_ndcg_at_100_std
      value: 61.096383293836574
    - type: nauc_ndcg_at_10_diff1
      value: 6.791377920463332
    - type: nauc_ndcg_at_10_max
      value: 57.50019332833286
    - type: nauc_ndcg_at_10_std
      value: 49.201028841219426
    - type: nauc_ndcg_at_1_diff1
      value: 54.92683440362145
    - type: nauc_ndcg_at_1_max
      value: 83.8667228129276
    - type: nauc_ndcg_at_1_std
      value: 1.6738604063586122
    - type: nauc_ndcg_at_20_diff1
      value: -5.1948699196314925
    - type: nauc_ndcg_at_20_max
      value: 54.483087684806556
    - type: nauc_ndcg_at_20_std
      value: 50.54823818118781
    - type: nauc_ndcg_at_3_diff1
      value: 26.267246500164372
    - type: nauc_ndcg_at_3_max
      value: 63.0173212926611
    - type: nauc_ndcg_at_3_std
      value: 41.025597406368256
    - type: nauc_ndcg_at_5_diff1
      value: 16.910185454343036
    - type: nauc_ndcg_at_5_max
      value: 60.9328683868778
    - type: nauc_ndcg_at_5_std
      value: 36.70169905857712
    - type: nauc_precision_at_1000_diff1
      value: -46.374447765983525
    - type: nauc_precision_at_1000_max
      value: 35.36052337813863
    - type: nauc_precision_at_1000_std
      value: 14.219220668161018
    - type: nauc_precision_at_100_diff1
      value: -29.7838083657744
    - type: nauc_precision_at_100_max
      value: 43.93589400385112
    - type: nauc_precision_at_100_std
      value: 55.425045718579945
    - type: nauc_precision_at_10_diff1
      value: -12.016613405227687
    - type: nauc_precision_at_10_max
      value: 57.79924427743131
    - type: nauc_precision_at_10_std
      value: 49.022036703550675
    - type: nauc_precision_at_1_diff1
      value: 38.62433862433873
    - type: nauc_precision_at_1_max
      value: 80.78120136943666
    - type: nauc_precision_at_1_std
      value: -10.768751945222197
    - type: nauc_precision_at_20_diff1
      value: -23.95633847880195
    - type: nauc_precision_at_20_max
      value: 48.34715917258276
    - type: nauc_precision_at_20_std
      value: 48.82198285255887
    - type: nauc_precision_at_3_diff1
      value: 6.871296905858807
    - type: nauc_precision_at_3_max
      value: 70.54805793285054
    - type: nauc_precision_at_3_std
      value: 44.65108624094803
    - type: nauc_precision_at_5_diff1
      value: -9.074932448759695
    - type: nauc_precision_at_5_max
      value: 67.41284242437573
    - type: nauc_precision_at_5_std
      value: 23.876891983919577
    - type: nauc_recall_at_1000_diff1
      value: 8.142288830293255
    - type: nauc_recall_at_1000_max
      value: 38.85182826835104
    - type: nauc_recall_at_1000_std
      value: 68.60783819217335
    - type: nauc_recall_at_100_diff1
      value: 34.262914076287466
    - type: nauc_recall_at_100_max
      value: 12.87009658528838
    - type: nauc_recall_at_100_std
      value: 56.21330603762995
    - type: nauc_recall_at_10_diff1
      value: 49.33830945338758
    - type: nauc_recall_at_10_max
      value: 0.3539875530671406
    - type: nauc_recall_at_10_std
      value: 26.85864465557644
    - type: nauc_recall_at_1_diff1
      value: 53.48238396620123
    - type: nauc_recall_at_1_max
      value: 0.33476619393733076
    - type: nauc_recall_at_1_std
      value: 8.906362219128463
    - type: nauc_recall_at_20_diff1
      value: 44.21928181266254
    - type: nauc_recall_at_20_max
      value: -0.9198356057088594
    - type: nauc_recall_at_20_std
      value: 31.484376992896784
    - type: nauc_recall_at_3_diff1
      value: 53.038093080990876
    - type: nauc_recall_at_3_max
      value: -1.4170895916973003
    - type: nauc_recall_at_3_std
      value: 21.890202855574497
    - type: nauc_recall_at_5_diff1
      value: 49.39742214825278
    - type: nauc_recall_at_5_max
      value: 2.8412267611894517
    - type: nauc_recall_at_5_std
      value: 18.01598921859512
    - type: ndcg_at_1
      value: 91.0
    - type: ndcg_at_10
      value: 85.206
    - type: ndcg_at_100
      value: 67.29
    - type: ndcg_at_1000
      value: 60.584
    - type: ndcg_at_20
      value: 82.321
    - type: ndcg_at_3
      value: 88.642
    - type: ndcg_at_5
      value: 87.063
    - type: precision_at_1
      value: 94.0
    - type: precision_at_10
      value: 89.8
    - type: precision_at_100
      value: 69.78
    - type: precision_at_1000
      value: 26.738
    - type: precision_at_20
      value: 87.2
    - type: precision_at_3
      value: 92.0
    - type: precision_at_5
      value: 90.8
    - type: recall_at_1
      value: 0.246
    - type: recall_at_10
      value: 2.344
    - type: recall_at_100
      value: 16.962
    - type: recall_at_1000
      value: 57.325
    - type: recall_at_20
      value: 4.517
    - type: recall_at_3
      value: 0.731
    - type: recall_at_5
      value: 1.1780000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 31.455
    - type: map_at_1
      value: 2.9739999999999998
    - type: map_at_10
      value: 12.183
    - type: map_at_100
      value: 18.772
    - type: map_at_1000
      value: 20.415
    - type: map_at_20
      value: 14.451
    - type: map_at_3
      value: 6.507000000000001
    - type: map_at_5
      value: 8.66
    - type: mrr_at_1
      value: 40.816326530612244
    - type: mrr_at_10
      value: 57.70975056689341
    - type: mrr_at_100
      value: 58.18379126542391
    - type: mrr_at_1000
      value: 58.18379126542391
    - type: mrr_at_20
      value: 57.85552316164561
    - type: mrr_at_3
      value: 54.08163265306123
    - type: mrr_at_5
      value: 56.42857142857143
    - type: nauc_map_at_1000_diff1
      value: 3.1567471051481437
    - type: nauc_map_at_1000_max
      value: -1.5882060729791523
    - type: nauc_map_at_1000_std
      value: 18.69622198722074
    - type: nauc_map_at_100_diff1
      value: 3.3449677678147536
    - type: nauc_map_at_100_max
      value: -2.8928606866168405
    - type: nauc_map_at_100_std
      value: 15.789984947653412
    - type: nauc_map_at_10_diff1
      value: 2.9696743570444264
    - type: nauc_map_at_10_max
      value: -9.096749212011876
    - type: nauc_map_at_10_std
      value: -5.38545817258353
    - type: nauc_map_at_1_diff1
      value: 20.680780404542546
    - type: nauc_map_at_1_max
      value: -7.04722927447817
    - type: nauc_map_at_1_std
      value: -7.062494733973898
    - type: nauc_map_at_20_diff1
      value: 4.070437790119271
    - type: nauc_map_at_20_max
      value: -4.84491434686032
    - type: nauc_map_at_20_std
      value: 0.5846341109021014
    - type: nauc_map_at_3_diff1
      value: 11.9634978045925
    - type: nauc_map_at_3_max
      value: -8.27834591046608
    - type: nauc_map_at_3_std
      value: -8.687615453381065
    - type: nauc_map_at_5_diff1
      value: 0.9195191526009436
    - type: nauc_map_at_5_max
      value: -1.673813362719489
    - type: nauc_map_at_5_std
      value: -6.67549753473631
    - type: nauc_mrr_at_1000_diff1
      value: 19.877993208719573
    - type: nauc_mrr_at_1000_max
      value: -10.37776706406218
    - type: nauc_mrr_at_1000_std
      value: 7.132169578056367
    - type: nauc_mrr_at_100_diff1
      value: 19.877993208719573
    - type: nauc_mrr_at_100_max
      value: -10.37776706406218
    - type: nauc_mrr_at_100_std
      value: 7.132169578056367
    - type: nauc_mrr_at_10_diff1
      value: 20.414285568401457
    - type: nauc_mrr_at_10_max
      value: -9.677800295687861
    - type: nauc_mrr_at_10_std
      value: 8.001103690180859
    - type: nauc_mrr_at_1_diff1
      value: 22.393284073955723
    - type: nauc_mrr_at_1_max
      value: -5.889370191243167
    - type: nauc_mrr_at_1_std
      value: -1.5183536173658247
    - type: nauc_mrr_at_20_diff1
      value: 20.455564720604055
    - type: nauc_mrr_at_20_max
      value: -10.230642830103074
    - type: nauc_mrr_at_20_std
      value: 7.863582453266621
    - type: nauc_mrr_at_3_diff1
      value: 17.554895390732618
    - type: nauc_mrr_at_3_max
      value: -15.618463505555052
    - type: nauc_mrr_at_3_std
      value: 5.913231577966864
    - type: nauc_mrr_at_5_diff1
      value: 18.393678507779914
    - type: nauc_mrr_at_5_max
      value: -11.903593353147762
    - type: nauc_mrr_at_5_std
      value: 7.580745996262831
    - type: nauc_ndcg_at_1000_diff1
      value: 13.746937095530473
    - type: nauc_ndcg_at_1000_max
      value: -0.9319249687895838
    - type: nauc_ndcg_at_1000_std
      value: 38.56328031451904
    - type: nauc_ndcg_at_100_diff1
      value: 13.854865944415895
    - type: nauc_ndcg_at_100_max
      value: -7.142142012591404
    - type: nauc_ndcg_at_100_std
      value: 35.61341954818848
    - type: nauc_ndcg_at_10_diff1
      value: 9.010144273248759
    - type: nauc_ndcg_at_10_max
      value: -15.320014897424574
    - type: nauc_ndcg_at_10_std
      value: 2.84883880489144
    - type: nauc_ndcg_at_1_diff1
      value: 20.939533945592967
    - type: nauc_ndcg_at_1_max
      value: -6.387319972188946
    - type: nauc_ndcg_at_1_std
      value: -0.5258673122126726
    - type: nauc_ndcg_at_20_diff1
      value: 14.660827309009496
    - type: nauc_ndcg_at_20_max
      value: -13.476196120145994
    - type: nauc_ndcg_at_20_std
      value: 8.22391881710838
    - type: nauc_ndcg_at_3_diff1
      value: 13.429985227235935
    - type: nauc_ndcg_at_3_max
      value: -14.904544592570247
    - type: nauc_ndcg_at_3_std
      value: 1.599779998183342
    - type: nauc_ndcg_at_5_diff1
      value: 8.085466231900622
    - type: nauc_ndcg_at_5_max
      value: -9.09591969526831
    - type: nauc_ndcg_at_5_std
      value: 3.5794092637248505
    - type: nauc_precision_at_1000_diff1
      value: -9.31941215946743
    - type: nauc_precision_at_1000_max
      value: 31.52913520470716
    - type: nauc_precision_at_1000_std
      value: 22.720784312185856
    - type: nauc_precision_at_100_diff1
      value: 8.958548406995279
    - type: nauc_precision_at_100_max
      value: 15.100597910674104
    - type: nauc_precision_at_100_std
      value: 71.04548238175113
    - type: nauc_precision_at_10_diff1
      value: 12.4698194690008
    - type: nauc_precision_at_10_max
      value: -15.84870544871496
    - type: nauc_precision_at_10_std
      value: 7.575297622501928
    - type: nauc_precision_at_1_diff1
      value: 22.393284073955723
    - type: nauc_precision_at_1_max
      value: -5.889370191243167
    - type: nauc_precision_at_1_std
      value: -1.5183536173658247
    - type: nauc_precision_at_20_diff1
      value: 15.393505718138758
    - type: nauc_precision_at_20_max
      value: -3.70684298539384
    - type: nauc_precision_at_20_std
      value: 29.426137824970304
    - type: nauc_precision_at_3_diff1
      value: 9.997768085465394
    - type: nauc_precision_at_3_max
      value: -17.12224314347674
    - type: nauc_precision_at_3_std
      value: -1.343018166772313
    - type: nauc_precision_at_5_diff1
      value: 3.8936997437913554
    - type: nauc_precision_at_5_max
      value: -5.689104289687632
    - type: nauc_precision_at_5_std
      value: 3.181098051304285
    - type: nauc_recall_at_1000_diff1
      value: 9.908303508158387
    - type: nauc_recall_at_1000_max
      value: 6.174506592699848
    - type: nauc_recall_at_1000_std
      value: 77.41931114780012
    - type: nauc_recall_at_100_diff1
      value: 10.286839241876192
    - type: nauc_recall_at_100_max
      value: -6.6138697026666815
    - type: nauc_recall_at_100_std
      value: 49.608313692633224
    - type: nauc_recall_at_10_diff1
      value: 2.215545846659851
    - type: nauc_recall_at_10_max
      value: -17.83025802478445
    - type: nauc_recall_at_10_std
      value: -3.3784768673705465
    - type: nauc_recall_at_1_diff1
      value: 20.680780404542546
    - type: nauc_recall_at_1_max
      value: -7.04722927447817
    - type: nauc_recall_at_1_std
      value: -7.062494733973898
    - type: nauc_recall_at_20_diff1
      value: 6.974410239251615
    - type: nauc_recall_at_20_max
      value: -14.161147924731646
    - type: nauc_recall_at_20_std
      value: 9.328412057721454
    - type: nauc_recall_at_3_diff1
      value: 7.904589805754212
    - type: nauc_recall_at_3_max
      value: -12.1912388648593
    - type: nauc_recall_at_3_std
      value: -9.221542013385555
    - type: nauc_recall_at_5_diff1
      value: -3.2604132752706914
    - type: nauc_recall_at_5_max
      value: -6.886351441658915
    - type: nauc_recall_at_5_std
      value: -7.014252851712789
    - type: ndcg_at_1
      value: 39.796
    - type: ndcg_at_10
      value: 31.455
    - type: ndcg_at_100
      value: 42.388999999999996
    - type: ndcg_at_1000
      value: 53.556000000000004
    - type: ndcg_at_20
      value: 30.808000000000003
    - type: ndcg_at_3
      value: 35.831
    - type: ndcg_at_5
      value: 32.845
    - type: precision_at_1
      value: 40.816
    - type: precision_at_10
      value: 27.143
    - type: precision_at_100
      value: 8.449
    - type: precision_at_1000
      value: 1.6179999999999999
    - type: precision_at_20
      value: 19.387999999999998
    - type: precision_at_3
      value: 35.374
    - type: precision_at_5
      value: 31.019999999999996
    - type: recall_at_1
      value: 2.9739999999999998
    - type: recall_at_10
      value: 19.39
    - type: recall_at_100
      value: 51.636
    - type: recall_at_1000
      value: 86.99900000000001
    - type: recall_at_20
      value: 26.478
    - type: recall_at_3
      value: 7.703
    - type: recall_at_5
      value: 11.42
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 86.9384765625
    - type: ap
      value: 31.737513704141552
    - type: ap_weighted
      value: 31.737513704141552
    - type: f1
      value: 71.5490757306975
    - type: f1_weighted
      value: 89.14632533489856
    - type: main_score
      value: 86.9384765625
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 73.57668364459535
    - type: f1
      value: 73.90467103648074
    - type: f1_weighted
      value: 73.42158415034704
    - type: main_score
      value: 73.57668364459535
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 58.574148097494685
    - type: v_measure
      value: 58.574148097494685
    - type: v_measure_std
      value: 0.9443161637490822
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.1385229778864
    - type: cosine_accuracy_threshold
      value: 83.86307954788208
    - type: cosine_ap
      value: 80.17965893449055
    - type: cosine_f1
      value: 73.0614300100705
    - type: cosine_f1_threshold
      value: 80.7942807674408
    - type: cosine_precision
      value: 69.8603755416466
    - type: cosine_recall
      value: 76.56992084432717
    - type: dot_accuracy
      value: 88.2100494724921
    - type: dot_accuracy_threshold
      value: 83.84793996810913
    - type: dot_ap
      value: 80.18603932881858
    - type: dot_f1
      value: 73.07643714466204
    - type: dot_f1_threshold
      value: 80.87586164474487
    - type: dot_precision
      value: 70.10909090909091
    - type: dot_recall
      value: 76.3060686015831
    - type: euclidean_accuracy
      value: 88.1385229778864
    - type: euclidean_accuracy_threshold
      value: 56.77661895751953
    - type: euclidean_ap
      value: 80.1784070881624
    - type: euclidean_f1
      value: 73.04830369529574
    - type: euclidean_f1_threshold
      value: 61.91838979721069
    - type: euclidean_precision
      value: 69.96859144720948
    - type: euclidean_recall
      value: 76.41160949868075
    - type: main_score
      value: 80.18603932881858
    - type: manhattan_accuracy
      value: 88.0431543184121
    - type: manhattan_accuracy_threshold
      value: 3755.6137084960938
    - type: manhattan_ap
      value: 79.98270453664578
    - type: manhattan_f1
      value: 72.68242015061023
    - type: manhattan_f1_threshold
      value: 3892.494583129883
    - type: manhattan_precision
      value: 71.54907975460122
    - type: manhattan_recall
      value: 73.85224274406332
    - type: max_ap
      value: 80.18603932881858
    - type: max_f1
      value: 73.07643714466204
    - type: max_precision
      value: 71.54907975460122
    - type: max_recall
      value: 76.56992084432717
    - type: similarity_accuracy
      value: 88.1385229778864
    - type: similarity_accuracy_threshold
      value: 83.86307954788208
    - type: similarity_ap
      value: 80.17965893449055
    - type: similarity_f1
      value: 73.0614300100705
    - type: similarity_f1_threshold
      value: 80.7942807674408
    - type: similarity_precision
      value: 69.8603755416466
    - type: similarity_recall
      value: 76.56992084432717
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 89.7892653393876
    - type: cosine_accuracy_threshold
      value: 79.69566583633423
    - type: cosine_ap
      value: 87.4579867302024
    - type: cosine_f1
      value: 79.91620843152658
    - type: cosine_f1_threshold
      value: 78.53609323501587
    - type: cosine_precision
      value: 77.7155329210622
    - type: cosine_recall
      value: 82.24514936864799
    - type: dot_accuracy
      value: 89.78732487289945
    - type: dot_accuracy_threshold
      value: 80.05315661430359
    - type: dot_ap
      value: 87.44916182456272
    - type: dot_f1
      value: 79.90419878751591
    - type: dot_f1_threshold
      value: 78.57890725135803
    - type: dot_precision
      value: 77.73409057812728
    - type: dot_recall
      value: 82.19895287958116
    - type: euclidean_accuracy
      value: 89.78538440641131
    - type: euclidean_accuracy_threshold
      value: 62.29925751686096
    - type: euclidean_ap
      value: 87.45904868911386
    - type: euclidean_f1
      value: 79.93127404474657
    - type: euclidean_f1_threshold
      value: 65.61101078987122
    - type: euclidean_precision
      value: 77.62060210373595
    - type: euclidean_recall
      value: 82.38373883584848
    - type: main_score
      value: 87.46554314325058
    - type: manhattan_accuracy
      value: 89.76597974152986
    - type: manhattan_accuracy_threshold
      value: 3988.5299682617188
    - type: manhattan_ap
      value: 87.46554314325058
    - type: manhattan_f1
      value: 79.97181740645973
    - type: manhattan_f1_threshold
      value: 4235.905838012695
    - type: manhattan_precision
      value: 77.13713427283783
    - type: manhattan_recall
      value: 83.02279026793964
    - type: max_ap
      value: 87.46554314325058
    - type: max_f1
      value: 79.97181740645973
    - type: max_precision
      value: 77.73409057812728
    - type: max_recall
      value: 83.02279026793964
    - type: similarity_accuracy
      value: 89.7892653393876
    - type: similarity_accuracy_threshold
      value: 79.69566583633423
    - type: similarity_ap
      value: 87.4579867302024
    - type: similarity_f1
      value: 79.91620843152658
    - type: similarity_f1_threshold
      value: 78.53609323501587
    - type: similarity_precision
      value: 77.7155329210622
    - type: similarity_recall
      value: 82.24514936864799
    task:
      type: PairClassification
tags:
- mteb
- sentence-transformers
- transformers
- sentence-similarity
license: mit
---



# Updates

New open-source models and ToDoList will be listed on https://github.com/DunZhang/Stella/blob/main/news_and_todo.md.

You can also find these models on my [homepage](https://huggingface.co/infgrad).

# Introduction

The models are trained based on `Alibaba-NLP/gte-large-en-v1.5` and `Alibaba-NLP/gte-Qwen2-1.5B-instruct`. Thanks for
their contributions!

**We simplify usage of prompts, providing two prompts for most general tasks, one is for s2p, another one is for s2s.**

Prompt of s2p task(e.g. retrieve task):

```text
Instruct: Given a web search query, retrieve relevant passages that answer the query.\nQuery: {query}
```

Prompt of s2s task(e.g. semantic textual similarity task):

```text
Instruct: Retrieve semantically similar text.\nQuery: {query}
```

The models are finally trained by [MRL]((https://arxiv.org/abs/2205.13147)), so they have multiple dimensions: 512, 768,
1024, 2048, 4096, 6144 and 8192.

The higher the dimension, the better the performance.
**Generally speaking, 1024d is good enough.** The MTEB score of 1024d is only 0.001 lower than 8192d.

# Model directory structure

The model directory structure is very simple, it is a standard SentenceTransformer directory **with a series
of `2_Dense_{dims}`
folders**, where `dims` represents the final vector dimension.

For example, the `2_Dense_256` folder stores Linear weights that convert vector dimensions to 256 dimensions.
Please refer to the following chapters for specific instructions on how to use them.

# Usage

You can use `SentenceTransformers` or `transformers` library to encode text.

## Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

# This model supports two prompts: "s2p_query" and "s2s_query" for sentence-to-passage and sentence-to-sentence tasks, respectively.
# They are defined in `config_sentence_transformers.json`
prompt_name = "s2p_query"
queries = [
    "What are some ways to reduce stress?",
    "What are the benefits of drinking green tea?",
]
# docs do not need any prompts
docs = [
    "There are many effective ways to reduce stress. Some common techniques include deep breathing, meditation, and physical activity. Engaging in hobbies, spending time in nature, and connecting with loved ones can also help alleviate stress. Additionally, setting boundaries, practicing self-care, and learning to say no can prevent stress from building up.",
    "Green tea has been consumed for centuries and is known for its potential health benefits. It contains antioxidants that may help protect the body against damage caused by free radicals. Regular consumption of green tea has been associated with improved heart health, enhanced cognitive function, and a reduced risk of certain types of cancer. The polyphenols in green tea may also have anti-inflammatory and weight loss properties.",
]

# ！The default dimension is 1024, if you need other dimensions, please clone the model and modify `modules.json` to replace `2_Dense_1024` with another dimension, e.g. `2_Dense_256` or `2_Dense_8192` !
model = SentenceTransformer("infgrad/stella_en_400M_v5", trust_remote_code=True).cuda()
query_embeddings = model.encode(queries, prompt_name=query_prompt_name)
doc_embeddings = model.encode(docs)
print(query_embeddings.shape, doc_embeddings.shape)
# (2, 1024) (2, 1024)

similarities = model.similarity(query_embeddings, doc_embeddings)
print(similarities)
# tensor([[0.8398, 0.2990],
#         [0.3282, 0.8095]])
```

## Transformers

```python
import os
import torch
from transformers import AutoModel, AutoTokenizer
from sklearn.preprocessing import normalize

query_prompt = "Instruct: Given a web search query, retrieve relevant passages that answer the query.\nQuery: "
queries = [
    "What are some ways to reduce stress?",
    "What are the benefits of drinking green tea?",
]
queries = [query_prompt + query for query in queries]
# docs do not need any prompts
docs = [
    "There are many effective ways to reduce stress. Some common techniques include deep breathing, meditation, and physical activity. Engaging in hobbies, spending time in nature, and connecting with loved ones can also help alleviate stress. Additionally, setting boundaries, practicing self-care, and learning to say no can prevent stress from building up.",
    "Green tea has been consumed for centuries and is known for its potential health benefits. It contains antioxidants that may help protect the body against damage caused by free radicals. Regular consumption of green tea has been associated with improved heart health, enhanced cognitive function, and a reduced risk of certain types of cancer. The polyphenols in green tea may also have anti-inflammatory and weight loss properties.",
]

# The path of your model after cloning it
model_dir = "{Your MODEL_PATH}"

vector_dim = 1024
vector_linear_directory = f"2_Dense_{vector_dim}"
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).cuda().eval()
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
vector_linear = torch.nn.Linear(in_features=model.config.hidden_size, out_features=vector_dim)
vector_linear_dict = {
    k.replace("linear.", ""): v for k, v in
    torch.load(os.path.join(model_dir, f"{vector_linear_directory}/pytorch_model.bin")).items()
}
vector_linear.load_state_dict(vector_linear_dict)
vector_linear.cuda()

# Embed the queries
with torch.no_grad():
    input_data = tokenizer(queries, padding="longest", truncation=True, max_length=512, return_tensors="pt")
    input_data = {k: v.cuda() for k, v in input_data.items()}
    attention_mask = input_data["attention_mask"]
    last_hidden_state = model(**input_data)[0]
    last_hidden = last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0)
    query_vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]
    query_vectors = normalize(vector_linear(query_vectors).cpu().numpy())

# Embed the documents
with torch.no_grad():
    input_data = tokenizer(docs, padding="longest", truncation=True, max_length=512, return_tensors="pt")
    input_data = {k: v.cuda() for k, v in input_data.items()}
    attention_mask = input_data["attention_mask"]
    last_hidden_state = model(**input_data)[0]
    last_hidden = last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0)
    docs_vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]
    docs_vectors = normalize(vector_linear(docs_vectors).cpu().numpy())

print(query_vectors.shape, docs_vectors.shape)
# (2, 1024) (2, 1024)

similarities = query_vectors @ docs_vectors.T
print(similarities)
# [[0.8397531  0.29900077]
#  [0.32818374 0.80954516]]
```

# FAQ

Q: The details of training?

A: The training method and datasets will be released in the future. (specific time unknown, may be provided in a paper)

Q: How to choose a suitable prompt for my own task?

A: In most cases, please use the s2p and s2s prompts. These two prompts account for the vast majority of the training
data.

Q: How to reproduce MTEB results?

A: Please use evaluation scripts in `Alibaba-NLP/gte-Qwen2-1.5B-instruct` or `intfloat/e5-mistral-7b-instruct`

Q: Why each dimension has a linear weight?

A: MRL has multiple training methods, we choose this method which has the best performance.

Q: What is the sequence length of models?

A: 512 is recommended, in our experiments, almost all models perform poorly on specialized long text retrieval datasets. Besides, the
model is trained on datasets of 512 length. This may be an optimization term.

If you have any questions, please start a discussion on community.