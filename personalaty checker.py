#personality checker

import random

print('Welcome to the personality checker!')
print('Here you can *kind of* check your personality')
print('I am not responsible for any misunderstandings caused by this app.')

#checks if you are sure to continue otherwise kills itself
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
sureCheck = int(input('Are you sure you want to proceed? [ 1 for yes 2 for no]: '))

if(sureCheck == 1):
    print('Thanks for understanding!')
else:
    print('Nevermind.')
    quit()

#Real part starts *drumroll pls*
#spoiler: contains a ton of if else things pls send help compressing em

#question 1
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ques1 = str(input('> What is your name? Mine is PC :D : '))
rint = random.randint(1, 5)
if(rint == 1):
    print('> Wow! Nice name!')
elif(rint == 2):
    print('> Amazing!')
elif(rint == 3):
    print('> Suits you very well! :D')
elif(rint == 4):
    print('> Got a reason to get this name.')
else:
    print('> Wait, you seem amazing! :o')

#ques2
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ques2 = int(input('> What is your age? : '))

q2ans = 0

if (ques2 <= 5):
    print("> You seem irrelevent to proceed. Quitting :')")
    quit()
elif(ques2 <= 10):
    print('> You seem very mature very soon! *mind blown*')
    q2ans = 5
elif(ques2 <= 15):
    print('> :D')
    q2ans = 3
elif(ques2 <= 20):
    print('> Same age as my maker! Amazing!')
    q2ans = 2
else:
    print('> Lets continue :D')
    q2ans = 1

#ques3
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('M for Male, F for Female, N to ignore')
ques3 = str(input('> What is your gender? *seems rude but needed sorry*: '))

q3ans = 0
if(ques3 == str(ques3 == 'M')):
    print('> Well, you got this!')
    q3ans = 1
elif(ques3 == 'F'):
    print('> No worries!')
    q3ans = 3
else:
    print('> Ahh You got this! :D')
    q3ans = 2

#ques4
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Do you love your family?')

ques4 = str(input('> Y for yes and N for no: '))

q4ans = 0
if(ques4 == 'Y'):
            q4ans = 1
else:
    print('> Proceeding..')

#ques5
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Do you love games?')
ques5 = str(input('> Y for yes and N for no: '))

q5ans = 0
if(ques5 == 'Y'):
    q5ans = 1
elif(ques5 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword.')

#ques6
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Do you love gardening?')
ques6 = str(input('> Y for yes and N for no: '))

q6ans = 0
if(ques6 == 'Y'):
    q6ans = 1
elif(ques6 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword')

#ques7
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Are you open to talks or want to stay alone?')
ques7 = str(input('> Y for yes and N for no: '))

q7ans = 0
if(ques7 == 'Y'):
    q7ans = 1
elif(ques7 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword')

#ques8
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Do people like being with you?')
ques8 = str(input('> Y for yes and N for no: '))

q8ans = 0
if(ques8 == 'Y'):
    q8ans = 1
elif(ques8 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword')

#ques9
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Do you appreciate art?')
ques9 = str(input('> Y for yes and N for no: '))

q9ans = 0
if(ques9 == 'Y'):
    q9ans = 1
elif(ques9 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword')

#ques10
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('> Finally, Do you love yourself?')
ques10 = str(input('Y for yes and N for no: '))

q10ans = 0
if(ques10 == 'Y'):
    q10ans = 1
elif(ques10 == 'N'):
    print('> Proceeding...')
else:
    print('[!] You have entered wrong keyword')

#analysing the score

score = q2ans + q3ans + q4ans + q5ans + q6ans + q7ans + q8ans + q9ans + q10ans

if(score <= 15):
    print('''> You are a kind, loving and honest person.
                You love your family and you love to care about others''')
elif(score <= 13):
    print('''> You love being all yourself and to make people happy.
                You love to enjoy your life to fullest''')
elif(score <= 10):
    print('''> You love being alone and to enjoy your life without any
                disturbance. You truly care about your privacy.''')
elif(score <= 8):
    print('''> You love to be all yourself and to stay happy even if you
                got no source of happiness''')
else:
    print('''> You seem very unmotivated and kind of depressed. But mate,
                Everything's gonna be fine! Don't worry about your
                future cuz all that matters is your present. :D''')
          
