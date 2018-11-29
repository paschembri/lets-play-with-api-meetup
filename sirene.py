import requests
import json

company_name = 'Netsach'

url = (
    f'https://data.opendatasoft.com/api/records/1.0/search/?'
    f'dataset=sirene%40public'
    f'&facet=rpet'
    f'&facet=depet'
    f'&facet=libcom'
    f'&facet=epci'
    f'&facet=siege'
    f'&facet=libapet'
    f'&facet=libtefet'
    f'&facet=saisonat'
    f'&facet=libnj'
    f'&facet=libapen'
    f'&facet=ess'
    f'&facet=libtefen'
    f'&facet=categorie'
    f'&facet=proden'
    f'&facet=libtu'
    f'&facet=liborigine'
    f'&facet=libtca'
    f'&facet=libreg_new'
    f'&facet=nom_dept'
    f'&facet=section'
    f'&q={company_name}'
)

response = requests.get(url)

json_response = json.dumps(response.json(), indent=4)

print(json_response)
