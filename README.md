# Python Tap

A tool for REPL Driven Development.


## What is Python Tap?
Python Tap is used during development and when running code.
With this tool, you can store and process data such as function input parameters
or local variables. This is very useful when inspecting code and flows, and when
running code in a REPL. You will have all the _tapped_ data available in the session.

>It is closely related to the variables available when debugging, but you have the data available from anywhere in the code base.

You can use Python Tap when running code in debug mode too.

Python Tap itself, doesn't do any processing of data, but the functions you add to the `tap` does that.

Included in this library, there are default taps. You can also write your own, or add
any existing function accepting _*args_ and _**kwargs_ (such as a _logger_).

You decorate functions, or call the `tap` function directly.
The `tap` function will run the added _taps_ (functions) with the input to the target function.

This library heavily inspired by the `tap>` feature in Clojure.

## Usage

