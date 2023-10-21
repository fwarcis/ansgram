from __future__ import annotations

from configparser import ConfigParser
from dataclasses import dataclass


def load_cfg(path: str) -> Cfg:
    cfg = ConfigParser()
    cfg.read(path)

    return Cfg(
        BotCfg(token=cfg["bot"].get("token")),
        DbCfg(
            path=cfg["db"].get("path"),
            dbms=DbmsCfg(
                echo=cfg["dbms"].getboolean("echo"),
                expire_on_commit=cfg["dbms"].getboolean("expire_on_commit"),
            ),
        ),
    )


@dataclass
class Cfg:
    bot: BotCfg
    db: DbCfg


@dataclass
class BotCfg:
    token: str


@dataclass
class DbCfg:
    path: str
    dbms: DbmsCfg


@dataclass
class DbmsCfg:
    echo: bool
    expire_on_commit: bool
