import json
import string

with open('/tmp/config.json') as config_file:
  data = json.load(config_file)
plugin_array = [ k+":"+v for k, v in data["plugins"].items() ]
plugin_list = ' '.join([str(x) for x in plugin_array])
print(plugin_list)
