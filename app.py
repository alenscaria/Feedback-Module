from flask import Flask,render_template, request
app=Flask(__name__) 
import pandas as pd
import openpyxl






@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/feedback') 
def feedback():
    return render_template('feedback.html')


@app.route('/admin/feedbacks') 
def adminFeedback():
    workbook=openpyxl.load_workbook('feedback.xlsx',data_only=True)
    sheet_name='Feedback'
    df=pd.read_excel('feedback.xlsx',sheet_name=sheet_name)

    feedback_count=len(df)
    table_html=df.to_html(classes='table table-striped',index=False)
    return render_template('adminFeedback.html',table=table_html,feedback_count=feedback_count)




if __name__=='__main__':
    app.run(debug=True)
