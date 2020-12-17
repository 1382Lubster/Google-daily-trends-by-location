import pandas as pd
import os
import json
import sys

from pytrends.request import TrendReq
pytrend = TrendReq()


def Gtrends(loc):
	df = pytrend.today_searches(pn=loc)
	print(df.head(50))
	result = df.to_json(orient='index')
	parsed = json.loads(result)
	return parsed

if __name__ == "__main__":
	loc = sys.argv[1]
	# Get Google Hot Trends data
	parsed=Gtrends(loc)	
	print("Trends in ",loc)
	with open("google_{}_trends.json".format(loc),"w") as wp:
		wp.write(json.dumps(parsed, indent=4))
