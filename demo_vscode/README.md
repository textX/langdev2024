# textX VS Code Extension Demo

Install textX VS Code Extension. The new option should appear in the sidebar.

There you can:
- view current projects with registered languages
- view registered generators
- refresh projects with languages
- create new project by providing wheel file

Right click on `setup.py` file and click "Install textX project".

The tx-drone project with Drone language will appear in top section of the textX sidebar. The new generator for Drone language and python as a target, will appear in the bottom section only after restarting VS Code. This will be improved in the next version.

Language and generator are defined in `tx_drone/__init__.py` file, and referenced from entry points specified in `setup.py` file.

Notice syntax highlighting on the grammar and program files (`tx_drone` and `examples.dr`). When you try making changes, validation with error reporting will occur.

Running the registered code generator can be done by using the textx CLI. Before that, we need to activate extension's virtual environment. Running generators from extension's sidebar will be the improvement for the next version.

``` bash
(macOS, Linux) source ~/.vscode/extensions/textx.textx-0.2.0/textxls/bin/activate
(Windows) .\%USERPROFILE%\.vscode\extensions\textx.textx-0.2.0\textxls\bin\activate
```

Now we can run the registered generator

``` bash
textx generate example.dr --language Drone --target python --overwrite
```

The `dist/drone.py` file will be generated, and it can be executed on DJI Tello drone.

