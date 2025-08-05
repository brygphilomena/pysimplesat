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

page_responses = simplesat_api_client.responses.search.paginated(1)
responses = page_responses.all()
print(responses)
for response in responses:
    print(response.id)