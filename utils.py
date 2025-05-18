# utils.py
import xml.etree.ElementTree as ET

def convert_quotepro_to_acord(data):
    acord = ET.Element("ACORD")
    insurance = ET.SubElement(acord, "Insurance")

    policy_number = ET.SubElement(insurance, "PolicyNumber")
    policy_number.text = data.get("policyNumber", "N/A")

    customer = data.get("customer", {})
    name = ET.SubElement(insurance, "CustomerName")
    name.text = customer.get("name", "N/A")

    email = ET.SubElement(insurance, "CustomerEmail")
    email.text = customer.get("email", "N/A")

    return ET.tostring(acord, encoding="utf-8", method="xml")
