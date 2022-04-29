def Job_profile(name):
    print("Hello " + name +",Welcome to the IT tech support profile ")
def Join_date(dates):
    print("The Date of Joining is " +dates)
def Leave_taken(days):
    print("The Number of leaves taken is "+days)
def Productivity(Time_spent , No_days):
    return Time_spent*No_days
Productivity1 = Productivity (5,6)
Productivity2 = Productivity (6,7)
sum = Productivity1 + Productivity2 
Job_profile("Jinit")
Join_date("23 rd August")
Leave_taken("0")
name=("Jinit")
print("The Productivity for 1st Month of " +str(name) + " is " +str(Productivity1))
print("The Sum of Productivity is " +str(name) + " is " + str(sum) )
def Time_left(Seconds):
    Hours = Seconds//3600
    Minutes = (Seconds-Hours*3600)//60
    Seconds = (Seconds-Hours*3600-Minutes*60)
    return Hours,Minutes,Seconds

Hours,Minutes,Seconds=Time_left(5000)
print("There is " + str(Hours) +" Hour left and " +str(Minutes)+ 
" Minutes left  "+str(Seconds)+ " Seconds Left For todays work to complete")
#print(10>11)
#print (10 != 10 )
#print("cat"=="tiger")
#print("big">"small")
#def get_username () :
#    username=get_username()
#def valid_username() :
#    while not valid_username()
#    print("Invalid Username ")
#    username=get_username()
def leaves (n):
     x=20
     if n <= x :
        print ("The Number of leaves taken are  "+str(n)+ ". No Pay cut .")
     else :
         print("The number of leaves taken are greater that is " +str(n)+ " . There will be a paycut" )
leaves (26)
leaves (12)
def leaves (n):
     x=20
     while n<=x :
         n += 1
     print("The number of leaves are " +str (n)+ " .")
leaves (35)
for left in range (7):
    for right in range (left,7):
        print("["+str(left)+"|"+str(right)+"]" , end = " ")
    print()

teams = ["IT","HR","MANAGERS","STAFF"]
for home_teams in teams :
    for away_teams in teams :
        if home_teams != away_teams :
            print (home_teams +"vs"+ away_teams)

def numbers_pr(intn):
    if intn > 101 :
         numbers_pr (100)
         print (intn,'\n')
