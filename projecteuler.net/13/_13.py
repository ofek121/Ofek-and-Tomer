#https://projecteuler.net/problem=13
with open ("big_number.txt", "r") as file_data:
    data=file_data.read().replace('\n','')
data= map(int, data)
print(sum(data))