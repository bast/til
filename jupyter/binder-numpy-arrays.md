# Inspecting npy/npz files using Binder

We need a Python environment with `numpy` and `scipy`. Fortunately we can use
one of [Binder](https://mybinder.org/)'s [sample
repositories](https://mybinder.readthedocs.io/en/latest/examples/sample_repos.html)
for this:

1. Open <http://mybinder.org/v2/gh/binder-examples/requirements/HEAD> in your
   browser. This may take few seconds to spin up.

2. Top left click "Upload Files" icon (arrow up symbol). Upload the npy/npz
   file(s).  Wait until the upload is complete. This can take few seconds
   depending on the file size. You can track this in the JupyterLab terminal
   with `ls -lh`.

3. Open the "Python 3" Notebook (big button top center).

4. In the notebook cell paste the following code:
   ```python
   import numpy as np

   data = np.load("filename.npz", allow_pickle=True)

   keys = list(data.keys())
   print(f"available keys: {keys}")

   print(f"printing the first record {keys[0]} just as an example:")
   print(data[keys[0]])
   ```

5. Adjust "filename.npz" to the actual file name.

6. Run the cell with Shift+Enter.

7. Now that you see available keys, you can print specific values of `data`.
