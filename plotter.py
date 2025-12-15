from PIL import Image
import os
import math

# Configuration
ROLL_WIDTH_CM = 90
DPI = 300  # Print quality (300 DPI is standard for good prints)
ROLL_WIDTH_PX = int(ROLL_WIDTH_CM * DPI / 2.54)  # Convert cm to pixels
PADDING = 20  # Padding between photos in pixels
PHOTO_SIZE = 800  # Target size for each photo (will maintain aspect ratio)

# Input/Output paths
INPUT_FOLDER = "."  # Put your photos here
OUTPUT_FILE = "photo_collage.jpg"


def resize_image_aspect_ratio(img, target_size):
    """Resize image maintaining aspect ratio to fit within target_size"""
    img.thumbnail((target_size, target_size), Image.Resampling.LANCZOS)
    return img


def arrange_photos_grid(photo_paths, roll_width_px, padding, photo_size):
    """Arrange photos in a grid layout to minimize height"""

    # Load and resize all images
    images = []
    for path in photo_paths:
        try:
            img = Image.open(path)
            img = resize_image_aspect_ratio(img, photo_size)
            images.append(img)
            print(f"Loaded: {os.path.basename(path)} - Size: {img.size}")
        except Exception as e:
            print(f"Error loading {path}: {e}")

    if not images:
        print("No images loaded!")
        return None

    # Calculate how many photos fit per row
    max_width_per_photo = max(img.width for img in images)
    photos_per_row = max(1, (roll_width_px + padding) // (max_width_per_photo + padding))

    print(f"\nArranging {len(images)} photos, ~{photos_per_row} per row")

    # Arrange in rows
    rows = []
    current_row = []
    current_row_width = 0
    max_row_height = 0

    for img in images:
        if current_row_width + img.width + padding > roll_width_px and current_row:
            # Start new row
            rows.append((current_row, max_row_height))
            current_row = [img]
            current_row_width = img.width
            max_row_height = img.height
        else:
            # Add to current row
            if current_row:
                current_row_width += padding
            current_row.append(img)
            current_row_width += img.width
            max_row_height = max(max_row_height, img.height)

    # Add last row
    if current_row:
        rows.append((current_row, max_row_height))

    # Calculate total height
    total_height = sum(row_height + padding for _, row_height in rows) + padding

    print(f"Total canvas size: {roll_width_px}px x {total_height}px")
    print(f"Estimated height: {total_height * 2.54 / DPI:.1f} cm")
    print(f"Estimated cost: ${(total_height * 2.54 / DPI / 100) * 15:.2f}")

    # Create canvas
    canvas = Image.new('RGB', (roll_width_px, total_height), 'white')

    # Place photos
    y_offset = padding
    for row_images, row_height in rows:
        x_offset = padding

        # Center the row if it doesn't fill the width
        row_width = sum(img.width for img in row_images) + padding * (len(row_images) - 1)
        if row_width < roll_width_px:
            x_offset = (roll_width_px - row_width) // 2

        for img in row_images:
            # Center vertically in row
            y_pos = y_offset + (row_height - img.height) // 2
            canvas.paste(img, (x_offset, y_pos))
            x_offset += img.width + padding

        y_offset += row_height + padding

    return canvas


def main():
    # Get all JPEG files from input folder
    if not os.path.exists(INPUT_FOLDER):
        print(f"Please create folder '{INPUT_FOLDER}' and add your photos!")
        return

    photo_paths = []
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            photo_paths.append(os.path.join(INPUT_FOLDER, file))

    photo_paths.sort()  # Sort for consistent ordering

    if not photo_paths:
        print(f"No photos found in '{INPUT_FOLDER}'!")
        return

    print(f"Found {len(photo_paths)} photos")
    print(f"Roll width: {ROLL_WIDTH_CM}cm ({ROLL_WIDTH_PX}px at {DPI} DPI)")
    print(f"Photo size: ~{PHOTO_SIZE}px\n")

    # Create collage
    canvas = arrange_photos_grid(photo_paths, ROLL_WIDTH_PX, PADDING, PHOTO_SIZE)

    if canvas:
        # Save with high quality
        canvas.save(OUTPUT_FILE, 'JPEG', quality=95, dpi=(DPI, DPI))
        print(f"\n✓ Collage saved as '{OUTPUT_FILE}'")
        print(f"Ready to print!")


if __name__ == "__main__":
    main()