# 🔐 OTP Generator & Verifier

A secure and lightweight Python application built with Streamlit that generates and verifies One-Time Passwords (OTP) via Gmail SMTP. Perfect for adding an authentication layer to your projects or learning about email-based verification systems!

## ✨ Features

- 🔒 **Secure OTP Generation** - Uses Python's `secrets` module for cryptographically strong random 6-digit codes
- 📧 **Email Delivery** - Sends OTPs via Gmail SMTP with customizable message templates
- ⏱️ **Time-Based Expiration** - OTPs automatically expire after 5 minutes
- 🛡️ **Rate Limiting** - Maximum 3 verification attempts per OTP
- 🎨 **Modern UI** - Built with Streamlit for an interactive web interface
- ⚙️ **Configurable** - Easy customization through `Config.ini` file
- 🔑 **Secure Password Management** - Supports `.env` file for automatic password fetching
- ❌ **Error Handling** - Comprehensive error checking and user-friendly messages

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Gmail account with App Password enabled

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/xXParm06Xx/otp-via-streamlit.git
cd otp-via-streamlit
```

2. **Install dependencies:**

Choose one of the following methods:

**Option A: Using pip (Standard)**
```bash
pip install -r requirements.txt
```

**Option B: Using uv**
```bash
pip install uv
uv sync
```

3. **Set up your Gmail App Password:**

To get a Google App Password:
- Go to your [Google Account](https://myaccount.google.com/)
- Search for "App passwords"
- Create a new app password
- Copy the 16-character password

4. **Configure environment variables (Optional but Recommended):**

Create a `.env` file in the project root:
```bash
touch .env
```

Add your app password to `.env`:
```
MY_PASS = "Paste_Your_App_16_Character_App_Password_Here"
```

⚠️ **Important:** Add `.env` to your `.gitignore` file to keep your password secure!

5. **Customize email settings (Optional):**

Edit `Config.ini` to customize your email template:
```ini
[EMAIL]
smtp_server = smtp.gmail.com
smtp_port = 587
subject = Your OTP Verification Code
message = Hello,

    Your One-Time Password (OTP) for Verification is : {otp}

    This code will expire in 5 minutes.
    Please do not share it with anyone for security reasons.

    Thanks
```

## 🎮 Usage

1. **Run the application:**
```bash
streamlit run main.py
```

2. **In the sidebar:**
   - Enter your name
   - Enter your email (sender's email)
   - Your password will be auto-fetched from `.env`, or manually enter your App Password

3. **Send an OTP:**
   - Enter the receiver's email address
   - Click "📩 Send OTP"
   - The receiver will get a 6-digit OTP via email

4. **Verify the OTP:**
   - Enter the OTP received
   - Click "Verify OTP"
   - You have 3 attempts within 5 minutes

## 📁 Project Structure

```
otp-via-streamlit/
│
├── main.py              # Main application file
├── Config.ini           # Email configuration file
├── .env                 # Environment variables (create this)
├── .env_example         # Template for .env file (if made manually, rename it to .env)
├── requirements.txt     # Python dependencies
├── uv.lock             # UV environment lock file
└── README.md           # You are here!
```

## 🛠️ How It Works

### OTP Generation
1. User enters sender and receiver email addresses
2. System generates a secure 6-digit OTP using `secrets.randbelow()`
3. OTP is stored in session state with a timestamp

### Email Delivery
1. Message template is loaded from `Config.ini`
2. OTP is inserted into the template
3. Email is sent via Gmail SMTP with TLS encryption

### Verification Process
1. User enters the OTP received via email
2. System checks:
   - Has the OTP expired? (5-minute window)
   - Does the entered OTP match?
   - Have attempts been exceeded? (3 maximum)
3. Appropriate feedback is displayed

## 📋 Requirements

```
streamlit
python-dotenv
```

Install with:
```bash
pip install streamlit python-dotenv
```

## 🔒 Security Features

- **Secure Random Generation**: Uses `secrets` module instead of `random`
- **Time-Limited OTPs**: Automatic expiration after 5 minutes
- **Rate Limiting**: Maximum 3 verification attempts
- **TLS Encryption**: All emails sent over secure SMTP connection
- **Session State**: OTPs stored securely in Streamlit session
- **Environment Variables**: Passwords never hardcoded in source

## 🎯 Use Cases

- 🔐 **Authentication Prototypes** - Test email-based 2FA systems
- 📚 **Learning Projects** - Understand SMTP, Streamlit, and OTP workflows
- 🧪 **Small Applications** - Add quick email verification to personal projects
- 🎓 **Educational Purposes** - Learn about secure password handling and session management

## ⚠️ Important Notes

- This project is for **educational purposes** and small-scale use
- For production applications, consider:
  - Using dedicated email services (SendGrid, AWS SES, etc.)
  - Implementing database storage for OTPs
  - Adding more robust rate limiting
  - Implementing proper logging and monitoring
  - Adding CAPTCHA to prevent abuse
  - Using more secure authentication methods

## 🐛 Troubleshooting

### "Config Error" Message
- Ensure `Config.ini` exists in the project directory
- Verify the `[EMAIL]` section is present and properly formatted

### "OTP failed to send" Error
- Check your Gmail App Password is correct
- Ensure you're using an App Password, not your regular Gmail password
- Verify your internet connection
- Check if Gmail SMTP is accessible from your network

### "Password not fetched" Warning
- Create a `.env` file in the project root
- Add `MY_PASS=your_app_password`
- Restart the Streamlit application

### OTP Not Received
- Check spam/junk folder
- Verify the receiver's email address is correct
- Ensure sender email has SMTP access enabled

## 💡 Future Enhancements

- [ ] Database integration for OTP history
- [ ] Multiple OTP delivery methods (SMS, WhatsApp)
- [ ] Admin dashboard for monitoring
- [ ] Custom OTP length configuration
- [ ] Email templates with HTML formatting
- [ ] Multi-language support
- [ ] QR code generation for OTP
- [ ] Export verification logs

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Parminder Singh**
- GitHub: [@xXParm06Xx](https://github.com/xXParm06Xx)

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Python smtplib for email functionality
- Google for Gmail SMTP services

---

**Made with ❤️ by Parm**

If you find this project helpful, consider giving it a ⭐!

## 📞 Support

Having issues? Feel free to:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

---

**⚡ Quick Start Command:**
```bash
pip install streamlit python-dotenv && streamlit run main.py
```