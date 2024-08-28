#!/bin/bash
uvicorn src.main:app --proxy-headers --host 0.0.0.0 --port 34880
