from flask import Flask, render_template, url_for, redirect, request
import relays
import time

app = Flask(__name__)

start_time = {
        "mv": "OFF",
        "z1": "OFF",
        "z2": "OFF",
        "z3": "OFF",
        "z4": "OFF",
        "z5": "OFF",
        "z6": "OFF",
        "z7": "OFF",
        }

status = {
    "mv": "Inactive",
    "z1": "Inactive",
    "z2": "Inactive",
    "z3": "Inactive",
    "z4": "Inactive",
    "z5": "Inactive",
    "z6": "Inactive",
    "z7": "Inactive",
}

@app.route("/index", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        if request.form.get('mv_on') == 'ON':
            status.update(mv = "Active")
            relays.mv_on()
            start_time.update(mv = time.ctime())
            
        elif request.form.get('mv_off') == 'OFF':
            status.update(mv = "Inactive")
            relays.mv_off()
            start_time.update(mv = "")

        if request.form.get('z1_on') == 'ON':
            status.update(z1 = "Active")
            relays.one_on()
            start_time.update(z1 = time.ctime())

        elif request.form.get('z1_off') == 'OFF':
            status.update(z1 = "Inactive")
            relays.one_off()
            start_time.update(z1 = "")
            
        if request.form.get('z2_on') == 'ON':
            status.update(z2 = "Active")
            relays.two_on()
            start_time.update(z2 = time.ctime())
            
        elif request.form.get('z2_off') == 'OFF':
            status.update(z2 = "Inactive")
            relays.two_off()
            start_time.update(z2 = "")
           
        if request.form.get('z3_on') == 'ON':
            status.update(z3 = "Active")
            relays.three_on()
            start_time.update(z3 = time.ctime())
            
        elif request.form.get('z3_off') == 'OFF':
            status.update(z3 = "Inactive")
            relays.three_off()
            start_time.update(z3 = "")
            
        if request.form.get('z4_on') == 'ON':
            status.update(z4 = "Active")
            relays.four_on()
            start_time.update(z4 = time.ctime())
            
        elif request.form.get('z4_off') == 'OFF':
             status.update(z4 = "Inactive")
             relays.four_off()
             start_time.update(z4 = "")
           
        if request.form.get('z5_on') == 'ON':
            status.update(z5 = "Active")
            relays.five_on()
            start_time.update(z5 = time.ctime())
            
        elif request.form.get('z5_off') == 'OFF':
            status.update(z5 = "Inactive")
            relays.five_off()
            start_time.update(z5 = "")
            
        if request.form.get('z6_on') == 'ON':
            status.update(z6 = "Active")
            relays.six_on()
            start_time.update(z6 = time.ctime())
            
        elif request.form.get('z6_off') == 'OFF':
            status.update(z6 = "Inactive")
            relays.six_off()
            start_time.update(z6 = "")
            
        if request.form.get('z7_on') == 'ON':
            status.update(z7 = "Active")
            relays.seven_on()
            start_time.update(z7 = time.ctime())
            
        elif request.form.get('z7_off') == 'OFF':
            status.update(z7 = "Inactive")
            relays.seven_off()
            start_time.update(z7 = "")
            

        else:
            return render_template('index.html', title='PIrigation Control', status=status, start_time=start_time)
    elif request.method =='GET':
        print("No Post Back Call")
    return render_template('index.html', status=status, start_time=start_time)


if __name__=="__main__":
   app.run(host='0.0.0.0', debug=True)
