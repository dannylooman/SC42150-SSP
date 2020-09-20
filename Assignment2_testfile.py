import Communication
import Audio

# Instantiate communication object
transmit = Communication.Comm()

# Load audio
length_seconds = 5
datasend = Audio.read_audiofile('gong.wav', length_seconds)

# Send
transmit.write(datasend)
