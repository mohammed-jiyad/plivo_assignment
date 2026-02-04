# 📞 Plivo Multi-Level IVR System

A Python Flask-based Interactive Voice Response (IVR) system built with the Plivo Voice API. This application handles two-level IVR menus with language selection, call routing, and call transfer capabilities.

## ✨ Features

- ✅ **Outbound Call Triggering** - Initiate calls from a web interface
- ✅ **Multi-Level IVR Menus** - Two-level menu system for user interaction
- ✅ **Language Selection** - Support for multiple languages (English/Spanish)
- ✅ **Audio Playback** - Play messages to callers
- ✅ **Call Transfer** - Route calls to associates
- ✅ **Self-Transfer Protection** - Prevent calling the same number
- ✅ **Call Status Tracking** - Monitor call status and hangup causes
- ✅ **Web UI** - Simple HTML interface to initiate calls

## 🏗️ Project Structure

```
Plivo Project/
├── app.py                          # Main Flask application with routes
├── config.py                       # Configuration and Plivo credentials
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
│
├── services/
│   └── call_service.py            # Outbound call initiation logic
│
├── ivr_flows/
│   ├── level1.py                  # Level 1 menu (language selection)
│   ├── level2.py                  # Level 2 menu (action selection)
│   └── action_handler.py          # Final action (audio/transfer)
│
├── utils/
│   └── helpers.py                 # Utility functions (phone validation)
│
└── templates/
    └── index.html                 # Web UI for call initiation
```

## 📋 Prerequisites

- Python 3.8+
- Plivo Account with API credentials
- ngrok (for local tunneling)

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd "Plivo Project"
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** with your Plivo credentials:

```env
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=your_plivo_phone_number
ASSOCIATE_NUMBER=associate_phone_number
BASE_URL=https://your-ngrok-url.ngrok.io
```

## 🚀 Running the Application

### Start the Flask Server

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Expose to the Internet with ngrok

In another terminal:

```bash
ngrok http 5000
```

Update the `BASE_URL` in your `.env` file with the ngrok URL provided.

## 📞 IVR Flow

### Step 1: Outbound Call

- User enters a phone number in the web UI
- System triggers an outbound call via Plivo

### Step 2: Level 1 Menu (Language Selection)

- Caller selects language (English/Spanish)
- System registers the selection

### Step 3: Level 2 Menu (Action Selection)

- Caller chooses to hear a message or connect to an associate
- System routes accordingly

### Step 4: Final Action

- **Audio Option:** Play a recorded message
- **Transfer Option:** Route call to associate (with self-transfer protection)

## 🔌 API Endpoints

| Endpoint       | Method   | Description                           |
| -------------- | -------- | ------------------------------------- |
| `/`            | GET      | Home page with call initiation form   |
| `/call`        | POST     | Trigger outbound call                 |
| `/answer`      | GET/POST | Level 1 IVR (language selection)      |
| `/level2`      | POST     | Level 2 IVR (action selection)        |
| `/action`      | GET/POST | Execute final action (audio/transfer) |
| `/dial_status` | POST     | Webhook for call status updates       |

## 📦 Dependencies

```
Flask==3.0.0          # Web framework
plivo==4.44.0         # Plivo Voice API SDK
python-dotenv==1.0.1  # Environment variable management
gunicorn==21.2.0      # WSGI server for production
```

## 🔐 Configuration (config.py)

The following environment variables are required:

- `PLIVO_AUTH_ID` - Your Plivo authentication ID
- `PLIVO_AUTH_TOKEN` - Your Plivo authentication token
- `PLIVO_PHONE_NUMBER` - Your Plivo virtual number
- `ASSOCIATE_NUMBER` - Associate number for call transfers
- `BASE_URL` - Your public URL (ngrok or domain)

## 🛠️ Development

### Running Tests

```bash
# Add your test commands here
```

### Building for Production

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📝 License

MIT

## 🤝 Support

For issues or questions, please create an issue in the repository.

---

**Note:** This project uses Plivo's Voice API. Ensure you have sufficient account credits before testing.
