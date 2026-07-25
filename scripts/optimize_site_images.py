from pathlib import Path
import re

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"


def convert(source: Path, destination: Path, max_width: int, quality: int) -> None:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        if image.width > max_width:
            height = round(image.height * max_width / image.width)
            image = image.resize((max_width, height), Image.Resampling.LANCZOS)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "transparency" in image.info else "RGB")
        image.save(destination, "WEBP", quality=quality, method=6)


for publication in (ROOT / "_publications").glob("*.md"):
    source = IMAGES / f"{publication.stem}.png"
    convert(source, source.with_suffix(".webp"), max_width=1600, quality=82)

portfolio_sources = set()
for portfolio in (ROOT / "_portfolio").glob("*.md"):
    content = portfolio.read_text(encoding="utf-8")
    for webp_path in re.findall(r'src="/images/([^\"]+\.webp)"', content):
        stem = Path(webp_path).stem
        matches = [path for path in IMAGES.glob(f"{stem}.*") if path.suffix.lower() in {".jpg", ".jpeg", ".png"}]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one source image for {webp_path}, found {len(matches)}")
        portfolio_sources.add(matches[0])

for source in portfolio_sources:
    convert(source, source.with_suffix(".webp"), max_width=1200, quality=80)
