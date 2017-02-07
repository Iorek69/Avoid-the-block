import cx_Freeze

executables = cx_Freeze.Executable("Intro.py")

cx_Freeze.setup(
    name = "Vroom_vroom",
    options = {"build_exe": {"packages":["pygame"],"include_files":["car.png"]}},
    executables = executables
    )
