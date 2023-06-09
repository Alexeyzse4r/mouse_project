from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import pyautogui
import socket
import random
from plyer import accelerometer
from kivy.clock import Clock


Builder.load_string("""
<Label>
    font_size: 40
<Offset>:
    canvas:
        Rectangle:
            source:"pics/background.png"
            pos: self.pos
            size: self.size

<RoundedButton@Button>
    background_color: (0,0,0,0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (46/255,46/255,46/255,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [50]

<MainWindow>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            source: 'pics/background.png'
            pos: self.pos
            size: self.size
    name: "main"
    ip: ip
    GridLayout:
        cols: 1
        rows: 5
        spacing: 10
        padding: 25, 50
        Label:
            multiline: True
            color: (0,0,0,1)
            bold: True
            italic: True
            pos_hint: {'center_x': 0.5}
            size: 270, 50
        GridLayout:
            cols: 1
            spacing: 10
            padding: 30, 60, 10, 30
            GridLayout:
                cols: 2
                size_hint_x: self.parent.width*0.04
                size_hint_y: self.parent.height*0.0004
                Label:
                    text: "IP: "
                    bold: True
                    italic: True
                    color: 1,1,1,1
                    font_hint: 82
                    size_hint: 0.02,0.002
                    color: (1,1,1,1)

                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                TextInput:
                    id: ip
                    on_text: self.foreground_color = (1,1,1,1)
                    on_text: self.foreground_bold = True
                    on_text: self.foreground_font_size = 80
                    font_size: 40
                    cursor_color: (185/255, 240/255, 41/255, 1)
                    color: 1,1,1,1
                    size_hint: 0.04,0.00004
                    multiline: True
                    background_color: (46/255,46/255,46/255,0.5)
        RoundedButton:
            text: "Enter"
            font_hint: 32
            bold: True
            italic: True
            size_hint: 0.5, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_press: root.btn()

        RoundedButton:
            text: "Touchpad"
            font_hint: 32
            bold: True
            italic: True
            size_hint: 0.5, 0.5
            radius: [70]
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release:
                app.root.current = "touchpad"
                root.manager.transition.direction = "left"

        RoundedButton:
            text: "Mouse"
            font_hint: 32
            bold: True
            italic: True
            size_hint: 0.5, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release:
                app.root.current = "mouse"
                root.manager.transition.direction = "right"

<TouchPadWindow>
    name: "touchpad"
    btn: btn
    Button:
        id: btn
        text: "Menu"
        font_hint: 32
        bold: True
        italic: True
        pos_hint: {'center_x': 0.5,'top': 1}
        size_hint: 1,0.1
        color: (185/255, 240/255, 41/255, 1)
        background_color: (46/255,46/255, 46/255, 1)
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

<MouseWindow>:
    name: "mouse"
    GridLayout:
        cols: 1
        size: root.width, root.height
        Button:
            text: "Menu"
            color: (185/255, 240/255, 41/255, 1)
            font_hint: 32
            bold: True
            italic: True
            pos_hint: {'center_x': 0.5,'top': 1}
            size_hint: 1,0.3
            background_color: (46/255,46/255,46/255,1)
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "left"

        Label:
            text: " "
        GridLayout:
            cols: 3
            spacing: 10
            padding: 10
            Button:
                text:"Right"
                color: (46/255,46/255, 46/255, 1)
                font_hint: 32
                italic: True
                bold: True
                size_hint:0.3,.3
                background_color: (185/255,240/255,41/255,1)
                background_normal: ''
                on_press: root.leftbtn()

            GridLayout:
                cols: 1
                rows: 2
                spacing: 5
                padding: 5
                size_hint: 0.3, 0.3
                Button:
                    text: 'UP'
                    color: (185/255, 240/255, 41/255, 1)
                    background_color: (46/255,46/255, 46/255, 1)
                    font_hint: 32
                    italic: True
                    bold: True
                    size_hint:0.3,.5
                    on_press: root.scrol(20)

                Button:
                    text: "DW"
                    color: (185/255, 240/255, 41/255, 1)
                    background_color: (46/255,46/255, 46/255, 1)
                    font_hint: 32
                    italic: True
                    bold: True
                    size_hint: 0.3,.5
                    on_press: root.scrol(-20)

            Button:
                text:"Right"
                color: (46/255,46/255, 46/255, 1)
                font_hint: 32
                italic: True
                bold: True
                #size: 150,100
                size_hint:0.3,.3
                background_color: (185/255,240/255,41/255,1)
                background_normal: ''
                on_press: root.rightbtn()

        Label:
            text: " "
""")

