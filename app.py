from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "paises.csv")

def cargar_paises():
    paises = []
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                poblacion = int(row.get("poblacion", "") or 0)
            except ValueError:
                poblacion = None
            try:
                superficie = int(row.get("superficie", "") or 0)
            except ValueError:
                superficie = None

            pais = {
                "pais": row.get("pais", "").strip(),
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": row.get("continente", "").strip()
            }
            paises.append(pais)
    return paises

PAISES = cargar_paises()

@app.route("/paises", methods=["GET"])
def get_all_paises():
    return jsonify(PAISES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
