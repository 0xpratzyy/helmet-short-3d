"""make_audio.py - narration (ElevenLabs v4, channel narrator, [quickly] delivery), a music bed (ElevenLabs music) and word
timings (faster-whisper) for the helmet short. Runs locally: reads ~/.elevenlabs_key and never prints it.
usage: uv run --with faster-whisper --with numpy tools/make_audio.py"""
import json, os, subprocess, sys, tempfile, urllib.request, wave
import numpy as np
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = ("The helmet clicks onto your head, while tiny sensors around the cockpit start tracking exactly where it points. "
          "A display inside the visor paints target boxes over the real sky, and the jet's computer knows every direction you look. "
          "When you turn your head toward an enemy plane, the missile's seeker swings to match your gaze, locking on even when the "
          "target is beside you, not ahead. Now, if you wore this helmet in Bengaluru traffic, you could lock onto every gap between "
          "the lanes, plotting your escape before an auto-rickshaw takes it first.")
key = open(os.path.expanduser('~/.elevenlabs_key')).read().strip()
def post(url, body, timeout=600):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method='POST',
                                 headers={'xi-api-key': key, 'Content-Type': 'application/json'})
    return urllib.request.urlopen(req, timeout=timeout).read()
voice = os.path.join(D, 'audio/voice.wav')
if not os.path.exists(voice):
    open(voice, 'wb').write(post('https://api.elevenlabs.io/v1/text-to-speech/b3FDzVJsu4VjESdDgFZg?output_format=wav_48000',
        {'text': '[quickly] ' + SCRIPT, 'model_id': 'eleven_v4', 'seed': 7,
         'voice_settings': {'stability': 0.5, 'similarity_boost': 0.85}}))
with wave.open(voice) as w: dur = w.getnframes() / w.getframerate()
print(f'voice: {dur:.2f} s')
music = os.path.join(D, 'audio/music.mp3')
if not os.path.exists(music):
    chunk = {'text': '[Bed]\n{light, curious and playful: plucky synth and marimba over soft drums, steady energy from start to finish, '
                     'a small lift in the last third, ends on a clean button}',
             'duration_ms': int((dur + 1.5) * 1000),
             'positive_styles': ['light curious upbeat instrumental', 'plucky synth', 'marimba', 'soft drums', 'steady energy',
                                 '110 BPM', 'playful explainer', 'background music under a voiceover'],
             'negative_styles': ['vocals', 'singing', 'humming', 'choir', 'lyrics', 'EDM drop', 'dubstep', 'heavy bass', 'distortion'],
             'context_adherence': 'high'}
    open(music, 'wb').write(post('https://api.elevenlabs.io/v1/music?output_format=mp3_48000_192',
                                 {'composition_plan': {'chunks': [chunk]}, 'model_id': 'music_v2_5', 'seed': 5}, 900))
print('music: ok')
from faster_whisper import WhisperModel
tmp = tempfile.mktemp(suffix='.wav')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', voice, '-ac', '1', '-ar', '16000', tmp], check=True)
with wave.open(tmp) as w: x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
os.remove(tmp)
segs, _ = WhisperModel('small', device='cpu', compute_type='int8').transcribe(x, language='en', word_timestamps=True)
words = [[round(wd.start, 3), round(wd.end, 3), wd.word.strip()] for s in segs for wd in s.words]
json.dump({'duration_s': round(dur, 3), 'script': SCRIPT, 'words': words}, open(os.path.join(D, 'audio/words.json'), 'w'), indent=1)
print(f'words: {len(words)} (script has {len(SCRIPT.split())})')
