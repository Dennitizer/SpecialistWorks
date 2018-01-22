import math
hour = []
min = []

while True:
    inp = input('time hh:mm ')
    if inp == "" :
        break
    time = inp
    hold = time.split(':')
    hour.append(hold[0])
    min.append(hold[1])  
              
for i in range(len(hour)):
    hour[i] = int(hour[i])
sumhour = (sum(hour))
#print(sumhour)

for i in range(len(min)):
    min[i] = int(min[i])
summin= sum(min)
#print(summin)
while summin >= 60:
    summin = summin - 60
    sumhour = sumhour + 1
    if summin < 60:
        break
print(sumhour,"uren",summin,"minuten")
formin = (summin * 1.66)
formin = int(math.ceil(formin))
formin = (format(formin, '02d'))
#print(sumhour,':',formin)
print('worked hours to fill in = ', sumhour,':',formin)
