from typing import List

from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.executors.base_executor import VersionFlags
from dmoj.executors.compiled_executor import CompiledExecutor
from dmoj.executors.mixins import StripCarriageReturnsMixin


class Executor(StripCarriageReturnsMixin, CompiledExecutor):
    ext = 'zig'
    command = 'zig'
    compiler_time_limit = 30
    compiler_read_fs = [
        RecursiveDir('~/.cache'),
        RecursiveDir('/opt/zig/lib'),
        RecursiveDir('/usr/include'),
        RecursiveDir('/usr/lib'),
        RecursiveDir('/lib'),
        RecursiveDir('/lib64'),
    ]
    compiler_write_fs = [
        RecursiveDir('~/.cache'),
    ]
    compiler_required_dirs = [
        '~/.cache',
        '/opt/zig/lib',
        '/usr/include',
        '/usr/lib',
        '/lib',
        '/lib64',
    ]

    test_program = """
const std = @import("std");

pub fn main() !void {
    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();

    var line_buf: [50]u8 = undefined;
    while (try stdin.readUntilDelimiterOrEof(&line_buf, '\\n')) |line| {
        if (line.len == 0) break;
        try stdout.print("{}", .{line});
    }
}"""

    def get_compile_args(self) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, 'build-exe', self._code, '-O', 'ReleaseFast', '--name', self.problem]

    @classmethod
    def get_version_flags(cls, command: str) -> List[VersionFlags]:
        return ['version']
