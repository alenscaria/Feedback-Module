from flask import Flask,render_template, request
app=Flask(__name__) 

@app.route('/feedback') 
def feedback():
    return render_template('feedback.html')


@app.route('/admin/feedbacks') 
def adminFeedback():
    return render_template('adminFeedback.html')




if __name__=='__main__':
    app.run(debug=True)
