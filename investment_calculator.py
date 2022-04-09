#takes input from user, calculates the amount at end of each year, stores data in year-amount pairs in a dictionary
r = input('Percentage annual rate of return: ')
r= int(r)
P = input('Principle amount: ')
P = int(P)
inv = input('Amount invested regularly: ')
inv = int(inv)
freq = input('Number of investments per year: ')
freq = int(freq)
t = input('Number of years: ')
t = int(t)


year_amount = {}
year_amount['Year 0'] = P
start = P
for i in range(1,t+1):
    end = (start + freq*inv)*(1+r/100)
    year_amount['Year '+str(i)] = end
    start = end

for i,k in year_amount.items():
    print(i+': '+"{:.2f}".format(k))













