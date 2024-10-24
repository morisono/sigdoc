import os
import subprocess
import argparse
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import track
from rich.progress import Progress
import datetime

sizes = [
    # Basic
    (16, 16), (24, 24), (32, 32), (64, 64), (96, 96), (128, 128), (256, 256), (512, 512), (1024, 1024), (2048, 2048), # 1:1
    (600, 300), (800, 400), (1280, 640), (1600, 800), (2400, 1200), # 2:1
    (1500, 500), (2000, 667), (3000, 1000), # 3:1
    (640, 360), (1280, 720), (1920, 1080), (2560, 1440),
     (3840, 2160), # 16:9
    (360, 640), (720, 1280), (1080, 1920), (1440, 2560),
     (2160, 3840), # 9:16

    # Advanced
    # (1440, 960), (1920, 1280), (2400, 1600), # 3:2
    # (1000, 750), (1500, 1125), (2000, 1500), (3000, 2250), # 4:3
    # (1000, 400), (1500, 600), (2000, 800), (3000, 1200), # 5:2
    # (1000, 600), (1500, 900), (2000, 1200), (3000, 1800), # 5:3
    # (1000, 800), (1500, 1200), (2000, 1600), (3000, 2400), # 5:4
    # (1000, 700), (1500, 1050), (2000, 1400), (3000, 2100), # 10:7
    # (1000, 900), (1500, 1350), (2000, 1800), (3000, 2700), # 10:9
    # (300, 600), (400, 800), (640, 1280), (800, 1600), (1200, 2400), # 1:2
    # (500, 1500), (667, 2000), (1000, 3000), # 1:3
    # (960, 1440), (1280, 1920), (1600, 2400), # 2:3
    # (750, 1000), (1125, 1500), (1500, 2000), (2250, 3000), # 3:4
    # (400, 1000), (600, 1500), (800, 2000), (1200, 3000), # 2:5
    # (600, 1000), (900, 1500), (1200, 2000), (1800, 3000), # 3:5
    # (800, 1000), (1200, 1500), (1600, 2000), (2400, 3000), # 4:5
    # (700, 1000), (1050, 1500), (1400, 2000), (2100, 3000), # 7:10
    # (900, 1000), (1350, 1500), (1800, 2000), (2700, 3000), # 9:10

    # Custom
    # (1024, 768),  # 4:3 - Presentation
    # (1600, 2400),  # 2:3 - E-Book Cover
    # (1200, 627),   # 1:1 - Linkedin Post
    # (736, 1128),   # 1:1 - Pinterest Post
    # (2490, 3510),  # 1:1 - Brochure Cover
    # (1050, 600),   # 7:4 - Business Card
    # (1500, 2100),  # 1:1.4 - Postcard
    # (1200, 1800),  # 2:3 - Photo Print
    # (1800, 750),   # 24:10 - Coupon
    # (2400, 1125),  # 64:30 - Gift Certificate
    # (2550, 3300),  # 17:22 - Flyer
    # (3300, 2550),  # 22:17 - Certificate
    # (800, 800),    # 1:1 - Youtube Profile Image
    # (2560, 1440),  # 16:9 - Youtube Channel Art
]
exts = ["png", "jpg", "webp"] # tiff, ics, icns, ico, bmp, gif, jp2, jpeg


def convert(input_file, cmd, timestamp):
    console = Console()
    base_name = os.path.splitext(input_file)[0]

    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...", total=len(sizes) * len(exts))

        for ext in exts:
            base_dir = f'{timestamp}/{ext}'
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)

            for size in sizes:
                progress.update(task, advance=1, description=f"Converting {ext} images")
                output_file = f"{base_dir}/{base_name}-{size[0]}x{size[1]}.{ext}"
                command = f"{cmd} {input_file} -o {output_file} -w {size[0]} -h {size[1]}"
                subprocess.run(command, shell=True)
                console.log(f"Generated {output_file}")


cmd = "svg2png"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
parser = argparse.ArgumentParser(description='Convert SVG to PNG.')
parser.add_argument('input_file', type=str, help='Input SVG file')
args = parser.parse_args()
convert(args.input_file, cmd, timestamp)
