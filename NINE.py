from PIL import Image
zad = int(input("Введи задание: "))
if zad == 1:
    image_path = "puppy.jpg"
    image = Image.open(image_path)

    image.show()

    print("Формат изображения:", image.format)
    print("Размер изображения (ширина x высота):", image.size)
    print("Цветовая модель:", image.mode)

elif zad == 2:
    from PIL import Image, ImageOps

    original_image = Image.open("puppy.jpg")

    width, height = original_image.size
    resized_image = original_image.resize((width // 3, height // 3))
    resized_image.save("lilpuppy.jpg")

    horizontal_flip = ImageOps.mirror(original_image)
    horizontal_flip.save("puppymirrorHOR.jpg")

    vertical_flip = ImageOps.flip(original_image)
    vertical_flip.save("puppymirrorVERT.jpg")

elif zad == 3:
    import os
    from PIL import Image, ImageFilter

    output_dir = "Done"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, 6):
        input_filename = f"{i}.jpg"
        output_filename = f"{output_dir}/filtered_{i}.jpg"

        image = Image.open(input_filename)
        filtered = image.filter(ImageFilter.CONTOUR)
        filtered.save(output_filename)

elif zad == 4:
    import os
    from PIL import Image, ImageDraw, ImageFont


    def add_watermark(input_image_path, output_folder, watermark_text, position=(10, 10), font_size=36):
        image = Image.open(input_image_path).convert("RGBA")

        watermark_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)

        try:
            font = ImageFont.truetype("comic.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        draw.text(position, watermark_text, fill=(255, 0, 70, 180), font=font)

        watermarked = Image.alpha_composite(image, watermark_layer)

        os.makedirs(output_folder, exist_ok=True)

        output_path = os.path.join(output_folder, os.path.basename(input_image_path))
        watermarked.convert("RGB").save(output_path, "JPEG")
        print(f"Файл сохранён: {output_path}")

    add_watermark("XDx.jpg", "XDxdone", "XD XD XD XD XD")
