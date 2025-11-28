#!/bin/bash

# Curl test to verify MCP interface.
# Modify payload as needed if MCP interface changes.

curl -X POST http://127.0.0.1:5000/analyze \
     -H "Content-Type: application/json" \
     -d '{"user_input": "Testowa treść wiadomości.", "style": "Profesjonalny"}'