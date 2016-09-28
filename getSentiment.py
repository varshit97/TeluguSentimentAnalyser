#import commands
import json
import requests
import unirest

f = open('advSenti', 'r')
allLines = f.readlines()
for line in allLines:
    #result = commands.getoutput('curl -d "text=%s" http://text-processing.com/api/sentiment/' %(line.strip()))
    #print result
    response = unirest.post("https://community-sentiment.p.mashape.com/text/",
            headers = {
                "X-Mashape-Key": "OOCoKcRZL7mshoTbBg14YYS9HLE1p14dlYAjsniu4kpSwMvh7g",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
                },
            params = {
                "txt": ' '.join(line.split(' ')[:-1])
                }
            )
    print ' '.join(line.split(' ')[:-1]), response.body["result"]["confidence"], response.body["result"]["sentiment"]
    """resulty = json.loads(result.split('\n')[-1])
    print resulty
    print line.strip()
    print resulty["probability"]["pos"]
    print resulty["probability"]["neg"]
    print resulty["probability"]["neutral"]
    print resulty["label"]
    print "-----------------------------------------"
    """
f.close()
