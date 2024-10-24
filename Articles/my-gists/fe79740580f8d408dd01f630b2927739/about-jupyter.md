The error you're encountering suggests that the `nbconvert` tool is unable to find a required template named 'lab' in the specified directories. This problem often arises due to an incomplete or incorrect installation of `nbconvert` or its dependencies, especially when dealing with custom or non-standard installations.

Here's a step-by-step guide to troubleshoot and resolve this issue:

### Step 1: Update nbconvert and Jupyter

Ensure that all related packages are up-to-date:

```sh
pip install --upgrade nbconvert jupyter
```

### Step 2: Check Installed Templates

Verify that the required templates are installed. You can list available templates using:

```sh
jupyter nbconvert --template-paths
```

### Step 3: Reinstall nbconvert with Extras

Sometimes, `nbconvert` may be missing some optional dependencies. Reinstall it with extras:

```sh
pip install nbconvert[all]
```

### Step 4: Install Jupyter Lab Templates

If you're using Jupyter Lab, ensure that the lab templates are available. You can try installing `nbconvert` with the Jupyter Lab extension:

```sh
pip install jupyterlab
```

### Step 5: Check Configuration

Ensure that the Jupyter configuration files are correctly set up and that the template paths are correct. You can manually check the paths listed in the error message to confirm the presence of the 'lab' sub-directory.

### Step 6: Custom Template Path

If you have a custom template, ensure it's correctly specified. You can specify the template path directly in your nbconvert command:

```sh
jupyter nbconvert --to html --template=<template-name> tmp/demo.ipynb
```

Replace `<template-name>` with the correct template name if you have a custom template.

### Step 7: Clean Environment

Sometimes, issues arise due to conflicts in the environment. Consider creating a clean virtual environment:

```sh
python -m venv nbconvert-env
source nbconvert-env/bin/activate
pip install nbconvert jupyter
jupyter nbconvert --to html tmp/demo.ipynb
```

### Example of a Clean Execution

Here's an example command to convert a notebook to HTML after performing the above steps:

```sh
jupyter nbconvert --to html tmp/demo.ipynb
```

### Additional Resources

For more detailed information, you can refer to the [official nbconvert documentation](https://nbconvert.readthedocs.io/en/latest/).

By following these steps, you should be able to resolve the template path error and successfully convert your Jupyter notebook to HTML. If the problem persists, consider providing more context about your setup or any custom configurations you might have.