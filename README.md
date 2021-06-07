# XFORMAL: A Benchmark for Multilingual Formality Style Transfer

A description of the XFORMAL corpus can be found in our NAACL 2021 paper “Olá, Bonjour, Salve! XFORMAL: A Benchmark for Multilingual Formality Style Transfer”:
[https://aclanthology.org/2021.naacl-main.256.pdf](https://aclanthology.org/2021.naacl-main.256.pdf)
[https://arxiv.org/pdf/2104.04108.pdf](https://arxiv.org/pdf/2104.04108.pdf)

For any questions, please contact Eleftheria Briakou (ebriakou@cs.umd.edu) and Joel Tetreault (tetreaul@gmail.com).

## Obtaining XFORMAL

The XFORMAL corpus was created using the Yahoo Answers corpus: [L6 - Yahoo! Answers Comprehensive Questions and Answers version 1.0](https://webscope.sandbox.yahoo.com/catalog.php?datatype=l).  Access to XFORMAL requires users to first gain access to L6 via [Yahoo Webscope](https://webscope.sandbox.yahoo.com/catalog.php?datatype=l).  Once you have obtained access, please forward the acknowledgement (forward the approval email or screenshot the download page) to Joel Tetreault (tetreaul@gmail.com), along with your affiliation and a short description of how you will be using the data, and we will email the XFORMAL dataset.

Please note that the XFORMAL set is 22MB which may be too large for many email clients.  

The XFORMAL dataset contains the following subdirectories.  Note the mturk and rule_based portions can also be downloaded from this repository above.

* `gyafc_translated`: the GYAFC translated into Brazilian Portuguese, Italian, and French.  Note that in the test subdirectories, "informal.ref0" refers to one set of informal rewrites of "formal".  Conversely, "formal.ref3" refers to one set of formal rewrites of "informal".

* `mturk`: Amazon Mechanical Turk templates, qualification tests, and annotations results. 

* `papers`: the XFORMAL and GYAFC papers downloaded from arxiv on May 29.

* `rule_based`: scripts for replicating rule based formality style transfer in the three languages of XFORMAL.

* `xformal_eval`: dataset consisting of informal sentences with multiple human generated formality rewrites in Brazilian Portuguese, Italian, and French.

## Referencing XFORMAL

When making use of the corpus, scripts, translations or mturk templates, please cite our paper with the following bib file:  [https://aclanthology.org/2021.naacl-main.256.bib](https://aclanthology.org/2021.naacl-main.256.bib)
