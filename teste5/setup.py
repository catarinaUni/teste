from cx_Freeze import setup, Executable

# Defina o nome do script Python que você deseja converter
script_name = 'script.py'

# Configuração do cx_Freeze
build_exe_options = {
    'packages': ['gi', 'gi.repository', 'Gimp', 'GimpUi', 'GLib'],
    'excludes': ['tkinter'],  # Exclua pacotes desnecessários
    'include_files': [],  # Inclua arquivos adicionais se necessário
}

# Configuração do setup
setup(
    name="GIMP Python Plug-in",
    version="0.1",
    description="My first Python plug-in for GIMP 3.0",
    options={'build_exe': build_exe_options},
    executables=[Executable(script_name)],
)
