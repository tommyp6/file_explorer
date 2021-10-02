from GUI_toolkit import App

# place holder for where tools in the tool bar will be stored

'''
Plan:
1. Box layout in horizontal orientation to display buttons at the top
2. Box layout in vertical orientation to display input box under the buttons
3. Box layout in vertical orientation (with scroll enabled) to display a list made of buttons
'''
def set_default_button_attrs(button):
    button.colour = (216, 216, 216)
    button.hover_colour = (158, 158, 158)
    button.rounded = True
    button.radius = 0.1
    button.text_colour = (79, 99, 103)
    button.text_align = "center"
    
    return button

def create_tool_bar():
    tool_layout = BoxLayout()
    tool_layout.mode = "horizontal"
    tool_layout.background_colour = (240, 240, 240)
    tool_layout.padding = [0.1, 0.1, 0.05, 0.05]
    
    copy = Button()
    copy = set_default_button_attrs(copy)
    copy.text = "Copy"
    copy.bind(Explorer.copy_button)
    tool_layout.add_widget(copy)
    
    paste = Button()
    paste = set_default_button_attrs(paste)
    paste.text = "Paste"
    paste.bind(Explorer.paste_button())
    tool_layout.add_widget(paste)
    
    return tool_layout

class Explorer(App):
    def build(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.title = "File Explorer"

        tool_bar = create_tool_bar()

        screen = {tool_bar : 1}

        return screen

    def copy_button(self):
        tools.copy()

    def paste_button(self):
        pass

if __name__ == "__main__":
    Explorer.run()
