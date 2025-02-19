import anywidget
import pathlib
import traitlets

class ReactomeWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = """
    .reactome-widget {
    }
    """
    diagramId = traitlets.Unicode("R-HSA-5693568").tag(sync=True)
    width = traitlets.Int(950).tag(sync=True)
    height = traitlets.Int(500).tag(sync=True)

# Example instantiation:
# ReactomeWidget(diagramId="R-HSA-5693568", width=950, height=500)
