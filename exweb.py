from bottle import route,template,run
@route('/')
def index():
	return template('<b>bmi= {{bmi}}</b>!!', 
	bmi=str(bmi(180.0,72.5)))

def bmi(h,w):
	height=h/100
	weight=w
	# return weight / (height * height)
	return round(weight / (height * height), 1)
	
# run(host='localhost', port=8080)
run(host='0.0.0.0', port=8080)

