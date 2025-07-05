import pyaudio

def list_microphones():
    p = pyaudio.PyAudio()
    mics = [p.get_device_info_by_index(i).get('name') for i in range(p.get_device_count())]
    p.terminate()
    return mics
