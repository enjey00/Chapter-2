alpha = float(input())
 
hour = 30
minute = hour/60
second = minute/60
 
h = alpha//hour
m = alpha % 30 * 2
s = alpha % 0.5*120
 
print(int(h), int(m), int(s))