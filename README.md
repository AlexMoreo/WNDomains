# WNDomains
A simple Python API wrapping some functionality around WordNetDomains. 

WordNetDomains is a lexical resource developed by the HLT Research Unit that extends WordNet2.0 with domain labels. See [their home project](http://wndomains.fbk.eu/index.html) for more information.

This class assumes you have downloaded WordNet2.0 and WordNetDomains and that they are on the same data home. Since some of the resources required need permissions from the authors, this class does not attempt to download them automatically.

* WordNet2.0 can be downloaded at https://wordnetcode.princeton.edu/2.0/WordNet-2.0.tar.gz
* WordNetDomains can be downloaded from the home project page at http://wndomains.fbk.eu/index.html 

Further requirements:
* Python3
* NLTK
