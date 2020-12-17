import pandas as pd
import os
import json
import sys

from pytrends.request import TrendReq
pytrend = TrendReq()




if __name__ == "__main__":
	# Get Google Hot Trends data
	loc = sys.argv[1]
	print("Trends in ",loc)

	df = pytrend.today_searches(pn=loc)
	print(df.head(50))
	result = df.to_json(orient='index')
	parsed = json.loads(result)
	 
	
with open("google_{}_trends.json".format(loc),"w") as wp:
	wp.write(json.dumps(parsed, indent=4))