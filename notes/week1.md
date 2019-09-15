## Week 1

Plan:

1. *CS* The Algorithm Design Manual: Data Structures 65 - 83
- [x] 2.2 The Big Oh Notation
- [ ] 3.1 Contiguous vs. Linked Data Structures
- [ ] 3.2 Stacks and Queues
- [ ] 3.3 Dictionaries
- [ ] 3.4 Binary Search Trees
- [ ] 3.5 Priority Queues

2. *ML*
- [ ] Confusion matrix
- [ ] Precision/Recall
- [ ] Accuracy
- [ ] ROC curve (AUC)
- [ ] PR curve
- [ ] Convolutional NN

3. *Math*
- [ ] Probability

---
### Saturday Sept. 14th, 2019

1. The Big Oh Notation

* Common complexity functions: log n, n, n log n, n^2, 2^n, n!
    - Roughly the same time for n = 10
    - Algos with O(n!) running time become useless for n ≥ 20
    - Algos with O(2^n) become impractical for n > 40
    - Algos with O(n^2) remain usable for approx n = 10,000... but hopeless for n > 1,000,000
    - O(n) and O(n log n) algorithms remain practical on inputs of one billion items
    - O(log n) algorithms are tractible and preferred for any input

* Selection sort has complexity O(n^2)
