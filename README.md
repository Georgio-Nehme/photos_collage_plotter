# Photo Roll Collage Generator

Efficiently arrange multiple photos onto a print roll canvas with specified width. Optimizes layout to minimize height and printing costs while maintaining photo quality and aspect ratios.

## Features

- 📐 Arranges photos in grid layout to minimize roll height
- 🖼️ Maintains original aspect ratios (no stretching/distortion)
- 💰 Calculates estimated print height and cost
- 🎨 Customizable photo size, padding, and DPI
- 📏 Configurable roll width (default: 90cm)
- 🎯 300 DPI output for professional print quality

## Use Case

Perfect for creating photo timelines, memory walls, or gift prints on large-format roll paper. Ideal when charged by linear meter for printing.

## Installation
```bash
pip install Pillow
```

## Usage

1. Create `input_photos` folder
2. Add your JPEG/PNG images
3. Run script:
```bash
python photo_collage.py
```
4. Output: `photo_collage.jpg` ready for printing

## Configuration

- `ROLL_WIDTH_CM`: Canvas width in centimeters (default: 90)
- `PHOTO_SIZE`: Target photo dimension in pixels (default: 800)
- `PADDING`: Space between photos in pixels (default: 20)
- `DPI`: Print resolution (default: 300)

## Example Output
```
Found 150 photos
Arranging 150 photos, ~4 per row
Total canvas size: 10630px x 30000px
Estimated height: 254.0 cm
Estimated cost: $38.10
✓ Collage saved as 'photo_collage.jpg'
```

## License

MIT
```

Short and sweet version for the repo description field:
```
Efficiently arrange photos on a print roll canvas. Minimizes height to reduce printing costs while maintaining quality. Perfect for creating large-format photo timelines and memory prints.