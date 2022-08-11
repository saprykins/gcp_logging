# gcp_logging

structured logging using json official [basic ex](https://cloud.google.com/logging/docs/samples/logging-write-log-entry)  

more info [here](https://medium.com/google-cloud/structured-logging-in-google-cloud-61ee08898888) and [here](https://medium.com/google-cloud/python-and-stackdriver-logging-2ade460c90e3)

Query to find a record with specific value (King Arthur) of name
```
severity=ERROR AND 
jsonPayload.name="King Arthur"
```

Basic search logging query [here](https://cloud.google.com/logging/docs/view/query-library)

[Language](https://cloud.google.com/logging/docs/view/logging-query-language)

Next steps: 

[Create Sink](https://cloud.google.com/logging/docs/samples/logging-create-sink)

[Configure export to sink](https://cloud.google.com/logging/docs/export/configure_export_v2)

Labs for logging overview
[Fundamentals of Cloud Logging](https://partner.cloudskillsboost.google/focuses/42342?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688932)

[Monitoring and Logging for Cloud Functions](https://partner.cloudskillsboost.google/focuses/11617?catalog_rank=%7B%22rank%22%3A11%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688941)

[Cloud Monitoring: Qwik Start](https://partner.cloudskillsboost.google/focuses/11545?catalog_rank=%7B%22rank%22%3A20%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688941)
