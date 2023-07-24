import json

gcp_auth_key = <<gcp_auth>>

with open('auth.json', 'w') as outfile:
    json.dump(gcp_auth_key, outfile)