import base64

import cv2
import flet as tf
import threading
import time

class RegisterApp:
    def __init__(self,camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)
        self.running = False
        self.current_frame = None

    def start_stream(self):
        self.running = True
        def stream():
            while self.running:
                ret,frame = self.cap.read()
                if ret:
                    _,buffer = cv2.imencode('.png', frame)
                    self.current_frame = base64.b64encode(buffer).decode('utf-8')
                else:
                    self.current_frame = None
                time.sleep(0.03)
        threading.Thread(target=stream, daemon=True).start()


    def stop_stream(self):
        self.running = False
        self.cap.release()

    def run_ui(self):
        def main(page: tf.Page):
            page.title = "Attendance System"
            image = tf.Image()
            page.add(image)

            def update_image():
                while self.running:
                    if self.current_frame:
                        image.src_base64 = self.current_frame
                        page.update()
                    time.sleep(0.03)#30fps
            threading.Thread(target=update_image, daemon=True).start()

            def stop_streaming(e):
                self.stop_stream()
                page.add(tf.Text("Streaming detenido",color='red'))
                page.update()
            page.add(tf.Button("Stop Streaming",on_click=stop_streaming))
        self.start_stream()
        tf.app(target=main)


if __name__=="__main__":
    app = RegisterApp()
    try:
        app.run_ui()
    finally:
        app.stop_stream()