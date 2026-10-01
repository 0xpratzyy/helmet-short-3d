# Brief: "Aiming A Missile Just By Looking 🤯": a 3D short made in Blender

Make a finished **29-second vertical (9:16) 3D-animated short** in Blender, cut to the narration in `audio/voice.wav`, with captions and the music bed, and deliver it as an MP4 on a branch of this repo.

Format reference: `reference/format-blueprint.md`. It's a dissection of a viral 3D explainer reel; follow its rules: a new angle on every clause, the camera always moving, cartoon overlays for invisible processes, white 2–4-word captions, and a studio → real place → absurd place escalation.

## Inputs in this repo

| File | What |
|---|---|
| `audio/voice.wav` | The final narration (28.48 s, 48 kHz). Don't change its timing; the picture follows the voice. |
| `audio/words.json` | Word timings `[start, end, word]` plus the script text. Cut and caption from these. |
| `audio/music.mp3` | Instrumental bed (about 30 s), light, curious and plucky. |
| `reference/format-blueprint.md` | The format to follow (pacing, captions, overlays, sound). |

## Look

- **Style: clean, bright, toy-like 3D.** Simple shapes built from primitives with bevels and subdivision, smooth soft lighting, saturated colour, shallow depth of field, gentle motion blur. A polished low-poly "toy commercial" look is the goal; don't attempt photorealism.
- **Palette:**
  - studio background: flat cyan infinite cyc, about `#3DB8E0`
  - accents and overlays: neon green `#3CE36B`
  - pilot suit: olive `#5A6B3C`
  - helmet: light grey, with a dark tinted visor and a green glow
  - sky: soft blue gradient with puffy white clouds
  - Bengaluru road: warm grey asphalt and bright buses
  - auto-rickshaws: the classic green body and yellow top
  - lock state: red `#E5484D`
- **Characters:** one stylised pilot (a capsule body, rounded gloves, a helmet with a visor), no face detail needed, and no real person's likeness.
- **Vehicles:** a generic delta-wing fighter for "our" jet, light grey; a darker grey generic jet as the "enemy plane". Neither should be modelled on a specific real aircraft. A scooter, buses, cars and auto-rickshaws (three wheels, green and yellow) built from simple shapes.
- **Never include:** national insignia, roundels, flags, real logos, text on vehicles, or maps.
- **Overlays:** emissive green square target boxes; a red box with a small "LOCK" label; dotted tracking lines; a translucent green look cone or beam; arrows; a glowing green route line. Build them as emissive objects in the scene or draw them in compositing, whichever is quicker to make look clean.

## Shot list (cut on the first word of each line; times are from `audio/words.json`)

