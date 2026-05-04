# worlds.khddd — wheel branch

This is an **orphan branch** auto-built by [MultiworldGG/build-and-publish-action](https://github.com/MultiworldGG/build-and-publish-action).
It contains a pip-installable layout of the `khddd` world from this repo.

- **World:** Kingdom Hearts Dream Drop Distance
- **Version:** 0.0.9
- **Source ref:** `cd68ada456d3dea6973f86120281be266985b132`
- **Built:** 2026-05-04 13:52 UTC

## Install

```
pip install git+https://github.com/lallaria/Archipelago.git@wheel/worlds/khddd/0.0.9
```

After install, `worlds.khddd` is importable in any environment that has the
MultiworldGG worlds-namespace stub installed (the monorepo provides it).

## How this branch is structured

```
pyproject.toml
src/
  worlds/
    khddd/
      ...the world's Python source...
```

This is a pip-installable [namespace-package](https://peps.python.org/pep-0420/)
contribution under the shared `worlds.` namespace. It coexists with all other
per-world install branches because none of them ship `worlds/__init__.py`.

## Important

- This branch is force-pushed on every release of this world.
- The `wheel/worlds/khddd/0.0.9` **tag** is immutable — pin
  to it for reproducibility. Pinning to the branch tip
  (`wheel/worlds/khddd`) gets the latest published version.
- Source for this build lives at `cd68ada456d3dea6973f86120281be266985b132` on the default branch.
