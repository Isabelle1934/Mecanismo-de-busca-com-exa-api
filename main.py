from exa_py import Exa

exa = Exa('YOUR_KEY_HERE')
query = input('Search here: ')
response = exa.search(
  'Best Chicago cold brew',
  num_results=10,
)
