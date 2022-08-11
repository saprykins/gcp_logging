# gcp_logging

structured logging using json official [basic ex](https://cloud.google.com/logging/docs/samples/logging-write-log-entry)  

more info [here](https://medium.com/google-cloud/structured-logging-in-google-cloud-61ee08898888) and [here](https://medium.com/google-cloud/python-and-stackdriver-logging-2ade460c90e3)

Query to find a record with specific value (King Arthur) of name
```
severity=ERROR AND 
jsonPayload.name="King Arthur"
```
