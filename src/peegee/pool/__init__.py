# peegee - a small typed wrapper around asyncpg for personal projects
# Copyright (C) 2023 Violet McKinney <opensource@viomck.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from peegee import Pool
from pool.context import WrappedPoolAcquireContext
from typing import Any
import asyncpg

class WrappedPool:
    pool: Pool

    def __init__(self, pool: Pool):
        self.pool = pool

    def acquire(self) -> WrappedPoolAcquireContext:
        return WrappedPoolAcquireContext(self.pool.acquire())



def create_pool(
    dsn: str | None = None,
    *args: list[Any],
    **kwargs: dict[str, Any],
) -> WrappedPool:
    return WrappedPool(asyncpg.create_pool(
        dsn,
        *args,
        **kwargs,
    ))
