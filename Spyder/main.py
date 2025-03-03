from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        # 主布局
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 标题
        title_label = Label(text="记牌得分工具", font_size=24, size_hint=(1, 0.1))
        layout.add_widget(title_label)

        # 输入框
        self.input = TextInput(hint_text="请输入赢家", size_hint=(1, 0.2))
        layout.add_widget(self.input)

        # 按钮
        submit_button = Button(text="提交", size_hint=(1, 0.2))
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)

        # 结果显示
        self.result_label = Label(text="", size_hint=(1, 0.5))
        layout.add_widget(self.result_label)

        return layout

    def on_submit(self, instance):
        # 获取输入内容
        winner = self.input.text
        self.result_label.text = f"赢家是: {winner}"

if __name__ == "__main__":
    MainApp().run()