from flask import Flask, render_template, request,redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', error_message=None)

@app.route('/submit' , methods=['POST'])
def process_form():
    
    
    device_description = request.form.get('device_description').split(" , ")
    type_description = request.form.get('type_description').split(" , ")
    manufacturer = request.form.get('manufacturer').split(" , ")
    # # Process the data (use your existing logic)
    # # Return the filtered project names
    # # You can render a new template with the resultpis
    
    result = process_jupyter_code(device_description, type_description, manufacturer)
    if type(result) == str : 
        
        return render_template('index.html', error_message=result)
    else:
        return render_template('result.html', result=result)
        

def process_jupyter_code(device, type_desc, manuf):
    # Your logic here: Convert Jupyter code into Python functions
    # Execute the code using input parameters
    # Return the result
    arr = [device, type_desc, manuf]
    import pandas as pd
    import numpy as np
    df = pd.read_csv("Material Analytics p.csv",encoding='latin-1')
    imp_features = ['Device Description','Type Description' , 'Manufacturer']
    y =  dict.fromkeys(imp_features, [])
    i = 0 
    for x in imp_features:
        values = arr[i]
        y[x] = values
        i= i+1

    from ItemCheck import item_check
    
    for i in y:
        if(len(y[i][0])) != 0:
            result = item_check(df[str(i)] , y[i])
            if(result == 0):
                ans = f"Wrong Inputs Given in {i}"
                return ans
    
    from Fetch import find_projects_by_input
    combined = df['Name'].tolist()
    for i in y :
        if(len(y[i][0])) != 0:
            combined = set(find_projects_by_input(df, str(i) ,y[i]))& set(combined)
    return combined
   



if __name__ == '__main__':
    app.run(debug=True)

