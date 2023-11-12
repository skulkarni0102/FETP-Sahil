# FETP Sahil

This is an assessment of Google authentication and pattern printing.

## Installation

you can get your google credential [here](https://console.cloud.google.com/apis/credentials) and in Authorized redirect URIs add -> https://127.0.0.1:5000/login/callback

```bash
python -m venv <virtual-environment-name>
.\env\Scripts\activate
set GOOGLE_CLIENT_ID="Your Client ID"
set GOOGLE_CLIENT_SECRET="Your Client SECRET"
python app.py
```

## Instead of setting environment variable

In app.py you can change the variable to your credentials

```python
CLIENT_ID = "GOOGLE_CLIENT_ID"
CLIENT_SECRET = "GOOGLE_CLIENT_SECRET"
```

## Screenshots

![Image](https://github.com/skulkarni0102/FETP-Sahil/blob/main/Screenshots/ss1.png)

##
![Image](https://github.com/skulkarni0102/FETP-Sahil/blob/main/Screenshots/ss2.png)

##
![Image](https://github.com/skulkarni0102/FETP-Sahil/blob/main/Screenshots/ss3.png)
