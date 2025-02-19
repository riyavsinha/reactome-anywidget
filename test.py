import marimo

__generated_with = "0.11.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from reactome_anywidget import ReactomeWidget
    import anywidget
    import traitlets
    return ReactomeWidget, anywidget, mo, traitlets


@app.cell
def _(ReactomeWidget, mo):
    mo.ui.anywidget(ReactomeWidget()).center()
    return


@app.cell
def _():
    js = """
    async function loadReactomeScript() {
          if (!window.Reactome) {
            return new Promise((resolve, reject) => {
              const script = document.createElement('script');
              script.src = "https://reactome.org/DiagramJs/diagram/diagram.nocache.js";
              script.onload = () => resolve();
              script.onerror = () => reject(new Error("Failed to load Reactome DiagramJS library"));
              document.head.appendChild(script);
            });
          }
        }

        async function render({ model, el }) {
          await loadReactomeScript();

          // Save the original document.getElementById
          const originalGetElementById = document.getElementById.bind(document);

          // Override document.getElementById to also search within our widget's element
          document.getElementById = function(id) {
            return originalGetElementById(id) || el.querySelector('#' + id);
          };

          // Generate a unique container id
          const uniqueId = model.model_id || Math.random().toString(36).substring(2);
          const containerId = "reactomeDiagramHolder-" + uniqueId;

          // Create and append the container to our widget element (shadow DOM)
          let container = document.createElement("div");
          container.id = containerId;
          // Optionally add some styling:
          container.style.border = "1px solid #ddd";
          container.style.padding = "10px";
          container.style.backgroundColor = "#f9f9f9";
          el.appendChild(container);

          // Retrieve parameters from the model
          const diagramId = model.get("diagramId") || "R-HSA-109582";
          const width = model.get("width") || 950;
          const height = model.get("height") || 500;

          // Create the Reactome Diagram widget
          let diagram = Reactome.Diagram.create({
              "placeHolder": containerId,
              "width": width,
              "height": height
          });

          diagram.onDiagramLoaded(function(loadedId) {
              console.info("Diagram loaded:", loadedId);
              if (loadedId === diagramId) {
                  diagram.selectItem(diagramId);
              }
          });

          diagram.loadDiagram(diagramId);
          model.reactomeDiagram = diagram;

          // (Optional) Restore document.getElementById if you don't need the override later.
          // If DiagramJS calls getElementById later during interactions, you might want to leave it overridden.
          // document.getElementById = originalGetElementById;
        }

        export default { render };
    """
    return (js,)


@app.cell
def _(anywidget, js, traitlets):
    class ReactomeWidget2(anywidget.AnyWidget):
        __use_shadow_dom__ = False
        _esm = js
        _css = """
        .reactome-widget {
            background-color: ;
        }
        """
        diagramId = traitlets.Unicode("R-HSA-109582").tag(sync=True)
        width = traitlets.Int(950).tag(sync=True)
        height = traitlets.Int(500).tag(sync=True)
    return (ReactomeWidget2,)


@app.cell
def _(ReactomeWidget2, mo):
    mo.ui.anywidget(ReactomeWidget2(diagramId="R-HSA-5693568")).center()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
