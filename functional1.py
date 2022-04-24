ENVIRONMENT = "dev"

def fetch_data_real():
    print("fetching data from the databse")


def fetch_data_fake():
    """
    Creating fake function to deliver the result
    """
    print("fetching fake data")
    return {
        "name": "Valee",
        "age": 40
    }

fetch_data = fetch_data_real if ENVIRONMENT == "prod" else fetch_data_fake
data = fetch_data()
print(data)