| # | Starts at word (≈ s) | Picture | Caption |
|---|---|---|---|
| 1 | "The" (0.0) | Close-up, cyan studio: gloved hands lower the helmet onto the pilot's head; slow push-in. Already moving on frame 1. | The helmet clicks |
| 2 | "onto" (0.7) | Extreme close-up: the visor snaps down with a green glow | onto your head |
| 3 | "while" (1.6) | Wide orbit: the pilot in an open cockpit tub floating in the cyan studio; small sensors on the canopy frame light up green | while tiny sensors |
| 4 | "around" (2.4) | Low orbit past a sensor block on the canopy frame | around the cockpit |
| 5 | "start" (3.1) | Dotted green tracking lines run from the sensors to the helmet | start tracking |
| 6 | "exactly" (3.8) | The pilot tilts his head; the lines follow it | exactly where it points |
| 7 | "A" (5.5) | Hard cut to the sky: our jet banks through clouds, camera tracking alongside | A display inside the visor |
| 8 | "paints" (6.8) | POV through the visor (a dark rounded frame edge): green target boxes pop onto distant clouds | paints target boxes |
| 9 | "over" (8.1) | POV continues, slight drift; more boxes appear | over the real sky |
| 10 | "and" (9.1) | Inside the cockpit: instrument glow, the helmet in the foreground | and the jet's computer |
| 11 | "knows" (10.1) | Over the shoulder: a translucent green cone projects from the helmet and sweeps as the head moves | knows every direction you look |
| 12 | "When" (12.1) | Close on the pilot turning his head hard left | When you turn your head |
| 13 | "toward" (12.9) | POV: a dark grey enemy jet off the left wing; a green box snaps onto it | toward an enemy plane |
| 14 | "the" (14.4) | Under-wing close-up: a missile with a glass seeker dome; the seeker rotates sideways | the missile's seeker |
| 15 | "swings" (15.1) | Side view: the helmet's beam and the seeker's beam swing until they line up | swings to match your gaze |
| 16 | "locking" (16.8) | POV: the box flashes and turns red, LOCK | locking on |
| 17 | "even" (17.3) | Top-down wide: our jet, with the enemy jet beside it at 9 o'clock, not ahead | even when the target |
| 18 | "is" (18.4) | Same top-down view: a green arrow along our nose, a red arc to the side target | is beside you, not ahead |
| 19 | "Now," (20.3) | Hard cut: the same helmeted pilot on a scooter in dense city traffic, camera tracking | Now, if you wore this helmet |
| 20 | "in" (21.8) | Wide street: buses, cars, green-and-yellow auto-rickshaws, a bit of chaos | in Bengaluru traffic |
| 21 | "you" (23.1) | POV through the visor: green boxes snap onto gaps between vehicles | you could lock onto every gap |
| 22 | "between" (24.5) | POV continues, boxes multiply | between the lanes |
| 23 | "plotting" (25.6) | Wide, slightly high angle: a glowing green route line threads through the lanes | plotting your escape |
| 24 | "before" (26.4) | An auto-rickshaw zips into the gap; the box flashes red | before an auto-rickshaw |
| 25 | "takes" (27.5) | Close on the visor, pilot motionless (deadpan) as the auto drives off; hold to the end | takes it first |

The video ends 0.5 s after the last word (about 28.9 s).

## Captions

- **Font:** white bold sans. Download Montserrat Bold from `github.com/google/fonts` (`ofl/montserrat`); if that fails, use DejaVu Sans Bold. About 80 px on 1080×1920, sentence case.
- **Style:** a soft dark drop shadow, no box, no outline.
- **Position:** centred horizontally, with the baseline at about 78% of the frame height.
- **Timing:** the "Caption" text above, switching exactly on the first word of each line and holding until the next one starts.

## Sound

Voice at full level. Music bed underneath, about 9 dB quieter than the voice, with a short fade-out after the last word. Master to about −14 LUFS integrated (ffmpeg `loudnorm`), true peak −1 dBTP, AAC 192 kbps.

## Technical

- **Blender:** `pip install bpy` (Python 3.11 wheels) or `apt-get install blender`, whichever works here. Build everything with Python scripts in `blender/` so the scene can be rebuilt.
- **Render:** 1080×1920 at 24 fps. Use Cycles on CPU with low samples (16–32) plus the OpenImageDenoise denoiser, or EEVEE if a working OpenGL context is available (try `xvfb-run`).
- **Render time:** first time one frame, then pick settings so the whole render takes no more than about 90 minutes. If needed, render at 720×1280 and upscale with ffmpeg (lanczos). Render shot by shot as PNG sequences, so a crash only costs one shot.
- **Assembly:** use ffmpeg: image sequences → edit, then captions, voice and music → final H.264 (yuv420p, CRF 18–20, `+faststart`). Keep the file under 50 MB.
- **Self-check:** before delivering, pull a contact sheet of about 12 frames and look at it. Check that every shot reads clearly (subject centred, nothing cut off by the 9:16 frame or hidden behind captions) and that the captions are legible. Fix anything broken.

## Deliver

1. Create the branch `render/v1`.
2. Commit:
   - `out/aiming_a_missile_by_looking.mp4`
   - `out/contact_sheet.jpg`
   - the `blender/` scripts
   - a short `out/NOTES.md`: render settings, total render time, anything you'd improve
3. Push.

Don't commit the PNG sequences or caches.
