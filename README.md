aurum is a bash-like shell for interacting with database servers. It's still
very much in an alpha state of development and is mostly infrastructure at this
point with very few useful commands. The eventual goal is for it to provide a
concise alternative to SQL for common database tasks.

# Requirements

* Python 2.7.2+
* SQLAlchemy 0.7.6+

# Configuration

The `aurum` executable will look for configuration file at `~/.aurum`. Here are
the sections and settings that are currently supported.

    [general]
    prompt = "aurum> "

    [dsn]
    name = "protocol://username:password@host/database"

The `prompt` setting is similar in concept to the `$PSO` variable of bash, but
currenty only supports string literals.

Each line in the `[dsn]` section provides a [DSN](http://en.wikipedia.org/wiki/Data_Source_Name) for a particular 
server and database with a shorthand name for later reference.

# Usage

For now, clone the repo and execute `./bin/aurum` with no arguments.
Eventually, this will support specifying a DSN name to automatically connect to
it. This will place you in the "root" from which you'll eventually be able to
list available DSNs and their subentities and navigate between them.

# Development

Commands exist as classes in `lib/aurum/commands` that extend from
`aurum.commands.Command` and implement any of its `do_*` methods, which
represent particular contexts in which the command can be invoked such as when
no DSN is active or when a specific DSN, database, table, or column is active. 

A `do_all` method is also supported, which is executed if it exists when none
of the other `do_*` methods declared by `Command` are overridden. This is
useful when the command operation does not vary based on the context.

Note: These `do_*` methods are processed like those of any
[Cmd](http://docs.python.org/library/cmd.html) subclass. Specifically, if 
they return a `True` value, the shell will terminate. The base `Command` class
and `exit` Command subclass are good examples of this behavior being used.

# FAQ

## Why the name "aurum?"

This was partly influenced by the use of SQLAlchemy for the project. One of the
original goals of the craft of alchemy was to transmute base metals into noble
metals like gold or, in Latin, "aurum," the word from which the chemical
element takes its symbol Au. Another influence was my eventual hope for this
project, that it become as useful as its name implies.
