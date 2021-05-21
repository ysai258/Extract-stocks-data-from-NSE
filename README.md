# Extract-stocks-data-from-NSE
# Extract_data.py:
1. First we access the https://www.nseindia.com/ using headers.
2. Then we extract cookies from the nse website.
3. Using those cookies we create a session.
4. Then access the api of nse website. Sample api link for SBIN is
https://www.nseindia.com/api/quote-equity?symbol=SBIN
5. Then we take the required data i.e open , close etc.
![Problem1_Code](https://user-images.githubusercontent.com/48080730/119086740-90bf2600-ba23-11eb-84ea-9225c9a50ba6.png)
![Problem1_Output](https://user-images.githubusercontent.com/48080730/119086751-9583da00-ba23-11eb-81bb-926cd36c90a7.png)
# last_Thursday.py:
1. To get last Thursday for a given month and year we get the number of days in that month in the respective year.
2. Then looping from backwards of day i.e., in april we loop from 30 we check which day is it if we get Thursday then we return that date.
3. To check whether the given date is last Thursday we convert the given date which is string to date format.
4. Then we call get last Thursday of that month and check both if both are equal then return true else false.
![Problem2_Code](https://user-images.githubusercontent.com/48080730/119086887-d2e86780-ba23-11eb-91e9-b8ebe33ab459.png)
![Problem2_Output](https://user-images.githubusercontent.com/48080730/119086894-d54ac180-ba23-11eb-8a2d-cc5fe5334fb7.png)