# Declare both screens
class MainWindow(Screen):
    ip = ObjectProperty(None)

    def btn(self):
        iP = self.ip.text
        print("Ip: ", iP)
        connection(iP)
        # self.ip.text = ""

arr=[]
def send_data(host, port, x, y):
    arr = [2]
    arr[0] = x
    arr[1] = y
    # Создаем объект сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключаемся к хосту и порту
    sock.connect((host, port))
    # Кодируем данные в байты и отправляем их
    sock.sendall(bytes(arr, 'utf-8'))
    # Закрываем соединение
    sock.close()

def connection(ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.connect(("192.168.0.179", 1234))
    client.connect((ip, 1234))
    while True:
        client.send(input().encode("utf-8")) #сюда вместо инпута вставить отправку touch.pos
        print()

class MouseWindow(Screen):
    def leftbtn(self):
        print("left")
        print(f"{random.uniform(0,1000)} {random.uniform(0,1000)}")

    def rightbtn(self):
        print("right")
        print(f"{random.uniform(0, 1000)} {random.uniform(0, 1000)}")

    def scrol(self, cur):
        pyautogui.vscroll(cur)
        print("scrol ", cur)

    def acceler(self):
        try:
            accelerometer.enable()  # enable the accelerometer
            Clock.shedule_interval(self.update, 1.0 / 10)
        except:
            self.display.text = "Failed to start accelerometr\n"

    def update(self, dt):
        self.position_status = \
            'Telephone is in ' \
            '{}\n'.format('static' if self.check_static() else 'hand')
        try:
            x, y, z = accelerometer.acceleration[0], \
                      accelerometer.acceleration[1], \
                      accelerometer.acceleration[2]
            self.results['X'].append(x)
            self.results['Y'].append(y)
            self.results['Z'].append(z)
            self.results['time'].append(self.get_time())
            text = "Accelerometer:\n" \
                   "X = %.2f\n" \
                   "Y = %.2f\n" \
                   "Z = %.2f\n" % (x, y, z)
        except:
            text = "Cannot read accelerometer!\n"
        self.display.text = self.position_status + "\n" + \
                            text + "\n" + \
                            self.restart_status + \
                            self.save_status

'''
def accel():
    droid = android.Android()
    dt = 100  # 100ms between sensings
    endTime = 30000  # sample for 3000ms
    timeSensed = 0
    droid.startSensingTimed(2, dt)
    while timeSensed <= endTime:
        print(droid.sensorsReadAccelerometer().result)
        time.sleep(dt / 1000.0)
        timeSensed += dt
    droid.stopSensing()

def send_port(self, x, y):
    arr = [2]
    arr[0] = x
    arr[1] = y
    ser = Serial(port='COM4', baudrate=115200, timeout=0.1)
    ser.open()
    self.write(ser, arr)
    if ser.is_open:
        ser.flushInput() #чистим буффер
        ser.flushOutput()
        try:
            ser.write(arr)
        except Exception as exc:
            print('type: {0}, message: {1}'.format(type(exc), str(exc)))
'''

class TouchPadWindow(Screen):
    btn = ObjectProperty(None)
    def on_touch_move(self, touch):
        print("Mouse Move", touch)

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(TouchPadWindow(name='touchpad'))
        sm.add_widget(MouseWindow(name='mouse'))

        return sm

if __name__ == '__main__':
    TestApp().run()