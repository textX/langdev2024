# textX CLI Demo

This is a short demo of the [textX language](https://github.com/textX/textX).

Create and activate virtual env

``` bash
python -m venv venv
source venv/bin/activate
```

If running in VS Code terminal, select `./venv/bin/python` as python interpreter. Use the *Python: Select Interpreter* command from the Command Palette (macOS - <span style="color:blue">⇧⌘P</span>, Windows, Linux - <span style="color:blue">Ctrl+Shift+P</span>).

Install textX

``` bash
pip install "textx"
# dependencies:
# Arpeggio
```

Metamodel and model validation (Try changing `drone.tx` and `example.dr`)

``` bash
python main.py
```

Install textX CLI

``` bash
pip install "textx[cli]"
# dependencies:
# Arpeggio
# click
```

List registered languages

``` bash
textx list-languages
# textX
```

Metamodel and model validation via CLI

``` bash
textx check drone.tx
textx check example.dr --gramar drone.tx
```

List registered generators

``` bash
textx list-generators
# any -> dot
# textX -> dot
# textX -> PlantUML  
```

Visualize grammar

``` bash
textx generate drone.tx --target plantuml
dot -Tpng -O example.dot
```

Visualize model

``` bash
textx generate drone.tx --target plantuml
plantuml drone.pu
```