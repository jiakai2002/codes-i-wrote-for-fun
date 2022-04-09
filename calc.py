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
    end = (start + freq*inv)*(1+r)
    year_amount['Year ',str(i)] = end
    start = en

print(year_amount)













