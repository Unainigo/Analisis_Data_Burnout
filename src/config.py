from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw" / "mental_health_burnout_tech_2026.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_mental_health_burnout_tech_2026.csv"
OUT_PATH_GRAPH = ROOT / "Imagenes" 