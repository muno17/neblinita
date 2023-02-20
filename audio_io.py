# Audio I/O information
print(f"portaudio version: {pa_get_version()}")
print(pa_list_host_apis())
print("- - - - - - - - - - - -")
print(pa_list_devices())
print("- - - - - - - - - - - -")
print(f"default input: {pa_get_default_input()}")
print(f"default output: {pa_get_default_output()}")
print("-----------------------")