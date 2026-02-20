import re

def generate_figure(description: str) -> dict:
    """Generate figure configuration from natural language description"""
    desc_lower = description.lower()
    
    # Detect chart type
    if "line" in desc_lower or "trend" in desc_lower:
        chart_type = "line"
    elif "bar" in desc_lower or "column" in desc_lower:
        chart_type = "bar"
    elif "scatter" in desc_lower or "point" in desc_lower:
        chart_type = "scatter"
    else:
        chart_type = "line"
    
    # Extract title
    title_match = re.search(r'title[:\s]+["\']?([^"\']+)["\']?', desc_lower)
    title = title_match.group(1).strip() if title_match else "Scientific Figure"
    
    # Extract axis labels
    xlabel_match = re.search(r'x[-\s]?axis[:\s]+["\']?([^"\']+)["\']?', desc_lower)
    ylabel_match = re.search(r'y[-\s]?axis[:\s]+["\']?([^"\']+)["\']?', desc_lower)
    xlabel = xlabel_match.group(1).strip() if xlabel_match else "X Axis"
    ylabel = ylabel_match.group(1).strip() if ylabel_match else "Y Axis"
    
    config = {
        "type": chart_type,
        "title": title.title(),
        "xlabel": xlabel.title(),
        "ylabel": ylabel.title(),
        "data": {
            "x": [1, 2, 3, 4, 5],
            "y": [2, 4, 3, 5, 6]
        },
        "style": {
            "font_size": 12,
            "title_size": 14,
            "line_width": 2,
            "marker_size": 6,
            "color": "blue",
            "figure_width": 8,
            "figure_height": 6
        }
    }
    
    return config
