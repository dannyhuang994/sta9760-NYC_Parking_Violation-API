 ### STA9760 project 1 - part 1

### Before you run this, you will need to obtain an APP_TOKEN from NYC Open Data API via https://data.cityofnewyork.us/signup.
-----------------------------------------------------------------------------------------------------------------------------

Replace YOUR_APP_TOKEN with the actual token you have obtained.
Use the following command lines to build the image and run an instance:

##### docker build -t bigdata:1.0 .
-----------------------------------------------------------------------------------------------------------------------------
##### docker run -e APP_KEY=YOUR_APP_TOKEN -v $(pwd):/app bigdata:1.0 python main.py --page_size=1 --num_pages=11 --output=result.json
-----------------------------------------------------------------------------------------------------------------------------

--page_size is the number of data point per line. This is required. 

--num_pages is the number of lines of data you want. This is optional. When it is omitted or --num_pages=None, the program will read the data until every line from the API is exhausted.

--output is the name of the output file. When it is omitted, each line will be printed on the console.
