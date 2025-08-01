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

answers = simplesat_api_client.responses.search.paginated(1,5)
print(answers)
print(answers.data)