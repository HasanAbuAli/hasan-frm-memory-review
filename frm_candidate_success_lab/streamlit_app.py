from pathlib import Path
import runpy

PAGE = Path(__file__).resolve().parents[1] / "pages" / "03_FRM_Candidate_Success_Lab.py"
runpy.run_path(str(PAGE), run_name="__main__")
