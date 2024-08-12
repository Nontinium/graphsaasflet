import flet as ft

def main(page: ft.Page):

    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            # Process the selected file here (e.g., upload, save, etc.)
            pass

    file_picker = ft.FilePicker(on_result=on_file_picked)

    page.overlay.append(file_picker)
    
    page.add(
        ft.Column(
            [
                ft.Text("Click the button to upload a file."),
                ft.ElevatedButton(
                    "Upload File", 
                    on_click=lambda _: file_picker.pick_files()
                ),
            ]
        )
    )

ft.app(target=main)
