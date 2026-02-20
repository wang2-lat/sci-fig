import typer
from rich.console import Console
from pathlib import Path
import yaml
from generator import generate_figure
from editor import edit_parameters
from exporter import export_figure

app = typer.Typer(help="AI-powered scientific figure generator")
console = Console()

@app.command()
def generate(
    description: str = typer.Argument(..., help="Natural language description of the figure"),
    output: str = typer.Option("figure.yaml", help="Output config file")
):
    """Generate figure configuration from description"""
    console.print(f"[green]Generating figure from:[/green] {description}")
    config = generate_figure(description)
    
    with open(output, 'w') as f:
        yaml.dump(config, f)
    
    console.print(f"[green]Configuration saved to:[/green] {output}")
    console.print("[yellow]Use 'edit' command to modify parameters[/yellow]")

@app.command()
def edit(
    config_file: str = typer.Argument(..., help="Configuration file to edit")
):
    """Interactively edit figure parameters"""
    if not Path(config_file).exists():
        console.print(f"[red]Error:[/red] {config_file} not found")
        raise typer.Exit(1)
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    updated_config = edit_parameters(config)
    
    with open(config_file, 'w') as f:
        yaml.dump(updated_config, f)
    
    console.print(f"[green]Configuration updated:[/green] {config_file}")

@app.command()
def export(
    config_file: str = typer.Argument(..., help="Configuration file"),
    output: str = typer.Option("figure.png", help="Output file (png/pdf/svg)"),
    dpi: int = typer.Option(300, help="DPI for raster formats")
):
    """Export figure to high-resolution image"""
    if not Path(config_file).exists():
        console.print(f"[red]Error:[/red] {config_file} not found")
        raise typer.Exit(1)
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    export_figure(config, output, dpi)
    console.print(f"[green]Figure exported to:[/green] {output}")

if __name__ == "__main__":
    app()
