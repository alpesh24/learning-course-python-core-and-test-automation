from robot.api.deco import keyword
from robot.api.logger import console

class ClassLibrary:
    def __init__(self, name):
        """The library should accept one required argument, 'name', and store it as instance
        attribute 'name' (e.g. self.name)."""
        self.name = name

    @keyword
    def my_name_is(self, surname=None):
        """
        The keyword should accept a positional argument 'surname' with a default value of None.
        The keyword should access the value given as an argument to the library - 'name'.
        The keyword should log a following message when called: "Got name=<name>, surname=<surname>"
        For example: "Got name=James, surname="
        Logs should appear in the console.
        Use the robot.api.logger API provided by Robot Framework.
        The keyword should return a string "My name is <name>" if 'surname' is None,
        or "My name is <surname>, <name> <surname>" if 'surname' was given.
        For example: "My name is James"; "My name is Bond, James Bond"
        """
        console(f"Got name={self.name}, surname={surname}")
        if surname is None:
            return f"My name is {self.name}"
        else:
            return f"My name is {surname}, {self.name} {surname}"

    @keyword
    def concatenate_varargs(self, *args):
        """The keyword should accept a variable number of positional arguments.
        The keyword should log a following message when called: "Got args=<values>"
        For example: "Got args=('first', 'second')"
        Logs should appear in the console.
        The keyword should return a string made of space-separated arguments it received.
        For example: "first second"
        """
        console(f"Got args={args}")
        return ' '.join(args)

    @keyword
    def definitions(self, **kwargs):
        """The keyword should accept a variable number of keyword arguments.
        The keyword should log a following message when called: "Got args=<values>"
        For example: "Got args={'key': 'value'}"
        Logs should appear in the console.
        The keyword should return a string of this format: "<key1> is a <value1>, <key2> is a <value2>"
        (each new pair is appended to the string with a comma and a space).
        For example: "apple is a fruit, cake is a lie"
        """
        console(f"Got args={kwargs}")
        result = [f"{key} is a {value}" for key, value in kwargs.items()]
        return ', '.join(result)

    @keyword
    def knights_of_ni(self, *, loud=False):
        """The keyword should accept a single keyword-only argument 'loud'
        with a default value of boolean 'False' and no other arguments.
        The keyword should log a following message when called: "Got loud=<value>"
        For example: "Got loud=False"
        Logs should appear in the console.
        The keyword should return the string "We are the knights of Ni!" if 'loud' is False,
        and "WE ARE THE KNIGHTS OF NI!" otherwise."""
        console(f"Got loud={loud}")
        if loud:
            return "WE ARE THE KNIGHTS OF NI!"
        else:
            return "We are the knights of Ni!"

    @keyword('Raise ${base:\d+} to the power of ${power:\d+}')
    def raise_to_the_power_of(self, base, power):
        """The keyword should take two embedded arguments: 'base', after the word 'raise', and
        'power', after the word 'of'.
        Use the 'keyword' decorator from robot.api.deco module to implement embedded arguments.
        Arguments should be converted to integers.
        The keyword should log a following message when called: "Got base=<value>, power=<value>"
        For example: "Got base=4, power=3"
        Logs should appear in the console.
        The keyword should return an integer: 'base' raised to the power of 'power'.
        For example, with base=2 and power=4: 16
        """
        base, power = int(base), int(power)
        console(f"Got base={base}, power={power}")
        return base ** power
