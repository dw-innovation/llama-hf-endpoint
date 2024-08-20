from handler import EndpointHandler

# init handler
my_handler = EndpointHandler(path=".")

# prepare sample payload
non_holiday_payload = {"inputs": "I am quite excited how this will turn out", "date": "2022-08-08"}
holiday_payload = {"inputs": "Today is a though day", "date": "2022-07-04"}

# test the handler
non_holiday_pred = my_handler(non_holiday_payload)
holiday_payload = my_handler(holiday_payload)

# show results
print("non_holiday_pred", non_holiday_pred)
print("holiday_payload", holiday_payload)
# non_holiday_pred [{'label': 'joy', 'score': 0.9985942244529724}]
# holiday_payload [{'label': 'happy', 'score': 1}]