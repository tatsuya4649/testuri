import yaml
import json

with open("path.yaml") as f:
	obj = yaml.safe_load(f)

print(json.dumps(obj,indent=4))
