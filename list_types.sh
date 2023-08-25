#!/bin/bash
curl -u ${LAMBDA_CLOUD_TOKEN}: \
    https://cloud.lambdalabs.com/api/v1/instance-types \
    | jq '.data[].instance_type.name'
