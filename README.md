# sci-fig

AI-powered scientific figure generator with editable parameters for research papers.

## Features

- Generate figure configurations from natural language descriptions
- Interactively edit figure parameters (fonts, colors, dimensions, labels)
- Export high-resolution figures (PNG/PDF/SVG, 300+ DPI)
- Support for line plots, bar charts, and scatter plots

## Installation


## Usage

### Generate a figure configuration


This creates a `figure.yaml` configuration file.

### Edit parameters interactively


Adjust fonts, colors, dimensions, and labels through an interactive menu.

### Export to high-resolution image


## Example Workflow


## Configuration File Format

The YAML configuration file contains:
- Chart type (line/bar/scatter)
- Title and axis labels
- Data points
- Style parameters (fonts, colors, dimensions)

You can manually edit the YAML file or use the interactive editor.
# 安装依赖
pip install -r requirements.txt

# 生成图表配置
python main.py generate "line chart showing temperature trend, x-axis: Time, y-axis: Temperature"

# 编辑参数
python main.py edit figure.yaml

# 导出图片
python main.py export figure.yaml --output result.png --dpi 300