physics = [15 , 12 , 8 , 8 , 7 , 7 , 7 , 6 , 5 , 3]
history = [10 , 25 , 17 , 11 , 13 , 17 , 20 , 13 , 9 , 15]

xy = sum([x*y for x,y in zip(physics , history)])
xmean = sum(physics) / len(physics)
ymean = sum(history) / len(history)
x_2 = sum([x*x for x in physics])

numerator = xy - ymean*(sum(physics))
denominator = x_2 - xmean*(sum(physics))

slope = numerator/denominator
intercept = ymean - slope*xmean

prediction = slope*10 + intercept

print("%.2f" %prediction)