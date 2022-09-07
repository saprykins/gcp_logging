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

[Configure export to sink](https://cloud.google.com/logging/docs/export/configure_export_v2)

This is probably too much // [Create Sink](https://cloud.google.com/logging/docs/samples/logging-create-sink)

Analysis in BQ. Basic SQL syntax [here](https://www.w3schools.com/sql/sql_where.asp)
```
SELECT jsonPayload.name, jsonPayload.quest
FROM `tenacious-post-355715.dataset_for_sink_test._Default_20220816`
WHERE jsonPayload.name='test 1'
```

Alerting

# Next steps: 

Check all on AF

# Labs for logging overview
[Fundamentals of Cloud Logging](https://partner.cloudskillsboost.google/focuses/42342?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688932) // Explains how to create metrics on logging, HTTP 200 

[Monitoring and Logging for Cloud Functions](https://partner.cloudskillsboost.google/focuses/11617?catalog_rank=%7B%22rank%22%3A11%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688941)

[Cloud Monitoring: Qwik Start](https://partner.cloudskillsboost.google/focuses/11545?catalog_rank=%7B%22rank%22%3A20%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17688941) // Create alerts

# Other
[Operations suit](https://medium.com/google-cloud/measuring-reliability-in-gcp-step-by-step-slo-creation-guide-using-cloud-operation-sandbox-99043bd0e70f)

# Searching to answer: "a metric is zero for more than 10 min"

Grouping and Alignment basics [link](https://cloud.google.com/monitoring/api/v3/aggregation)

Alerting with MQL [link](https://cloud.google.com/monitoring/mql/alerts)

Example for alert filter

When a VM stops:  
```
resource.type="gce_instance"
resource.labels.instance_id="2355846314441647236"
protoPayload.methodName="v1.compute.instances.stop"
```

GCP MQL general [link](https://cloud.google.com/monitoring/mql)

Send alerts based on metrics [lab](https://partner.cloudskillsboost.google/focuses/11615?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=17860031)

Distribution, not count metrics and [historgram buckets](https://cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics)

MQL basic  
```
fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
| align rate(30m)
```

A couple of more metrics like 'compute.googleapis.com/instance/cpu/utilization
' are [here](https://www.dynatrace.com/support/help/how-to-use-dynatrace/infrastructure-monitoring/cloud-platform-monitoring/google-cloud-platform-monitoring/gcp-supported-service-metrics-new/compute-engine-monitoring)
