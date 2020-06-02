from WNDomains import WordNetDomains


wnd = WordNetDomains(wordnet_home='../WordNet/')

print('Domains for bank-n (first sense only)')
print(wnd.get_domains('bank', 'n', first_sense_only=True))

print('Domains for bank-n (all senses)')
print(wnd.get_domains('bank', 'n'))

print('Domains for bank (all part-of-speechs)')
print(wnd.get_domains('bank'))

print('List of synsets for domain "banking"')
banking_synsets = wnd.get_synsets('banking')
print(f'domain "banking" covers {len(banking_synsets)} synsets: {banking_synsets}')

print('Set of domains in WordNetDomains')
print(wnd.get_all_domains())