# worlds.khddd — wheel branch

This is an **orphan branch** auto-built by [MultiworldGG/build-and-publish-action](https://github.com/MultiworldGG/build-and-publish-action).
It contains a pip-installable layout of the `khddd` world from this repo.

- **World:** Kingdom Hearts Dream Drop Distance
- **Version:** 0.0.15
- **Source ref:** `0.0.15`
- **Built:** 2026-05-05 14:08 UTC

## Install

```
pip install git+https://github.com/lallaria/Archipelago.git@wheel/worlds/khddd/0.0.15
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
- The `wheel/worlds/khddd/0.0.15` **tag** is immutable — pin
  to it for reproducibility. Pinning to the branch tip
  (`wheel/worlds/khddd`) gets the latest published version.
- Source for this build lives at `0.0.15` on the default branch.
