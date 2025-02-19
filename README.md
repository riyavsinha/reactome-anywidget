# Reactome Anywidget

This is a widget that allows you to embed a Reactome pathway diagram in environments like JupyterLab or Marimo notebooks.

## Installation

```bash
pip install reactome-anywidget
```

## Usage

### JupyterLab

```python
from reactome_anywidget import ReactomeWidget
ReactomeWidget(diagramId="R-HSA-199420", width=800, height=600)
```

### Marimo

```python
import marimo as mo
from reactome_anywidget import ReactomeWidget

mo.ui.anywidget(ReactomeWidget, diagramId="R-HSA-199420", width=800, height=600).center()
```

## Known Issues

This widget does not fully work in Marimo. The diagram is displayed, but search functionality won't render. This is possibly due to the fact that Marimo allows creating elements in a shadow DOM, which the Reactome widget cannot access.

