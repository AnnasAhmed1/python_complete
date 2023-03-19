print('welcome to Quiz')
answer=input('are you ready to play quiz? (yes/no):')
score=0
total_question=5

if answer.lower()=='yes':
	answer=input('Question 1: what is 36+55? =')
	if answer.lower()=='91':
	       score +=1
	       print('correct')
	else:
	       print('Wrong Answer :(')
	       print('correct answer is 91')
	
	
	              
	answer=input('Question 2: what is 71-40? =')
	if answer.lower()=='31':
	       score +=1
	       print('correct')
	else:
	        print('Wrong Answer :(')
	        print('correct answer is 31')
	
	
	
	answer=input('Question 3: what is 7 x 5? =')
	if answer.lower()=='35':
	       score +=1
	       print('correct')
	else:              
	       print('Wrong Answer :(')
	       print('correct answer is 31')
	
	
	
	answer=input('Question 4: What is 9 x 7 =')
	if answer.lower()=='63':
	        score +=1 
	        print('correct')
	else: 
	        print('Wrong Answer :(')
	        print('correct Answer is 63')
	
	       
	
	answer=input('Question 5: What is 160-137? =')
	if answer.lower()=='23':
	       score +=1 
	       print('correct')
	else:
	       print('Wrong Answer :(')
	       print('correct Answer is 23')
	
	
	print('Thankyou for playing this small quiz game,you attempted',score,'questions correctly!')
	mark=(score/total_question)*100
	print('Marks obtained:',mark)
	print('BYE HAVE A GOOD DAY!')
else:
               print('Program ended!')
               





               
               


              
              
       


