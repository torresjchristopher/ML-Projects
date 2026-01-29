# Sample Quarto files

These QMD files can be rendered individually:

        quarto render mermaid.qmd


Or, because the directoty contains a project file *_quarto.yml* then can all be rendered
at once:

        quarto render

The files highlight different features built into Quarto:

* *mermaid.qmd* - demonstrates a *mermaid* figure,
* *graphviz.qmd* - demonstrates *graphviz* figure,
* *gantt.qmd* - demonstrates a gantt chart creating using *mermaid*.


The project file *_quarto.yml* specifies how and where the files are rendered.  In this example the files are rendered to the *../docs* folder as *html* files.  See the *_quarto.yml* file for details.
