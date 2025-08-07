import os
from pysimplesat import SimpleSatAPIClient
from dotenv import load_dotenv

load_dotenv()

privatekey = os.getenv('SIMPLESAT_API_TOKEN')

# init client
simplesat_api_client = SimpleSatAPIClient(
    privatekey,
)

#surveys = simplesat_api_client.surveys.get()
#print(surveys)
data = {"start_date": "2015-04-11T17:00:00Z"}

page_responses = simplesat_api_client.responses.search.paginated(1, data=data)
responses = page_responses.all()
print(responses)
for response in responses:
    pass
#    print(response.id)