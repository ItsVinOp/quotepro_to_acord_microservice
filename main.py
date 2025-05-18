from flask import Flask, request, jsonify
from xml.etree.ElementTree import Element, SubElement, tostring
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)

def convert_to_acord_xml(data):
    insurance = Element("Insurance")

    policy = SubElement(insurance, "PolicyNumber")
    policy.text = data.get("policy_number", "N/A")

    name = SubElement(insurance, "CustomerName")
    name.text = data.get("customer", {}).get("name", "N/A")

    email = SubElement(insurance, "CustomerEmail")
    email.text = data.get("customer", {}).get("email", "N/A")

    acord = Element("ACORD")
    acord.append(insurance)

    return tostring(acord, encoding="unicode")

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return '''
        <h2>QuotePro → ACORD XML Microservice</h2>
        <p>Use <code>POST</code> method with JSON body to convert QuotePro JSON to ACORD XML.</p>
        <p>POST here: <code>/convert</code></p>
        '''

    try:
        data = request.get_json()
        xml_data = convert_to_acord_xml(data)
        response = {
            "payload": xml_data,
            "type": "acord-xml"
        }
        return jsonify(response)

    except Exception as e:
        logging.error("Error in conversion", exc_info=True)
        return jsonify({"error": "Invalid input or internal error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
