---
library_name: transformers
tags:
- sentence-transformers
- gte
- mteb
- transformers.js
- sentence-similarity
license: apache-2.0
language:
- en
model-index:
- name: gte-base-en-v1.5
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 74.7910447761194
    - type: ap
      value: 37.053785713650626
    - type: f1
      value: 68.51101510998551
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 93.016875
    - type: ap
      value: 89.17750268426342
    - type: f1
      value: 92.9970977240524
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 53.312000000000005
    - type: f1
      value: 52.98175784163017
  - task:
      type: Retrieval
    dataset:
      type: mteb/arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
    metrics:
    - type: map_at_1
      value: 38.193
    - type: map_at_10
      value: 54.848
    - type: map_at_100
      value: 55.388000000000005
    - type: map_at_1000
      value: 55.388999999999996
    - type: map_at_3
      value: 50.427
    - type: map_at_5
      value: 53.105000000000004
    - type: mrr_at_1
      value: 39.047
    - type: mrr_at_10
      value: 55.153
    - type: mrr_at_100
      value: 55.686
    - type: mrr_at_1000
      value: 55.688
    - type: mrr_at_3
      value: 50.676
    - type: mrr_at_5
      value: 53.417
    - type: ndcg_at_1
      value: 38.193
    - type: ndcg_at_10
      value: 63.486
    - type: ndcg_at_100
      value: 65.58
    - type: ndcg_at_1000
      value: 65.61
    - type: ndcg_at_3
      value: 54.494
    - type: ndcg_at_5
      value: 59.339
    - type: precision_at_1
      value: 38.193
    - type: precision_at_10
      value: 9.075
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 22.096
    - type: precision_at_5
      value: 15.619
    - type: recall_at_1
      value: 38.193
    - type: recall_at_10
      value: 90.754
    - type: recall_at_100
      value: 99.431
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 66.28699999999999
    - type: recall_at_5
      value: 78.094
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 47.508221208908964
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 42.04668382560096
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 61.828759903716815
    - type: mrr
      value: 74.37343358395991
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 85.03673698773017
    - type: cos_sim_spearman
      value: 83.6470866785058
    - type: euclidean_pearson
      value: 82.64048673096565
    - type: euclidean_spearman
      value: 83.63142367101115
    - type: manhattan_pearson
      value: 82.71493099760228
    - type: manhattan_spearman
      value: 83.60491704294326
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 86.73376623376623
    - type: f1
      value: 86.70294049278262
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 40.31923804167062
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 37.552547125348454
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-android
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: f46a197baaae43b4f621051089b82a364682dfeb
    metrics:
    - type: map_at_1
      value: 30.567
    - type: map_at_10
      value: 41.269
    - type: map_at_100
      value: 42.689
    - type: map_at_1000
      value: 42.84
    - type: map_at_3
      value: 37.567
    - type: map_at_5
      value: 39.706
    - type: mrr_at_1
      value: 37.053000000000004
    - type: mrr_at_10
      value: 46.900999999999996
    - type: mrr_at_100
      value: 47.662
    - type: mrr_at_1000
      value: 47.713
    - type: mrr_at_3
      value: 43.801
    - type: mrr_at_5
      value: 45.689
    - type: ndcg_at_1
      value: 37.053000000000004
    - type: ndcg_at_10
      value: 47.73
    - type: ndcg_at_100
      value: 53.128
    - type: ndcg_at_1000
      value: 55.300000000000004
    - type: ndcg_at_3
      value: 42.046
    - type: ndcg_at_5
      value: 44.782
    - type: precision_at_1
      value: 37.053000000000004
    - type: precision_at_10
      value: 9.142
    - type: precision_at_100
      value: 1.485
    - type: precision_at_1000
      value: 0.197
    - type: precision_at_3
      value: 20.076
    - type: precision_at_5
      value: 14.535
    - type: recall_at_1
      value: 30.567
    - type: recall_at_10
      value: 60.602999999999994
    - type: recall_at_100
      value: 83.22800000000001
    - type: recall_at_1000
      value: 96.696
    - type: recall_at_3
      value: 44.336999999999996
    - type: recall_at_5
      value: 51.949
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-english
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
    metrics:
    - type: map_at_1
      value: 28.538000000000004
    - type: map_at_10
      value: 38.757999999999996
    - type: map_at_100
      value: 40.129
    - type: map_at_1000
      value: 40.262
    - type: map_at_3
      value: 35.866
    - type: map_at_5
      value: 37.417
    - type: mrr_at_1
      value: 36.051
    - type: mrr_at_10
      value: 44.868
    - type: mrr_at_100
      value: 45.568999999999996
    - type: mrr_at_1000
      value: 45.615
    - type: mrr_at_3
      value: 42.558
    - type: mrr_at_5
      value: 43.883
    - type: ndcg_at_1
      value: 36.051
    - type: ndcg_at_10
      value: 44.584
    - type: ndcg_at_100
      value: 49.356
    - type: ndcg_at_1000
      value: 51.39
    - type: ndcg_at_3
      value: 40.389
    - type: ndcg_at_5
      value: 42.14
    - type: precision_at_1
      value: 36.051
    - type: precision_at_10
      value: 8.446
    - type: precision_at_100
      value: 1.411
    - type: precision_at_1000
      value: 0.19
    - type: precision_at_3
      value: 19.639
    - type: precision_at_5
      value: 13.796
    - type: recall_at_1
      value: 28.538000000000004
    - type: recall_at_10
      value: 54.99000000000001
    - type: recall_at_100
      value: 75.098
    - type: recall_at_1000
      value: 87.848
    - type: recall_at_3
      value: 42.236000000000004
    - type: recall_at_5
      value: 47.377
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gaming
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
    metrics:
    - type: map_at_1
      value: 37.188
    - type: map_at_10
      value: 50.861000000000004
    - type: map_at_100
      value: 51.917
    - type: map_at_1000
      value: 51.964999999999996
    - type: map_at_3
      value: 47.144000000000005
    - type: map_at_5
      value: 49.417
    - type: mrr_at_1
      value: 42.571
    - type: mrr_at_10
      value: 54.086999999999996
    - type: mrr_at_100
      value: 54.739000000000004
    - type: mrr_at_1000
      value: 54.762
    - type: mrr_at_3
      value: 51.285000000000004
    - type: mrr_at_5
      value: 53.0
    - type: ndcg_at_1
      value: 42.571
    - type: ndcg_at_10
      value: 57.282
    - type: ndcg_at_100
      value: 61.477000000000004
    - type: ndcg_at_1000
      value: 62.426
    - type: ndcg_at_3
      value: 51.0
    - type: ndcg_at_5
      value: 54.346000000000004
    - type: precision_at_1
      value: 42.571
    - type: precision_at_10
      value: 9.467
    - type: precision_at_100
      value: 1.2550000000000001
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_3
      value: 23.114
    - type: precision_at_5
      value: 16.250999999999998
    - type: recall_at_1
      value: 37.188
    - type: recall_at_10
      value: 73.068
    - type: recall_at_100
      value: 91.203
    - type: recall_at_1000
      value: 97.916
    - type: recall_at_3
      value: 56.552
    - type: recall_at_5
      value: 64.567
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gis
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: 5003b3064772da1887988e05400cf3806fe491f2
    metrics:
    - type: map_at_1
      value: 25.041000000000004
    - type: map_at_10
      value: 33.86
    - type: map_at_100
      value: 34.988
    - type: map_at_1000
      value: 35.064
    - type: map_at_3
      value: 31.049
    - type: map_at_5
      value: 32.845
    - type: mrr_at_1
      value: 26.893
    - type: mrr_at_10
      value: 35.594
    - type: mrr_at_100
      value: 36.617
    - type: mrr_at_1000
      value: 36.671
    - type: mrr_at_3
      value: 33.051
    - type: mrr_at_5
      value: 34.61
    - type: ndcg_at_1
      value: 26.893
    - type: ndcg_at_10
      value: 38.674
    - type: ndcg_at_100
      value: 44.178
    - type: ndcg_at_1000
      value: 46.089999999999996
    - type: ndcg_at_3
      value: 33.485
    - type: ndcg_at_5
      value: 36.402
    - type: precision_at_1
      value: 26.893
    - type: precision_at_10
      value: 5.989
    - type: precision_at_100
      value: 0.918
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 14.2
    - type: precision_at_5
      value: 10.26
    - type: recall_at_1
      value: 25.041000000000004
    - type: recall_at_10
      value: 51.666000000000004
    - type: recall_at_100
      value: 76.896
    - type: recall_at_1000
      value: 91.243
    - type: recall_at_3
      value: 38.035999999999994
    - type: recall_at_5
      value: 44.999
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-mathematica
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
    metrics:
    - type: map_at_1
      value: 15.909999999999998
    - type: map_at_10
      value: 23.901
    - type: map_at_100
      value: 25.165
    - type: map_at_1000
      value: 25.291000000000004
    - type: map_at_3
      value: 21.356
    - type: map_at_5
      value: 22.816
    - type: mrr_at_1
      value: 20.025000000000002
    - type: mrr_at_10
      value: 28.382
    - type: mrr_at_100
      value: 29.465000000000003
    - type: mrr_at_1000
      value: 29.535
    - type: mrr_at_3
      value: 25.933
    - type: mrr_at_5
      value: 27.332
    - type: ndcg_at_1
      value: 20.025000000000002
    - type: ndcg_at_10
      value: 29.099000000000004
    - type: ndcg_at_100
      value: 35.127
    - type: ndcg_at_1000
      value: 38.096000000000004
    - type: ndcg_at_3
      value: 24.464
    - type: ndcg_at_5
      value: 26.709
    - type: precision_at_1
      value: 20.025000000000002
    - type: precision_at_10
      value: 5.398
    - type: precision_at_100
      value: 0.9690000000000001
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 11.774
    - type: precision_at_5
      value: 8.632
    - type: recall_at_1
      value: 15.909999999999998
    - type: recall_at_10
      value: 40.672000000000004
    - type: recall_at_100
      value: 66.855
    - type: recall_at_1000
      value: 87.922
    - type: recall_at_3
      value: 28.069
    - type: recall_at_5
      value: 33.812
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-physics
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
    metrics:
    - type: map_at_1
      value: 30.175
    - type: map_at_10
      value: 41.36
    - type: map_at_100
      value: 42.701
    - type: map_at_1000
      value: 42.817
    - type: map_at_3
      value: 37.931
    - type: map_at_5
      value: 39.943
    - type: mrr_at_1
      value: 35.611
    - type: mrr_at_10
      value: 46.346
    - type: mrr_at_100
      value: 47.160000000000004
    - type: mrr_at_1000
      value: 47.203
    - type: mrr_at_3
      value: 43.712
    - type: mrr_at_5
      value: 45.367000000000004
    - type: ndcg_at_1
      value: 35.611
    - type: ndcg_at_10
      value: 47.532000000000004
    - type: ndcg_at_100
      value: 53.003
    - type: ndcg_at_1000
      value: 55.007
    - type: ndcg_at_3
      value: 42.043
    - type: ndcg_at_5
      value: 44.86
    - type: precision_at_1
      value: 35.611
    - type: precision_at_10
      value: 8.624
    - type: precision_at_100
      value: 1.332
    - type: precision_at_1000
      value: 0.169
    - type: precision_at_3
      value: 20.083000000000002
    - type: precision_at_5
      value: 14.437
    - type: recall_at_1
      value: 30.175
    - type: recall_at_10
      value: 60.5
    - type: recall_at_100
      value: 83.399
    - type: recall_at_1000
      value: 96.255
    - type: recall_at_3
      value: 45.448
    - type: recall_at_5
      value: 52.432
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-programmers
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
    metrics:
    - type: map_at_1
      value: 22.467000000000002
    - type: map_at_10
      value: 33.812999999999995
    - type: map_at_100
      value: 35.248000000000005
    - type: map_at_1000
      value: 35.359
    - type: map_at_3
      value: 30.316
    - type: map_at_5
      value: 32.233000000000004
    - type: mrr_at_1
      value: 28.310999999999996
    - type: mrr_at_10
      value: 38.979
    - type: mrr_at_100
      value: 39.937
    - type: mrr_at_1000
      value: 39.989999999999995
    - type: mrr_at_3
      value: 36.244
    - type: mrr_at_5
      value: 37.871
    - type: ndcg_at_1
      value: 28.310999999999996
    - type: ndcg_at_10
      value: 40.282000000000004
    - type: ndcg_at_100
      value: 46.22
    - type: ndcg_at_1000
      value: 48.507
    - type: ndcg_at_3
      value: 34.596
    - type: ndcg_at_5
      value: 37.267
    - type: precision_at_1
      value: 28.310999999999996
    - type: precision_at_10
      value: 7.831
    - type: precision_at_100
      value: 1.257
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 17.275
    - type: precision_at_5
      value: 12.556999999999999
    - type: recall_at_1
      value: 22.467000000000002
    - type: recall_at_10
      value: 54.14099999999999
    - type: recall_at_100
      value: 79.593
    - type: recall_at_1000
      value: 95.063
    - type: recall_at_3
      value: 38.539
    - type: recall_at_5
      value: 45.403
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 24.18591666666667
    - type: map_at_10
      value: 33.84258333333333
    - type: map_at_100
      value: 35.11391666666666
    - type: map_at_1000
      value: 35.23258333333333
    - type: map_at_3
      value: 30.764249999999997
    - type: map_at_5
      value: 32.52333333333334
    - type: mrr_at_1
      value: 28.54733333333333
    - type: mrr_at_10
      value: 37.81725
    - type: mrr_at_100
      value: 38.716499999999996
    - type: mrr_at_1000
      value: 38.77458333333333
    - type: mrr_at_3
      value: 35.157833333333336
    - type: mrr_at_5
      value: 36.69816666666667
    - type: ndcg_at_1
      value: 28.54733333333333
    - type: ndcg_at_10
      value: 39.51508333333334
    - type: ndcg_at_100
      value: 44.95316666666666
    - type: ndcg_at_1000
      value: 47.257083333333334
    - type: ndcg_at_3
      value: 34.205833333333324
    - type: ndcg_at_5
      value: 36.78266666666667
    - type: precision_at_1
      value: 28.54733333333333
    - type: precision_at_10
      value: 7.082583333333334
    - type: precision_at_100
      value: 1.1590833333333332
    - type: precision_at_1000
      value: 0.15516666666666662
    - type: precision_at_3
      value: 15.908750000000001
    - type: precision_at_5
      value: 11.505416666666669
    - type: recall_at_1
      value: 24.18591666666667
    - type: recall_at_10
      value: 52.38758333333333
    - type: recall_at_100
      value: 76.13666666666667
    - type: recall_at_1000
      value: 91.99066666666667
    - type: recall_at_3
      value: 37.78333333333334
    - type: recall_at_5
      value: 44.30141666666666
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-stats
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
    metrics:
    - type: map_at_1
      value: 21.975
    - type: map_at_10
      value: 29.781000000000002
    - type: map_at_100
      value: 30.847
    - type: map_at_1000
      value: 30.94
    - type: map_at_3
      value: 27.167
    - type: map_at_5
      value: 28.633999999999997
    - type: mrr_at_1
      value: 24.387
    - type: mrr_at_10
      value: 32.476
    - type: mrr_at_100
      value: 33.337
    - type: mrr_at_1000
      value: 33.403
    - type: mrr_at_3
      value: 29.881999999999998
    - type: mrr_at_5
      value: 31.339
    - type: ndcg_at_1
      value: 24.387
    - type: ndcg_at_10
      value: 34.596
    - type: ndcg_at_100
      value: 39.635
    - type: ndcg_at_1000
      value: 42.079
    - type: ndcg_at_3
      value: 29.516
    - type: ndcg_at_5
      value: 31.959
    - type: precision_at_1
      value: 24.387
    - type: precision_at_10
      value: 5.6129999999999995
    - type: precision_at_100
      value: 0.8909999999999999
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 12.73
    - type: precision_at_5
      value: 9.171999999999999
    - type: recall_at_1
      value: 21.975
    - type: recall_at_10
      value: 46.826
    - type: recall_at_100
      value: 69.554
    - type: recall_at_1000
      value: 87.749
    - type: recall_at_3
      value: 33.016
    - type: recall_at_5
      value: 38.97
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-tex
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: 46989137a86843e03a6195de44b09deda022eec7
    metrics:
    - type: map_at_1
      value: 15.614
    - type: map_at_10
      value: 22.927
    - type: map_at_100
      value: 24.185000000000002
    - type: map_at_1000
      value: 24.319
    - type: map_at_3
      value: 20.596
    - type: map_at_5
      value: 21.854000000000003
    - type: mrr_at_1
      value: 18.858
    - type: mrr_at_10
      value: 26.535999999999998
    - type: mrr_at_100
      value: 27.582
    - type: mrr_at_1000
      value: 27.665
    - type: mrr_at_3
      value: 24.295
    - type: mrr_at_5
      value: 25.532
    - type: ndcg_at_1
      value: 18.858
    - type: ndcg_at_10
      value: 27.583000000000002
    - type: ndcg_at_100
      value: 33.635
    - type: ndcg_at_1000
      value: 36.647
    - type: ndcg_at_3
      value: 23.348
    - type: ndcg_at_5
      value: 25.257
    - type: precision_at_1
      value: 18.858
    - type: precision_at_10
      value: 5.158
    - type: precision_at_100
      value: 0.964
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: precision_at_3
      value: 11.092
    - type: precision_at_5
      value: 8.1
    - type: recall_at_1
      value: 15.614
    - type: recall_at_10
      value: 37.916
    - type: recall_at_100
      value: 65.205
    - type: recall_at_1000
      value: 86.453
    - type: recall_at_3
      value: 26.137
    - type: recall_at_5
      value: 31.087999999999997
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-unix
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
    metrics:
    - type: map_at_1
      value: 23.078000000000003
    - type: map_at_10
      value: 31.941999999999997
    - type: map_at_100
      value: 33.196999999999996
    - type: map_at_1000
      value: 33.303
    - type: map_at_3
      value: 28.927000000000003
    - type: map_at_5
      value: 30.707
    - type: mrr_at_1
      value: 26.866
    - type: mrr_at_10
      value: 35.557
    - type: mrr_at_100
      value: 36.569
    - type: mrr_at_1000
      value: 36.632
    - type: mrr_at_3
      value: 32.897999999999996
    - type: mrr_at_5
      value: 34.437
    - type: ndcg_at_1
      value: 26.866
    - type: ndcg_at_10
      value: 37.372
    - type: ndcg_at_100
      value: 43.248
    - type: ndcg_at_1000
      value: 45.632
    - type: ndcg_at_3
      value: 31.852999999999998
    - type: ndcg_at_5
      value: 34.582
    - type: precision_at_1
      value: 26.866
    - type: precision_at_10
      value: 6.511
    - type: precision_at_100
      value: 1.078
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 14.582999999999998
    - type: precision_at_5
      value: 10.634
    - type: recall_at_1
      value: 23.078000000000003
    - type: recall_at_10
      value: 50.334
    - type: recall_at_100
      value: 75.787
    - type: recall_at_1000
      value: 92.485
    - type: recall_at_3
      value: 35.386
    - type: recall_at_5
      value: 42.225
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-webmasters
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
    metrics:
    - type: map_at_1
      value: 22.203999999999997
    - type: map_at_10
      value: 31.276
    - type: map_at_100
      value: 32.844
    - type: map_at_1000
      value: 33.062999999999995
    - type: map_at_3
      value: 27.733999999999998
    - type: map_at_5
      value: 29.64
    - type: mrr_at_1
      value: 27.272999999999996
    - type: mrr_at_10
      value: 36.083
    - type: mrr_at_100
      value: 37.008
    - type: mrr_at_1000
      value: 37.076
    - type: mrr_at_3
      value: 33.004
    - type: mrr_at_5
      value: 34.664
    - type: ndcg_at_1
      value: 27.272999999999996
    - type: ndcg_at_10
      value: 37.763000000000005
    - type: ndcg_at_100
      value: 43.566
    - type: ndcg_at_1000
      value: 46.356
    - type: ndcg_at_3
      value: 31.673000000000002
    - type: ndcg_at_5
      value: 34.501
    - type: precision_at_1
      value: 27.272999999999996
    - type: precision_at_10
      value: 7.470000000000001
    - type: precision_at_100
      value: 1.502
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_3
      value: 14.756
    - type: precision_at_5
      value: 11.225
    - type: recall_at_1
      value: 22.203999999999997
    - type: recall_at_10
      value: 51.437999999999995
    - type: recall_at_100
      value: 76.845
    - type: recall_at_1000
      value: 94.38600000000001
    - type: recall_at_3
      value: 34.258
    - type: recall_at_5
      value: 41.512
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-wordpress
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 17.474
    - type: map_at_10
      value: 26.362999999999996
    - type: map_at_100
      value: 27.456999999999997
    - type: map_at_1000
      value: 27.567999999999998
    - type: map_at_3
      value: 23.518
    - type: map_at_5
      value: 25.068
    - type: mrr_at_1
      value: 18.669
    - type: mrr_at_10
      value: 27.998
    - type: mrr_at_100
      value: 28.953
    - type: mrr_at_1000
      value: 29.03
    - type: mrr_at_3
      value: 25.230999999999998
    - type: mrr_at_5
      value: 26.654
    - type: ndcg_at_1
      value: 18.669
    - type: ndcg_at_10
      value: 31.684
    - type: ndcg_at_100
      value: 36.864999999999995
    - type: ndcg_at_1000
      value: 39.555
    - type: ndcg_at_3
      value: 26.057000000000002
    - type: ndcg_at_5
      value: 28.587
    - type: precision_at_1
      value: 18.669
    - type: precision_at_10
      value: 5.3420000000000005
    - type: precision_at_100
      value: 0.847
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 11.583
    - type: precision_at_5
      value: 8.466
    - type: recall_at_1
      value: 17.474
    - type: recall_at_10
      value: 46.497
    - type: recall_at_100
      value: 69.977
    - type: recall_at_1000
      value: 89.872
    - type: recall_at_3
      value: 31.385999999999996
    - type: recall_at_5
      value: 37.283
  - task:
      type: Retrieval
    dataset:
      type: mteb/climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
    metrics:
    - type: map_at_1
      value: 17.173
    - type: map_at_10
      value: 30.407
    - type: map_at_100
      value: 32.528
    - type: map_at_1000
      value: 32.698
    - type: map_at_3
      value: 25.523
    - type: map_at_5
      value: 28.038
    - type: mrr_at_1
      value: 38.958
    - type: mrr_at_10
      value: 51.515
    - type: mrr_at_100
      value: 52.214000000000006
    - type: mrr_at_1000
      value: 52.237
    - type: mrr_at_3
      value: 48.502
    - type: mrr_at_5
      value: 50.251000000000005
    - type: ndcg_at_1
      value: 38.958
    - type: ndcg_at_10
      value: 40.355000000000004
    - type: ndcg_at_100
      value: 47.68
    - type: ndcg_at_1000
      value: 50.370000000000005
    - type: ndcg_at_3
      value: 33.946
    - type: ndcg_at_5
      value: 36.057
    - type: precision_at_1
      value: 38.958
    - type: precision_at_10
      value: 12.508
    - type: precision_at_100
      value: 2.054
    - type: precision_at_1000
      value: 0.256
    - type: precision_at_3
      value: 25.581
    - type: precision_at_5
      value: 19.256999999999998
    - type: recall_at_1
      value: 17.173
    - type: recall_at_10
      value: 46.967
    - type: recall_at_100
      value: 71.47200000000001
    - type: recall_at_1000
      value: 86.238
    - type: recall_at_3
      value: 30.961
    - type: recall_at_5
      value: 37.539
  - task:
      type: Retrieval
    dataset:
      type: mteb/dbpedia
      name: MTEB DBPedia
      config: default
      split: test
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
    metrics:
    - type: map_at_1
      value: 8.999
    - type: map_at_10
      value: 18.989
    - type: map_at_100
      value: 26.133
    - type: map_at_1000
      value: 27.666
    - type: map_at_3
      value: 13.918
    - type: map_at_5
      value: 16.473
    - type: mrr_at_1
      value: 66.25
    - type: mrr_at_10
      value: 74.161
    - type: mrr_at_100
      value: 74.516
    - type: mrr_at_1000
      value: 74.524
    - type: mrr_at_3
      value: 72.875
    - type: mrr_at_5
      value: 73.613
    - type: ndcg_at_1
      value: 54.37499999999999
    - type: ndcg_at_10
      value: 39.902
    - type: ndcg_at_100
      value: 44.212
    - type: ndcg_at_1000
      value: 51.62
    - type: ndcg_at_3
      value: 45.193
    - type: ndcg_at_5
      value: 42.541000000000004
    - type: precision_at_1
      value: 66.25
    - type: precision_at_10
      value: 30.425
    - type: precision_at_100
      value: 9.754999999999999
    - type: precision_at_1000
      value: 2.043
    - type: precision_at_3
      value: 48.25
    - type: precision_at_5
      value: 40.65
    - type: recall_at_1
      value: 8.999
    - type: recall_at_10
      value: 24.133
    - type: recall_at_100
      value: 49.138999999999996
    - type: recall_at_1000
      value: 72.639
    - type: recall_at_3
      value: 15.287999999999998
    - type: recall_at_5
      value: 19.415
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 46.38999999999999
    - type: f1
      value: 41.444205512055234
  - task:
      type: Retrieval
    dataset:
      type: mteb/fever
      name: MTEB FEVER
      config: default
      split: test
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
    metrics:
    - type: map_at_1
      value: 87.35000000000001
    - type: map_at_10
      value: 92.837
    - type: map_at_100
      value: 92.996
    - type: map_at_1000
      value: 93.006
    - type: map_at_3
      value: 92.187
    - type: map_at_5
      value: 92.595
    - type: mrr_at_1
      value: 93.864
    - type: mrr_at_10
      value: 96.723
    - type: mrr_at_100
      value: 96.72500000000001
    - type: mrr_at_1000
      value: 96.72500000000001
    - type: mrr_at_3
      value: 96.64
    - type: mrr_at_5
      value: 96.71499999999999
    - type: ndcg_at_1
      value: 93.864
    - type: ndcg_at_10
      value: 94.813
    - type: ndcg_at_100
      value: 95.243
    - type: ndcg_at_1000
      value: 95.38600000000001
    - type: ndcg_at_3
      value: 94.196
    - type: ndcg_at_5
      value: 94.521
    - type: precision_at_1
      value: 93.864
    - type: precision_at_10
      value: 10.951
    - type: precision_at_100
      value: 1.1400000000000001
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 35.114000000000004
    - type: precision_at_5
      value: 21.476
    - type: recall_at_1
      value: 87.35000000000001
    - type: recall_at_10
      value: 96.941
    - type: recall_at_100
      value: 98.397
    - type: recall_at_1000
      value: 99.21600000000001
    - type: recall_at_3
      value: 95.149
    - type: recall_at_5
      value: 96.131
  - task:
      type: Retrieval
    dataset:
      type: mteb/fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
    metrics:
    - type: map_at_1
      value: 24.476
    - type: map_at_10
      value: 40.11
    - type: map_at_100
      value: 42.229
    - type: map_at_1000
      value: 42.378
    - type: map_at_3
      value: 34.512
    - type: map_at_5
      value: 38.037
    - type: mrr_at_1
      value: 47.839999999999996
    - type: mrr_at_10
      value: 57.053
    - type: mrr_at_100
      value: 57.772
    - type: mrr_at_1000
      value: 57.799
    - type: mrr_at_3
      value: 54.552
    - type: mrr_at_5
      value: 56.011
    - type: ndcg_at_1
      value: 47.839999999999996
    - type: ndcg_at_10
      value: 48.650999999999996
    - type: ndcg_at_100
      value: 55.681000000000004
    - type: ndcg_at_1000
      value: 57.979
    - type: ndcg_at_3
      value: 43.923
    - type: ndcg_at_5
      value: 46.037
    - type: precision_at_1
      value: 47.839999999999996
    - type: precision_at_10
      value: 13.395000000000001
    - type: precision_at_100
      value: 2.0660000000000003
    - type: precision_at_1000
      value: 0.248
    - type: precision_at_3
      value: 29.064
    - type: precision_at_5
      value: 22.006
    - type: recall_at_1
      value: 24.476
    - type: recall_at_10
      value: 56.216
    - type: recall_at_100
      value: 81.798
    - type: recall_at_1000
      value: 95.48299999999999
    - type: recall_at_3
      value: 39.357
    - type: recall_at_5
      value: 47.802
  - task:
      type: Retrieval
    dataset:
      type: mteb/hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
    metrics:
    - type: map_at_1
      value: 42.728
    - type: map_at_10
      value: 57.737
    - type: map_at_100
      value: 58.531
    - type: map_at_1000
      value: 58.594
    - type: map_at_3
      value: 54.869
    - type: map_at_5
      value: 56.55
    - type: mrr_at_1
      value: 85.456
    - type: mrr_at_10
      value: 90.062
    - type: mrr_at_100
      value: 90.159
    - type: mrr_at_1000
      value: 90.16
    - type: mrr_at_3
      value: 89.37899999999999
    - type: mrr_at_5
      value: 89.81
    - type: ndcg_at_1
      value: 85.456
    - type: ndcg_at_10
      value: 67.755
    - type: ndcg_at_100
      value: 70.341
    - type: ndcg_at_1000
      value: 71.538
    - type: ndcg_at_3
      value: 63.735
    - type: ndcg_at_5
      value: 65.823
    - type: precision_at_1
      value: 85.456
    - type: precision_at_10
      value: 13.450000000000001
    - type: precision_at_100
      value: 1.545
    - type: precision_at_1000
      value: 0.16999999999999998
    - type: precision_at_3
      value: 38.861000000000004
    - type: precision_at_5
      value: 24.964
    - type: recall_at_1
      value: 42.728
    - type: recall_at_10
      value: 67.252
    - type: recall_at_100
      value: 77.265
    - type: recall_at_1000
      value: 85.246
    - type: recall_at_3
      value: 58.292
    - type: recall_at_5
      value: 62.41100000000001
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 87.4836
    - type: ap
      value: 82.29552224030336
    - type: f1
      value: 87.42791432227448
  - task:
      type: Retrieval
    dataset:
      type: mteb/msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: c5a29a104738b98a9e76336939199e264163d4a0
    metrics:
    - type: map_at_1
      value: 23.015
    - type: map_at_10
      value: 35.621
    - type: map_at_100
      value: 36.809
    - type: map_at_1000
      value: 36.853
    - type: map_at_3
      value: 31.832
    - type: map_at_5
      value: 34.006
    - type: mrr_at_1
      value: 23.738999999999997
    - type: mrr_at_10
      value: 36.309999999999995
    - type: mrr_at_100
      value: 37.422
    - type: mrr_at_1000
      value: 37.461
    - type: mrr_at_3
      value: 32.592999999999996
    - type: mrr_at_5
      value: 34.736
    - type: ndcg_at_1
      value: 23.724999999999998
    - type: ndcg_at_10
      value: 42.617
    - type: ndcg_at_100
      value: 48.217999999999996
    - type: ndcg_at_1000
      value: 49.309
    - type: ndcg_at_3
      value: 34.905
    - type: ndcg_at_5
      value: 38.769
    - type: precision_at_1
      value: 23.724999999999998
    - type: precision_at_10
      value: 6.689
    - type: precision_at_100
      value: 0.9480000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.89
    - type: precision_at_5
      value: 10.897
    - type: recall_at_1
      value: 23.015
    - type: recall_at_10
      value: 64.041
    - type: recall_at_100
      value: 89.724
    - type: recall_at_1000
      value: 98.00999999999999
    - type: recall_at_3
      value: 43.064
    - type: recall_at_5
      value: 52.31099999999999
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 96.49794801641588
    - type: f1
      value: 96.28931114498003
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 82.81121751025992
    - type: f1
      value: 63.18740125901853
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 77.66644250168123
    - type: f1
      value: 74.93211186867839
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 81.77202420981843
    - type: f1
      value: 81.63681969283554
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 34.596687684870645
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 32.26965660101405
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 31.33619694846802
    - type: mrr
      value: 32.53719657720334
  - task:
      type: Retrieval
    dataset:
      type: mteb/nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
    metrics:
    - type: map_at_1
      value: 6.0729999999999995
    - type: map_at_10
      value: 13.245999999999999
    - type: map_at_100
      value: 16.747999999999998
    - type: map_at_1000
      value: 18.163
    - type: map_at_3
      value: 10.064
    - type: map_at_5
      value: 11.513
    - type: mrr_at_1
      value: 49.536
    - type: mrr_at_10
      value: 58.092
    - type: mrr_at_100
      value: 58.752
    - type: mrr_at_1000
      value: 58.78
    - type: mrr_at_3
      value: 56.398
    - type: mrr_at_5
      value: 57.389
    - type: ndcg_at_1
      value: 47.059
    - type: ndcg_at_10
      value: 35.881
    - type: ndcg_at_100
      value: 32.751999999999995
    - type: ndcg_at_1000
      value: 41.498000000000005
    - type: ndcg_at_3
      value: 42.518
    - type: ndcg_at_5
      value: 39.550999999999995
    - type: precision_at_1
      value: 49.536
    - type: precision_at_10
      value: 26.316
    - type: precision_at_100
      value: 8.084
    - type: precision_at_1000
      value: 2.081
    - type: precision_at_3
      value: 39.938
    - type: precision_at_5
      value: 34.056
    - type: recall_at_1
      value: 6.0729999999999995
    - type: recall_at_10
      value: 16.593
    - type: recall_at_100
      value: 32.883
    - type: recall_at_1000
      value: 64.654
    - type: recall_at_3
      value: 11.174000000000001
    - type: recall_at_5
      value: 13.528
  - task:
      type: Retrieval
    dataset:
      type: mteb/nq
      name: MTEB NQ
      config: default
      split: test
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
    metrics:
    - type: map_at_1
      value: 30.043
    - type: map_at_10
      value: 45.318999999999996
    - type: map_at_100
      value: 46.381
    - type: map_at_1000
      value: 46.412
    - type: map_at_3
      value: 40.941
    - type: map_at_5
      value: 43.662
    - type: mrr_at_1
      value: 33.98
    - type: mrr_at_10
      value: 47.870000000000005
    - type: mrr_at_100
      value: 48.681999999999995
    - type: mrr_at_1000
      value: 48.703
    - type: mrr_at_3
      value: 44.341
    - type: mrr_at_5
      value: 46.547
    - type: ndcg_at_1
      value: 33.98
    - type: ndcg_at_10
      value: 52.957
    - type: ndcg_at_100
      value: 57.434
    - type: ndcg_at_1000
      value: 58.103
    - type: ndcg_at_3
      value: 44.896
    - type: ndcg_at_5
      value: 49.353
    - type: precision_at_1
      value: 33.98
    - type: precision_at_10
      value: 8.786
    - type: precision_at_100
      value: 1.1280000000000001
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 20.577
    - type: precision_at_5
      value: 14.942
    - type: recall_at_1
      value: 30.043
    - type: recall_at_10
      value: 73.593
    - type: recall_at_100
      value: 93.026
    - type: recall_at_1000
      value: 97.943
    - type: recall_at_3
      value: 52.955
    - type: recall_at_5
      value: 63.132
  - task:
      type: Retrieval
    dataset:
      type: mteb/quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.808
    - type: map_at_10
      value: 84.675
    - type: map_at_100
      value: 85.322
    - type: map_at_1000
      value: 85.33800000000001
    - type: map_at_3
      value: 81.68900000000001
    - type: map_at_5
      value: 83.543
    - type: mrr_at_1
      value: 81.5
    - type: mrr_at_10
      value: 87.59700000000001
    - type: mrr_at_100
      value: 87.705
    - type: mrr_at_1000
      value: 87.70599999999999
    - type: mrr_at_3
      value: 86.607
    - type: mrr_at_5
      value: 87.289
    - type: ndcg_at_1
      value: 81.51
    - type: ndcg_at_10
      value: 88.41799999999999
    - type: ndcg_at_100
      value: 89.644
    - type: ndcg_at_1000
      value: 89.725
    - type: ndcg_at_3
      value: 85.49900000000001
    - type: ndcg_at_5
      value: 87.078
    - type: precision_at_1
      value: 81.51
    - type: precision_at_10
      value: 13.438
    - type: precision_at_100
      value: 1.532
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.363
    - type: precision_at_5
      value: 24.57
    - type: recall_at_1
      value: 70.808
    - type: recall_at_10
      value: 95.575
    - type: recall_at_100
      value: 99.667
    - type: recall_at_1000
      value: 99.98899999999999
    - type: recall_at_3
      value: 87.223
    - type: recall_at_5
      value: 91.682
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 58.614831329137715
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 66.86580408560826
  - task:
      type: Retrieval
    dataset:
      type: mteb/scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 5.093
    - type: map_at_10
      value: 13.014000000000001
    - type: map_at_100
      value: 15.412999999999998
    - type: map_at_1000
      value: 15.756999999999998
    - type: map_at_3
      value: 9.216000000000001
    - type: map_at_5
      value: 11.036999999999999
    - type: mrr_at_1
      value: 25.1
    - type: mrr_at_10
      value: 37.133
    - type: mrr_at_100
      value: 38.165
    - type: mrr_at_1000
      value: 38.198
    - type: mrr_at_3
      value: 33.217
    - type: mrr_at_5
      value: 35.732
    - type: ndcg_at_1
      value: 25.1
    - type: ndcg_at_10
      value: 21.918000000000003
    - type: ndcg_at_100
      value: 30.983
    - type: ndcg_at_1000
      value: 36.629
    - type: ndcg_at_3
      value: 20.544999999999998
    - type: ndcg_at_5
      value: 18.192
    - type: precision_at_1
      value: 25.1
    - type: precision_at_10
      value: 11.44
    - type: precision_at_100
      value: 2.459
    - type: precision_at_1000
      value: 0.381
    - type: precision_at_3
      value: 19.267
    - type: precision_at_5
      value: 16.16
    - type: recall_at_1
      value: 5.093
    - type: recall_at_10
      value: 23.215
    - type: recall_at_100
      value: 49.902
    - type: recall_at_1000
      value: 77.403
    - type: recall_at_3
      value: 11.733
    - type: recall_at_5
      value: 16.372999999999998
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 82.9365442977452
    - type: cos_sim_spearman
      value: 79.36960687383745
    - type: euclidean_pearson
      value: 79.6045204840714
    - type: euclidean_spearman
      value: 79.26382712751337
    - type: manhattan_pearson
      value: 79.4805084789529
    - type: manhattan_spearman
      value: 79.21847863209523
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 83.27906192961453
    - type: cos_sim_spearman
      value: 74.38364712099211
    - type: euclidean_pearson
      value: 78.54358927241223
    - type: euclidean_spearman
      value: 74.22185560806376
    - type: manhattan_pearson
      value: 78.50904327377751
    - type: manhattan_spearman
      value: 74.2627500781748
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 84.66863742649639
    - type: cos_sim_spearman
      value: 84.70630905216271
    - type: euclidean_pearson
      value: 84.64498334705334
    - type: euclidean_spearman
      value: 84.87204770690148
    - type: manhattan_pearson
      value: 84.65774227976077
    - type: manhattan_spearman
      value: 84.91251851797985
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 83.1577763924467
    - type: cos_sim_spearman
      value: 80.10314039230198
    - type: euclidean_pearson
      value: 81.51346991046043
    - type: euclidean_spearman
      value: 80.08678485109435
    - type: manhattan_pearson
      value: 81.57058914661894
    - type: manhattan_spearman
      value: 80.1516230725106
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 86.40310839662533
    - type: cos_sim_spearman
      value: 87.16293477217867
    - type: euclidean_pearson
      value: 86.50688711184775
    - type: euclidean_spearman
      value: 87.08651444923031
    - type: manhattan_pearson
      value: 86.54674677557857
    - type: manhattan_spearman
      value: 87.15079017870971
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 84.32886275207817
    - type: cos_sim_spearman
      value: 85.0190460590732
    - type: euclidean_pearson
      value: 84.42553652784679
    - type: euclidean_spearman
      value: 85.20027364279328
    - type: manhattan_pearson
      value: 84.42926246281078
    - type: manhattan_spearman
      value: 85.20187419804306
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 90.76732216967812
    - type: cos_sim_spearman
      value: 90.63701653633909
    - type: euclidean_pearson
      value: 90.26678186114682
    - type: euclidean_spearman
      value: 90.67288073455427
    - type: manhattan_pearson
      value: 90.20772020584582
    - type: manhattan_spearman
      value: 90.60764863983702
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_pearson
      value: 69.09280387698125
    - type: cos_sim_spearman
      value: 68.62743151172162
    - type: euclidean_pearson
      value: 69.89386398104689
    - type: euclidean_spearman
      value: 68.71191066733556
    - type: manhattan_pearson
      value: 69.92516500604872
    - type: manhattan_spearman
      value: 68.80452846992576
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 86.13178592019887
    - type: cos_sim_spearman
      value: 86.03947178806887
    - type: euclidean_pearson
      value: 85.87029414285313
    - type: euclidean_spearman
      value: 86.04960843306998
    - type: manhattan_pearson
      value: 85.92946858580146
    - type: manhattan_spearman
      value: 86.12575341860442
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 85.16657063002837
    - type: mrr
      value: 95.73671063867141
  - task:
      type: Retrieval
    dataset:
      type: mteb/scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
    metrics:
    - type: map_at_1
      value: 63.510999999999996
    - type: map_at_10
      value: 72.76899999999999
    - type: map_at_100
      value: 73.303
    - type: map_at_1000
      value: 73.32499999999999
    - type: map_at_3
      value: 70.514
    - type: map_at_5
      value: 71.929
    - type: mrr_at_1
      value: 66.333
    - type: mrr_at_10
      value: 73.75
    - type: mrr_at_100
      value: 74.119
    - type: mrr_at_1000
      value: 74.138
    - type: mrr_at_3
      value: 72.222
    - type: mrr_at_5
      value: 73.122
    - type: ndcg_at_1
      value: 66.333
    - type: ndcg_at_10
      value: 76.774
    - type: ndcg_at_100
      value: 78.78500000000001
    - type: ndcg_at_1000
      value: 79.254
    - type: ndcg_at_3
      value: 73.088
    - type: ndcg_at_5
      value: 75.002
    - type: precision_at_1
      value: 66.333
    - type: precision_at_10
      value: 9.833
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 28.222
    - type: precision_at_5
      value: 18.333
    - type: recall_at_1
      value: 63.510999999999996
    - type: recall_at_10
      value: 87.98899999999999
    - type: recall_at_100
      value: 96.5
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 77.86699999999999
    - type: recall_at_5
      value: 82.73899999999999
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.78514851485149
    - type: cos_sim_ap
      value: 94.94214383862038
    - type: cos_sim_f1
      value: 89.02255639097744
    - type: cos_sim_precision
      value: 89.2462311557789
    - type: cos_sim_recall
      value: 88.8
    - type: dot_accuracy
      value: 99.78217821782178
    - type: dot_ap
      value: 94.69965247836805
    - type: dot_f1
      value: 88.78695208970439
    - type: dot_precision
      value: 90.54054054054053
    - type: dot_recall
      value: 87.1
    - type: euclidean_accuracy
      value: 99.78118811881188
    - type: euclidean_ap
      value: 94.9865187695411
    - type: euclidean_f1
      value: 88.99950223992036
    - type: euclidean_precision
      value: 88.60257680872151
    - type: euclidean_recall
      value: 89.4
    - type: manhattan_accuracy
      value: 99.78811881188119
    - type: manhattan_ap
      value: 95.0021236766459
    - type: manhattan_f1
      value: 89.12071535022356
    - type: manhattan_precision
      value: 88.54886475814413
    - type: manhattan_recall
      value: 89.7
    - type: max_accuracy
      value: 99.78811881188119
    - type: max_ap
      value: 95.0021236766459
    - type: max_f1
      value: 89.12071535022356
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 68.93190546593995
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 37.602808534760655
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 52.29214480978073
    - type: mrr
      value: 53.123169722434426
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 30.967800769650022
    - type: cos_sim_spearman
      value: 31.168490040206926
    - type: dot_pearson
      value: 30.888603021128553
    - type: dot_spearman
      value: 31.028241262520385
  - task:
      type: Retrieval
    dataset:
      type: mteb/trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.22300000000000003
    - type: map_at_10
      value: 1.781
    - type: map_at_100
      value: 9.905999999999999
    - type: map_at_1000
      value: 23.455000000000002
    - type: map_at_3
      value: 0.569
    - type: map_at_5
      value: 0.918
    - type: mrr_at_1
      value: 84.0
    - type: mrr_at_10
      value: 91.067
    - type: mrr_at_100
      value: 91.067
    - type: mrr_at_1000
      value: 91.067
    - type: mrr_at_3
      value: 90.667
    - type: mrr_at_5
      value: 91.067
    - type: ndcg_at_1
      value: 78.0
    - type: ndcg_at_10
      value: 73.13499999999999
    - type: ndcg_at_100
      value: 55.32
    - type: ndcg_at_1000
      value: 49.532
    - type: ndcg_at_3
      value: 73.715
    - type: ndcg_at_5
      value: 72.74199999999999
    - type: precision_at_1
      value: 84.0
    - type: precision_at_10
      value: 78.8
    - type: precision_at_100
      value: 56.32
    - type: precision_at_1000
      value: 21.504
    - type: precision_at_3
      value: 77.333
    - type: precision_at_5
      value: 78.0
    - type: recall_at_1
      value: 0.22300000000000003
    - type: recall_at_10
      value: 2.049
    - type: recall_at_100
      value: 13.553
    - type: recall_at_1000
      value: 46.367999999999995
    - type: recall_at_3
      value: 0.604
    - type: recall_at_5
      value: 1.015
  - task:
      type: Retrieval
    dataset:
      type: mteb/touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
    metrics:
    - type: map_at_1
      value: 3.0380000000000003
    - type: map_at_10
      value: 10.188
    - type: map_at_100
      value: 16.395
    - type: map_at_1000
      value: 18.024
    - type: map_at_3
      value: 6.236
    - type: map_at_5
      value: 7.276000000000001
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 46.292
    - type: mrr_at_100
      value: 47.446
    - type: mrr_at_1000
      value: 47.446
    - type: mrr_at_3
      value: 41.156
    - type: mrr_at_5
      value: 44.32
    - type: ndcg_at_1
      value: 32.653
    - type: ndcg_at_10
      value: 25.219
    - type: ndcg_at_100
      value: 37.802
    - type: ndcg_at_1000
      value: 49.274
    - type: ndcg_at_3
      value: 28.605999999999998
    - type: ndcg_at_5
      value: 26.21
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 21.837
    - type: precision_at_100
      value: 7.776
    - type: precision_at_1000
      value: 1.522
    - type: precision_at_3
      value: 28.571
    - type: precision_at_5
      value: 25.306
    - type: recall_at_1
      value: 3.0380000000000003
    - type: recall_at_10
      value: 16.298000000000002
    - type: recall_at_100
      value: 48.712
    - type: recall_at_1000
      value: 83.16799999999999
    - type: recall_at_3
      value: 7.265000000000001
    - type: recall_at_5
      value: 9.551
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 83.978
    - type: ap
      value: 24.751887949330015
    - type: f1
      value: 66.8685134049279
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 61.573288058856825
    - type: f1
      value: 61.973261751726604
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 48.75483298792469
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 86.36824223639506
    - type: cos_sim_ap
      value: 75.53126388573047
    - type: cos_sim_f1
      value: 67.9912831688245
    - type: cos_sim_precision
      value: 66.11817501869858
    - type: cos_sim_recall
      value: 69.9736147757256
    - type: dot_accuracy
      value: 86.39804494248078
    - type: dot_ap
      value: 75.27598891718046
    - type: dot_f1
      value: 67.91146284159763
    - type: dot_precision
      value: 63.90505003490807
    - type: dot_recall
      value: 72.45382585751979
    - type: euclidean_accuracy
      value: 86.36228169517793
    - type: euclidean_ap
      value: 75.51438087434647
    - type: euclidean_f1
      value: 68.02370523061066
    - type: euclidean_precision
      value: 66.46525679758308
    - type: euclidean_recall
      value: 69.65699208443272
    - type: manhattan_accuracy
      value: 86.46361089586935
    - type: manhattan_ap
      value: 75.50800785730111
    - type: manhattan_f1
      value: 67.9220437187253
    - type: manhattan_precision
      value: 67.79705573080967
    - type: manhattan_recall
      value: 68.04749340369392
    - type: max_accuracy
      value: 86.46361089586935
    - type: max_ap
      value: 75.53126388573047
    - type: max_f1
      value: 68.02370523061066
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 88.80350836341057
    - type: cos_sim_ap
      value: 85.51101933260743
    - type: cos_sim_f1
      value: 77.9152271629704
    - type: cos_sim_precision
      value: 75.27815662910056
    - type: cos_sim_recall
      value: 80.74376347397599
    - type: dot_accuracy
      value: 88.84425815966158
    - type: dot_ap
      value: 85.49726945962519
    - type: dot_f1
      value: 77.94445269567801
    - type: dot_precision
      value: 75.27251864601261
    - type: dot_recall
      value: 80.81305820757623
    - type: euclidean_accuracy
      value: 88.80350836341057
    - type: euclidean_ap
      value: 85.4882880790211
    - type: euclidean_f1
      value: 77.87063284615103
    - type: euclidean_precision
      value: 74.61022927689595
    - type: euclidean_recall
      value: 81.42901139513397
    - type: manhattan_accuracy
      value: 88.7161873714441
    - type: manhattan_ap
      value: 85.45753871906821
    - type: manhattan_f1
      value: 77.8686401480111
    - type: manhattan_precision
      value: 74.95903683123174
    - type: manhattan_recall
      value: 81.01324299353249
    - type: max_accuracy
      value: 88.84425815966158
    - type: max_ap
      value: 85.51101933260743
    - type: max_f1
      value: 77.94445269567801
