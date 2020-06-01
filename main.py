from WNDomains import WordNetDomains

wnd = WordNetDomains(wordnet_home='/Users/moreo/WordNet/')
print(wnd.get_domains('bank', 'n'))
print(wnd.get_domains('bank'))
print(wnd.get_synsets('banking'))
print(wnd.get_all_domains())