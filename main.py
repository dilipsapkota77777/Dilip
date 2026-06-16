#!/usr/bin/env python3
import os
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

load_dotenv()

from skills import (
    EmailGeneratorSkill,
    ProspectResearchSkill,
    EmailPersonalizationSkill,
    FollowupSequencesSkill,
)

app = typer.Typer(help="Cold email AI — generate personalized cold emails with Claude")
console = Console()


@app.command()
def generate(
    prospect_name: str = typer.Option(..., "--name", "-n", help="Prospect's full name"),
    prospect_title: str = typer.Option(..., "--title", "-t", help="Prospect's job title"),
    prospect_company: str = typer.Option(..., "--company", "-c", help="Prospect's company"),
    sender_name: str = typer.Option(..., "--sender", "-s", help="Your name"),
    sender_company: str = typer.Option(..., "--sender-company", help="Your company"),
    product: str = typer.Option(..., "--product", "-p", help="Your product/service description"),
    benefit: str = typer.Option(..., "--benefit", "-b", help="Key benefit for this prospect"),
    full_pipeline: bool = typer.Option(False, "--full", "-f", help="Run full research + strategy pipeline"),
    with_followups: bool = typer.Option(False, "--followups", help="Also generate follow-up sequence"),
):
    """Generate a personalized cold email for a prospect."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print("[red]Error:[/red] ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key.")
        raise typer.Exit(1)

    console.print(f"\n[bold]Generating cold email for [cyan]{prospect_name}[/cyan] at [cyan]{prospect_company}[/cyan]...[/bold]\n")

    if full_pipeline:
        console.print("[dim]Step 1/3: Researching prospect...[/dim]")
        research_skill = ProspectResearchSkill()
        prospect = research_skill.research(prospect_name, prospect_title, prospect_company)

        console.print("[dim]Step 2/3: Building personalization strategy...[/dim]")
        personalization_skill = EmailPersonalizationSkill()
        strategy = personalization_skill.build_strategy(prospect, sender_name, sender_company, product)

        console.print("[dim]Step 3/3: Writing email...[/dim]")
        generator = EmailGeneratorSkill()
        email = generator.generate(prospect, strategy, sender_name, sender_company, product)
    else:
        console.print("[dim]Generating email...[/dim]")
        generator = EmailGeneratorSkill()
        email = generator.generate_simple(
            prospect_name, prospect_title, prospect_company,
            sender_name, sender_company, product, benefit,
        )
        prospect = None

    console.print(Panel(
        f"[bold]Subject:[/bold] {email.subject}\n"
        f"[bold]Preview:[/bold] {email.preview_text}\n\n"
        f"{email.body}",
        title="[green]Generated Email[/green]",
        border_style="green",
    ))

    if with_followups:
        console.print("\n[dim]Generating follow-up sequence...[/dim]\n")
        if prospect is None:
            from skills.prospect_research import ProspectProfile
            prospect = ProspectProfile(
                name=prospect_name,
                title=prospect_title,
                company=prospect_company,
                industry="unknown",
                pain_points=[benefit],
                recent_news=[],
                personalization_hooks=[benefit],
            )
        followup_skill = FollowupSequencesSkill()
        sequence = followup_skill.generate_sequence(prospect, email, sender_name, sender_company)

        for fu in sequence.followups:
            console.print(Panel(
                f"[bold]Strategy:[/bold] {fu.strategy}\n"
                f"[bold]Subject:[/bold] {fu.subject}\n\n"
                f"{fu.body}",
                title=f"[yellow]Follow-up #{fu.day} days[/yellow]",
                border_style="yellow",
            ))


@app.command()
def research(
    name: str = typer.Argument(..., help="Prospect's full name"),
    title: str = typer.Argument(..., help="Prospect's job title"),
    company: str = typer.Argument(..., help="Prospect's company"),
    context: str = typer.Option("", "--context", help="Additional context about the prospect"),
):
    """Research a prospect and show personalization insights."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print("[red]Error:[/red] ANTHROPIC_API_KEY not set.")
        raise typer.Exit(1)

    console.print(f"\n[bold]Researching [cyan]{name}[/cyan]...[/bold]\n")
    skill = ProspectResearchSkill()
    profile = skill.research(name, title, company, context)

    pain_points = "\n".join(f"  • {p}" for p in profile.pain_points)
    hooks = "\n".join(f"  • {h}" for h in profile.personalization_hooks)
    news = "\n".join(f"  • {n}" for n in profile.recent_news) if profile.recent_news else "  • None found"

    console.print(Panel(
        f"[bold]Industry:[/bold] {profile.industry}\n\n"
        f"[bold]Pain Points:[/bold]\n{pain_points}\n\n"
        f"[bold]Personalization Hooks:[/bold]\n{hooks}\n\n"
        f"[bold]Recent News:[/bold]\n{news}",
        title=f"[cyan]Prospect Profile: {profile.name}[/cyan]",
        border_style="cyan",
    ))


if __name__ == "__main__":
    app()
