S=FileNotFoundError
M='Invalid Server Name'
K='defaultServer.txt'
J='w'
I='r'
H='NewWorldStatusAPIKey.txt'
G=''
F=True
C=input
D='=========================================='
B=open
A=print
import requests as N,json,sys
def O(y):
	H=y
	while F:
		A("Enter 'List' To See All Servers/Status!");A('Or Enter Server Name To See Status!');A("Or Enter 'E' To Stop The Program!");B=C('Server Input: ').lower()
		if B==G:A(M)
		elif B=='list':B=G;E(B,H)
		elif B=='e':exit()
		else:A(D);E(B,H)
def E(x,y):
	E=x;F=y;G='https://new-world-server-status.p.rapidapi.com/servers/'+E;H={'x-rapidapi-host':'new-world-server-status.p.rapidapi.com','x-rapidapi-key':F};I=N.request('GET',G,headers=H);B=I.json()
	if B==[None]:A(M);A(D)
	else:
		for C in B:J=C['ServerName'];K=C['ServerStatus'];A(J+' '+'Is Currently: '+K);A(D)
def P():
	try:A=B(H,I);C=A.read();A.close();L(C)
	except S:A=B(H,J);A.close();Q()
def Q():
	while F:
		E=C('Please Input Your API Key: ')
		if E==G:A('Invalid API key')
		else:D=B(H,J);D.write(E);D=B(H,I);K=D.read();L(K);break
def L(apikey):
	G=apikey
	try:C=B(K,I);F=C.read();C.close()
	except S:C=B(K,J);H='Bifrost';C.write(H);C=B(K,I);F=C.read();C.close()
	A(D);A('Default Server Is: '+F);E(F,G);R(G)
def R(apiKey):
	L=apiKey
	while F:
		E=C('Do You Want To Change Your Default Server? Enter Y(yes) or N(no): ').lower();A(D)
		if E=='y':
			while F:
				H=C('Please Enter Your New Default Server: ')
				if H==G:A(M)
				else:I=B(K,J);I.write(H);I.close();A(D);break
		elif E=='n':O(L);break
		else:A('Invalid Input');A(D)
if __name__=='__main__':P()
