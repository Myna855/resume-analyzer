import sys
import os

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import box

sys.path.insert(0, os.path.dirname(__file__))

from parser import load_resume
from analyzer.extractor import extract_info
from analyzer.scorer import score_resume, generate_feedback
from analyzer.job_matcher import match_job
from report.generator import generate_report

console = Console()


def _color(score: int, high=70, mid=40) -> str:
    if score >= high:
        return "green"
    elif score >= mid:
        return "yellow"
    return "red"


def _readability_label(word_count: int) -> str:
    if word_count >= 300:
        return "Good"
    elif word_count >= 150:
        return "Fair"
    return "Too Short"


@click.command()
@click.argument("resume_file", type=click.Path(exists=True))
@click.option("--job", "-j", type=click.Path(exists=True), default=None,
              help="Path to job description .txt file (optional)")
@click.option("--output", "-o", default="report.html",
              help="Output HTML report path (default: report.html)")
@click.option("--no-browser", is_flag=True, default=False,
              help="Don't auto-open the report in browser")
def analyze(resume_file, job, output, no_browser):
    """Resume Analyzer — rule-based, fully offline, no API key needed."""

    console.print(Panel.fit(
        "[bold]Resume Analyzer[/bold]\n[dim]Rule-based · Fully offline · No API key needed[/dim]",
        border_style="blue"
    ))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("Parsing resume...", total=None)

        try:
            resume_text = load_resume(resume_file)
        except (FileNotFoundError, ValueError) as e:
            console.print(f"[red]Error:[/red] {e}")
            raise SystemExit(1)

        progress.update(task, description="Extracting information...")
        extracted = extract_info(resume_text)

        progress.update(task, description="Scoring resume...")
        scores = score_resume(resume_text, extracted)
        feedback = generate_feedback(resume_text, extracted, scores)

        job_match_result = None
        if job:
            progress.update(task, description="Matching job description...")
            try:
                with open(job, "r", encoding="utf-8") as f:
                    jd_text = f.read()
                job_match_result = match_job(resume_text, jd_text)
            except Exception as e:
                console.print(f"[yellow]Warning:[/yellow] Could not process job file: {e}")

        progress.update(task, description="Generating report...")
        report_path = generate_report(
            extracted=extracted,
            scores=scores,
            feedback=feedback,
            job_match=job_match_result,
            output_path=output,
            open_browser=not no_browser,
        )

    # Summary table
    overall = scores["overall_score"]
    table = Table(box=box.ROUNDED, border_style="blue", show_header=True)
    table.add_column("Field", style="bold")
    table.add_column("Result")

    table.add_row(
        "Overall Score",
        f"[{_color(overall)}]{overall}/100[/{_color(overall)}]"
    )
    table.add_row("Candidate", extracted.get("name") or "—")
    table.add_row("Skills Found", str(len(extracted.get("skills", []))))
    table.add_row(
        "Sections Detected",
        f"{len(scores['present_sections'])}/{len(scores['present_sections']) + len(scores['missing_sections'])}"
    )
    table.add_row("Word Count", str(extracted.get("word_count", 0)))
    table.add_row("Experience", f"{extracted.get('years_of_experience', 0)} years")

    if job_match_result:
        ms = job_match_result["match_score"]
        table.add_row(
            "Job Match Score",
            f"[{_color(ms)}]{ms}/100[/{_color(ms)}]"
        )
        if job_match_result["missing_skills"]:
            missing = job_match_result["missing_skills"]
            table.add_row(
                "Missing Skills",
                ", ".join(missing[:4]) + ("..." if len(missing) > 4 else "")
            )

    console.print(table)
    console.print(f"\n[green]✔[/green] Report saved: [bold]{report_path}[/bold]")
    if no_browser:
        console.print("[dim]Open the HTML file in a browser to view the full report.[/dim]")


if __name__ == "__main__":
    analyze()
