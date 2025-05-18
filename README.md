## 🚀 QuotePro → ACORD XML Microservice

A Python-based microservice that converts QuotePro JSON data into ACORD-compliant XML and returns it embedded inside a JSON structure required by ITC.

---

### 🧠 Use Case

This service is ideal for insurance or CRM platforms where:
- Frontend or CRM (like Zoho) sends data in **QuotePro JSON** format.
- ITC or legacy backend systems require **ACORD XML** inside JSON payload.

---

### 📦 Features

✅ Convert QuotePro JSON to ACORD XML  
✅ Embed XML inside JSON for ITC  
✅ Flask-based microservice (easy to deploy)  
✅ Basic error handling & logging  
✅ Easily testable via Postman or curl

---

### 🛠️ Tech Stack

- Python 3
- Flask
- XML.etree for XML generation
- Postman/curl for testing

---

### 📂 Project Structure

project/
├── main.py # Flask app
└── README.md # This file

yaml
Copy
Edit

---

### ⚙️ How to Run

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quotepro-acord-microservice.git
cd quotepro-acord-microservice
2. Install Requirements
bash
Copy
Edit
pip install flask
3. Run the Server
bash
Copy
Edit
python main.py
📮 How to Use
Endpoint
bash
Copy
Edit
POST http://localhost:5000/convert
Headers
pgsql
Copy
Edit
Content-Type: application/json
Sample Request Body
json
Copy
Edit
{
  "policy_number": "QP-98765",
  "customer": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
Sample Response
json
Copy
Edit
{
  "payload": "<ACORD><Insurance><PolicyNumber>QP-98765</PolicyNumber><CustomerName>John Doe</CustomerName><CustomerEmail>john@example.com</CustomerEmail></Insurance></ACORD>",
  "type": "acord-xml"
}
🧪 Testing
Use Postman or curl:

bash
Copy
Edit
curl -X POST http://localhost:5000/convert \
-H "Content-Type: application/json" \
-d '{
  "policy_number": "QP-12345",
  "customer": {
    "name": "Alice",
    "email": "alice@example.com"
  }
}'
📌 Future Improvements
Add authentication for secure access

Expand XML structure for full ACORD compliance

Integrate with Zoho CRM triggers

Add automated unit tests

👨‍💻 Author
Vinayak Shirke
LinkedIn
GitHub