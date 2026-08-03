from api.client import FirewallAPI
from api.parser import AddressParser


api = FirewallAPI()

response = api.get_addresses(

    page=1,

    per_page=5

)

addresses = AddressParser.parse(

    response.json()

)

print()

for address in addresses:

    print(address)