---
  
<!-- **English** | [中文](./README_zh.md) -->

# gte-base-en-v1.5

We introduce `gte-v1.5` series, upgraded `gte` embeddings that support the context length of up to **8192**, while further enhancing model performance.
The models are built upon the `transformer++` encoder [backbone](https://huggingface.co/Alibaba-NLP/new-impl) (BERT + RoPE + GLU).

The `gte-v1.5` series achieve state-of-the-art scores on the MTEB benchmark within the same model size category and prodvide competitive on the LoCo long-context retrieval tests (refer to [Evaluation](#evaluation)).

We also present the [`gte-Qwen1.5-7B-instruct`](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct),
a SOTA instruction-tuned multi-lingual embedding model that ranked 2nd in MTEB and 1st in C-MTEB.

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Institute for Intelligent Computing, Alibaba Group
- **Model type:** Text Embeddings
- **Paper:** Coming soon.

<!-- - **Demo [optional]:** [More Information Needed] -->

### Model list

| Models | Language | Model Size | Max Seq. Length | Dimension | MTEB-en | LoCo |
|:-----: | :-----: |:-----: |:-----: |:-----: | :-----: | :-----: |
|[`gte-Qwen1.5-7B-instruct`](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct)| Multiple | 7720 | 32768 | 4096 | 67.34 | 87.57 |
|[`gte-large-en-v1.5`](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) | English | 434 | 8192 | 1024 | 65.39 | 86.71 |
|[`gte-base-en-v1.5`](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5) | English | 137 | 8192 | 768 | 64.11 | 87.44 |


## How to Get Started with the Model

Use the code below to get started with the model.

```python
# Requires transformers>=4.36.0

import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]

model_path = 'Alibaba-NLP/gte-base-en-v1.5'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=8192, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = outputs.last_hidden_state[:, 0]
 
# (Optionally) normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
print(scores.tolist())
```

**It is recommended to install xformers and enable unpadding for acceleration, refer to [enable-unpadding-and-xformers](https://huggingface.co/Alibaba-NLP/new-impl#recommendation-enable-unpadding-and-acceleration-with-xformers).**


Use with `sentence-transformers`:

```python
# Requires sentence_transformers>=2.7.0

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

sentences = ['That is a happy person', 'That is a very happy person']

model = SentenceTransformer('Alibaba-NLP/gte-base-en-v1.5', trust_remote_code=True)
embeddings = model.encode(sentences)
print(cos_sim(embeddings[0], embeddings[1]))
```

Use with `transformers.js`:

```js
// npm i @xenova/transformers
import { pipeline, dot } from '@xenova/transformers';

// Create feature extraction pipeline
const extractor = await pipeline('feature-extraction', 'Alibaba-NLP/gte-base-en-v1.5', {
    quantized: false, // Comment out this line to use the quantized version
});

// Generate sentence embeddings
const sentences = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]
const output = await extractor(sentences, { normalize: true, pooling: 'cls' });

// Compute similarity scores
const [source_embeddings, ...document_embeddings ] = output.tolist();
const similarities = document_embeddings.map(x => 100 * dot(source_embeddings, x));
console.log(similarities); // [34.504930869007296, 64.03973265120138, 19.520042686034362]
```

## Training Details

### Training Data

- Masked language modeling (MLM): `c4-en`
- Weak-supervised contrastive (WSC) pre-training: [GTE](https://arxiv.org/pdf/2308.03281.pdf) pre-training data
- Supervised contrastive fine-tuning: [GTE](https://arxiv.org/pdf/2308.03281.pdf) fine-tuning data

### Training Procedure

To enable the backbone model to support a context length of 8192, we adopted a multi-stage training strategy.
The model first undergoes preliminary MLM pre-training on shorter lengths.
And then, we resample the data, reducing the proportion of short texts, and continue the MLM pre-training.

The entire training process is as follows:
- MLM-2048: lr 5e-4, mlm_probability 0.3, batch_size 4096, num_steps 70000, rope_base 10000
- MLM-8192: lr 5e-5, mlm_probability 0.3, batch_size 1024, num_steps 20000, rope_base 500000
- WSC: max_len 512, lr 2e-4, batch_size 32768, num_steps 100000
- Fine-tuning: TODO


## Evaluation


### MTEB

The results of other models are retrieved from [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

The gte evaluation setting: `mteb==1.2.0, fp16 auto mix precision, max_length=8192`, and set ntk scaling factor to 2 (equivalent to rope_base * 2).

| Model Name | Param Size (M) | Dimension | Sequence Length | Average (56) | Class. (12) | Clust. (11) | Pair Class. (3) | Reran. (4) | Retr. (15) | STS (10) | Summ. (1) |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**gte-large-en-v1.5**](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) | 434 | 1024 | 8192 | **65.39** | 77.75 | 47.95 | 84.63 | 58.50 | 57.91 | 81.43 | 30.91 |
| [mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) | 335 | 1024 | 512 | 64.68 | 75.64 | 46.71 | 87.2 | 60.11 | 54.39 | 85 | 32.71 |
| [multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct) | 560 | 1024 | 514 | 64.41 | 77.56 | 47.1 | 86.19 | 58.58 | 52.47 | 84.78 | 30.39 |
| [bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)| 335 | 1024 | 512 | 64.23 | 75.97 | 46.08 | 87.12 | 60.03 | 54.29 | 83.11 | 31.61 |
| [**gte-base-en-v1.5**](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5) | 137 | 768 | 8192 | **64.11** | 77.17 | 46.82 | 85.33 | 57.66 | 54.09 | 81.97 | 31.17 |
| [bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)| 109 | 768 | 512 | 63.55 | 75.53 | 45.77 | 86.55 | 58.86 | 53.25 | 82.4 | 31.07 |


### LoCo

| Model Name |  Dimension | Sequence Length | Average (5) | QsmsumRetrieval | SummScreenRetrieval | QasperAbastractRetrieval | QasperTitleRetrieval |  GovReportRetrieval |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [gte-qwen1.5-7b](https://huggingface.co/Alibaba-NLP/gte-qwen1.5-7b) | 4096 | 32768 |  87.57 | 49.37 | 93.10 | 99.67 | 97.54 | 98.21 | 
| [gte-large-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-v1.5) |1024 | 8192 | 86.71 | 44.55 | 92.61 | 99.82 | 97.81 | 98.74 |
| [gte-base-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-v1.5) | 768 | 8192 | 87.44 | 49.91  | 91.78 | 99.82 | 97.13 | 98.58 |



## Citation
If you find our paper or models helpful, please consider citing them as follows:

```
@article{li2023towards,
  title={Towards general text embeddings with multi-stage contrastive learning},
  author={Li, Zehan and Zhang, Xin and Zhang, Yanzhao and Long, Dingkun and Xie, Pengjun and Zhang, Meishan},
  journal={arXiv preprint arXiv:2308.03281},
  year={2023}
}
```


