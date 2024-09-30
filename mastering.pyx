# mastering.pyx
import matchering as mg

# Function to get file paths from the user
cpdef str get_file_path(str prompt):
    return input(prompt).strip()

# Sending all log messages to the default print function
mg.log(print)

# Process the mastering
cpdef void process_mastering(str target_path):
    # Hardcoded reference track path
    cdef str reference_path = "/Users/gavinmorrison/Python/matchering_master/assets/08 _Slash Evans ft L.O.W (done).wav"

    mg.process(
        target=target_path,
        reference=reference_path,
        results=[
            mg.pcm16("my_song_master_16bit.wav"),
            mg.pcm24("my_song_master_24bit.wav"),
        ],
    )
