# Saudi Gateway — AI B-Roll Prompt Library

Copy-paste these into **Runway Gen-3**, **Kling**, or **Pika**. Append to every prompt:

> cinematic documentary style, natural lighting, 4K, no text overlays, no watermarks, professional stock footage aesthetic

---

## Property Pillar

### Riyadh skyline
```
Aerial drone shot of modern Riyadh skyline at golden hour, Kingdom Centre tower visible, desert city atmosphere, slow cinematic push forward
```

### KAFD financial district
```
King Abdullah Financial District Riyadh, gleaming modern glass towers, wide establishing shot, business district, clear sky
```

### Luxury residential
```
Modern luxury apartment building exterior in Middle Eastern city, clean architecture, palm trees, affluent residential district, slow pan
```

### NEOM / giga-project (label as artist impression in edit)
```
Futuristic sustainable city concept aerial view, Red Sea coastline, visionary architecture, artist impression style, soft daylight
```

### Property documents
```
Close-up of hands reviewing property contract documents on desk, professional office setting, shallow depth of field, no readable text
```

### Diriyah heritage
```
Atarazah Olaya Diriyah heritage district Saudi Arabia, mud-brick architecture, traditional Najdi buildings, golden hour warm light
```

### Red Sea coast
```
Aerial view of Red Sea coastline Saudi Arabia, turquoise water, pristine beach, luxury resort development, cinematic
```

---

## Business Pillar

### Modern office / boardroom
```
Professional corporate boardroom Middle East, floor-to-ceiling windows, city view, empty chairs, business atmosphere
```

### Government building exterior
```
Modern government administrative building exterior, formal architecture, flagpoles, clear day, establishing shot
```

### Business handshake
```
Professional business handshake in modern office, suits, diverse executives, shallow depth of field, warm lighting
```

### Laptop / portal work
```
Over-shoulder shot of professional working on laptop showing government portal dashboard, modern office, no readable screen text
```

### Warehouse / logistics
```
Large modern logistics warehouse Saudi Arabia, trucks loading, industrial scale, aerial and ground shots
```

### Hiring / team
```
Diverse professional team meeting in modern Saudi office, presentation screen blurred, collaborative atmosphere
```

---

## Generic / Transitions

### Desert aerial
```
Vast Saudi Arabian desert landscape aerial, sand dunes, dramatic shadows, cinematic slow flyover
```

### Map animation base (use in Canva, not AI video)
Generate static in Ideogram:
```
Minimal flat map of Saudi Arabia on dark navy background, gold border outline, clean infographic style, no labels
```

### Gateway / arch motif
```
Historic stone arch gateway Middle Eastern architecture, Diriyah style, warm golden light, symbolic entrance, cinematic
```

### Vision 2030 abstract
```
Abstract visualization of economic growth, green and gold particles, dark background, modern motion graphics style
```

---

## Stock Search Terms (Pexels / Storyblocks)

When AI clips look too synthetic, search stock with these terms:

| Scene | Search terms |
|-------|-------------|
| Riyadh | `riyadh skyline`, `saudi arabia city`, `kingdom centre` |
| Business | `corporate meeting`, `signing contract`, `office middle east` |
| Property | `luxury apartment`, `real estate agent`, `house keys` |
| Government | `government building`, `official documents`, `passport stamp` |
| Construction | `construction site aerial`, `crane building`, `master planned community` |

---

## Per-Video Shot Lists

Full shot lists auto-generated per script by:

```bash
python channel/automation/prepare_video.py channel/content/scripts/01-foreigners-buy-property-ksa.md
```

See `output/*/broll_shotlist.json` for script-specific scenes.
