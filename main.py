from flask import Flask , session , request , send_from_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

head = "<br> <a href='/'>home-page<a><br>\
	<a href='/yourlast'>check-your-last-submit</a><br><br>"

def gaohead():
	return '<div align="center">\
		welcome ' + session.get('usn') + "<br><br>\
		<a href='/'>home-page<a><br>\
		<a href='/yourlast'>check-your-last-submit</a><br>\
		<a href='/edit-problem'>edit-problem</a><br><br>"
		
def gaotail():
	return '</div>'

@app.route('/')
def face():
	if str(type(session.get('usn'))) == "<class 'NoneType'>":
		return \
			'<div align="center">\
				<form action="/login" method="POST">\
					username <input type="text" name="usnm"><br>\
					password <input type="password" name="pswd"><br>\
					<button>submit</button>\
				</form>\
				if you enter a new username<br>\
				then this operation will be seen as register<br>\
				attention it!<br>\
			</div>'
	else:
		res = gaohead()
		try:
			f = open('pro/overview','r')
			res = res + f.read()
		except:
			f = open('pro/overview','r',encoding='gbk')
			res = res + f.read()
		return res + gaotail()
	
@app.route('/login',methods=["POST"])
def login():
	A = request.form.get('usnm')
	SB = request.form.get('pswd')
	hs = 2333
	mod = int('1000000000000000009')
	for char in SB:
		hs = (hs * 998244353 + ord(char)) % mod
	B = str(hs)
	
	if os.path.isfile('usr/' + A):
		print(A + " is comming")
	else:
		print(A + " is registing")
		os.system('mkdir usr/' + A)
		f = open('usr/' + A + '/pswd','w')
		f.write(B)
	f = open('usr/' + A + '/pswd','r')
	t = f.read().split('\n')
	print(t[0])
	if t[0] == B:
		session['usn'] = A
	return '\
		<script type="text/javascript">\
			function Gogogo(){\
				window.location.href="/";\
			}\
			window.onload=Gogogo();\
		</script>'

@app.route('/prob/<pid>')
def seeprob(pid):
	res = gaohead()
	res = res + '<a href="/sbmt/' + pid + '">submit</a><br><br>'
	try:
		f = open('pro/'+pid+'/stat','r')
		res = res + f.read()
	except:
		f = open('pro/'+pid+'/stat','r',encoding='gbk')
		res = res + f.read()
	return res

@app.route('/sbmt/<pid>')
def sbmt(pid):
	res = gaohead()
	return res+\
		'<form action="/submit" method="POST">\
			<input type="text" name="pid" value="' + pid + '"><br>\
			<textarea name="code" rows="10" cols="80"></textarea><br>\
			<button>submit</button>\
		</form>' + gaotail()

@app.route('/submit',methods=['POST'])
def submit():
	rq = request
	tot = 0
	
	if 1:
		f = open("sub/cnt","r")
		t = f.read().split('\n')
		tot = int(t[0])
		f.close()
	tot += 1
	if 1:
		f = open("sub/cnt","w")
		f.write(str(tot))
		f.close()
	
	print(tot,session['usn'],rq.form.get('code'),rq.form.get('pid'))
	os.system("mkdir sub/" + str(tot))
	
	if 1:
		f = open("sub/" + str(tot) + "/bel","w")
		f.write(session['usn'])
	if 1:
		f = open("sub/" + str(tot) + "/x.cpp","w")
		f.write(rq.form.get('code'))
	if 1:
		f = open("sub/" + str(tot) + "/pid","w")
		f.write(rq.form.get('pid'))
	if 1:
		f = open("sub/" + str(tot) + "/ans","w")
		f.write('<h1>pending</h1>')
	if 1:
		f = open("sub/todo/" + str(tot),"w")
		f.write('this file is empty')
	if 1:
		f = open("usr/" + session['usn'] +"/alllast","w")
		f.write(str(tot))
	res = gaohead()
	return res + '<h3>submit complete</h3>' + gaotail()

@app.route('/rslt/<sid>')
def rslt(sid):
	res = gaohead()
	f = open("sub/" + sid + "/ans","r")
	res = res + f.read() + '<br>'
	res = res + "<a href='/codes/" + sid + "'><h3>download-code</h3></a>"
	return res

@app.route("/codes/<sid>")
def codes(sid):
	return send_from_directory("","sub/" + sid + "/x.cpp",as_attachment=True)

@app.route('/yourlast')
def ylst():
	A = session['usn']
	if os.path.isfile('usr/' + A + '/alllast'):
		print(A + ' is checking his submit')
	else:
		return "you don't have any submits. what's your problem?"
	sid = ''
	f = open('usr/' + A + '/alllast','r')
	t = f.read().split('\n')
	sid = t[0]
	return '\
		<script type="text/javascript">\
			function Gogogo(){\
				window.location.href="/rslt/' + sid + '";\
			}\
			window.onload=Gogogo();\
		</script>'

@app.route('/edit-problem')
def edit():
	res = gaohead()
	return res+\
		'<form action="/do-edit" method="POST" enctype="multipart/form-data">\
			problem-id <input type="text" name="pid"><br>\
			zip <input type="file" name="zip"><br>\
			<button>submit</button>\
		</form>\
		if you enter a new problem-id<br>\
		then this operation will be seen as insert a new problem<br>\
		<h4>All operations have Response Delay!!!</h4>\
		attention it!' + gaotail()

@app.route('/do-edit',methods=["POST"])
def doedit():
	pid = request.form.get('pid')
	fi = request.files.get('zip')
	
	if os.path.isfile('pro/' + pid + '/bel'):
		f = open('pro/' + pid + '/bel',"r")
		t = f.read().split('\n')
		if t[0] != session['usn']:
			return gaohead() + "you can only modify your problem, what's your problem?"
	
	os.system("rm -r pro/" + pid)
	os.system("mkdir pro/" + pid)
	fi.save("pro/" + pid + "/tmp.zip")
	os.system("unzip pro/" + pid + "/tmp.zip -d pro/" + pid)
	os.system("echo '" + session['usn'] + "'>pro/" + pid + "/bel")
	
	return gaohead() + "<h1>ok</h1>" + gaotail()

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)





