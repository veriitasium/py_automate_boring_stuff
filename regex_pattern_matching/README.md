# Pattern matching with regular expressions

## Finding patterns without using Regular Expressions

Say we want to validate a phone number with the patern: 3 numbers, a hyphen, 3 numbers, a hyphen, four numbers; It's also written as 'XXX-XXX-XXXX'
Let's create a functioin `is_phone_number()` that checks whether a given phone number follows the mentioned pattern, returning `True` or `False`:

<a href="#a-place-in-the-document>

```Python
def is_phone_number(text):
        if len(text) != 12:
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
            
        if text[3] != '-':
            return False

        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            
        if text[7] != '-':
            return False
        
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
```

</a>

Steps involved in the function `is_phone_number`:
1. First, the function checks the length of the text (string) is whether 12 or not.
2. Then, it checks the first three numbers of the string are decimal
3. an added hyphen is checked after the numbers
4. Previous 2 validation processes repeat themselves (whether the rest of the string starts with 3 decimal numbers followed by a hyphen)
5. And finally, four more numbers is checked at the end.

Only after all these requirements have been successfully satisfied, the function will return `True` as an indication of the text (string) is a pattern matching phone number. Otherwise, `False`

If we run this code, the output looks like this:
```console
415-555-4242 is a phone number:
True
Moshi moshi is a phone number:
False
```

As seen, in the first input, there is a phone number that matches the pattern. Hence the function returned `True`. That said, since `Moshi moshi` string does not follow the given pattern, we received the output `False`.

---

What if we don't want to pass a phone number manually, meaning the program checks the number on its own in a string??
We could use this code block instead of typing by ourselves:
```Python

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"

for i in range(len(message)):
    chunk = message[i:i + 12]

    if is_phone_number(chunk):
        print(f"Phone number found: {chunk}")
```
this command will, without us inputting a phone number, go through all string literals and, once it finds the pattern matching string, the number will be displayed as an output, say: `Phone number found: 415-555-9999`

HOWEVER!!! Our function only checks with a single pattern; not to mention, how long the program has become...
What if we want to check Uzbekistan phone number - **(998) XX XXX-XX-XX**
`is_phone_number()` function would fail to recognize it. Thus... Using **Regular Expressions**, in short `regexes`, will bring ease to <a id="a-place-in-the-document">our validation process</a> process. 

How to use Regular Expressions in Python:
- All the regex functions are in the `re` module. Install it on your program by the command `import re` on top of python file.
- Pass a string representing your Regular Expressions to `re.compile()`; it returns a Regex object. For example:
    ```python
    phone_number_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
    ```
    why `r`? assume you want to add `\n` in your string but the language interprets it in different way - a single newline character. Since we do not wnat that, we have to double add `\` backslash like `\\n`. That said, doing it over and over and over again is tedious. Hence, by putting an `r` before the first (double) quote of the string, we can mark our string as a _raw string_, which doesn't escape characters.
- Search a phone number matching our string regular expression from the passed string argument:
    ```python
    mo = phone_number_regex.search(text)
    ```
    Once the function `search()` finds the match, it returns a `Match` object, also written as `mo` in program. If not, `None` is assigned.
- After the program has found the match to our regular expression and stored it in the Match object (`mo`), then we can call `group()` on `mo` to return the Match:
    ```python
    print('Phone number found: ' + mo.group())
    ```

To put all together:
```python
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
```
The output:
```console
Phone number found: 415-555-4242
```