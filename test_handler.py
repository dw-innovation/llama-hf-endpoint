from handler import EndpointHandler

# init handler
my_handler = EndpointHandler(path=".")

# prepare sample payload
non_holiday_payload = {"inputs": "Find all book stores of brand thalia"}

# test the handler
non_holiday_pred = my_handler(non_holiday_payload)

# show results
print(non_holiday_pred)
