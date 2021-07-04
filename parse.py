#!/bin/env python3
import yaml
import json
import argparse
import sys

parser = argparse.ArgumentParser(description="Test HTTP URI")

parser.add_argument('yaml',help='URI YAML File')

args = parser.parse_args()

with open(args.yaml) as f:
	obj = yaml.safe_load(f)

path_json = json.dumps(obj,indent=4)
print(path_json)
