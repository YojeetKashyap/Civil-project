from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained models and scaler
labour_model = joblib.load("labour_model.pkl")
equipment_model = joblib.load("equipment_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/site", methods=["GET", "POST"])
def site():
    predicted_labour_cost = None
    predicted_equipment_cost = None

    if request.method == "POST":
        try:
            # Get user input
            area = float(request.form["area"])
            length_of_site = float(request.form["length_of_site"])
            width = float(request.form["width"])

            # Prepare input for prediction
            user_input = np.array([[area, length_of_site, width]])
            user_input_scaled = scaler.transform(user_input)

            # Predict costs
            predicted_labour_cost = labour_model.predict(user_input_scaled)[0]
            predicted_equipment_cost = equipment_model.predict(user_input_scaled)[0]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("site.html", 
                           labour_cost=predicted_labour_cost, 
                           equipment_cost=predicted_equipment_cost)
    
    

scaler_2 = joblib.load("scaler_2.pkl")
labour_model_2= joblib.load("labour_model_2.pkl")
material_model_2 = joblib.load("material_model_2.pkl")
transport_model_2 = joblib.load("transport_model_2.pkl")
water_model_2 = joblib.load("water_model_2.pkl")

@app.route("/Excavation", methods=["GET", "POST"])
def index():
    predicted_labour_cost = None
    predicted_material_cost = None
    predicted_transport_cost = None
    predicted_water_cost = None

    if request.method == "POST":
        try:
       
            Excavation_on_site = float(request.form["Excavation_on_site"])
            length_of_excavation = float(request.form["length_of_excavation"])
            width_of_excavation = float(request.form["width_of_excavation"])
            depth_of_excavation = float(request.form["depth_of_excavation"])

    
            user_input = np.array([[Excavation_on_site,length_of_excavation, width_of_excavation, depth_of_excavation]])
            user_input_scaled = scaler_2.transform(user_input)

            # Predict costs
            predicted_labour_cost = labour_model_2.predict(user_input_scaled)[0]
            predicted_material_cost = material_model_2.predict(user_input_scaled)[0]
            predicted_transport_cost = transport_model_2.predict(user_input_scaled)[0]
            predicted_water_cost = water_model_2.predict(user_input_scaled)[0]
            

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("excavation.html", 
                           labour_cost=predicted_labour_cost, 
                           material_cost=predicted_material_cost, 
                           transport_cost=predicted_transport_cost, 
                           water_cost=predicted_water_cost)
    
    
    

material_model_3 = joblib.load("material_model_3.pkl")
transport_model_3 = joblib.load("transport_model_3.pkl")
equipment_model_3 = joblib.load("equipment_model_3.pkl")
scaler_3 = joblib.load("scaler_3.pkl")



@app.route("/SandFilling", methods=["GET", "POST"])
def sand_filling():
    predicted_material_cost = None
    predicted_transport_cost = None
    predicted_equipment_cost = None

    if request.method == "POST":
        try:
            # Get user input
            length = float(request.form["length"])
            width = float(request.form["width"])
            height = float(request.form["height"])
            sand_filling = float(request.form["sand_filling"])

            # Prepare input
            user_input = np.array([[length, width, height, sand_filling]])
            user_input_scaled = scaler_3.transform(user_input)

            # Predict costs
            predicted_material_cost = material_model_3.predict(user_input_scaled)[0]
            predicted_transport_cost = transport_model_3.predict(user_input_scaled)[0]
            predicted_equipment_cost = equipment_model_3.predict(user_input_scaled)[0]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("sand.html", 
                           material_cost=predicted_material_cost, 
                           transport_cost=predicted_transport_cost, 
                           equipment_cost=predicted_equipment_cost)





material_model_4 = joblib.load("material_model_4.pkl")
transport_model_4 = joblib.load("transport_model_4.pkl")
labour_model_4 = joblib.load("labour_model_4.pkl")
water_model_4 = joblib.load("water_model_4.pkl")
scaler_4 = joblib.load("scaler_4.pkl")

@app.route("/PCC",methods=["GET","POST"])
def PCC():
    predicted_material_cost = None
    predicted_transport_cost = None
    predicted_labour_cost = None
    predicted_water_cost = None

    if request.method == "POST":
        try:
            # Get user input
            length = float(request.form["length"])
            width = float(request.form["width"])
            height = float(request.form["height"])

            # Prepare input
            user_input = np.array([[length, width, height]])
            user_input_scaled = scaler_4.transform(user_input)

            # Predict costs
            predicted_material_cost = material_model_4.predict(user_input_scaled)[0]
            predicted_transport_cost = transport_model_4.predict(user_input_scaled)[0]
            predicted_labour_cost = labour_model_4.predict(user_input_scaled)[0]
            predicted_water_cost = water_model_4.predict(user_input_scaled)[0]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("PCC.html", 
                           material_cost=predicted_material_cost, 
                           transport_cost=predicted_transport_cost, 
                           labour_cost=predicted_labour_cost,
                           water_cost=predicted_labour_cost)

    

material_model_5 = joblib.load("material_model_5.pkl")
labour_model_5 = joblib.load("labour_model_5.pkl")
water_model_5 = joblib.load("water_model_5.pkl")
scaler_5 = joblib.load("scaler_5.pkl")

@app.route("/footing",methods=["GET","POST"])
def footing():
    predicted_material_cost = None
    predicted_labour_cost = None
    predicted_water_cost = None

    if request.method == "POST":
        try:
            # Get user input
            length = float(request.form["length"])
            width = float(request.form["width"])
            height = float(request.form["height"])

            # Prepare input
            user_input = np.array([[length, width, height]])
            user_input_scaled = scaler_5.transform(user_input)

            # Predict costs
            predicted_material_cost = material_model_5.predict(user_input_scaled)[0]
            predicted_labour_cost = labour_model_5.predict(user_input_scaled)[0]
            predicted_water_cost = water_model_5.predict(user_input_scaled)[0]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("footing.html", 
                           material_cost=predicted_material_cost, 
                           labour_cost=predicted_labour_cost,
                           water_cost=predicted_labour_cost)
    

material_model_6 = joblib.load("material_model_6.pkl")
labour_model_6 = joblib.load("labour_model_6.pkl")
water_model_6 = joblib.load("water_model_6.pkl")
scaler_6 = joblib.load("scaler_6.pkl")

@app.route("/pedestrial",methods=["GET","POST"])
def pedestrial():
    predicted_material_cost = None
    predicted_labour_cost = None
    predicted_water_cost = None

    if request.method == "POST":
        try:
            # Get user input
            length = float(request.form["length"])
            width = float(request.form["width"])
            height = float(request.form["height"])

            # Prepare input
            user_input = np.array([[length, width, height]])
            user_input_scaled = scaler_6.transform(user_input)

            # Predict costs
            predicted_material_cost = material_model_6.predict(user_input_scaled)[0]
            predicted_labour_cost = labour_model_6.predict(user_input_scaled)[0]
            predicted_water_cost = water_model_6.predict(user_input_scaled)[0]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("pedestrial.html", 
                           material_cost=predicted_material_cost, 
                           labour_cost=predicted_labour_cost,
                           water_cost=predicted_labour_cost)
    

if __name__ == "__main__":
    app.run(debug=True)
