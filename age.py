driving = input('Have you drive a car?')
if driving != 'yes' and driving != 'no':
    print('只能輸入 yes or no') 
    raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18 :
		print('PASS!!')
	else:
		print('奇怪 你怎麼會開過車')
elif driving == 'no':
	if age >= 18 :
		print('你可以找考駕照了呀, 怎麼還不去考?')
	else: 
		print('再過幾年就可以考駕照了')
