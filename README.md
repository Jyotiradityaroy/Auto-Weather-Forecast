# 🌦 Auto Weather Forecast API (Kolkata)

A Flask-based backend API that automatically generates daily weather forecasts for **Kolkata**, stores forecast data in **MongoDB**, and sends automated email updates every day at **8:00 AM**.

This project demonstrates backend API design, database integration, scheduling systems, and automated email workflows.

---

## 🚀 Tech Stack

- **Flask** – REST API Framework  
- **MongoDB** – NoSQL Database  
- **APScheduler** – Automated Daily Scheduling  
- **Open-Meteo API** – Weather Data Provider  
- **Gmail SMTP** – Email Delivery  
- **Python 3.x**

---

## 📁 Project Structure

```
Auto-Weather-Forecast/
│
├── backend/
│   ├── app.py              # Main Flask application
│   ├── db.py               # MongoDB connection
│   ├── forecast.py         # Weather forecast logic
│   ├── email_utils.py      # Email sending functionality
│   ├── scheduler.py        # Daily automated email scheduler
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables (NOT pushed to GitHub)
```

---

## 📌 Features

- 📍 Fixed location: Kolkata (22.5726, 88.3639)
- 📊 7-day weather forecast generation
- 💾 Forecast data stored in MongoDB
- 📧 Manual email configuration via API
- ⏰ Automatic daily email at 8:00 AM
- 🔄 Manual forecast trigger endpoint
- 🧩 Modular backend structure
- 🛠 Clean API design

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jyotiradityaroy/Auto-Weather-Forecast.git
cd Auto-Weather-Forecast/backend
```

---

### 2️⃣ Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Inside the `backend/` folder, create a file named `.env`:

```
MONGO_URI=your_mongodb_connection_string
EMAIL=yourgmail@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

⚠️ IMPORTANT:

- Use a **Gmail App Password**
- Do NOT use your actual Gmail password
- Do NOT upload `.env` to GitHub

---

### 5️⃣ Run the Application

```bash
python app.py
```

Server will start at:

```
http://localhost:5000
```

---

## 🧪 API Endpoints

---

### 🔹 Health Check

```
GET /
```

Response:

```json
{
  "status": "Weather API Running"
}
```

---

### 🔹 Set Email Recipient

```
POST /set-email
```

Request Body:

```json
{
  "email": "yourmail@gmail.com"
}
```

Response:

```json
{
  "message": "Recipient email set successfully"
}
```

---

### 🔹 Manually Generate Forecast

```
GET /generate-forecast
```

This will:
- Fetch latest 7-day forecast
- Store forecast data in MongoDB
- Send email immediately

---

## ⏰ Automatic Daily Email

The system automatically sends weather updates every day at:

```
8:00 AM (Server Time)
```

This is handled using **APScheduler**.

⚠️ Note: The backend must remain running for scheduled emails to work.

---

## 🗄 MongoDB Structure

**Database:** `weather_app`  
**Collection:** `forecast_data`

### Example Forecast Document

```json
{
  "date_generated": "2026-03-01",
  "forecast": [
    { "date": "2026-03-01", "avg_temp": 28.5 },
    { "date": "2026-03-02", "avg_temp": 29.1 }
  ]
}
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| MONGO_URI | MongoDB connection string |
| EMAIL | Gmail address |
| EMAIL_PASSWORD | Gmail App Password |

---

## 🌍 Deployment

This project can be deployed on:

- Render
- Railway
- AWS EC2
- DigitalOcean
- Any VPS

Make sure to:
- Set environment variables in the hosting platform
- Keep the server running for the scheduler to work

---

## 🔮 Future Improvements

- Multiple recipient support
- HTML email templates
- Docker containerization
- Logging system
- Admin authentication
- Unsubscribe endpoint
- Production-grade scheduling (Celery)

---

## 👨‍💻 Author

**Jyotiraditya Roy**  
Computer Science & AI Enthusiast  

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
