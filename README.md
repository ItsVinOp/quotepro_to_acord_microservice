🚀 QuotePro → ACORD XML Microservice
A Python-based microservice that converts QuotePro JSON data into ACORD-compliant XML and returns it embedded inside a JSON structure required by ITC.

🧠 Use Case
This service is ideal for insurance or CRM platforms where:

Frontend or CRM (like Zoho) sends data in QuotePro JSON format.

ITC or legacy backend systems require ACORD XML inside JSON payload.

📦 Features

Convert QuotePro JSON to ACORD XML

Embed XML inside JSON for ITC

Flask-based microservice (easy to deploy)

Basic error handling and logging

Easily testable via Postman or curl

🛠️ Tech Stack

Python 3

Flask

XML.etree (standard library for XML generation)

Postman / curl for API testing

📂 Project Structure

project/
├── main.py # Flask app
└── README.md # Project documentation

⚙️ How to Run

Clone the Repository
git clone https://github.com/your-username/quotepro-acord-microservice.git
cd quotepro-acord-microservice

Install Requirements
pip install flask

Run the Server
python main.py

📮 How to Use

Endpoint:
POST http://localhost:5000/convert

Headers:
Content-Type: application/json

Sample Request Body:
{
"policy_number": "QP-98765",
"customer": {
"name": "John Doe",
"email": "john@example.com"
}
}

Sample Response:
{
"payload": "<ACORD><Insurance><PolicyNumber>QP-98765</PolicyNumber><CustomerName>John Doe</CustomerName><CustomerEmail>john@example.com</CustomerEmail></Insurance></ACORD>",
"type": "acord-xml"
}

🧪 Testing

Use Postman or curl:

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
LinkedIn: https://www.linkedin.com/in/your-link
GitHub: https://github.com/your-username

