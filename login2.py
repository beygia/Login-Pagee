import os,json
import hashlib
from colorama import Fore as f

if not os.path.exists('alb.json'): open('alb.json','a+').write('{}')	

def signup(data,user,pas_lis):
	if not 'users' in data:
		print(1)
		data['users']={}
			
	elif user in data['users']:
			print(f.RED,' This name has already been selected')
			exit()
	else:
		pass			
			
	data['users'][user]={'user_name': user, 'password': pas_lis}	
	
	print('>>',len(data["users"]))
			
	json.dump(data,open('alb.json','w'))	
	print('  user {} signed up'.format(user))	
	return
			   
			   
def login(data,user,pase):	
	if user in data['users']:
		if pase==data['users'][user]['password']:
			print(' loged in')
			p=input(f.WHITE+' Do you want to continue?(y,n) :')
			if p=='y':
				pass
			else:
				exit()	
		else:
			print('password is wrong')			
	else:
		print('user is not found')
		

while 1:
	data=json.load(open('alb.json', 'r'))
	
	print(f.YELLOW,'┌─[', f.GREEN,'MOHQ TM', f.YELLOW,'/',f.GREEN,'@Home')

	select=input(f.WHITE+""" 
	 
		       [ 1 ] - Admin page
		       [ 2 ] - Sign up new user
		       [ 3 ] - Login
Select One :""" )
	
	if select=='1':
		user_n=input(' Enter username :')
		user_p=input(' Enter password :')

		if user_n=='admin' and user_p=='admin':
			os.system('clear')
			print(f.YELLOW,'*' * 40)
			print(f.GREEN,'           WELCOME ADMIN')	
			print(f.YELLOW,'*' * 40,'\n')
			print(f.GREEN,'        [ * ] You can access user information\n')
			#تعداد کاربران ثبت شده
			print(f.WHITE,'        Number of registered users :',len(data['users']))
			
			admin=input(f.WHITE+' \nSearch for peoples names :')
		
			if admin in data['users']:
				print(f.GREEN,data['users'][admin])
			else:
				print(f.RED,' not users in data')						
			exit()
		else:
			print(f.RED,' username or password invalid !')
			exit()			
			
			
	if select=='2':
		os.system('clear')		
		print(f.YELLOW,'┌─[', f.GREEN,'MOHQ TM', f.YELLOW,'/',f.GREEN,'@Home', f.YELLOW,'/' , f.GREEN,'Sign up')
		
		user=input(f.WHITE+' Enter User Name :')
		print(f.YELLOW,' \n Password included (lowercase, uppercase, number, Eight digits)\n')
		password=input(f.WHITE+' Enter Your Password :')
		
		low=password.lower()
		up=password.upper()
		
		i = 0
		nums = ["0","1","2","3","4","5","6","7","8","9"]
		num = 0
		a = 0
		while num < 10 :
  	 	 while i < len( password ):
    
    	  	  if  password[i] == nums[num] :
      	   	   a = a+1
    	  	  else :
      	   	   pass
    	  	  i = i + 1
  	 	 i = i-i
  	 	 num = num + 1
		if a==0:
			print(f.RED,' [ ! ] Password is weak !!!') 			
			
		if password==low:
			print(f.RED,' [ ! ] The Password must be uppercase!')
			
		elif password==up:
			print(f.RED,' [ ! ] The Password must be lowercase!')
										
		elif len(password)<6:
			print(f.RED,' [ ! ] Password must be more than eight digits!')
						
		else:
			print(f.GREEN,' Password is Strong√')
			
		pas=hashlib.md5(password.encode('utf-8')).hexdigest()
		pas_lis=pas	
		signup(data,user,pas_lis)	
		
		break
										
	if select=='3':
		os.system('clear')
		print(f.YELLOW,'┌─[', f.GREEN,'MOHQ TM', f.YELLOW,'/',f.GREEN,'@Home', f.YELLOW,'/' , f.GREEN,'Login')
		user=input(f.WHITE+'enter user name :')
		password=input('enter your password :')
		pase=hashlib.md5(password.encode('utf-8')).hexdigest()
		
		login(data,user,pase)	
