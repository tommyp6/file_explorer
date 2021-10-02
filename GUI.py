from GUI_toolkit import App

# place holder for where tools in the tool bar will be stored

'''
Plan:
1. Box layout in horizontal orientation to display buttons at the top
2. Box layout in vertical orientation to display input box under the buttons
3. Box layout in vertical orientation (with scroll enabled) to display a list made of buttons
'''

'''Access Peter's file to get the list of files and passing through the directory'''
def get_files_to_display(directory):
    files = file.function(directory)
    return files

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

def create_search_bar():
    bar_layout = BoxLayout()
    bar_layout.mode = "horizontal"
    bar_layout.background_colour = (240, 240, 240)

    search_bar = Text_input()
    search_bar.default_text = "Search here"
    bar_layout.add_widget(search_bar)

    search_button = Button_widget()
    search_button.icon = "search"
    search_button.icon_align = "centre"
    bar_layout.add_widget(search_button)

    return bar_layout, input_box

def update_files(directory):
    file_buttons = []
    files = get_files_to_display(directory)

    for file in get_files_to_display():
        file_button = Button_widget()
        file_button.text = file
        file_layout.add_widget(file_button)
        file_buttons.append(file_button)

    return file_buttons

def show_files(layout_height, directory):
    file_buttons = []
    files = get_files_to_display()
    real_size = files * 50
    if real_size > layout_height:
        real_height = real_size / layout_height
    file_layout = BoxLayout()
    file_layout.mode = "vertical"
    file_layout.background_colour = (240, 240)
    file_layout.scroll_enabled = True
    file_layout.real_size = real_size

    update_files(directory)

    return tool_layout

class Explorer(App):
    def build(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.title = "File Explorer"

        tool_bar = create_tool_bar()
        search_bar, input_box = create_search_bar()
        file_tray = show_files(self.screen_height * 0.8, directory)

        self.search_bar = input_box

        screen = {tool_bar : 0.2, search_bar : 0.1, file_tray : 0.7}

        return screen

    def copy_button(self):
        #tools.copy()
        pass

    def paste_button(self):
        pass

    def search_button(self):
        pass

    def somehow_access_button_actions(self, new_directory):
        file_tray.reset_widgets()
        update_files(new_directory)

if __name__ == "__main__":
    Explorer.run()
