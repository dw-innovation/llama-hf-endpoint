from handler import EndpointHandler

# init handler
my_handler = EndpointHandler(path=".")

# prepare sample payload
test_payload = {"inputs": "Find all book stores of brand thalia"}

# test the handler
response = my_handler(test_payload)

# show results
print(response)
