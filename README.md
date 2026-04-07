# PyScan ChainChecker for TeamPCP infection

Unofficial fork of [Pyscan](https://github.com/ohaswin/pyscan) customized to specifically search for Python package versions 
affected by the [TeamPCP supply chain attack](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/).

Performs a quick scan of the following:

- Versions of dependencies installed in the current Python environment; to see if any version numbers known to be compromised is installed.
- Virtualenvs and wheel files on the local file system.
- Known artifacts of past TeamPCP exploitation.

Install and run as follows:

```bash
pip install [...]
pyscan-chainchecker --all
```

