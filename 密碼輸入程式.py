x = 0
while x < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', 2-x , '次機會')
		x = x + 1
print('失敗! 已達輸入上限')