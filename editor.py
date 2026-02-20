from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.table import Table

console = Console()

def edit_parameters(config: dict) -> dict:
    """Interactively edit figure parameters"""
    console.print("\n[bold cyan]Figure Parameter Editor[/bold cyan]\n")
    
    # Display current configuration
    table = Table(title="Current Configuration")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Type", config["type"])
    table.add_row("Title", config["title"])
    table.add_row("X Label", config["xlabel"])
    table.add_row("Y Label", config["ylabel"])
    table.add_row("Font Size", str(config["style"]["font_size"]))
    table.add_row("Title Size", str(config["style"]["title_size"]))
    table.add_row("Color", config["style"]["color"])
    table.add_row("Figure Width", str(config["style"]["figure_width"]))
    table.add_row("Figure Height", str(config["style"]["figure_height"]))
    
    console.print(table)
    console.print()
    
    # Edit options
    while True:
        console.print("[yellow]Options:[/yellow]")
        console.print("1. Edit title")
        console.print("2. Edit axis labels")
        console.print("3. Edit font sizes")
        console.print("4. Edit colors")
        console.print("5. Edit figure dimensions")
        console.print("6. Save and exit")
        
        choice = Prompt.ask("Select option", choices=["1", "2", "3", "4", "5", "6"])
        
        if choice == "1":
            config["title"] = Prompt.ask("Enter title", default=config["title"])
        elif choice == "2":
            config["xlabel"] = Prompt.ask("Enter X label", default=config["xlabel"])
            config["ylabel"] = Prompt.ask("Enter Y label", default=config["ylabel"])
        elif choice == "3":
            config["style"]["font_size"] = IntPrompt.ask("Font size", default=config["style"]["font_size"])
            config["style"]["title_size"] = IntPrompt.ask("Title size", default=config["style"]["title_size"])
        elif choice == "4":
            config["style"]["color"] = Prompt.ask("Color", default=config["style"]["color"])
        elif choice == "5":
            config["style"]["figure_width"] = FloatPrompt.ask("Width (inches)", default=config["style"]["figure_width"])
            config["style"]["figure_height"] = FloatPrompt.ask("Height (inches)", default=config["style"]["figure_height"])
        elif choice == "6":
            break
        
        console.print("[green]Updated![/green]\n")
    
    return config
