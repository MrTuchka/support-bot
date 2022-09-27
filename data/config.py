from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
WEBHOOK_URL = env.str("WEBHOOK_URL")

dp_api = {
  "type": "service_account",
  "project_id": "support-bot-8eaa0",
  "private_key_id": "c67d44557723ad0b6bf55fadbb93709052c03ebc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDaBczL0F/WiXM1\naQHt9dTwcPw1xVRQmNnV8rOApt9QUKzlaIElQPzJZYDQ+f+8esiZNu3PB7EzT0R9\nZWTQXNQ4s9C/EFmyyrlOoIF32/Y1/RNIyvTwMF7m3yNPeuM6/SkIUuCT04e7lT/0\nIlDHzDCr3TTiF+70mG1vRt0cb9j2/45okmehMEnfwi+VFbbPFq/wMACWonwpVyOl\npHhjSowOXZhMsZMNvUiepbDV/SM4IgEuo8y9oBmN0ao3cuMcLBItDPNUJoYSoHgi\nHNNH3HESGcQd3UEJVWJBJuyaOuWYht9FDXXV7+uDB+nBGsz9xB5Zocyy5wp4FYwM\ntLoR7b2nAgMBAAECggEACqRj1cMLGo7FB+NjS7lHNqFdPkaukeyUHYRmTK5YkjQN\n7HjIbQgaDr6cpha96/ZWWlw7CXMHrEh/QFu1qxIM7eOhGeJzbm3E09iz2STshMAg\ns9nsUNkbmMtljtihxNxcp2JcQfr+UiK752/RX59Q9OKsVSjz6g6SsO7VljDDd3L0\n8O6ndqkqCevB7VzpnxDp1WyVATKFRK7C9v7Mf1cq4EZMqY0X+8uuwacuo1cj2KRG\no/Sf8CgglwErUIfOIjEGWvVqCIYIB0tQh+sOpY8XTtmt89Pa/GjGvugyw5I376Gt\nptv+hW814oCvpcW+h5PWbq6h715NTR59fSbU+LLBQQKBgQDuhVrljc5j1xIK8yEd\n+oXFM7h8I8Uf59DsWyJwXU60ZpwN8m17QchT5xWAIZwhaH4IIQEe6xMcPGKUHFbx\nIgupDYRbhRHDYMJBCeIdUXimNNEKkzjNPGEOIUUaej/PsonBEZW0J+1EsA3MsW5B\nYrt18YS0Vt0XzbozU0d3g9IxIQKBgQDp/+XuUwg27rI8Y/Lq8A1IqJZfai4Rfw+l\nqjycN/I42a11jtyoaScWYXYULIOkmXQs5BTNnCDlYUxUeCstRp4qi4F4ryVcjoyv\nCJPQPcsJDGt4rkTWXsdsE82FUcH8s9gLMSznGN1+mDFmFl1gXckJg/UIg7ZZJM/Q\neGu6yk7txwKBgQDVdK5l5MQhgWV6Ox8WDw8L7j9ZiUFuTi0geGaXnElFFNbvfFcS\nCUrYG2OYaXuqQjMX30F7g/B0Qm4OElaUMV2yCpC6vpmo+byeK9QZXMHWLEovZpVc\nxn4tAQUwrtrQavzwtWX99gVWhR+0Yc1D4rHU2TFjmqD+HnRWXl8EzAmdQQKBgQDI\nMbOAqy76+Eoq2oPoNgnXYMyNwyS4uVEktbl3GXI06x641cm4l4XmYumHpvHVb6fy\nBAw8QFfwhsar+cdOy/zjf0j8fDPltNttoFP9s/AxxJtpuwaPtLS+pU6OwfzJ+v9Z\ny++TozVUalbQ9U9b88DcUDXh2/W03Iai33OjchQG3wKBgFri+RleRawiMXUslhOh\np4PWmEjs+TjP7/8Lm/FgDZAg9TPV7DFbrjrHu/iW1OYTpzr9pnrFxZmVsrhop49d\n8wcOXcHliu7nSCCJsrautwYhSJXYn1LXQYFfJydJO87w29tBzebqont4szuCx3kO\nHednxj7kISQy+J09BCH/aFt/\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-rgam6@support-bot-8eaa0.iam.gserviceaccount.com",
  "client_id": "108342786303015142481",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rgam6%40support-bot-8eaa0.iam.gserviceaccount.com"
}