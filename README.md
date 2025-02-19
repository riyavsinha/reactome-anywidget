# Reactome Anywidget

This is a widget built on [AnyWidget](https://anywidget.dev/) that allows you to embed a Reactome pathway diagram in environments like JupyterLab or Marimo notebooks.

<img width="1174" alt="Screenshot 2025-02-19 at 1 26 47 AM" src="https://github.com/user-attachments/assets/602c1619-22de-41b7-965b-c420e3b4f5c4" />

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

