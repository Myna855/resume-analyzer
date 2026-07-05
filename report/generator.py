import os
import webbrowser

from jinja2 import Environment, FileSystemLoader


def generate_report(
    extracted: dict,
    scores: dict,
    feedback: dict,
    job_match: dict,
    output_path: str,
    open_browser: bool = True,
) -> str:
    templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    env.globals["enumerate"] = enumerate  # make enumerate available in template

    template = env.get_template("report.html")
    html = template.render(
        extracted=extracted,
        scores=scores,
        feedback=feedback,
        job_match=job_match,
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    if open_browser:
        webbrowser.open(f"file://{os.path.abspath(output_path)}")

    return os.path.abspath(output_path)
