import matplotlib.pyplot as plt
from pathlib import Path

def export_figure(config: dict, output: str, dpi: int = 300):
    """Export figure to file"""
    fig, ax = plt.subplots(
        figsize=(config["style"]["figure_width"], config["style"]["figure_height"])
    )
    
    x = config["data"]["x"]
    y = config["data"]["y"]
    chart_type = config["type"]
    style = config["style"]
    
    # Plot based on type
    if chart_type == "line":
        ax.plot(x, y, color=style["color"], linewidth=style["line_width"], 
                marker='o', markersize=style["marker_size"])
    elif chart_type == "bar":
        ax.bar(x, y, color=style["color"])
    elif chart_type == "scatter":
        ax.scatter(x, y, color=style["color"], s=style["marker_size"]*10)
    
    # Set labels and title
    ax.set_xlabel(config["xlabel"], fontsize=style["font_size"])
    ax.set_ylabel(config["ylabel"], fontsize=style["font_size"])
    ax.set_title(config["title"], fontsize=style["title_size"], fontweight='bold')
    
    # Grid and styling
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=style["font_size"]-2)
    
    plt.tight_layout()
    
    # Save with appropriate format
    ext = Path(output).suffix.lower()
    if ext == '.pdf':
        plt.savefig(output, format='pdf', dpi=dpi, bbox_inches='tight')
    elif ext == '.svg':
        plt.savefig(output, format='svg', bbox_inches='tight')
    else:
        plt.savefig(output, format='png', dpi=dpi, bbox_inches='tight')
    
    plt.close()
