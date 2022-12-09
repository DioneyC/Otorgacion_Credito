from flask import Flask, request, render_template, jsonify 
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
import numpy as np

def conexion(nom, apepat, apemat, fecnac, RFC, ingmens, numdep, estado): 
    data = [nom, apepat, apemat, fecnac, RFC, ingmens,numdep,estado]
    
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="localhost",
                                    port="5432",
                                    dbname="credito")
    
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO ESTATUS(PRIMER_NOMBRE, APELLIDO_PAT, APELLIDO_MAT, FECHA_NAC, RFC, INGRESOS_MENSUALES, DEPENDIENTES, APROBADO) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', data)  
        connection.commit()
        
        sql = 'SELECT IDU, RFC, APROBADO FROM ESTATUS'
        data = sqlio.read_sql_query(sql, connection)

        last = len(data)
        ultimo = data.tail(1)

        ID = int(ultimo["idu"].values)
        RFC = ultimo["rfc"].values
        ESTATUS = ultimo["aprobado"].values

        #dat = {"ID":ID, "RFC":RFC[0], "ESTATUS":ESTATUS[0]}
        
        dat = f'ID: {ID} \n RFC: {RFC[0]} \n ESTADO: {ESTATUS[0]}'
        
        return dat
    
    except: 
    
        return "TODOMAL("

app = Flask(__name__)

@app.route("/home")
def home(): 
    
    return render_template('main3.html')

@app.route("/info", methods = ['GET', 'POST'])
def getinfo(): 
    data = request.get_json() 
    
    nom = data["nombre"].upper() 
    apepat = data["apepat"].upper()
    apemat = data["apemat"].upper()
    fecnac = data["fecnac"]
    ingmens = float(data["ingmens"])
    numdep = int(data["depec"])
    estado = ""
    ID = 1
    
    if ingmens > 25000.00:
        estado = "Aprobado"
    
    elif ingmens >= 15000.00 and ingmens <= 25000.00:
        if numdep < 3: 
            estado = "Aprobado"
        else: 
            estado = "Rechazado"
    else: 
        estado = "Rechazado"

    RFC = apepat[:2]+apemat[:1]+nom[:1]+fecnac[2:4]+fecnac.split("-")[1]+fecnac.split("-")[2]
    
    respuesta = conexion(nom, apepat, apemat, fecnac, RFC, ingmens, numdep, estado)

    return jsonify(respuesta)  #{"ID":ID, "Estado":estado, "RFC":RFC, "INGMENS":ingmens}


# ingresar data a una BD 


if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000)

