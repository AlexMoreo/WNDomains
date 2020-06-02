from collections import defaultdict
from nltk.corpus import WordNetCorpusReader
from os.path import exists


class WordNetDomains:
    """
    API wrapping some functionality around WordNetDomains. WordNetDomains works with WordNet2.0 (and currently not with
    WordNet3.0). This class assumes you have downloaded WordNet2.0 and WordNetDomains and that they are on the same
    data home.
    WordNet2.0 can be downloaded at https://wordnetcode.princeton.edu/2.0/WordNet-2.0.tar.gz
    WordNetDomains can be downloaded from the home project page at http://wndomains.fbk.eu/index.html (it requires
    some permissions that can be granted by filling an online form).
    See http://wndomains.fbk.eu/index.html for more information.
    """
    def __init__(self, wordnet_home):
        assert exists(f'{wordnet_home}/WordNet-2.0'), f'error: missing WordNet-2.0 in {wordnet_home}'
        assert exists(f'{wordnet_home}/wn-domains-3.2'), f'error: missing WordNetDomains in {wordnet_home}'

        # load WordNet2.0
        self.wn = WordNetCorpusReader(f'{wordnet_home}/WordNet-2.0/dict', 'WordNet-2.0/dict')

        # load WordNetDomains (based on https://stackoverflow.com/a/21904027/8759307)
        self.domain2synsets = defaultdict(list)
        self.synset2domains = defaultdict(list)
        for i in open(f'{wordnet_home}/wn-domains-3.2/wn-domains-3.2-20070223', 'r'):
            ssid, doms = i.strip().split('\t')
            doms = doms.split()
            self.synset2domains[ssid] = doms
            for d in doms:
                self.domain2synsets[d].append(ssid)

    def get_domains(self, word, pos=None, first_sense_only=False):
        """
        Gets a set of domains associated with a given word, possibly restricted to a specific pos
        :param word: the word (string)
        :param pos: the part-of-speech of the word (optional)
        :param first_sense_only: if True, only the first sense concurs in the set of domains. The first sense returned
        by WordNet is assumed to be the most common one, and is a typical baseline in tasks of word sense disambiguation.
        :return: a set of domains (strings) linked to the word according to WordNetDomains
        """
        word_synsets = self.wn.synsets(word, pos=pos)
        if first_sense_only:
            word_synsets = word_synsets[:1]
        domains = []
        for synset in word_synsets:
            domains.extend(self.get_domains_from_synset(synset))
        return set(domains)

    def get_domains_from_synset(self, synset):
        """
        Gets a set of domains associated with a given synset
        :param synset: the synset
        :return: a set of domains (strings) linked to the synset according to WordNetDomains
        """
        return self.synset2domains.get(self._askey_from_synset(synset), set())

    def get_synsets(self, domain):
        """
        Gets a list of synsets linked to the given domain as according to WordNetDomains (empty if the domain does
        not exist)
        :param domain: a string representing the domain. Should be a domain of those considered in WordNetDomains
        :return: a list of synset objects linked to the domain
        """
        return [self._synset_from_key(key) for key in self.domain2synsets.get(domain, [])]

    def get_all_domains(self):
        """
        Gets a set of all the domains in WordNetDomains
        :return: a set of domains (strings)
        """
        return set(self.domain2synsets.keys())

    def _synset_from_key(self, key):
        offset, pos = key.split('-')
        return self.wn.synset_from_pos_and_offset(pos, int(offset))

    def _askey_from_synset(self, synset):
        return self._askey_from_offset_pos(synset.offset(), synset.pos())

    def _askey_from_offset_pos(self, offset, pos):
        return str(offset).zfill(8) + "-" + pos
