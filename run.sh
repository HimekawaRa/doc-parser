#!/bin/bash
source venv/bin/activate
nohup uvicorn main:app --host 127.0.0.1 --port 8080 > app.log 2>&1 &