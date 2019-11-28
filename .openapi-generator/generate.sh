#!/bin/bash

npx openapi-generator generate \
  -i https://api.pollination.cloud/sdk_openapi.json \
  -t .openapi-generator/templates/python \
  -g python \
  -o . \
  --skip-validate-spec \
  -c .openapi-generator/config.json