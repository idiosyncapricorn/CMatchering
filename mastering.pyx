import matchering as mg
import urllib.request
import io

# Function to download file data from a URL and return it as an in-memory file
cpdef bytes download_file(str url):
    response = urllib.request.urlopen(url)
    return response.read()

# Sending all log messages to the default print function
mg.log(print)

# Process the mastering using URLs
cpdef void process_mastering(str target_url):
    # Download target and reference file data
    cdef bytes target_data = download_file(target_url)
    
    # Hardcoded reference track URL
    cdef str reference_url = "https://example.com/path/to/reference.wav"
    cdef bytes reference_data = download_file(reference_url)

    # Mastering process using data from the URLs
    mg.process(
        target=io.BytesIO(target_data),
        reference=io.BytesIO(reference_data),
        results=[
            mg.pcm16("my_song_master_16bit.wav"),
            mg.pcm24("my_song_master_24bit.wav"),
        ],
    )

# Example usage:
# process_mastering("https://example.com/path/to/target.wav")